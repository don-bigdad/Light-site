from django.shortcuts import render, redirect
from .models import *
from .forms import UserFormQuestion
def base(request):
    if request.method == "POST":
        message = UserFormQuestion(request.POST)
        if message.is_valid():
            message.save()
            return redirect("/")

    category = Category.objects.filter(is_visible=True)
    product = Product.objects.filter(is_visible=True)
    sale_item = SaleItem.objects.filter(is_visible=True)
    slider = CustomSlider.objects.all()
    form = UserFormQuestion()
    data = {
        "categories":category,
        "product":product,
        "sale_item":sale_item,
        "slider":slider,
        "form":form,
    }

    return render(request,"base.html",context=data)