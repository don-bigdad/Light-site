from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET

from base.models import Product, SaleItem

from .cart import Cart
from .forms import OrderForm



@require_GET
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')

@require_GET
def cart_add_sale_item(request, sale_item_id,sale_item_slug):
    cart = Cart(request)
    sale_item = get_object_or_404(SaleItem,id=sale_item_id,slug=sale_item_slug)
    cart.add_sale_item(sale_item=sale_item, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')

def cart_remove_sale_item(request, sale_item_id,sale_item_slug):
    cart = Cart(request)
    sale_item = get_object_or_404(SaleItem, id=sale_item_id,slug=sale_item_slug)
    cart.remove_sale_item(sale_item)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')




def cart_detail(request):
    cart = Cart(request)
    form = OrderForm()
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            order_form.save()
            for elem in cart:
                if elem.get("slug"):
                    cart_remove_sale_item(request,elem.get("id"),elem.get("slug"))
                else:
                    cart_remove(request,elem.get("id"))
        # email = send_mail()
        # email.send_email()
        return redirect("/")


    data ={"cart":cart,"form":form}
    return render(request, 'cart_detail.html', context=data)
