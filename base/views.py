from django.shortcuts import render, redirect, get_object_or_404

from cart.cart import Cart
from .models import *
from .forms import UserFormQuestion, MailingForm

from django.core.paginator import Paginator


def base(request):
    if request.method == "POST":
        message = UserFormQuestion(request.POST)
        if message.is_valid():
            message.save()
            return redirect("/")
        mail = MailingForm(request.POST)
        mail.save()
        return redirect("/")

    category = Category.objects.filter(is_visible=True)


    product = Product.objects.filter(is_visible=True)

    p = Paginator(product,50)
    page = request.GET.get("page")
    prod_list = p.get_page(page)

    cart = Cart(request)

    sale_item = SaleItem.objects.filter(is_visible=True)
    form = UserFormQuestion()
    mailing = MailingForm()
    data = {
        "categories":category,
        "product":product,
        "prod_list":prod_list,
        "sale_item":sale_item,
        "form":form,
        "mailing":mailing,
        "cart":cart,
    }

    return render(request,"base.html",context=data)


def about_product(request,id,slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request,'product_detail.html',{'product': product})


def about_sale_product(request, slug):
    about_sale_item = get_object_or_404(SaleItem,slug=slug)
    return render(request,"about_sale_item.html",{'about_sale_item': about_sale_item})
