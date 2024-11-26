from django.urls import path
from .views import show_food, food_detail, add_food, get_food, get_food_by_id, filter_foods, add_to_favorites, show_json, show_json_by_id, add_to_fav_flutter

app_name = 'foods'

urlpatterns = [
    path('', show_food, name='show_food'),
    path('food_detail/<int:food_id>/', food_detail, name='food_detail'),
    path('add_food/', add_food, name='add_food'),
    path('get_food/', get_food, name='get_food'),
    path('get_food/<int:id>/', get_food_by_id, name="get_food_by_id"),
    path('filter_foods/', filter_foods, name='filter_foods'),
    path('add_to_favorites/<int:food_id>/', add_to_favorites, name='add_to_favorites'),
    path("json/", show_json, name="show_json"),
    path("add_to_fav_flutter/<int:food_id>/<int:user_id>/", add_to_fav_flutter, name="add_to_fav_flutter")
]


