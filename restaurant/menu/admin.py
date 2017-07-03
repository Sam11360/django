from django.contrib import admin

# Register your models here.
from .models import Menu, Plat
admin.site.register(Menu)
admin.site.register(Plat)
