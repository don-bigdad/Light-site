from django.urls import path
from .views import manager, update_contact_to_processed, back_to_main_page, update_unchecked_orders, \
    unchecked_orders

app_name = "manager"

urlpatterns=[
    path("contact/",manager,name="contact_forms"),
    path("contact/update/<int:pk>/",update_contact_to_processed,name="update_contact_to_processed"),
    path("contact/index.html/",back_to_main_page,name="back"),
    path("orders/",unchecked_orders,name="unchecked_orders"),
    path("orders/update/<int:pk>",update_unchecked_orders,name="update_unchecked_orders"),
]