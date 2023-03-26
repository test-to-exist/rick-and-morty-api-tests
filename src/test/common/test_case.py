import configparser
import os
import unittest


class ConfigInit:
    def __init__(self):
        app_config = configparser.ConfigParser()
        app_config.read("./../../config/config.ini")
        os.environ['BASEURL'] = app_config['APP']['BASEURL']
        self.base_url = os.environ.get('BASEURL')