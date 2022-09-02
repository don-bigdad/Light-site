from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET

from base.models import Product, SaleItem

from .cart import Cart


@require_GET
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')

@require_GET
def cart_add_sale_item(request, sale_item_id,sale_item_slug):
    cart = Cart(request)
    sale_item = get_object_or_404(SaleItem, id=sale_item_id+100,slug=sale_item_slug)
    cart.add_sale_item(sale_item=sale_item, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})
