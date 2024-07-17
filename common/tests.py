from django.test import TestCase
from common import models


class Test_AboutApp(TestCase):

    def test_model_save_find_order_automatically_about_app(self):
        about_app_1 = models.AboutApp.objects.create(
            caption='nega ilovani ishlatish kerak',
            text='nima')
        self.assertEqual(about_app_1.order, 1)

        about_app_2 = models.AboutApp.objects.create(
            caption='xoxlasang ishlatma',
            text='majburmassan'
        )
        self.assertEqual(about_app_2.order, 2)


class Test_FAQ(TestCase):

    def test_model_save_find_order_automatically_faq(self):
        faq1 = models.FAQ.objects.create(
            question='Test question',
            answer_en='Test answer in English')
        self.assertEqual(faq1.order, 1)

        faq2 = models.FAQ.objects.create(
            question='Test question 2',
            answer_en='Test answer in English 2'
        )
        self.assertEqual(faq2.order, 2)
