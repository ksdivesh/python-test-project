from django.shortcuts import render, redirect
from django.http import HttpResponse
from students.models import Category, Product, SliderImage, Cart
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    categoryList = Category.objects.all()
    products = Product.objects.all()
    sliders = SliderImage.objects.all()

    # for product in products:
    #     # print(product.productimage_set.all())
    #     for product_image in product.productimage_set.all():
    #         print(product_image.image)

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

    if request.method == "POST":

        # user =  User.objects.filter(username = request.POST['username'])

        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                        email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])

        user.save()

        # id = user.id;

        # company = Company(user_id = id, company_name = request.POST[;COM])

        messages.success(request, "You have registered successfully.")
        return redirect('/login')

    return render(request, "register.html")


def login(request):

    return render(request, "login.html")


def postlogin(request):

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        auth_login(request, user)
        return redirect('/customer_profile')

    messages.error(
        request, "You have entered wrong username or password", extra_tags='danger')

    return render(request, "login.html")


@login_required
def customer_profile(request):
    return render(request, "customer_profile.html")


@login_required
def add_to_cart(request):

    cart = Cart(user_id=request.user.id,
                product_id=int(request.POST['product_id']))
    cart.save()
    messages.success(request, "Item added to cart successfully")
    return redirect("/")


@login_required
def cart(request):
    cartList = Cart.objects.filter(user_id=request.user.id)
    context = {
        'cartList': cartList
    }
    return render(request, "cart.html", context)


def logout(request):
    auth_logout(request)
    messages.success(request,  "You have logged out successfully")
    return redirect('/login')
