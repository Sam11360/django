from django.contrib import admin

# Register your models here.
from .models import Menu, Plat, Restaurant
admin.site.register(Menu)
admin.site.register(Plat)
admin.site.register(Restaurant)
