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
for file in listdir("src/ext"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"src.ext.{name}")

if __name__ == "__main__":
    print("[INFO]: Starting bot...")
    # use token from config
    bot.run(TOKEN)