from django.urls import path
from .views import review_fnd, get_reviews_json,food_detail, drink_detail, get_reviews_template, reviews_template, get_all_reviews_partial, review_fnd_ajax, get_all_reviews_json, get_csrf_token_ajax, review_fnd_flutter, food_review_detail, drink_review_detail

app_name = "reviews"

urlpatterns = [
    path('food_detail/<int:food_id>/', food_detail, name='food_detail'),
    path('food_detail/<int:food_id>/reviews/', food_review_detail, name='review_detail'),
    path('drink_detail/<int:drink_id>/', drink_detail, name='drink_detail'),
    path('drink_detail/<int:food_id>/reviews/', drink_review_detail, name='review_detail'),
    path('get_template', reviews_template, name='get_template'),
    path('get_reviews_template', get_all_reviews_partial, name='get_reviews_template'),
    path('get_all_reviews_json', get_all_reviews_json, name='get_all_reviews_json'),
    path('<str:content_type>/<int:object_id>/review_fnd', review_fnd, name='review_fnd'),
    path('<str:content_type>/<int:object_id>/review_fnd_ajax', review_fnd_ajax, name='review_fnd_ajax'),
    path('<str:content_type>/<int:object_id>/review_fnd_flutter', review_fnd_flutter, name='review_fnd_flutter'),
    path('<str:content_type>/<int:object_id>/get_reviews_json', get_reviews_json, name='get_reviews_json'),
    path('<str:content_type>/<int:object_id>/get_reviews_template', get_reviews_template, name='get_reviews_template'),
    path('get_csrf_token_reviews', get_csrf_token_ajax, name='get_csrf_token_reviews'),
]