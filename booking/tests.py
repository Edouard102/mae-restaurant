from django.test import TestCase
from datetime import date
from django.contrib.auth import get_user_model
from .models import Booking, Table

# Create your tests here.


class TableBookingTest(TestCase):
    def setUp(self):
        # Creating tables
        Table.objects.create(table_number=1, table_num_seats=4)
        Table.objects.create(table_number=2, table_num_seats=2)
        Table.objects.create(table_number=3, table_num_seats=1)
        Table.objects.create(table_number=4, table_num_seats=1)

        # Creating a user
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Creating a booking
        Booking.objects.create(
            customer=self.user,
            customer_name='John Doe',
            party_size=3,
            email='john@example.com',
            phone='123456789',
            booking_date=date(2024, 4, 1),
            booking_time=12,
            table=Table.objects.get(table_number=1),
            notes='Notes for the booking',
            allergies='Allergy information'
        )

    def test_table_creation(self):
        table = Table.objects.get(table_number=1)
        self.assertEqual(table.table_number, 1)
        self.assertEqual(table.table_num_seats, 4)

    def test_booking_creation(self):
        booking = Booking.objects.get(customer_name='John Doe')
        self.assertEqual(booking.customer, self.user)
        self.assertEqual(booking.party_size, 3)
        self.assertEqual(booking.email, 'john@example.com')
        self.assertEqual(booking.phone, '123456789')
        self.assertEqual(booking.booking_date, date(2024, 4, 1))
        self.assertEqual(booking.booking_time, 12)
        self.assertEqual(booking.table.table_number, 1)
        self.assertEqual(booking.notes, 'Notes for the booking')
        self.assertEqual(booking.allergies, 'Allergy information')
