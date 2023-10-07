import os
import unittest

import requests
from jsonschema.validators import validate

from src.config.config_to_env import load_config
from src.schemas.location_schema import location_schema


class TestPositiveLocationEndpoint(unittest.TestCase):

    def setUp(self):
        load_config()
        self.base_url = os.environ.get('BASEURL')
        self.endpoint = 'location'

    def test_location_should_return_response_with_valid_schema(self):
        response = requests.get(f"{self.base_url}/{self.endpoint}/1")
        self.assertEqual(response.status_code, 200)
        validate(response.json(), schema=location_schema)

    def test_location(self):
        response = requests.get(f"{self.base_url}/{self.endpoint}")
        self.assertEqual(response.status_code, 200)
        response_body = response.json()
        self.assertGreater(len(response_body['results']), 0)

        response = requests.get(f"{self.base_url}/{self.endpoint}/0")
        # print(0)
        # print(response.json())

        response = requests.get(f"{self.base_url}/{self.endpoint}/1")
        # print(1)
        # print(response.json())

        response = requests.get(f"{self.base_url}/{self.endpoint}/7")
        # print(7)
        # print(response.json())

        response = requests.get(f"{self.base_url}/{self.endpoint}/10000")
        # print(10000)
        # print(response.json())

        response = requests.get(f"{self.base_url}/{self.endpoint}/a")
        # print('a')
        # print(response.json())

        response = requests.get(f"{self.base_url}/{self.endpoint}/-3")
        # print('-3')
        # print(response.json())

        response = requests.get(f"{self.base_url}/{self.endpoint}/3")
        # print('3')
        # print(response.json())
