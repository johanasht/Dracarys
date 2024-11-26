from django.urls import path
from recommended.views import show_page, show_food_json

app_name = 'recommended'

urlpatterns = [
    path('', show_page, name='show_page'),
    path("show_food_json/", show_food_json, name="show_food_json")

]