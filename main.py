import unittest
import os
import configparser

if __name__ == '__main__':
    app_config = configparser.ConfigParser()
    app_config.read("./config/config.ini")
    os.environ['BASEURL'] = app_config['APP']['BASEURL']
    loader = unittest.TestLoader()
    start_dir = 'test'
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)
