from django.shortcuts import render, redirect
from foods.models import Food
from drinks.models import Drink
from foods.views import food_detail
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from .forms import FavoriteFilter
import random
# Create your views here.

def show_page (request):
    food_items = list(Food.objects.all())
    drink_items = list(Drink.objects.all())
    form = FavoriteFilter(request.GET)


    random_food_items = random.sample(food_items, 6)
    random_drink_items = random.sample(drink_items, 6)


    data_for_food = []
    data_for_drink = []

    for food in random_food_items:
        food_data = serializers.serialize('python', [food])[0]
        data_for_food.append(food_data)

    for drink in random_drink_items:
        drink_data = serializers.serialize('python', [drink])[0]
        data_for_drink.append(drink_data)

    
    context = {
        'food': data_for_food,
        'drink': data_for_drink
    }
    
    if form.is_valid() :
        type = form.cleaned_data.get("type")
        if type == "Foods" :
            context = {
                'food': data_for_food
            }
        elif type == "Drinks" :
            context = {
                'drink': data_for_drink
            }
        else :
             context = {
                'food': data_for_food,
                'drink': data_for_drink
            }    
    return render(request, 'index.html', context)



def show_food_json(request):
    data = list(Food.objects.all())
    random_items = random.sample(data, 6)
    return HttpResponse(serializers.serialize("json", random_items), content_type="application/json")