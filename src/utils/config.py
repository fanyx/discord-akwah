import os
import logging

from configparser import ConfigParser


def build_config():
    config_path = os.getenv("AKWAH_CONFIG_PATH")
    if config_path == None:
        config_path = "config.ini"
    
    try:
        config_file = open(config_path)
    except FileNotFoundError:
        logging.critical("Unable to locate the configuration file.")
        sys.exit(1)

    config = ConfigParser()
    config.read_file(config_file)
    logging.info("Finished building configuration.")

    return config

