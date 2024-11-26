from django import forms
from .models import Food
from .models import Drink

class FoodFilterForm(forms.Form):
    category = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Nasi/Mie/Snack/Lainnya'}))

class DrinkFilterForm(forms.Form):
    category = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Kopi/Nonkopi'}))
