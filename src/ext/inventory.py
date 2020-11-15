from discord.ext import commands
from src.utils.config import build_config


class Inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = build_config()

    @commands.group()
    @commands.guild_only()
    async def inventory(self, ctx):
        """
        Manage user's inventory
        
        Usage: ~ak inventory [subcommand]
        """
        pass

    @inventory.command(name="list", aliases=["ls"])
    @commands.guild_only()
    async def inventory_list(self, ctx):
        """
        List user's own inventory

        Usage: ~ak inventory {ls, list}
        """

        # needs database model and connection 
        pass

    @inventory.command(name="use")
    @commands.guild_only()
    async def inventory_use(self, ctx, *, ):
        """
        Use an item in user's inventory

        Usage: ~ak inventory use [itemId]
        """

        pass


