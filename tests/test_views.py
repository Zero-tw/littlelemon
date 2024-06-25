from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from restaurant.models import Menu, Booking
from littlelemonAPI.serializers import MenuSerializer, BookingSerializer

class MenuItemsViewSetTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.menu_item = Menu.objects.create(title='Pasta', price=12.99, inventory=20)
        self.menu_url = reverse('menu-items-list')

    def test_create_menu_item(self):
        data = {'title': 'Pizza', 'price': '9.99', 'inventory': 15}  
        serializer = MenuSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        response = self.client.post(self.menu_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)
        self.assertEqual(Menu.objects.get(id=response.data['id']).title, 'Pizza')

    def test_list_menu_items(self):
        response = self.client.get(self.menu_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        serialized_data = MenuSerializer(self.menu_item)
        self.assertEqual(response.data[0], serialized_data.data)

    def test_retrieve_menu_item(self):
        url = reverse('menu-items-detail', args=[self.menu_item.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = MenuSerializer(self.menu_item)
        self.assertEqual(response.data, serialized_data.data)

    def test_destroy_menu_item(self):
        url = reverse('menu-items-detail', args=[self.menu_item.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 0)


class BookingViewSetTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.booking = Booking.objects.create(name='John Doe', no_of_guests=4, booking_date='2023-06-25')
        self.booking_url = reverse('booking-list')

    def test_create_booking(self):
        data = {'name': 'Jane Doe', 'no_of_guests': 2, 'booking_date': '2023-06-26'}
        serializer = BookingSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        response = self.client.post(self.booking_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)
        self.assertEqual(Booking.objects.get(id=response.data['id']).name, 'Jane Doe')

    def test_list_bookings(self):
        response = self.client.get(self.booking_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        serialized_data = BookingSerializer(self.booking)
        self.assertEqual(response.data[0], serialized_data.data)

    def test_retrieve_booking(self):
        url = reverse('booking-detail', args=[self.booking.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = BookingSerializer(self.booking)
        self.assertEqual(response.data, serialized_data.data)

    def test_destroy_booking(self):
        url = reverse('booking-detail', args=[self.booking.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)
