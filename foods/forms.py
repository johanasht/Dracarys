from django import forms
from .models import Food

class FoodFilterForm(forms.Form):
    category = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Nasi/Mie/Snack/Lainnya'}))

class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['merchant_area', 'merchant_name', 'category', 'product', 'calories', 'description']