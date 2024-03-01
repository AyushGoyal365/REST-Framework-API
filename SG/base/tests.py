from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice = Invoice.objects.create(date='2024-03-01', customer_name='Ayush Goyal')
    
    def test_create_invoice(self):
        data = {
            'date': '2024-03-01',
            'customer_name': 'Ayush Goyal',
            'details': [
                {
                    'description': 'Django developer',
                    'quantity': 1,
                    'unit_price': 550000,
                    'price': 30000
                }
            ]
        }
        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, 201)