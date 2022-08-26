from django.shortcuts import render,HttpResponse

def client(request):
    return render(request,"index.html",context={})