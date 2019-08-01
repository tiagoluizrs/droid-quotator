import unittest
from calendar import timegm
from datetime import datetime, timedelta
import time

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from django import get_version
from django.test import TestCase
from django.test.utils import override_settings
from rest_framework import status
from rest_framework.test import APIClient

from rest_framework_jwt import utils, views
from rest_framework_jwt.compat import get_user_model
from rest_framework_jwt.settings import api_settings, DEFAULTS

from . import utils as test_utils

User = get_user_model()

NO_CUSTOM_USER_MODEL = 'Custom User Model only supported after Django 1.5'

orig_datetime = datetime


class LoginTestCase(TestCase):
    def setUp(self):
        self.email = 'tiagoluizribeirodasilva@gmail.com'
        self.password = '#Senha123'

        self.data = {
            'email': self.email,
            'password': self.password
        }
        self.user = User.objects.create_user(
            email=self.email, password=self.password
        )

    def test_login(self):
        client = APIClient(enforce_csrf_checks=True)
        response = client.post('/login/', self.data, format='json')
        decoded_payload = utils.jwt_decode_handler(response.data['token'])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(decoded_payload['email'], self.username)

