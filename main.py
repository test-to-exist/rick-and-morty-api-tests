import requests
import unittest


class TestCharacterEndpoint(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://rickandmortyapi.com/api'

    def test_character_endpoint(self):
        response = requests.get(f"{self.base_url}/character")
        self.assertEqual(response.status_code, 200)
        response_body = response.json()
        self.assertGreater(len(response_body['results']), 0)

        response = requests.get(f"{self.base_url}/character/1")
        print(response.json())


if __name__ == '__main__':
    unittest.main()