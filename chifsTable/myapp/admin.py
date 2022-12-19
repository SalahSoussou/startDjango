from django.contrib import admin

# Register your models here.

from .models import Menu
from .models import Catigoty

admin.site.register(Menu)
admin.site.register(Catigoty)
