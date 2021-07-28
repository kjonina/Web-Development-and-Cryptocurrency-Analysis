from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from thesis.views import thesis


class TestViews(TestCase):

    def setUp(self):
        self.client =  Client()
        self.thesis_url = reverse('thesis')


    def test_thesis_GET(self):
        response = self.client.get(self.thesis_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'thesis/thesis_home.html')
