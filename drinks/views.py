from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Drink
from .forms import DrinkFilterForm
from user_auth.models import UserProfile
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json


def show_drink(request):
    Drink.objects.filter(calories__isnull=True).delete()

    drinks = Drink.objects.all().values()
    form = DrinkFilterForm(request.GET)

    if form.is_valid():
        category = form.cleaned_data.get("category")

        if category:
            drinks = drinks.filter(category=category).distinct()

    context = {
        'form': form, 
        'drinks': drinks,
    }

    return render(request, 'drinks.html', context)

def drink_detail(request, drink_id):
    drink = get_object_or_404(Drink, id=drink_id)
    context = {'drink': drink}
    return render(request, 'drink_detail.html', context)

@csrf_exempt
def add_drink(request):
    if request.method == "POST":
        merchant_area = request.POST.get('merchant_area')
        calories = request.POST.get('calories')
        merchant_name = request.POST.get('merchant_name')
        category = request.POST.get('category')
        product = request.POST.get('product')
        description = request.POST.get('description')

        new_drink = Drink(merchant_area=merchant_area, calories=calories, merchant_name=merchant_name, category=category, product=product,
                        description=description)
        new_drink.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def add_to_favorites(request, drink_id):
    if request.user.is_authenticated:
        user = UserProfile.objects.filter(user=request.user).first()
        drink = get_object_or_404(Drink, id=drink_id)
        user.favdrink.add(drink)
        print("Dipanggil")
        print(user.favdrink)
        return redirect('favfnd:show_favorites')
    else:
        return redirect(reverse("user_auth:login"))

def get_drink(request):
    data = Drink.objects.all().distinct()
    return HttpResponse(serializers.serialize("json", data), 
    content_type="application/json")

def get_drink_by_id(request, id):
    data = Drink.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def filter_drink(request):
    category = request.GET.get('category', '')
    drinks = Drink.objects.all()
    if category:
        drinks = drinks.filter(category=category)
    drinks_json = serializers.serialize('json', drinks)
    print(category)
    return JsonResponse(drinks_json, safe=False)

def show_json(request):
    data = Drink.objects.all().values().distinct()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_json_by_id(request, id):
    data = Drink.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@csrf_exempt
def add_to_fav_flutter (request, drink_id, user_id) :
    if request.method == 'POST' :
            data = json.loads(request.body)
            user_id = data.get('user_id')
            user = UserProfile.objects.filter(user=user_id).first()
            drink = get_object_or_404(Drink, id=drink_id)
            user.favdrink.add(drink)
            return JsonResponse({"status": "success", "message": "Berhasil ditambahkan ke favorite!"}, status=200)
    else :
        return JsonResponse({"status": "error", "message": "invalid request method"}, status=401)