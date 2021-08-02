from django.test import TestCase

from blog.models import Blog
from datetime import datetime


class TestBlogModel(TestCase):
    def setUp(self):
        self.Project1 = Blog.objects.create(
            title = 'Django Testing',
            pub_date = datetime.now,
            body = 'A Django application is a Python package that is specifically intended for use in a Django project. An application may use common Django conventions, such as having models , tests , urls , and views submodules. A Django application is a Python package that is specifically intended for use in a Django project. An application may use common Django conventions, such as having models , tests , urls , and views submodules.',
            image = 'null',
            slug = 'Django-Testing')

    def test_model_title(self):
        self.assertEqual(str(self.Project1.title), "Django Testing")

    def test_model_body(self):
        self.assertEqual(str(self.Project1.body), "A Django application is a Python package that is specifically intended for use in a Django project. An application may use common Django conventions, such as having models , tests , urls , and views submodules. A Django application is a Python package that is specifically intended for use in a Django project. An application may use common Django conventions, such as having models , tests , urls , and views submodules.")

    # def test_pub_date(self):
    #     self.assertEqual(pub_date_pretty, "2021-07-29 12:51:16.439995")


## DO NOT WORK
    # def test_summary(self):
    #     self.assertEqual(self.Project1.summary(self.Project1.summary), "A Django application is a Python package that is specifically intended for use in a Django project. An application may use common Django conventions, such as having models , tests , urls , and views submodules.")
    #
    # def test_pub_date_pretty(self):
    #     self.assertEqual(pub_date_pretty(self.Project1.pubdate), "29 Jul 2021")
