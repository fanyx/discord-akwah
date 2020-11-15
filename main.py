import logging
import sys
from os import listdir

from discord.ext.commands import Bot
from src.utils.config import build_config

# read config at configured location \\ default to 'config.ini'
config = build_config()

# spawn discord bot instance
# init token from config
bot = Bot(command_prefix="~ak ")
TOKEN = config['AUTH']['token']

# load extensions
for file in os.listdir("src/ext"):
    if file.endswith(".py"):
        name = file[:-3]
        try:
            bot.load_extension(f"src.ext.{name}")
        except NoEntryPointError:
            logging.error(f"Extension {name} cannot be loaded. [No setup function]")
        except ExtensionFailed:
            logging.error(f"Extension {name} failed to load. [Execution error]")

        logging.info("Finished loading extensions.")

if __name__ == "__main__":
    logging.info("Starting bot...")
    # use token from config
    bot.run(TOKEN)