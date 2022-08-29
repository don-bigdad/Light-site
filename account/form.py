from django import forms
from django.contrib.auth import  get_user_model

user = get_user_model()

class RegisterUser(forms.ModelForm):

    class Meta:
        model = user
        fields = ("username","email")

    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={
        "type": "text",
        "name": "username",
        "placeholder": "Username",
        "required": "",
        "id": "id_username",
        "pattern": "[A-Za-z0-9]{4,20}",
        "title": "minimal length of user field 4",
    }))
    password = forms.CharField(max_length=15,widget=forms.PasswordInput(attrs={
        "type": "password",
        "name": "password",
        "placeholder": "Password",
        "required": "",
        "id": "id_password",
        "pattern": "[A-Za-z0-9]{4,20}",
        "title": "minimal length of password field 4",
    }))
    repeat_password = forms.CharField(max_length=15,widget=forms.PasswordInput({
        "type": "password",
        "name": "password",
        "placeholder": "Password",
        "required": "",
        "id": "id_password",
        "pattern": "[A-Za-z0-9]{4,20}",
        "title": "minimal length of password field 4",
    }))
    email = forms.CharField(max_length=30,widget=forms.EmailInput(attrs={
        "type":"email",
        "name":"email"
    }))


    def clean_repeat_password(self):

        if not self.cleaned_data["repeat_password"]:
            raise forms.ValidationError("You must confirm your password")
        if self.cleaned_data["password"] != self.cleaned_data["repeat_password"]:
            raise forms.ValidationError("Password don`t match")
        return self.cleaned_data["repeat_password"]