from django.contrib import admin

# Register your models here.

from .models import Menu, Catigoty, LogForm

admin.site.register(Menu)
admin.site.register(Catigoty)
admin.site.register(LogForm)
