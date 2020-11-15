from os import getenv

from configparser import ConfigParser

def build_config():
    config_path = getenv("AKWAH_CONFIG_PATH")
    if config_path == None:
        config_path = "config.ini"

    config = ConfigParser()
    config.read_file(open(config_path))
    return config

