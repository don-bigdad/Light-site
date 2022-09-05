from django import forms


from cart.models import UserOrderForm



class OrderForm(forms.ModelForm):


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
    order =forms.CharField(empty_value="aaa",max_length=15,widget=forms.TextInput(attrs={
        "type":"hidden",
        "class":"form-control",
        "name":"phone",
        "id":"phone",
    }))
    email = forms.CharField(empty_value="aaa", max_length=200, widget=forms.TextInput(attrs={
        "type": "hidden",
        "class": "form-control",
        "name": "email",
        "id": "email",
    }))


    class Meta:
        model = UserOrderForm
        fields = "__all__"


