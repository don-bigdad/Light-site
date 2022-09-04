from django.urls import path

import manager.views
from . import views

app_name = "cart"

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path("add/<int:sale_item_id>/<slug:sale_item_slug>/",views.cart_add_sale_item,name="cart_add_sale_item"),
    path('remove/<int:sale_item_id>/<slug:sale_item_slug>/', views.cart_remove_sale_item, name='cart_remove_sale_item'),
    path("delete",views.cart_delete,name="remove_all_items"),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('back_to_main_page/',manager.views.back_to_main_page,name="back")
]
