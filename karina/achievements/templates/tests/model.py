from django.test import TestCase

from jobs.models import Job


class TestBlogModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.title = Job.objects.create(title="Django Testing")
        cls.summary = Job.objects.create(summary="This will be a miracle if this works!")

    def test_model_title(self):
        self.assertEqual(str(self.title), "Django Testing")

    def test_model_body(self):
        self.assertEqual(str(self.summary), "This will be a miracle if this works!")






## run in the command line
# coverage run --omit="*/myvenv/*" manage.py test
# coverage report
# python manage.py test achievements
