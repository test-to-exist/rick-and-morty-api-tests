import os
import unittest

import requests
from jsonschema import validate

from src.config.config_to_env import load_config
from src.schemas.character_schema import character_schema

filter_param_list = [
    ('name', 'Rick'),
    ('status', 'Alive'),
    ('species', 'Human'),
    ('type', 'Parasite'),
    ('gender', 'Male')
]


class TestPositiveCharacterEndpoint(unittest.TestCase):
    def setUp(self):
        load_config()
        self.base_url = os.environ.get('BASEURL')
        self.endpoint = 'character'

    def test_character_options_returns_status_204(self):
        response = requests.options(f"{self.base_url}/{self.endpoint}")
        self.assertEqual(response.status_code, 204)

    def test_character_should_return_list(self):
        response = requests.get(f"{self.base_url}/{self.endpoint}")
        self.assertEqual(response.status_code, 200)
        response_body = response.json()
        self.assertGreater(len(response_body['results']), 0)

    def test_character_should_return_response_with_valid_schema(self):
        response = requests.get(f"{self.base_url}/{self.endpoint}/1")
        self.assertEqual(response.status_code, 200)
        validate(response.json(), schema=character_schema)

    def test_character_should_return_specific_list_for_multiple_param(self):
        response = requests.get(f"{self.base_url}/{self.endpoint}/1,3,5")
        self.assertEqual(response.status_code, 200)
        response_body = response.json()
        self.assertEqual(len(response_body), 3)

    def test_character_endpoint_should_return_list_when_some_params_empty(self):
        response = requests.get(f"{self.base_url}/{self.endpoint}/1,2,3,4,5,,7,,")
        self.assertEqual(response.status_code, 200)
        response_body = response.json()
        self.assertGreater(len(response_body), 0)

    def test_character_list_can_be_filtered(self):
        print("\n")
        for filter_name, filter_val in filter_param_list:
            with self.subTest(filter_name=filter_name, filter_val=filter_val):
                print(f"Character list filtering Subtest - Filtering by: \"{filter_name}\" with value: \"{filter_val}\"")
                response = requests.get(f"{self.base_url}/{self.endpoint}?{filter_name}={filter_val}")
                self.assertEqual(response.status_code, 200)
                response_body = response.json()
                self.assertTrue(len(response_body['results']) > 0)
                for value in map(lambda x: x[filter_name], response_body['results']):
                    self.assertTrue(filter_val in value)
