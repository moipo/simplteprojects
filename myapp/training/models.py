from django.db import models #дефолтный класс моделей из пакета db

# Create your models here. #продукт
class Unnes(models.Model): #класс MODEL определен в классе models. max length required.
    title = models.CharField(max_length = 120) #max_length
    description = models.TextField(default = "simple title")
    additional_descrition = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places = 2, max_digits=10000)
