from django.urls import path
from .views import manager,manager_order,update_contact_to_processed,back_to_main_page

app_name = "manager"

urlpatterns=[
    path("contact/",manager,name="contact_forms"),
    path("contact/update/<int:pk>/",update_contact_to_processed,name="update_contact_to_processed"),
    path("order_check/",manager_order),
    path("contact/index.html/",back_to_main_page,name="back")
]