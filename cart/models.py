from django.core.validators import RegexValidator
from django.db import models

class UserOrderForm(models.Model):
    mobile_re = RegexValidator(regex=r"^(\d{3}[- .]?){2}\d{4}$",message="Input number in format xxx xxx xxxx")

    name = models.CharField(max_length=40,db_index=True)
    phone = models.CharField(max_length=15,validators=[mobile_re,])
    is_processed = models.BooleanField(default=False)
    email = models.CharField(max_length=400,auto_created=True)
    order = models.TextField(max_length=400,auto_created=True)


    def __str__(self):
        return self.name
