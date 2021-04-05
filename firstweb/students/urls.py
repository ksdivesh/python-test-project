from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('fee', views.fee, name='fee'),
    path('products', views.products, name='products')
    
]
