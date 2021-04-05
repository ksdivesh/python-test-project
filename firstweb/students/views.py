from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "index.html")

def fee(request):
    return render(request, "fees/fee.html")

def products(request):
    return render(request, "products.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return HttpResponse("This is login page")
