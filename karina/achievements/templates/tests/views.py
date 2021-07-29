from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from jobs.views import home, COVID_Dashboard, AirBnB_Listing


class TestViews(TestCase):

    def setUp(self):
        self.client =  Client()
        self.home_url = reverse('home')
        self.COVID_Dashboard_url = reverse('COVID_Dashboard')
        self.AirBnB_Listing_url = reverse('AirBnB_Listing')


    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/home.html')

    def test_COVID_Dashboard_url(self):
        response = self.client.get(self.COVID_Dashboard_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/covid.html')

    def test_AirBnB_Listing_url(self):
        response = self.client.get(self.AirBnB_Listing_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/airbnb_listings.html')
