import configparser
import os

from src.utils import get_project_root


def load_config():
    root = get_project_root()
    app_config = configparser.ConfigParser()
    config_path = os.path.join(root, 'src/config/config.ini')
    app_config.read(config_path)
    os.environ['BASEURL'] = app_config['APP']['BASEURL']
