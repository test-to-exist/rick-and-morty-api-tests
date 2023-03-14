import unittest
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    loader = unittest.TestLoader()
    start_dir = 'test'
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)
