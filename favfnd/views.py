from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.core import serializers
from user_auth.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from .models import Drink
from .models import Food
from .forms import FoodFilterForm, DrinkFilterForm
from django.shortcuts import get_object_or_404
# Create your views here.

def show_favorites(request):
    if request.user.is_authenticated:
        return render(request, 'favorites.html')
    else :
        return redirect(reverse("user_auth:login"))

def show_favfood(request) :
    form = FoodFilterForm(request.GET)
    user = UserProfile.objects.filter(user=request.user).first()
    data_food = user.favfood.all()

    if form.is_valid() :
        category = form.cleaned_data.get("category")
        if category:
            data_food = data_food.filter(category=category)
        
    context = {
         "favfood": data_food,
    }
    return render(request, 'favorite_food.html', context)

def show_favdrink(request):
    form = DrinkFilterForm(request.GET)
    user = UserProfile.objects.filter(user=request.user).first()
    data_drink = user.favdrink.all()
    if form.is_valid() :
        category = form.cleaned_data.get("category")
        if category:
            data_drink = data_drink.filter(category=category)
    
    context = {
        "favdrink": data_drink
    }
    return render(request, 'favorite_drink.html', context)

   

@csrf_exempt
def filter_drink(request):
    category = request.GET.get('category', '')
    user = UserProfile.objects.filter(user=request.user).first()
    data_drinks = user.favdrink.all()
    if category:
        data_drinks = data_drinks.filter(category=category)
    drinks_json = serializers.serialize('json', data_drinks)
    print(category)
    return JsonResponse(drinks_json, safe=False)

@csrf_exempt
def filter_foods(request):
    category = request.GET.get('category', '')
    user = UserProfile.objects.filter(user=request.user).first()
    data_food = user.favfood.all()
    if category:
        data_food = data_food.filter(category=category)
    foods_json = serializers.serialize('json', data_food)
    return JsonResponse(foods_json, safe=False)

def show_json_favfood_by_user_id (request, user_id) :
    user = UserProfile.objects.filter(user=user_id).first()
    datafood = user.favfood.all()
    return HttpResponse(serializers.serialize("json", datafood), content_type="application/json")
     
def show_json_favdrink_by_user_id (request, user_id) :
    user = UserProfile.objects.filter(user=user_id).first()
    datafood = user.favdrink.all()
    return HttpResponse(serializers.serialize("json", datafood), content_type="application/json")
     
def remove_favdrink(request, drink_id):
    if request.method == "POST":
        if request.user.is_authenticated:
            user = UserProfile.objects.filter(user=request.user).first()
            try:
                drink = get_object_or_404(user.favdrink, id=drink_id)
                user.favdrink.remove(drink)
                return redirect('favfnd:show_favdrink')
            except Exception as e:
                print("Error:", e)
        else:
            print("User not authenticated")
    else:
        print("Invalid request method:", request.method)
    return JsonResponse({"success": False, "message": "Unauthorized or invalid request."}, status=403)

def remove_favfood(request, food_id):
    if request.method == "POST":
        if request.user.is_authenticated:
            user = UserProfile.objects.filter(user=request.user).first()
            try:
                food = get_object_or_404(user.favfood, id=food_id)
                user.favfood.remove(food)
                return redirect('favfnd:show_favfood')
            except Exception as e:
                print("Error:", e)
        else:
            print("User not authenticated")
    else:
        print("Invalid request method:", request.method)
    return JsonResponse({"success": False, "message": "Unauthorized or invalid request."}, status=403)