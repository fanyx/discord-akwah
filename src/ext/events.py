import discord
from discord.ext import commands
from peewee import *

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Defines all startup checks

        - migrations
        - activity
        - presence
        """
        print(f"[INFO]: Startup complete | {self.bot.user}")

def setup(bot):
    bot.add_cog(Events(bot))