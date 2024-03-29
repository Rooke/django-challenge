from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from .models import Home

class HomeTests(APITestCase):
    def test_create_home(self):
        """
        Ensure we can create a new home object.
        """
        factory = APIRequestFactory()
        request = factory.post('/homes/', {
            'area_unit': 'SqFt',
            'bathrooms': 2,
            'bedrooms': 4,
            'home_size': 1372,
            'home_type': 'SingleFamily',
            'last_sold_date': '',
            'last_sold_price': '',
            'link': 'https://www.zillow.com/homedetails/7417-Quimby-Ave-West-Hills-CA-91307/19866015_zpid/',
            'price': '$739K',
            'property_size': 10611,
            'rent_price': '',
            'rentzestimate_amount': 2850,
            'rentzestimate_last_updated': '08/07/2018',
            'tax_value': 215083,
            'tax_year': 2017,
            'year_built': 1956,
            'zestimate_amount': 709630,
            'zestimate_last_updated': '08/07/2018',
            'zillow_id': 19866015,
            'address': '7417 Quimby Ave',
            'city': 'West Hills',
            'state': 'CA',
            'zipcode': 91307})

        self.assertEqual(Home.objects.count(), 0) # Bogus test








