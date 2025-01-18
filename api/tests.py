from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.

class UserCreateAPITests(APITestCase):
    def setUp(self):
        pass

    def test_create_user(self):
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuserid',
            'password': 'test123',
            'email': 'test@mail.com',
        }
        
        # Make a POST request
        response = self.client.post('/api/1.0/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username=data["username"]).exists())
        self.assertIn('message', response.json())

class GetJWTTokenAPITests(APITestCase):
    def setUp(self):
        # Set up any initial data here, e.g., creating users or test data
        self.user = User.objects.create_user(username="testuserid", password="test123", email="test@email.com")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

    def test_get_token(self):
        data = {
            'username': 'testuserid',
            'password': 'test123',
        }
        
        # Make a POST request
        response = self.client.post('/api/1.0/token/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.json())
        self.assertIn('access', response.json())

class CoinsAPITests(APITestCase):
    def setUp(self):
        # Set up any initial data here, e.g., creating users or test data
        self.user = User.objects.create_user(username="testuserid", password="test123", email="test@email.com")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

        # getting token
        data = {
            'username': 'testuserid',
            'password': 'test123',
        }
        
        # Make a POST request
        response = self.client.post('/api/1.0/token/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.json())
        self.assertIn('access', response.json())
        self.access_token = response.json()["access"]

    def test_coins_list(self): 
        # Make a GET request
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }
        response = self.client.get('/api/1.0/coins/list/', format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('coins_list', response.json())
        self.assertTrue(len(response.data["coins_list"]) > 0)

    def test_coins_categories(self): 
        # Make a GET request
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }
        response = self.client.get('/api/1.0/coins/categories/', format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('coins_categories', response.json())
        self.assertTrue(len(response.data["coins_categories"]) > 0)

    def test_coins_markets(self): 
        # Make a GET request
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }
        response = self.client.get('/api/1.0/coins/markets/', format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('coins_markets', response.json())
        self.assertEqual(len(response.data["coins_markets"]), 10)

    def test_coins_markets_with_custome_pagination(self): 
        # Make a GET request
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }
        response = self.client.get('/api/1.0/coins/markets/?per_page=5&page=2', format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('coins_markets', response.json())
        self.assertTrue(len(response.data["coins_markets"]), 5)

    def test_coins_markets_with_custome_coins(self): 
        # Make a GET request
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }
        response = self.client.get('/api/1.0/coins/markets/?coin_id=yoyo,yuge-meme,bitcoin', format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('coins_markets', response.json())
        self.assertTrue(len(response.data["coins_markets"]), 3)

    def test_coins_markets_with_custome_coin_category(self): 
        # Make a GET request
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }
        response = self.client.get('/api/1.0/coins/markets/?category_id=velas-ecosystem,manufacturing,hyperxpad-launchpad', format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('coins_markets', response.json())
        self.assertTrue(len(response.data["coins_markets"]), 3)
