from django.db import models
from django.contrib.auth.models import User
from foods.models import Food
from drinks.models import Drink

class UserProfile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10)
    favfood = models.ManyToManyField(Food, related_name="favfood")
    favdrink = models.ManyToManyField(Drink, related_name="favdrink")