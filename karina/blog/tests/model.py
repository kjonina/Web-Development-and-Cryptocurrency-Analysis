from django.test import TestCase

from blog.models import Blog


class TestBlogModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.title = Blog.objects.create(title="Django Testing")
        cls.body = Blog.objects.create(body="This will be a miracle if this works!")

    def test_model_title(self):
        self.assertEqual(str(self.title), "Django Testing")

    def test_model_body(self):
        self.assertEqual(str(self.body), "This will be a miracle if this works!")

    # def test_pub_date_pretty(self):
    #     self.assertEqual(pub_date_pretty('2021/05/05 05:05:05'), "5 May 2021")


## run in the command line
# coverage run --omit="*/myvenv/*" manage.py test
# coverage report
# python manage.py test achievements
