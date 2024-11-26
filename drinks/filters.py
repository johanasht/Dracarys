from .models import Drink
import django_filters

class DrinkFilter(django_filters.FilterSet):
    class Meta:
        model = Drink
        fields = ['category']
