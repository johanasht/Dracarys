from django.contrib.auth.forms import UserCreationForm
from django import forms
from user_auth.models import UserProfile
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm) :
    user_type = forms.ChoiceField(
        choices = (("admin", "Admin"), ("user", "User")),
        label="Choose your user type:",
        required=True
    )
    email = forms.EmailField(label = "Email", required=True)

    class Meta:
        model = User
        fields = ['user_type','username','email','password1','password2'] 

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
        UserProfile.objects.create(
            user=user,
            user_type = self.cleaned_data["user_type"],
        )
        return user