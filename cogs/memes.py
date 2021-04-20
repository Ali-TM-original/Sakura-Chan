from discord.ext import commands
import discord
import os
import asyncpraw

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
USER_AGENT = os.getenv('USER_AGENT')

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['memes'])
    async def meme(self, ctx):
        reddit = asyncpraw.Reddit(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        user_agent=USER_AGENT)


        subreddit = await reddit.subreddit("memes")
        post = await subreddit.random()
        em=discord.Embed(title=post.title, url=post.url, color=0xffcff1)
        em.set_image(url=post.url)
        em.set_footer(text=f"Posted by {post.author} - {post.score} votes.")
        await ctx.send(embed=em)
        await subreddit.close()

    @commands.command()
    async def srchreddit(self, ctx,*,subreddit=None):
        reddit = asyncpraw.Reddit(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        user_agent=USER_AGENT)

        if subreddit is None:
            subreddit = 'memes'
        subreddit = await reddit.subreddit(subreddit)
        post = await subreddit.random()
        em=discord.Embed(title=post.title, url=post.url, color=0xffcff1)
        em.set_image(url=post.url)
        em.set_footer(text=f"Posted by {post.author} - {post.score} votes.")
        await ctx.send(embed=em)
        await subreddit.close()

def setup(bot):
    bot.add_cog(Reddit(bot))
