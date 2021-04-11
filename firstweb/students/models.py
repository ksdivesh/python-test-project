from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    # dunder method

    def __str__(self):
        return self.name + " (" + str(self.created_at) + ")"


class Product(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=1000)
    discount = models.IntegerField(max_length=2, default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.IntegerField(max_length=1, default=0)
    qty = models.IntegerField(max_length=6, default=0)
    main_image = models.ImageField(
        upload_to='static/images/products', null=True)
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " (" + self.category.name + ")"


class ProductImage(models.Model):
    image = models.ImageField(upload_to='static/images/products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.product.name, str(self.image))


class SliderImage(models.Model):
    image = models.ImageField(upload_to='static/images/sliders/')
    name = models.CharField(max_length=100, null=True)
    tagline = models.CharField(max_length=255, null=True)
    active = models.IntegerField(max_length=1, default=0)

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
