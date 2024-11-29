from django import forms
from .models import Drink

class DrinkFilterForm(forms.Form):
    category = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Kopi/Nonkopi'}))

class AddDrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ['merchant_area', 'calories', 'merchant_name',  'category', 'product', 'description']