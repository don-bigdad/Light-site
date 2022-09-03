from decimal import Decimal

from django.conf import settings

from base.models import Product


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price),"id":product_id}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def add_sale_item(self, sale_item, quantity=1, update_quantity=False):
        sale_item_id = str(sale_item.id+1000)
        if sale_item_id not in self.cart:
            self.cart[sale_item_id] = {'quantity': 0, 'price': str(sale_item.new_price),"Sale_item_name":sale_item.name,
             "Sale_item_picture":sale_item.picture.url,"slug":sale_item.slug,"id":sale_item.id}
        if update_quantity:
            self.cart[sale_item_id]['quantity'] = quantity
        else:
            self.cart[sale_item_id]['quantity'] += quantity
        self.save()


    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def remove_sale_item(self, sale_item):
        sale_item_id = str(sale_item.id+1000)
        if sale_item_id in self.cart:
            del self.cart[sale_item_id]
            self.save()


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())
