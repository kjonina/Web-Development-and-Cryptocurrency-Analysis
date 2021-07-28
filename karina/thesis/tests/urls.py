from django.test import TestCase
from django.test import SimpleTestCase

from django.urls import reverse, resolve

from .views import thesis

## DOES NOT WORK YET!
class TestUrls(SimpleTestCase):

    def test_thesis_url_resolves(self):
        url = reverse('thesis')
        self.assertEqual(resolve(url).func, thesis)
