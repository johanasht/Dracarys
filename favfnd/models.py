from django.db import models
from django.db import models
from django.contrib.auth.models import User
from foods.models import Food
from drinks.models import Drink


# Create your models here.

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    merchant_area = models.CharField(max_length=255)
    merchant_name = models.CharField(max_length=255, )
    category = models.CharField(max_length=13)
    product = models.CharField(max_length=255, )
    description = models.CharField(max_length=255, )
    food = models.ManyToManyField(Food)
    drink = models.ManyToManyField(Drink)
