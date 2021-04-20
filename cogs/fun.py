from discord.ext import commands
import discord
import json
from PIL import Image
from io import BytesIO
import wikipedia
import random
import asyncio
import upsidedown
import time
from utils.request import req


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def getyoda(self, string):
        htmlst = string.replace(" ", "%20")
        url = f"http://yoda-api.appspot.com/api/v1/yodish?text={htmlst}"
        r = await self.bot.session.get(url)
        resp = await r.json()
        return resp["yodish"]


    @commands.command()
    async def roast(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} do you think i am stupid or what?')
        elif member.id == 410452466631442443:
            await ctx.send(f'Bitch he is my creator. {ctx.author.mention} you can go fuck yourself.')
        elif member is not None and discord.Member.id != 410452466631442443:
            obj = req()
            x = await obj.magic('https://evilinsult.com/generate_insult.php?lang=en&type=json')    
            x = x.decode("utf-8")
            j = json.loads(x)          
            await ctx.send(j['insult'])

    @commands.command()
    async def future(self, ctx, *, question):
        site = random.choice(open("assets/answers.txt").readlines())
        ques = ("Question: " + question)
        ans = ("Answer: " + site)
        embed_var5 = discord.Embed(title=ques, description=ans, color=0x222222)
        await ctx.send(embed=embed_var5)

    @commands.command()
    async def factophobia(self, ctx, fact):
        try:
            obj = req()
            response = await obj.magic(f'https://some-random-api.ml/animal/{fact}')    
            response = response.decode("utf-8")
            j = json.loads(response)
            content = j['fact']
            image = j['image']
            embed = discord.Embed(title=f'Facts about {fact}', description=content, color=0x222222)
            embed.set_image(url=image)
            await ctx.send(embed=embed)
        except Exception as e:
            pass

    # all the facts:
    # Dog
    # Cat
    # Panda
    # Fox
    # Birb
    # Koala
    # Kangaroo
    # Racoon
    # elephant
    # giraffe
    # whale

    @commands.command()
    async def animu(self, ctx, lol):
        try:
            obj = req()
            response = await obj.magic(f'https://some-random-api.ml/animu/{lol}')  
            response = response.decode("utf-8")  
            j = json.loads(response)
            img = j['link']
            embed = discord.Embed(title='Anime!', color=0x222222)
            embed.set_image(url=img)
            await ctx.send(embed=embed)
        except:
            print('Unexpected error occured')

    # for animu lol can be"
    #    1.wink
    #    2.pat
    #    3.hug
    #    4.face - palm

    @commands.command()
    async def encode(self, ctx, *, message):
        await ctx.message.delete()
        obj = req()
        response = await obj.magic(f'https://some-random-api.ml/base64?encode={message}')
        response = response.decode("utf-8")         
        j = json.loads(response)
        b64 = j["base64"]
        await ctx.send(b64)

    @commands.command()
    async def decode(self, ctx, *, message):
        await ctx.message.delete()
        obj = req()
        response = await obj.magic(f'https://some-random-api.ml/base64?decode={message}')
        response = response.decode("utf-8")         
        j = json.loads(response)
        b46 = j['text']
        await ctx.send(b46)

    @commands.command()
    async def spank(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send('Who the fuck are you trying to spank?')
        else:
            template = Image.open('meme 2.0.png')  # 163,77  size=66x81
            author_pic = ctx.author.avatar_url_as(size=64)
            member_pic = member.avatar_url_as(size=64)
            data_author = BytesIO(await author_pic.read())
            data_member = BytesIO(await member_pic.read())
            author_pfp = Image.open(data_author)
            member_pfp = Image.open(data_member)
            template.paste(author_pfp, (163, 77))  # (163, 77)
            template.paste(member_pfp, (151, 214))  # (151, 214)
            template.save('lmao.jpg')
            await ctx.send(file=discord.File('lmao.jpg'))

    @commands.command()
    async def coinflip(self, ctx):
        coinsides = ['Heads', 'Tails']
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}!**")

    @commands.command()
    async def hack(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} who the fuck are you trying to hack?')
        elif member is not None:
            IP = ".".join(map(str, (random.randint(0, 255)
                                    for _ in range(4))))
            user_name = f'{member.display_name}{random.randint(0, 100)}'
            password = random.choice(open("assets/passwords.txt").readlines())
            site = random.choice(open("assets/websites.txt").readlines())
            responses = ['Choke me daddy', 'Sup Beautyful', 'N***a', 'Whore', 'OH YEAH! MORE PLZ', 'You like it deep?',
                         'I only date 14 year olds']
            msg = await ctx.channel.send(f'Starting Scripts!')
            await asyncio.sleep(2)
            await msg.edit(content='Setting up server')
            await asyncio.sleep(1)
            await msg.edit(content='infiltrated the technological systems')
            await asyncio.sleep(0.5)
            await msg.edit(content='Locating IP Address')
            await asyncio.sleep(1.5)
            await msg.edit(content=f'IP fetched. ip={IP}')
            await asyncio.sleep(1)
            await msg.edit(content='Injecting Torjan, Zeus Gameover, CryptoLocker')
            await asyncio.sleep(1)
            await msg.edit(content=f'Finding Discord Credentials.')
            await asyncio.sleep(.1)
            await msg.edit(content=f'Finding Discord Credentials..')
            await asyncio.sleep(.1)
            await msg.edit(content=f'Finding Discord Credentials...')
            await asyncio.sleep(.1)
            await msg.edit(content=f'Finding Discord Credentials...')
            await asyncio.sleep(.2)
            await msg.edit(content=f'Username=**{user_name}**\n'
                                   f'Password=**{password}**')
            await asyncio.sleep(.2)
            await msg.edit(content=f'Hacking Education Records')
            await asyncio.sleep(1)
            await msg.edit(content=f'Changing Grades to F')
            await asyncio.sleep(1)
            await msg.edit(content=f'Fetching Browser History')
            await asyncio.sleep(1)
            await msg.edit(content=f'The most searches site by the user is {site}')
            await asyncio.sleep(1)
            await msg.edit(content=f'Copying all the messages to database')
            await asyncio.sleep(1)
            await msg.edit(content=f'**Last Message sent:** {random.choice(responses)}')
            await asyncio.sleep(1)
            await msg.edit(content=f'**Raising wanted level to 5 stars**')
            await asyncio.sleep(1)
            await msg.edit(content=f'**Hiring Hitman.**')
            await asyncio.sleep(1)
            await msg.edit(content=f'You have Hacked the fuck out of {member.display_name}!\n'
                                   f'Ending the hack!')

    @commands.command()
    async def ovo(self, ctx, *, text):
        ovo = text.replace("l", "v").replace("L", "v").replace("r", "v").replace("R", "v")
        await ctx.send(f"{ovo} ovo")

    @commands.command()
    async def wiki(self, ctx, *, search):
        try:
            wikipedia.set_lang("en")
            summary = wikipedia.summary(search, sentences=5)
            wiki_embed = discord.Embed(title='WikiSearch', color=0x222222)
            wiki_embed.add_field(name=search, value=summary, inline=False)
            await ctx.send(embed=wiki_embed)
        except:
            await ctx.send(f'{search} not found!')

    @commands.command()
    async def ratewaifu(self, ctx, author: discord.Member = None):
        if author is None:
            author = ctx.message.author
        random_rating = random.randint(0, 100)
        embed = discord.Embed(title=f'***{author.display_name} is {random_rating}% good Waifu***', color=0x222222)
        await ctx.send(embed=embed)

    @commands.command()
    async def howgay(self, ctx, author: discord.Member = None):
        if author is None:
            author = ctx.message.author
        random_rating = random.randint(0, 100)
        embed = discord.Embed(title=f'***{author.display_name} is {random_rating}% Gay***', color=0x222222)
        await ctx.send(embed=embed)

    @commands.command()
    async def choose(self, ctx, *args):
        choice = random.choice(args)
        await ctx.send('I chose '+choice)

    @commands.command()
    async def roll_dice(self, ctx, dice:int=3):
        if dice > 20:
            await ctx.send(f'Sorry, but i don\'t have {dice} dice')
            return
        if dice < 1:
            await ctx.send(f'Sorry, but i don\'t have {dice} die')
            return
        a = []
        for x in range(dice):
            a.append(str(random.randint(0, 10)))
        await ctx.send('You Rolled: \n`' + (', '.join(a)) + '`')

    @commands.command()
    async def predict(self, ctx):
        predicate = random.choice(['pseudo text', 'dog', 'cat', 'your mom', 'mr. beaver', 'people'])
        adjective = random.choice(['cool', 'bad', 'awesome', 'big', 'stupid', 'also stupid'])
        await ctx.send(predicate + ' is ' + adjective)

    @commands.command()
    async def scramble(self, ctx, *, text:str):
        await ctx.message.delete()
        a = list(text)
        random.shuffle(a)
        await ctx.send(''.join(a))

    @commands.command()
    async def reverse(self, ctx, *, text:str):
        await ctx.message.delete()
        a = list(text)
        a.reverse()
        await ctx.send(''.join(a))

    @commands.command()
    async def upsidedown(self, ctx, *, text:str):
        await ctx.message.delete()
        text = upsidedown.transform(text)
        await ctx.send(text)

    @commands.command(brief='Catch the pie within the time')
    async def catch(self, ctx):
        embed = discord.Embed(title='Catch the Pie!', color=discord.Color.green(), description='3')
        msg = await ctx.send(embed=embed)
        for x in ['2', '1']:
            await asyncio.sleep(1)
            embed.description = x
            await msg.edit(embed=embed)
        await asyncio.sleep(1)
        embed.description = 'NOW'
        await msg.edit(embed=embed)
        await msg.add_reaction('\U0001f967')
        time_perf = time.perf_counter()
        def check(reaction, user):
            return str(reaction.emoji) == '🥧' and user.name != self.bot.user.name
        
        reaction, user = await self.bot.wait_for('reaction_add', check=check)
        embed.description = f'{user.name} got it in {str(round((time.perf_counter()-time_perf)))} s'
        await msg.edit(embed=embed)


    @commands.command(cooldown_after_parsing=True)
    async def yoda(self, ctx, *, string: str):
        await ctx.trigger_typing()
        guild = ctx.guild
        embed = discord.Embed(title="DAGBOT - YODISH", color=guild.me.color)
        channel = ctx.channel
        y = await self.getyoda(string)
        embed.add_field(name="YODA SAYS", value=y, inline=True)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))
