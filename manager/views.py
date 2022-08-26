from django.shortcuts import render,HttpResponse

def manager(request):
    return HttpResponse("manager page")
