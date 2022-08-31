from django.shortcuts import render, redirect
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



    sale_item = SaleItem.objects.filter(is_visible=True)
    slider = CustomSlider.objects.all()
    form = UserFormQuestion()
    mailing = MailingForm()
    data = {
        "categories":category,
        "product":product,
        "prod_list":prod_list,
        "sale_item":sale_item,
        "slider":slider,
        "form":form,
        "mailing":mailing,
    }

    return render(request,"base.html",context=data)