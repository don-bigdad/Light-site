from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class SaleItem(models.Model):
    name = models.CharField(unique=True,max_length=70,db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    small_description = models.TextField(max_length=100,blank=True)
    past_price = models.DecimalField(max_digits=10,decimal_places=2)
    new_price = models.DecimalField(max_digits=10,decimal_places=2)
    is_visible = models.BooleanField(default=True)
    position = models.IntegerField(unique=True)
    picture = models.ImageField(upload_to="sale/%Y-%m-%d")

    @property #в шаблоне будет автоматом выставлятся процент скидки
    def sale_percent_auto_calculate(self):
        return 100 - self.new_price * 100 // self.past_price

    class Meta:
        ordering = ("position","new_price",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=40,unique=True,db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(unique=True, max_length=70, db_index=True)
    slug = models.SlugField(max_length=140,db_index=True)
    small_description = models.TextField(max_length=140,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    picture = models.ImageField(upload_to="product/%Y-%m-%d")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("about_product", args=[self.id, self.slug])

    class Meta:
        ordering = ("name",)
        index_together = (("id","slug"),)

    def __str__(self):
        return self.name


class UserForm(models.Model):

    mobile_re = RegexValidator(regex=r"^(\d{3}[- .]?){2}\d{4}$",message="Input number in format xxx xxx xxxx")

    name = models.CharField(max_length=40,db_index=True)
    phone = models.CharField(max_length=15,validators=[mobile_re,])
    date = models.DateField()
    time = models.TimeField()
    text = models.TextField(max_length=500,blank=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ("time",)

    def __str__(self):
        return self.name + "-" + str(self.date)

class Mailing(models.Model):
    email = models.EmailField()
    mailing_start_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email