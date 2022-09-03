from django.shortcuts import render, redirect
from base.models import UserForm
from cart.models import UserOrderForm
from django.contrib.auth.decorators import login_required,user_passes_test


def is_manager(user):
    return user.groups.filter(name="manager").exists()


@login_required(login_url="account:login")
@user_passes_test(is_manager)
def manager(request):
    uncalled_forms = UserForm.objects.filter(is_processed=False)
    return render(request,"Contact.html",context={"uncalled_forms":uncalled_forms})


@login_required(login_url="account:login")
@user_passes_test(is_manager)
def update_contact_to_processed(request,pk):
    UserForm.objects.filter(pk=pk).update(is_processed=True)
    return redirect("manager:contact_forms")

@login_required(login_url="account:login")
@user_passes_test(is_manager)
def unchecked_orders(request):
    orders = UserOrderForm.objects.filter(is_processed=False)
    return render(request, "Orders.html", context={"orders": orders})

@login_required(login_url="account:login")
@user_passes_test(is_manager)
def update_unchecked_orders(request,pk):
    UserOrderForm.objects.filter(pk=pk).update(is_processed=True)
    return redirect("manager:unchecked_orders")

def back_to_main_page(request):
    return redirect("/")

