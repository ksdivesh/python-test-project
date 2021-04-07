from django.shortcuts import render
from django.http import HttpResponse
from students.models import Category, Product, SliderImage
# Create your views here.


def index(request):
    categoryList = Category.objects.all()
    products = Product.objects.all()
    sliders = SliderImage.objects.all()
    data = {
        "categoryList": categoryList,
        "products": products,
        "sliders": sliders,
        "page_name": "Home"
    }

    return render(request, "index.html", data)


def fee(request):
    return render(request, "fees/fee.html")


def products(request):
    return render(request, "products.html")


def register(request):
    return render(request, "register.html")


def login(request):
    return HttpResponse("This is login page")
