from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Restaurant.views import BookingViewSet  # Replace 'yourapp' with your app's name
from Restaurant import views

# Define the DefaultRouter and register the BookingViewSet
router = routers.DefaultRouter()
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Restaurant.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),  # Add this for the BookingViewSet
]

# Register the UserViewSet
router.register(r'users', views.UserViewSet)

