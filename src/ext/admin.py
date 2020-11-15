import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def admin(self, ctx):
        """
        manages bot administration
        """
        pass

    @admin.command(name="reload")
    async def admin_reload(self, ctx, module):
        try:
            self.bot.reload_extension(f"src.ext.{module}")
            await ctx.send(f"Reload successful: [{module}]")
        except:
            await ctx.send(f"Reload failed: [{module}]")
        
def setup(bot):
    bot.add_cog(Admin(bot))