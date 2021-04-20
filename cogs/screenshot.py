from discord.ext import commands
import discord
import re
from asyncio import sleep

class Suggest(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command(help="Take a screenshot of a url page")
    async def ss(self, ctx, arg):
        auth = '17038-69yolo69sakura'
        msg = ctx.message
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',msg.content.lower())  
        if urls:
            #imgUrl = 'https://image.thum.io/get/auth/' + auth + '/' + arg
            imgUrl = f"https://image.thum.io/get/auth/17038-69yolo69sakura/{arg}"
            #imgUrl = f"https://image.thum.io/get/auth/17041-15167-5210acccef7b9f84f455fe89088b7cfb{arg}"
            lat = (round(self.bot.latency*1000, 2))
            em = discord.Embed(color=0xffcff1)
            em.set_image(url=imgUrl)
            em.set_footer(text=f"Screenshot latency | {lat}ms.")
            await ctx.send(embed=em)
        else:
            return await ctx.send("This isn't a link.")      

def setup(bot):
    bot.add_cog(Suggest(bot))
