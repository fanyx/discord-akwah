import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx = commands.Context):
        await ctx.send("pong")

def setup(bot):
    bot.add_cog(Test(bot))