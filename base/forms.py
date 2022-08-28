from django import forms
from .models import UserForm


class UserFormQuestion(forms.ModelForm):
    name = forms.CharField(max_length=40,widget=forms.TextInput(attrs={
        "type":"name",
        "class":"form-control",
        "id":"name",
        "placeholder":"Name",
        "required":"",
        "pattern":"[A-Za-z]{3,}",
        "title":"minimal lenght 3"
    }))

    phone = forms.CharField(max_length=15,widget=forms.TextInput(attrs={
        "type":"text",
        "class":"form-control",
        "name":"phone",
        "id":"phone",
        "required":"",
        "placeholder":"Your Phone",
        "pattern":"^(\d{3}[- .]?){2}\d{4}$",
        "title":"Input number in format xxx xxx xxxx",

    }))

    date = forms.DateField(widget=forms.DateField())
    time = forms.TimeField(widget=forms.TimeField())

    text = forms.CharField(max_length=500,widget=forms.Textarea(attrs={
        "сlass":"form-control",
        "name":"message",
        "rows":"5",
        "placeholder":"Message Theme"

    }))
    class Meta:
        model = UserForm
        fields = '__all__'