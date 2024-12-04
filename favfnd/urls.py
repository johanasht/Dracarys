from django.urls import path
from favfnd.views import show_favorites, show_favfood, show_favdrink, filter_foods, filter_drink, show_json_favfood_by_user_id, show_json_favdrink_by_user_id, remove_favdrink, remove_favfood

app_name = 'favfnd'

urlpatterns = [
    path('', show_favorites, name='show_favorites'),
    path("food/", show_favfood, name="show_favfood"),
    path('food/filter_foods/', filter_foods, name='filter_foods'),
    path("drink/", show_favdrink, name="show_favdrink"),
    path('drink/filter_drink/', filter_drink, name='filter_drink'),
    path("get-favfood/<int:user_id>/", show_json_favfood_by_user_id, name="show_json_favfood_by_user_id"),
    path("get-favdrink/<int:user_id>/", show_json_favdrink_by_user_id, name="show_json_favdrink_by_user_id"),
    path('remove-drink/<int:drink_id>/', remove_favdrink, name='remove_favdrink'),
    path('remove-food/<int:food_id>/', remove_favfood, name='remove_favfood'),
]
