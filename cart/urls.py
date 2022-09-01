from django.urls import path

import manager.views
from . import views

app_name = "cart"

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('back_to_main_page/',manager.views.back_to_main_page,name="back")
]
