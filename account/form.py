from django import forms
from django.contrib.auth import  get_user_model

User = get_user_model()

class RegisterUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username",)

    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=15)
    repeat_password = forms.CharField(max_length=15)
    email = forms.CharField(max_length=30)

