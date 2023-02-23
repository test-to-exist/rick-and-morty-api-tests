import unittest

import requests
from jsonschema.validators import validate

from schemas.location_schema import location_schema


class TestLocationEndpoint(unittest.TestCase):

    def setUp(self):
        self.base_url = 'https://rickandmortyapi.com/api'

    def test_location_should_return_response_with_valid_schema(self):
        response = requests.get(f"{self.base_url}/location/1")
        self.assertEqual(response.status_code, 200)
        validate(response.json(), schema=location_schema)

    def test_location(self):
        response = requests.get(f"{self.base_url}/location")
        self.assertEqual(response.status_code, 200)
        response_body = response.json()
        self.assertGreater(len(response_body['results']), 0)

        # response = requests.get(f"{self.base_url}/character/1")
        # print(response.json())
        #
        # response = requests.get(f"{self.base_url}/character/1000")
        # print(response.json())
        #
        # response = requests.get(f"{self.base_url}/character/0")
        print(response.json())

        response = requests.get(f"{self.base_url}/location/0")
        # print(0)
        # print(response.json())

        response = requests.get(f"{self.base_url}/location/1")
        # print(1)
        # print(response.json())

        response = requests.get(f"{self.base_url}/location/7")
        # print(7)
        # print(response.json())

        response = requests.get(f"{self.base_url}/location/10000")
        # print(10000)
        # print(response.json())

        response = requests.get(f"{self.base_url}/location/a")
        # print('a')
        # print(response.json())

        response = requests.get(f"{self.base_url}/location/-3")
        # print('-3')
        # print(response.json())

        response = requests.get(f"{self.base_url}/location/3")
        # print('3')
        # print(response.json())
        # response = requests.get(f"{self.base_url}/character/a")
