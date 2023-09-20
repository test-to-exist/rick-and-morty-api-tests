import os
import unittest

import requests
from jsonschema.validators import validate

from src.config.config_to_env import load_config
from src.schemas.episode_schema import episode_schema


class TestPositiveEpisodeEndpoint(unittest.TestCase):

    def setUp(self):
        load_config()
        self.base_url = os.environ.get('BASEURL')

    def test_episode_should_return_204(self):
        response = requests.get(f"{self.base_url}/episode")
        self.assertEqual(response.status_code, 200)
    def test_episode_should_return_response_with_valid_schema(self):
        response = requests.get(f"{self.base_url}/episode/1")
        self.assertEqual(response.status_code, 200)
        validate(response.json(), schema=episode_schema)
