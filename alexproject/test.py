import os
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.test import TestCase


class My_test(TestCase):
    def test_secret_key(self):
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        #self.assertNotEqual(SECRET_KEY, 'ola-tech')

        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'Wrong secret key : {e.messages}'
            self.fail(msg)
            #print(e.message)