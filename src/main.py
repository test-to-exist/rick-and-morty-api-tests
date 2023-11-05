import io
import unittest

import xmlrunner
from xmlrunner.extra.xunit_plugin import transform

from src.config.config_to_env import load_config

if __name__ == '__main__':
    load_config()
    loader = unittest.TestLoader()
    start_dir = 'test'
    suite = loader.discover(start_dir)

    out = io.BytesIO()
    unittest.main(
        failfast=False, buffer=False, catchbreak=False, exit=False)

    runner = xmlrunner.XMLTestRunner(output=out)
    # runner = unittest.TextTestRunner()
    runner.run(suite)

    with open('TEST-report.xml', 'wb') as report:
        report.write(transform(out.getvalue()))

