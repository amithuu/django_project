from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email','phone_number' ,'password1', 'password2'] 

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number']

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']