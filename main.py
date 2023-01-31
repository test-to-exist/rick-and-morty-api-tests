import unittest

import requests
from jsonschema import validate

schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "status": {
            "type": "string"
        },
        "species": {
            "type": "string"
        },
        "type": {
            "type": "string"
        },
        "gender": {
            "type": "string"
        },
        "origin": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "url": {
                    "type": "string"
                }
            },
            "required": [
                "name",
                "url"
            ]
        },
        "location": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "url": {
                    "type": "string"
                }
            },
            "required": [
                "name",
                "url"
            ]
        },
        "image": {
            "type": "string"
        },
        "episode": {
            "type": "array",
            "items": [
                {
                    "type": "string"
                }
            ]
        },
        "url": {
            "type": "string"
        },
        "created": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "name",
        "status",
        "species",
        "type",
        "gender",
        "origin",
        "location",
        "image",
        "episode",
        "url",
        "created"
    ]
}


class TestCharacterEndpoint(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://rickandmortyapi.com/api'

    # POSITIVE character endpoint tests
    def test_character_options(self):
        response = requests.options(f"{self.base_url}/character")
        print(response.headers)

    def test_character_should_return_list(self):
        response = requests.get(f"{self.base_url}/character")
        self.assertEqual(response.status_code, 200)
        response_body = response.json()
        self.assertGreater(len(response_body['results']), 0)

    def test_character_should_return_valid_character(self):
        response = requests.get(f"{self.base_url}/character/1")
        self.assertEqual(response.status_code, 200)
        validate(response.json(), schema=schema)

    def test_character_should_return_specific_list_for_multiple_param(self):
        response = requests.get(f"{self.base_url}/character/1,3,5")
        self.assertEqual(response.status_code, 200)
        response_body = response.json()
        self.assertEqual(len(response_body), 3)

    def test_character_endpoint_should_return_list_when_some_params_empty(self):
        response = requests.get(f"{self.base_url}/character/1,2,3,4,5,,7,,")
        self.assertEqual(response.status_code, 200)
        response_body = response.json()
        self.assertGreater(len(response_body), 0)

    # NEGATIVE character endpoint tests
    def test_character_should_return_error_for_an_invalid_param(self):
        response = requests.get(f"{self.base_url}/character/a")
        response_body = response.json()
        self.assertEqual('error' in response_body, True)
        self.assertEqual(response.status_code, 500)

    def test_character_endpoint_returns_not_found_error_for_character_out_of_range(self):
        response = requests.get(f"{self.base_url}/character/1000000")
        response_body = response.json()
        self.assertEqual('error' in response_body, True)
        self.assertEqual(response.status_code, 404)
        response = requests.get(f"{self.base_url}/character/0")
        response_body = response.json()
        self.assertEqual('error' in response_body, True)
        self.assertEqual(response.status_code, 404)

    def test_character(self):
        response = requests.get(f"{self.base_url}/character/1a")
        print(response.json())

        response = requests.get(f"{self.base_url}/character/0xbe")
        print(response.json())

        response = requests.get(f"{self.base_url}/character/300")
        print(response.json())

        response = requests.get(f"{self.base_url}/character/0xbe")
        print(response.json())

        response = requests.get(f"{self.base_url}/character/01010")
        print(response.json())

        response = requests.get(f"{self.base_url}/character/010")
        print(response.json())

        response = requests.get(f"{self.base_url}/character/0110")
        print(response.json())

        response = requests.get(f"{self.base_url}/character/1,2,3,4,5")
        print(response.json())

        response = requests.get(f"{self.base_url}/character/1,2,3,4,5,")
        print(response.json())

        response = requests.get(f"{self.base_url}/character/1,2,3,4,5,,7,,")
        print(response.json())

        response = requests.get(f"{self.base_url}/character/ , , , , , ")
        print(response.json())

        response = requests.get(f"{self.base_url}/character/1, ,3, ,5")
        print(response.json())

        response = requests.get(f"{self.base_url}/character/1,2,3,4,5")
        print(response.json())

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
        print(0)
        print(response.json())

        response = requests.get(f"{self.base_url}/location/1")
        print(1)
        print(response.json())

        response = requests.get(f"{self.base_url}/location/7")
        print(7)
        print(response.json())

        response = requests.get(f"{self.base_url}/location/10000")
        print(10000)
        print(response.json())

        response = requests.get(f"{self.base_url}/location/a")
        print('a')
        print(response.json())

        response = requests.get(f"{self.base_url}/location/-3")
        print('-3')
        print(response.json())

        response = requests.get(f"{self.base_url}/location/3")
        print('3')
        print(response.json())
        # response = requests.get(f"{self.base_url}/character/a")


if __name__ == '__main__':
    unittest.main()
