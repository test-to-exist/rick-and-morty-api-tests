import unittest

from src.config.config_to_env import load_config

if __name__ == '__main__':
    load_config()
    loader = unittest.TestLoader()
    start_dir = 'test'
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)
