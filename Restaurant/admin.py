from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]
# restaurant/admin.py

from django.contrib import admin
from .models import Menu, Booking

admin.site.register(Menu)
admin.site.register(Booking)
