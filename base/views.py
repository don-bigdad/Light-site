from django.shortcuts import render
from .models import *
def base(request):
    category = Category.objects.filter(is_visible=True)
    product = Product.objects.filter(is_visible=True)
    sale_item = SaleItem.objects.filter(is_visible=True)

    data = {
        "categories":category,
        "product":product,
        "sale_item":sale_item,
    }

    return render(request,"base.html",context=data)