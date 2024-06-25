from rest_framework import routers
from . import views
from djoser.views import UserViewSet
from django.urls import include, path



router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename="users")
router.register(r'menu-items', views.MenuItemsViewSet, basename= 'menu-items')
router.register(r'booking', views.BookingViewSet, basename= 'booking')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]