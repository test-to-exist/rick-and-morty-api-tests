import configparser
import os
import unittest

import requests
from jsonschema.validators import validate

from schemas.episode_schema import episode_schema


class TestEpisodeEndpoint(unittest.TestCase):

    def setUp(self):
        app_config = configparser.ConfigParser()
        app_config.read("./../../config/config.ini")
        os.environ['BASEURL'] = app_config['APP']['BASEURL']
        self.base_url = os.environ.get('BASEURL')

    def test_episode_should_return_response_with_valid_schema(self):
        response = requests.get(f"{self.base_url}/episode/1")
        self.assertEqual(response.status_code, 200)
        validate(response.json(), schema=episode_schema)
