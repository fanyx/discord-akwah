from os import getenv
from sys import exit

from configparser import ConfigParser

def build_config():
    if (config_path := getenv("CONFIG_PATH")) is None:
        config_path = "config.ini"

    config = ConfigParser()
    try:
        config.read_file(open(config_path))
    except FileNotFoundError:
        print("Unable to locate config file. Exiting...")
        exit(1)
    
    return config