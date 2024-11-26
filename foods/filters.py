from .models import Food
import django_filters

class FoodFilter(django_filters.FilterSet):
    class Meta:
        model = Food
        fields = ['category']
