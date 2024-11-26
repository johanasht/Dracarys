from django.urls import path
from .views import show_drink, drink_detail, add_drink, get_drink, get_drink_by_id, filter_drink, add_to_favorites, show_json, show_json_by_id, add_to_fav_flutter

app_name = 'drinks'

urlpatterns = [
    path('', show_drink, name='show_drink'),
    path('drink_detail/<int:drink_id>/', drink_detail, name='drink_detail'),
    path('add_drink/', add_drink, name='add_drink'),
    path('get_drink/', get_drink, name='get_drink'),
    path('get_drink/<int:id>/', get_drink_by_id, name="get_drink_by_id"),
    path('filter_drink/', filter_drink, name='filter_drink'),
    path('add_to_favorites/<int:drink_id>', add_to_favorites, name='add_to_favorites'),
    path("json/", show_json, name="show_json"),
    path("json/<int:id>", show_json_by_id, name="show_json_by_id"),
    path("add_to_fav_flutter/<int:drink_id>/<int:user_id>/", add_to_fav_flutter, name="add_to_fav_flutter")
]