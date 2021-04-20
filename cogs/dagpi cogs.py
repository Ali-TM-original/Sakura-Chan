import discord
from discord.ext import commands
from asyncdagpi import ImageFeatures


# for this to work you need bot.dagpi = dagpi in the main

class Dagcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hitler(self, ctx, author: discord.Member = None):
        await ctx.trigger_typing()
        author1 = author
        if author1 is None:
            author1 = ctx.author
        url = str(author1.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.hitler(), url)
        file = discord.File(fp=img.image, filename=f"pixel.{img.format}")
        await ctx.reply(file=file)

    @commands.command()
    async def jail(self, ctx, author: discord.Member = None):
        await ctx.trigger_typing()
        author1 = author
        if author1 is None:
            author1 = ctx.author
        url = str(author1.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.jail(), url)
        file = discord.File(fp=img.image, filename=f"pixel.{img.format}")
        await ctx.reply(file=file)

    @commands.command()
    async def pixel(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.pixel(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def ascii(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.ascii(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def rainbow(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.rainbow(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def captcha(self, ctx, member: discord.Member = None, *, text):
        await ctx.trigger_typing()
        if text is None:
            await ctx.send('You need text to make this work :)')
        elif text is not None:
            url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
            text = str(text)
            img = await self.bot.dagp.image_process(ImageFeatures.captcha(), url=url, text=text)
            await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def colors(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.colors(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def america(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.america(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def communism(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.communism(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def triggered(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.triggered(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def wasted(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.wasted(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def invert(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.invert(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def sobel(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.sobel(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def hog(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.hog(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def triangle(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.triangle(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def blur(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.blur(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def rgb(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.rgb(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def angel(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.angel(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def satan(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.satan(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def delete(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.delete(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def fedora(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.fedora(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def wanted(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.wanted(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def sith(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.sith(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def gay(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.gay(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def trash(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.trash(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def deepfry(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.deepfry(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def charcoal(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.charcoal(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def posterize(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.poster(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def sepai(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.sepia(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def swirl(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.swirl(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def paint(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.paint(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def night(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.night(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def magic(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.magik(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def blackguyes(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        #img = await self.bot.dagp.image_process(ImageFeatures.five_guys_one_girl(), url,
        #                                        url2=str(ctx.message.author.avatar_url))
        img = await self.bot.dagp.image_process(ImageFeatures.five_guys_one_girl(), str(ctx.message.author.avatar_url),url2=url)        
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def whyrugay(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.why_are_you_gay(), str(ctx.message.author.avatar_url),
                                                url2=url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def night(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.night(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def obama(self, ctx, member: discord.Member = None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.obama(), url)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def tweet(self, ctx, member: discord.Member = None, *, text=None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        if text is None:
            text = 'Where would you feel the pain if your leg got cut off'
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.tweet(), url, text=text, username=member.display_name)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def wtf(self, ctx, member: discord.Member = None, *, text1=None):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        if text1 is None:
            text1 = 'Where would you feel the pain if your leg got cut off'
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.modern_meme(), url, text=text1)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def discord(self, ctx, member: discord.Member = None, *, text):
        await ctx.trigger_typing()
        if member is None:
            member = ctx.author
        if text is None:
            text = 'Bitch WTF'
        name = member.display_name
        url = str(member.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.discord(), url, text=text, username=name)
        await ctx.send(file=discord.File(fp=img.image, filename=f"pixel.{img.format}"))

    @commands.command()
    async def shatter(self,ctx):
        url = str(ctx.message.author.avatar_url_as(format="png", static_format="png", size=1024))
        img = await self.bot.dagp.image_process(ImageFeatures.thought_image(), url,text='HOLA')
        await ctx.send(file=discord.File(fp=img.image, filename=f"shatter.{img.format}"))


def setup(bot):
    bot.add_cog(Dagcog(bot))
