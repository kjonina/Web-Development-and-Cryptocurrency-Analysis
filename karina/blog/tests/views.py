from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import allblogs, detail
from blog.models import Blog
from datetime import datetime

import json

class TestViews(TestCase):

    def setUp(self):
        self.client =  Client()
        self.allblogs_url = reverse('allblogs')
        self.detail_url = reverse('detail', args = ['project1'])
        self.Project1 = Blog.objects.create(
            title = 'project1',
            pub_date = datetime.now(),
            body = 'This is a test',
            image = 'null',
            slug = 'null')


    def test_allblogs_GET(self):
        response = self.client.get(self.allblogs_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/allblogs.html')


    def test_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/detail.html')
