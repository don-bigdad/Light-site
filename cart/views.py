from django.core.mail import send_mail

from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required

from Light.settings import EMAIL_HOST_USER
from base.models import Product, SaleItem

from .cart import Cart
from .forms import OrderForm
from .models import UserOrderForm


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

def cart_delete(request):
    cart = Cart(request)
    cart.cart_del()
    return redirect("/")

@login_required(login_url="account:login")
def cart_detail(request):
    cart = Cart(request)
    form = OrderForm()
    data = {"cart": cart, "form": form}
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_detail = "Your order is:"
            for elem in cart:
                order_detail += f" {elem.get('product')} - {elem.get('quantity')} \n"
            order_str = f'Dear {order_form.cleaned_data["name"]} thanks for order in our magazine.Our manager will contact you later' \
                        f'Detail:' \
                        f'{order_detail}.' \
                        f'Total to pay:{cart.get_total_price()}$\n' \
                        f'With our love Light magazine 🙂 !'
            UserOrderForm.objects.create(
                name = order_form.cleaned_data.get("name"),
                phone = order_form.cleaned_data.get("phone"),
                order = f'We have a new order {order_detail[13:]},total price is {cart.get_total_price()}!'
            )
            for elem in cart:
                if elem.get("slug"):
                    cart_remove_sale_item(request,elem.get("id"),elem.get("slug"))
                else:
                    cart_remove(request,elem.get("id"))
            send_mail("Success order in Light Magazine",order_str,EMAIL_HOST_USER,[request.user.email],fail_silently=False)

        return redirect("/")

    return render(request, 'cart_detail.html', context=data)
