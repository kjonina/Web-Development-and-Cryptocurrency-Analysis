from django.test import TestCase

from achievements.models import Achievement


class TestAchievementsModel(TestCase):

    def test_model_str(self):

        title = Achievement.objects.create(title="Django Testing")
        summary = Achievement.objects.create(summary="It will be a miracle if this works")
        # pub_date  = Achievement.objects.create(pub_date ="2021/05/19 05:05")

        self.assertEqual(str(title), "Django Testing")
        # self.assertEqual(to_datetime(pub_date), "2021/05/19 05:05")
        # self.assertEqual(str(summary), "It will be a miracle if this works")




## run in the command line
# coverage run --omit="*/myvenv/*" manage.py test
# coverage report
# python manage.py test achievements
