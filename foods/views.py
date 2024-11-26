from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Food
from .forms import FoodFilterForm
from user_auth.models import UserProfile
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json


def show_food(request):
    foods = Food.objects.all()
    form = FoodFilterForm(request.GET)
    
    if form.is_valid():
        category = form.cleaned_data.get("category")
        if category:
            foods = foods.filter(category=category)


    context = {
        'form': form,
        'foods': foods,
    }

    return render(request, 'foods.html', context)

def food_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    context = {'food': food}
    return render(request, 'food_detail.html', context)

@csrf_exempt
def add_food(request):
    if request.method == "POST":
        merchant_area = request.POST.get('merchant_area')
        merchant_name = request.POST.get('merchant_name')
        category = request.POST.get('category')
        product = request.POST.get('product')
        description = request.POST.get('description')

        new_food = Food(merchant_area=merchant_area, merchant_name=merchant_name, category=category, product=product,
                        description=description)
        new_food.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def add_to_favorites(request, food_id):
    if request.user.is_authenticated:
        user = UserProfile.objects.filter(user=request.user).first()
        food = get_object_or_404(Food, id=food_id)
        user.favfood.add(food)
        return redirect('favfnd:show_favorites')
    else:
        return redirect(reverse("user_auth:login"))

def get_food(request):
    data = Food.objects.all()
    return HttpResponse(serializers.serialize("json", data), 
    content_type="application/json")

def get_food_by_id(request, id):
    data = Food.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def filter_foods(request):
    category = request.GET.get('category', '')
    foods = Food.objects.all()
    if category:
        foods = foods.filter(category=category)
    foods_json = serializers.serialize('json', foods)
    return JsonResponse(foods_json, safe=False)


def show_json(request):
    data = Food.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Food.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_to_fav_flutter (request, food_id, user_id) :
    if request.method == 'POST' :
            data = json.loads(request.body)
            user_id = data.get('user_id')
            user = UserProfile.objects.filter(user=user_id).first()
            food = get_object_or_404(Food, id=food_id)
            user.favfood.add(food)
            return JsonResponse({"status": "success", "message": "Berhasil ditambahkan ke favorite!"}, status=200)
    else :
        return JsonResponse({"status": "error", "message": "invalid request method"}, status=401)
    



# def add_to_favorites(request, food_id):
#     if request.user.is_authenticated:
#         user = UserProfile.objects.filter(user=request.user).first()
#         food = get_object_or_404(Food, id=food_id)
#         user.favfood.add(food)
#         return redirect('favfnd:show_favorites')
#     else:
#         return redirect(reverse("user_auth:login"))``