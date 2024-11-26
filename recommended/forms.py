from django import forms

class FavoriteFilter(forms.Form):
    type = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Food/Drinks'}))
