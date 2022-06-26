from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Product(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True)
    article = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=30)
    color = models.CharField(max_length=50)
    quality = models.CharField(max_length=20)
    country_of_origin = models.CharField(max_length=30)
    importing_country = models.CharField(max_length=30)
    seller = models.CharField(max_length=15)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    is_published = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.article


class Brand(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name
