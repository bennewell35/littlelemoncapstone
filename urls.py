from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Restaurant.views import BookingViewSet
from Restaurant import views as restaurant_views  # Rename the 'views' module to avoid conflicts
from rest_framework.authtoken.views import obtain_auth_token  # Import obtain_auth_token

# Define the DefaultRouter and register the BookingViewSet
router = routers.DefaultRouter()
router.register(r'booking', BookingViewSet)
router.register(r'users', restaurant_views.UserViewSet)  # Register the UserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('Restaurant.urls')),
    path('api/', include(router.urls)),  # Include the BookingViewSet URLs
    path('littlelemoncapstone/', include('littlelemoncapstoneAPI.urls')),  # Add this pattern
    
    # Url patterns for Djoser endpoints
    path('menu-items/', restaurant_views.MenuItemsView.as_view(), name='menu-items-list'),
    path('menu-items/<int:pk>/', restaurant_views.SingleMenuItemView.as_view(), name='menu-item-detail'),
    path('message/', restaurant_views.msg, name='message'),
    
    # Add Djoser URL routes
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
