from django.urls import path
from . import views

urlpatterns = [
    path('Restaurant/', views.restaurant_list, name='restaurant_list'),
    path('Restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define a view named 'home' for the root URL
    # ... other URL patterns for your project ...
]

