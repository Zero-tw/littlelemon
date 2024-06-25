from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuModelTest(TestCase):

    def setUp(self):
        self.menu = Menu.objects.create(
            title='Pasta',
            price=12.99,
            inventory=20
        )

    def test_menu_creation(self):
        self.assertIsInstance(self.menu, Menu)
        self.assertEqual(self.menu.__str__(), 'Pasta : 12.99')
        self.assertEqual(self.menu.title, 'Pasta')
        self.assertEqual(self.menu.price, 12.99)
        self.assertEqual(self.menu.inventory, 20)

    def test_menu_title_max_length(self):
        max_length = self.menu._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_menu_price_max_digits(self):
        max_digits = self.menu._meta.get_field('price').max_digits
        self.assertEqual(max_digits, 10)

    def test_menu_price_decimal_places(self):
        decimal_places = self.menu._meta.get_field('price').decimal_places
        self.assertEqual(decimal_places, 2)


class BookingModelTest(TestCase):

    def setUp(self):
        self.booking = Booking.objects.create(
            name='John Doe',
            no_of_guests=4,
            booking_date='2023-06-25'
        )

    def test_booking_creation(self):
        self.assertIsInstance(self.booking, Booking)
        self.assertEqual(self.booking.__str__(), 'John Doe')
        self.assertEqual(self.booking.name, 'John Doe')
        self.assertEqual(self.booking.no_of_guests, 4)
        self.assertEqual(self.booking.booking_date, '2023-06-25')

    def test_booking_name_max_length(self):
        max_length = self.booking._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)