from django.shortcuts import render
from Restaurant import views

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
from django.shortcuts import render

def restaurant_list(request):
    # Your view logic here
    return render(request, 'restaurant_list.html', {})
from django.shortcuts import render

def restaurant_detail(request, restaurant_id):
    # Your view logic here
    return render(request, 'restaurant_detail.html', {'restaurant_id': restaurant_id})
# Restaurant/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # You'll need to create a 'home.html' template
