import aiozaneapi
import discord
from discord.ext import commands

class Zanecog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def floor(self,ctx, author: discord.Member = None):
        if author is None:
            author = ctx.message.author
        else:
            author = author    
        author = author.avatar_url
        image = await self.bot.zane.floor(str(author))
        file = discord.File(image, "floor.gif")
        await ctx.send(file=file)

    @commands.command()
    async def braille(self,ctx, author: discord.Member = None):
        if author is None:
            author = ctx.message.author
        else:
            author=author
        image = await self.bot.zane.braille(str(author.avatar_url))
        await ctx.send(image)


def setup(bot):
    bot.add_cog(Zanecog(bot))