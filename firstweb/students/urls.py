from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('customer_profile', views.customer_profile, name='customer_profile'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('postlogin', views.postlogin, name='postlogin'),
    path('fee', views.fee, name='fee'),
    path('products', views.products, name='products'),
    path('cart', views.cart, name='cart')

]
