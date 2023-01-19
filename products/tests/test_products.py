from django.urls import reverse, resolve
from django.test import SimpleTestCase
from products.views import ProductViewSet
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


Products_url = reverse("products-list")
class ProductsUrlTest(SimpleTestCase):
    
    # test Products url linked to correct viewset
    def test_get_Products_is_resolved(self):
        self.assertEquals(resolve(Products_url).func.__name__,ProductViewSet.__name__)
    
class ProductsAPIViewTests(APITestCase):

    def setUp(self):
        self.email = 'jpueblo@example.com'
        self.username = 'jpueblo'
        self.password = 'password'
        self.user = User.objects.create_user(
            self.username, self.email, self.password)
        self.data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post('/token/', self.data, format='json')
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
       

    def test_get_Products_authenticated(self):
        response = self.client.get(Products_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_Products_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(Products_url)
        self.assertEquals(response.status_code, 401)

