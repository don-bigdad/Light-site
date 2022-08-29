from django.shortcuts import render, redirect
from base.models import UserForm


def manager(request):
    uncalled_forms = UserForm.objects.filter(is_processed=False)
    return render(request,"Contact.html",context={"uncalled_forms":uncalled_forms})


def update_contact_to_processed(request,pk):
    UserForm.objects.filter(pk=pk).update(is_processed=True)
    return redirect("manager:contact_forms")


def manager_order(request):
    pass

