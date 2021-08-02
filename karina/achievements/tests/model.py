from django.test import TestCase

from achievements.models import Achievement


class TestAchievementsModel(TestCase):

    def setUp(self):
        self.Achievement1 = Achievement.objects.create(
            title = 'Django Testing',
            pub_date = '2021-07-29 12:51:16.439995',
            summary = 'This will be a miracle if this works!',
            image = 'null')


    def test_model_title(self):
        self.assertEqual(str(self.Achievement1.title), "Django Testing")

    def test_model_body(self):
        self.assertEqual(str(self.Achievement1.summary), "This will be a miracle if this works!")

    def test_pub_date(self):
        self.assertEqual(str(self.Achievement1.pub_date), "2021-07-29 12:51:16.439995")
