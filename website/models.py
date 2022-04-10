from django.db import models

# Create your models here.


class Currency(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    date_achieved = models.DateField(null=True)
    description = models.TextField(null=True)

class Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
