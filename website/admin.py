from django.contrib import admin
from .models import Currency, Registration, Profile

# Register your models here.
admin.site.register(Currency)
admin.site.register(Registration)
admin.site.register(Profile)
