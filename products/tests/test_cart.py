from django.urls import reverse, resolve
from django.test import SimpleTestCase
from products.views import CartViewSet
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

cart_url = reverse("cart-list")
class CartUrlTest(SimpleTestCase):
    
    # test cart url linked to correct viewset
    def test_get_cart_is_resolved(self):
        self.assertEquals(resolve(cart_url).func.__name__,CartViewSet.__name__)
    
class CartAPIViewTests(APITestCase):

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
       

    def test_get_cart_authenticated(self):
        response = self.client.get(cart_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_cart_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(cart_url)
        self.assertEquals(response.status_code, 401)

    def test_post_cart_authenticated(self):
        data = {
            "name": "Aylmar",
            "image": "http://dummyimage.com/110x100.png/dddddd/000000",
            "brand": "DYSL",
            "price": "74.000",
            "quantity": 96
        }
        response = self.client.post(cart_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
