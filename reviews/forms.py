from django.forms import ModelForm, TextInput
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        exclude = ("user", "object_id", "content_type")
