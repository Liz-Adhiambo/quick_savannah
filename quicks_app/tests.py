from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Customer, Order
from rest_framework_simplejwt.tokens import RefreshToken
from unittest.mock import patch

class SignupViewTest(APITestCase):
    def test_signup(self):
        url = reverse('signup')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword123',
            'number': '1234567890',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().number, '1234567890')


class CustomerListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user('testuser', 'test@example.com', 'testpassword123')

    def test_create_customer(self):
        self.client.login(username='testuser', password='testpassword123')
        url = reverse('customer_list')
        data = {'user':1,'number': '1234567890', 'name': 'Test Customer', 'code': 'TC123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'Test Customer')

    def test_get_customers(self):
        self.client.login(username='testuser', password='testpassword123')
        url = reverse('customer_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


