from rest_framework import viewsets, mixins
from .serializers import BookingSerializer, MenuSerializer
from restaurant.models import Menu, Booking
from rest_framework.permissions import IsAuthenticated, IsAdminUser



# Create your views here.
class MenuItemsViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    

class BookingViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]