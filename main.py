from configparser import ConfigParser
import logging
from discord import Client
import sys

# read config at default location
# ./config.ini
config = ConfigParser()
try:
    config.read_file(open("config.ini"))
except FileNotFoundError:
    logging.critical("Unable to locate the configuration file.")
    sys.exit(1)

# spawn discord client instance
# init token from config
bot = Client()
token = config['AUTH']['token']

if __name__ == "__main__":
    bot.run()