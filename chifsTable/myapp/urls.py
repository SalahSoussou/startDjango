from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('hello/', views.sau_hello),
    path('date/', views.date),
    path('menu/', views.menu),
]
