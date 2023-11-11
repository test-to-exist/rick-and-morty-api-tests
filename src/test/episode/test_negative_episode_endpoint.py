import os
import unittest

import requests

from src.config.config_to_env import load_config


class TestNegativeEpisodeEndpoint(unittest.TestCase):
    def setUp(self):
        load_config()
        self.base_url = os.environ.get('BASEURL')
        self.endpoint = 'episode'

    def test_episode_should_return_error_for_an_invalid_param(self):
        response = requests.get(f"{self.base_url}/{self.endpoint}/a")
        response_body = response.json()
        self.assertEqual('error' in response_body, True)
        self.assertEqual(response.status_code, 500)

    def test_episode_endpoint_returns_not_found_error_for_episode_out_of_range(self):
        response = requests.get(f"{self.base_url}/{self.endpoint}/1000000")
        response_body = response.json()
        self.assertEqual('error' in response_body, True)
        self.assertEqual(response.status_code, 404)
        response = requests.get(f"{self.base_url}/{self.endpoint}/0")
        response_body = response.json()
        self.assertEqual('error' in response_body, True)
        self.assertEqual(response.status_code, 404)
