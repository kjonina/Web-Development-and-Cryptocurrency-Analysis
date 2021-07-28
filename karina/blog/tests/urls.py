from django.test import TestCase
from django.test import SimpleTestCase

from django.urls import reverse, resolve

from blog.views import allblogs, detail

class TestUrls(SimpleTestCase):

    def test_allblogs_url_resolves(self):
        url = reverse('allblogs')
        self.assertEqual(resolve(url).func, allblogs)

    def test_detail_url_resolves(self):
        url = reverse('detail', args=[1])
        self.assertEqual(resolve(url).func, detail)









## run in the command line
# coverage run --omit="*/myvenv/*" manage.py test
# coverage report
# python manage.py test achievements
