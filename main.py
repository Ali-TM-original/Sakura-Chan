import discord
from discord.ext import commands, tasks
import json
import requests
import random
import asyncio
import os
import datetime
from datetime import datetime
import aiosqlite
from asyncdagpi import Client
from keep_alive import keep_alive
from googlesearch import search
import aiozaneapi
import logging
import urllib3



token = os.getenv('SECRET')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
USER_AGENT = os.getenv('USER_AGENT')
DAGPI = os.getenv('DAGPI')
APP_ID = os.getenv('WEATHER_APPID')
ZANE = os.getenv('ZANE')

async def _check_prefix(bot,message):
    async with aiosqlite.connect("prefix.db") as db:
        prefix  = ["sakura ", "Sakura "]
        cur = await db.cursor()
        await cur.execute('create table if not exists Streams(guild_id TEXT,prefix TEXT)')
        await cur.execute("SELECT * FROM Streams WHERE guild_id = ?", (message.guild.id,))
        result_prefix = await cur.fetchone()
        if result_prefix:
            return result_prefix
        else:
            return prefix    

bot = commands.Bot(command_prefix=_check_prefix,
                   intents=discord.Intents.all())

logging.getLogger('asyncio').setLevel(logging.CRITICAL)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

zane = aiozaneapi.Client(ZANE)
bot.zane = zane
bot.remove_command('help')

dagp = Client(DAGPI)
bot.dagp = dagp

headers = {'Authorization': DAGPI}


@tasks.loop(seconds=60)
async def change_status():
    status = f'Sakura Chan watching over {len(bot.guilds)} servers'
    await bot.change_presence(activity=discord.Game(status))


@bot.event
async def on_ready():
    print('we are ready to go. logged in as {0.user}'.format(bot))
    change_status.start()
    """
    for server in bot.guilds:
        print(server)
        for channel in server.text_channels:
            a = str(channel.type)
            if a.lower() == 'text':
                try:
                    invitelinknew = await channel.create_invite(destination=channel)
                    print(f'Invite link: {invitelinknew}, server:{server} ')
                    f = open("svinvite.txt", "a")
                    f.write(f'Invite link: {invitelinknew}, server:{server} ')
                    f.close()
                    break
                except discord.errors.Forbidden:
                    pass    
"""

@bot.event
async def on_message(message):
    if message.content == "./prefix":
        async with aiosqlite.connect("prefix.db") as db:
            cur = await db.cursor()
            #cur.execute('CREATE TABLE Transactions(Date TEXT, Number TEXT, Type TEXT, From TEXT, To TEXT, Amount REAL)')
            await cur.execute('create table if not exists Streams(guild_id TEXT,prefix TEXT)')
            await cur.execute("SELECT prefix FROM Streams WHERE guild_id = ?", (message.guild.id,))
            result_prefix = await cur.fetchone()
            if result_prefix is None:
                result_prefix = 'sakura'
            else:
                result_prefix = result_prefix[0]    
        await message.channel.send(f"My Prefix for this guild is {result_prefix}")
    else:                 
        await bot.process_commands(message)


@bot.event
async def on_member_join(member):
    guild_id = 791312826874200125
    genuine_guild_id = 814195365359386674
    if member.guild.id == guild_id:
        embed = discord.Embed(title=f'Welcome {member.name}', color=0x8E44AD)
        embed.add_field(
            name='***Thank you for joining and Support***',
            value=
            '***Really appreciate it. Stay here and give us Feedback on the bot.***',
            inline=False)
        await bot.get_channel(798586934062350386).send(embed=embed)
    elif member.guild.id == genuine_guild_id:
        embed = discord.Embed(title=f"Welcome {member.name} to Genuine's Cord", color=0x8E44AD)
        embed.add_field(
            name='***Thank you for joining ***',
            value=
            '***How about you take a look around familiarize and enjoy the community***',
            inline=False)
        embed.set_thumbnail(url=member.avatar_url)    
        await bot.get_channel(814195365359386678).send(embed=embed)           
    else:
        pass


@bot.event
async def on_member_remove(member):
    guild_id = 791312826874200125
    if member.guild.id == guild_id:
        embed = discord.Embed(title=f'{member.name} Left the Channel',
                              color=0x8E44AD)
        embed.add_field(
            name='***Another soilder down***',
            value='***Mission Failed boys we will get em next time***',
            inline=False)
        await bot.get_channel(805460410056179733).send(embed=embed)
    else:
        pass


@bot.event
async def on_guild_join(guild):
    channel = bot.get_channel(805106949825364018)
    myEmbed = discord.Embed(title=f'I have been Added to {guild.name}',
                            color=0x8E44AD,
                            timestamp=datetime.utcnow())
    myEmbed.set_thumbnail(url=guild.icon_url)
    myEmbed.add_field(name=f'Added to {guild.name}',
                      value=f'Member Count: {guild.member_count}')
    myEmbed.add_field(name='Server Owner:', value=f'{guild.owner.name}')
    myEmbed.set_footer(text=f'I am now in  {len(bot.guilds)} Servers')
    print(f"{guild.owner}")
    await channel.send(embed=myEmbed)


@bot.event
async def on_guild_remove(guild):
    channel = bot.get_channel(805106972613017642)
    try:
        embed = discord.Embed(title='I have been removed from a server!',
                            color=0x8E44AD,
                            timestamp=datetime.utcnow())
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name=f'Server: {guild.name}',
                        value=f'Member Count: {guild.member_count}')
        embed.add_field(name='Server Owner:', value=f'{guild.owner.name}')
        embed.set_footer(text=f'I am now in  {len(bot.guilds)} Servers')
        await channel.send(embed=embed)
    except AttributeError:
        pass
    except discord.errors.HTTPException:
        pass  

@bot.command()
@commands.has_permissions(administrator= True)
async def prefix(ctx,*,prefix=None):
    if prefix is None:
        await ctx.send("WTF ARE YOU DOING LMAO")
    else:
        prefix = prefix + " "
        async with aiosqlite.connect("prefix.db") as db:
            cur = await db.cursor()
            await cur.execute('create table if not exists Streams(guild_id TEXT,prefix TEXT)')
            await db.commit()
            await cur.execute("update Streams SET prefix = ? where guild_id=?", (prefix, ctx.message.guild.id))
            await db.commit()
        await ctx.send(f"I Have changed the prefix of this guild to {prefix} ")
        async with aiosqlite.connect("prefix.db") as db:
            cur = await db.cursor()
            await cur.execute('create table if not exists Streams(guild_id TEXT,prefix TEXT)')
            await db.commit()
            await cur.execute("SELECT * FROM Streams WHERE guild_id = ?", (ctx.message.guild.id,))
            await db.commit()
            result_prefix = await cur.fetchone()
            if result_prefix is None:
                await cur.execute('INSERT into Streams(guild_id, prefix) values(?,?)',(ctx.message.guild.id,prefix))
                await db.commit()

@bot.command()
async def reload(ctx):
    """Reloads a module."""
    if ctx.message.author.id == 410452466631442443:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.unload_extension(f'cogs.{filename[:-3]}')
                bot.load_extension(f'cogs.{filename[:-3]}')
        await ctx.send('**Bot has been refreshed**')
    else:
        await ctx.send('**I only let my creator touch me, I am shy 🤭**')


@bot.command()
async def sv_say(ctx, *, message):
    if ctx.message.author.id == 410452466631442443:
        embedvar = discord.Embed(title='Message From Creator',
                                 description='Listen Carefully',
                                 color=0x8E44AD)
        embedvar.add_field(name='Message ;)', value=message, inline=False)
        for guild in bot.guilds:
            await guild.text_channels[0].send(embed=embedvar)
    elif ctx.message.author.id != 410452466631442443:
        pass


# guild.text_channels[0].send(<message>)
@bot.command()
async def say(ctx, *, msg):
    await ctx.send(msg, tts=True)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.NoPrivateMessage):
        pass
    if isinstance(error, commands.BotMissingAnyRole):
        pass
    if isinstance(error, commands.ArgumentParsingError):
        pass
    if isinstance(error, commands.MissingRequiredArgument):
        pass
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.BotMissingPermissions):
        pass
    if isinstance(error, commands.DisabledCommand):
        pass


@bot.command()
async def fact(ctx):
    response = requests.get('https://api.dagpi.xyz/data/fact', headers=headers)
    facts = json.loads(response.text)
    fact = facts['fact']
    await ctx.send(f'**{fact}**')


@bot.command()
async def waifu(ctx):
    response = requests.get('https://api.dagpi.xyz/data/waifu',
                            headers=headers)
    waifu = json.loads(response.text)
    x = waifu['display_picture']
    embedvar10 = discord.Embed(title=f'{ctx.author.name} waifu',
                               color=0x8E44AD)
    embedvar10.set_image(url=x)
    embedvar10.set_footer(text=f'***requested by {ctx.author.name}***')
    await ctx.send(embed=embedvar10)


@bot.command()
async def logo(ctx):
    author = ctx.message.author
    channel = ctx.channel
    response = requests.get('https://api.dagpi.xyz/data/logo', headers=headers)
    logo = json.loads(response.text)
    q = logo['question'].lower()
    a = logo['brand'].lower()

    answer = logo['brand'].lower()
    embedvar10 = discord.Embed(title=f'Guess the logo.', color=0x8E44AD)
    embedvar10.set_image(url=q)
    embedvar10.set_footer(text=f'requested by {ctx.author.name}')
    await ctx.send(embed=embedvar10)
    await ctx.send(f'***Start guessing bish,You only have 20seconds***')

    def check(m):
        return m.author == author and m.channel == channel

    x = 0
    y = False
    for i in range(0, 3):
        x += 1
        try:
            response = await bot.wait_for('message', check=check, timeout=20)
            user_guess = str(response.content)
            if user_guess == a:
                await ctx.send(
                    f'{ctx.author.mention} guessed the correct logo :sunglasses:'
                )
                y = True
                break
            elif user_guess != a:
                await ctx.send(
                    f'{ctx.author.mention} that is not the right answer :(. Guess {x} of 3 '
                )
        except asyncio.TimeoutError:
            await ctx.send(f'{ctx.author.mention} you ran out of time')
            break
    if x == 3:
        await ctx.send(
            f'{ctx.author.mention} ran out of tries. the word was {answer}')
    elif y:
        await ctx.send(
            f'{ctx.author.mention} ended the guessing game by guessing the correct logo'
        )


@bot.command(aliases=['rockpaperscissors'])
async def rps(ctx):
    emoji = ['\N{curling stone}', '\N{NEWSPAPER}', '\N{BLACK SCISSORS}']
    list_emj = ['🥌', '📰', '✂']
    choice = random.choice(list_emj)
    player = ctx.message.author
    channel = ctx.message.channel
    embedv = discord.Embed(title='Rock Paper Scissor', color=0x222222)
    embedv.add_field(name='Rock', value='React with 🥌 for Rock', inline=False)
    embedv.add_field(name='Paper',
                     value='React with 📰  for Paper',
                     inline=False)
    embedv.add_field(name='Scissor',
                     value='React with ✂ for Scissor',
                     inline=False)
    embedv.timestamp = ctx.message.created_at
    m = await ctx.send(embed=embedv)
    for emj in emoji:
        await m.add_reaction(emj)
    ID = m.id
    print(choice)

    # author = ctx.author

    def check(reaction, user):
        if user == bot.user:
            pass
        elif user == ctx.author:
            return user == player and str(
                reaction.emoji
            ) == "🥌" or "📰 " or "✂" and reaction.message.id == ID
        else:
            pass

    try:
        reaction, user = await bot.wait_for('reaction_add',
                                            timeout=10,
                                            check=check)
        if str(reaction.emoji) == "🥌":
            if choice == '🥌':
                await ctx.send(
                    f'***Its a draw computer chose the same as you***')
            elif choice == '📰':
                await ctx.send(f'***Lmao noob wtf! you lost from a bot***')
            elif choice == '✂':
                await ctx.send(f'***Hmm nice you fucked that scissor.***')
        elif str(reaction.emoji) == "📰":
            if choice == '🥌':
                await ctx.send(f'***Its impressive how you win so easily***')
            elif choice == '📰':
                await ctx.send(
                    f'***Its a draw computer chose the same as you***')
            elif choice == '✂':
                await ctx.send(
                    f'***looks like you got your dick cut off by a scissor looser!***'
                )
        elif str(reaction.emoji) == "✂":
            if choice == '🥌':
                await ctx.send(f'***Get Fucked by a rock kid***')
            elif choice == '📰':
                await ctx.send(f'***Its impressive how you win so easily***')
            elif choice == '✂':
                await ctx.send(
                    f'***Its a draw computer chose the same as you***')

    except asyncio.TimeoutError:
        await ctx.send(f'{player.mention} ran out of time. Deleting Embed.')
        msg = await channel.fetch_message(ID)
        await msg.delete()


@bot.command()
async def guess(ctx):
    random_number = random.randint(0, 50)
    author = ctx.message.author
    channel = ctx.channel
    await ctx.send(f'{ctx.author.mention} started a guessing game')
    await ctx.send('Start guessing your numbah bish')

    x = 0
    y = False

    def msg_check(m):
        return m.author == author and m.channel == channel

    for i in range(0, 5):
        x += 1
        try:
            response = await bot.wait_for('message',
                                          check=msg_check,
                                          timeout=10.0)
            user_guess = int(response.content)

            if user_guess > int(random_number):
                await ctx.send('Your guess was higher than the secret number')

            if user_guess < int(random_number):
                await ctx.send('your guess was lower than the secret number'
                               )  # with str working fine.

            if user_guess == int(random_number):
                y = True
                await ctx.send('here have a Dollar $ for guessing correctly')
                break
        except asyncio.TimeoutError:
            await ctx.send(f'{ctx.author.mention} ran out of time')
            break

    if x == 5 and y is False:
        await ctx.send(
            f'lmao looser you ran out of tries. the number was {random_number}'
        )
    elif y:
        await ctx.send(
            f'{ctx.author.mention} ended the guessing game by guessing the correct number'
        )


@bot.command()
async def help(ctx):
    reactions = ['⏭', '◀', '▶', '⏮', "🛑"]
    author = ctx.message.author
    help_page1 = discord.Embed(title='Help', color=0x8E44AD)
    help_page1.add_field(name='***Game Commands***',
                         value='***React down to page 2***',
                         inline=False)
    help_page1.add_field(name='***Utils***',
                         value='***React down to page 3***',
                         inline=False)
    help_page1.add_field(name='***Music***',
                         value='***React down to page 4***',
                         inline=False)
    help_page1.add_field(name='***Moderation***',
                         value='***React down to page 5***',
                         inline=False)
    help_page1.add_field(name='***Image***',
                         value='***React down to page 6-8***',
                         inline=False)
    help_page1.add_field(name='***Fun***',
                         value='***React down to page 7***',
                         inline=False)
    help_page1.add_field(
        name='***How this works***',
        value="Add a reaction,wait,remove reaction then add to change page",
        inline=False)
    m = await ctx.send(embed=help_page1)
    for emj in reactions:
        await m.add_reaction(emj)

    message_id = m.id

    def check(reaction, user):
        if user == bot.user:
            pass
        elif user == ctx.author:
            return user and reaction.message.id == message_id and str(
                reaction.emoji) == "⏭" or str(reaction.emoji) == '◀' or str(
                    reaction.emoji) == '▶' or str(
                        reaction.emoji) == "⏮" or str(reaction.emoji) == "🛑"
        else:
            pass

    def embeds(num):
        embed1 = discord.Embed(title='***GAME Commands***', color=0x8E44AD)
        embed1.add_field(name='***sakura rps***',
                         value='**Reaction Based Rock Paper Scissor game**',
                         inline=False)
        embed1.add_field(name='***sakura guess***',
                         value='**Number guessing game**',
                         inline=False)
        embed1.add_field(name='***sakura logo***',
                         value='**Logo guessing game play if you are pero**',
                         inline=False)
        embed1.add_field(name='***sakura catch***',
                         value='**Lets see who catches the pie**',
                         inline=False)

        embed2 = discord.Embed(title='***UTILS Commands***', color=0x8E44AD)
        embed2.add_field(name='***sakura info***',
                         value="**Returns bot's version**",
                         inline=False)
        embed2.add_field(name='***sakura av***',
                         value="**Returns avatar of mentioned member**",
                         inline=False)
        embed2.add_field(name='***sakura sv***',
                         value="**Returns servers info**",
                         inline=False)
        embed2.add_field(name='***sakura whois***',
                         value="**Returns members info**",
                         inline=False)
        embed2.add_field(name='***sakura weather***',
                         value='**Returns weather of a location**',
                         inline=False)
        embed2.add_field(name='***<prefix if not set use default one> prefix <prefix>***',
                         value='**set prefix for your server**',
                         inline=False)                         

        embed3 = discord.Embed(title='***Musicaa Commands 24/7 STREAM***',
                               color=0x8E44AD)
        embed3.add_field(name='***sakura search_video <name>***',
                         value='**returns a youtube link of desired video**',
                         inline=False)
        embed3.add_field(name='***sakura join***',
                         value='**Joins your VC**',
                         inline=False)
        embed3.add_field(name='***sakura leave***',
                         value='**Leaves your VC**',
                         inline=False)
        embed3.add_field(name='***sakura play***',
                         value='**Plays ROCK RADIO**',
                         inline=False)
        embed3.add_field(name='***sakura pause***',
                         value='**Pauses Radio**',
                         inline=False)
        embed3.add_field(name='***sakura resume***',
                         value='**Resumes Radio**',
                         inline=False)
        embed3.add_field(name='***sakura volume <int>***',
                         value='**Set Volume of Stream**',
                         inline=False)
        embed3.add_field(name='***sakura play chill***',
                         value='**Plays Chill Mix**',
                         inline=False)

        embed4 = discord.Embed(title='***Moderation Commands***',
                               color=0x8E44AD)
        embed4.add_field(name='***sakura clear <amount>***',
                         value='Clears messages',
                         inline=False)
        embed4.add_field(name='***sakura kick <member> <reason>***',
                         value='**Kicks member**',
                         inline=False)
        embed4.add_field(name='***sakura ban <member> <reason>***',
                         value='**Bans members**',
                         inline=False)
        embed4.add_field(name='***sakura unban <member> <reason>***',
                         value='**unbans members**',
                         inline=False)
        embed4.add_field(name='***sakura length***',
                         value='**Shows amount of server i am in**',
                         inline=False)
        embed4.add_field(name='***sakura ban_list***',
                         value='**Shows list of banned member in a server**',
                         inline=False)

        embed5 = discord.Embed(title='***Image Commands***', color=0x8E44AD)
        embed5.add_field(name='***sakura spank <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed5.add_field(name='***sakura canny <member>***',
                         value='**Try to find out**',
                         inline=False)                         
        embed5.add_field(name='***sakura hitler <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed5.add_field(name='***sakura jail <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed5.add_field(name='***sakura pixel <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed5.add_field(name='***sakura ascii <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed5.add_field(name='***sakura rainbow <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed5.add_field(name='***sakura captcha <member> <text>***',
                         value='**Try to find out**',
                         inline=False)
        embed5.add_field(name='***sakura colors <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed5.add_field(name='***sakura america <member>***',
                         value='**Try to find out**',
                         inline=False)

        embed6 = discord.Embed(title='***Image Commands 2***', color=0x8E44AD)
        embed6.add_field(name='***sakura triggered <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed6.add_field(name='***sakura wasted <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed6.add_field(name='***sakura invert <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed6.add_field(name='***sakura sobel <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed6.add_field(name='***sakura hog <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed6.add_field(name='***sakura triangle <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed6.add_field(name='***sakura blur <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed6.add_field(name='***sakura rgb <member>***',
                         value='**Try to find out**',
                         inline=False)

        embed7 = discord.Embed(title='***Image Commands 3***', color=0x8E44AD)
        embed7.add_field(name='***sakura angel <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed7.add_field(name='***sakura satan <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed7.add_field(name='***sakura delete <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed7.add_field(name='***sakura fedora <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed7.add_field(name='***sakura wanted <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed7.add_field(name='***sakura sith <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed7.add_field(name='***sakura gay <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed7.add_field(name='***sakura trash <member>***',
                         value='**Try to find out**',
                         inline=False)

        embed8 = discord.Embed(title='***Image Commands 4***', color=0x8E44AD)
        embed8.add_field(name='***sakura deepfry <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed8.add_field(name='***sakura charcol <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed8.add_field(name='***sakura posterize <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed8.add_field(name='***sakura sepai <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed8.add_field(name='***sakura swirl <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed8.add_field(name='***sakura paint <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed8.add_field(name='***sakura night <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed8.add_field(name='***sakura magic <member>***',
                         value='**Try to find out**',
                         inline=False)

        embed9 = discord.Embed(title='***Image Commands 5***', color=0x8E44AD)
        embed9.add_field(name='***sakura blackguyes <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed9.add_field(name='***sakura whyrugay <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed9.add_field(name='***sakura night <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed9.add_field(name='***sakura obama <member>***',
                         value='**Try to find out**',
                         inline=False)
        embed9.add_field(name='***sakura tweet <member> <text>***',
                         value='**Try to find out**',
                         inline=False)
        embed9.add_field(name='***sakura wtf <member> <text>***',
                         value='**Try to find out**',
                         inline=False)
        embed9.add_field(name='***sakura discord <member> <text>***',
                         value='**Try to find out**',
                         inline=False)

        embed10 = discord.Embed(title='***Fun Commands***', color=0x8E44AD)
        embed10.add_field(name='***sakura roast <member>***',
                          value='**Roasts people**',
                          inline=False)
        embed10.add_field(name='***sakura future <question>***',
                          value='**Predicts your future**',
                          inline=False)
        embed10.add_field(name='***sakura factophobia <animal>***',
                          value='**Returns animal facts**',
                          inline=False)
        embed10.add_field(
            name='***sakura animu <type(hug,pat,wink,face-palm)>***',
            value='**Returns anime gif**',
            inline=False)
        embed10.add_field(name='***sakura encode <message>***',
                          value='**This should be fairly simple**',
                          inline=False)
        embed10.add_field(name='***sakura decode <message>***',
                          value='**This should be fairly simple**',
                          inline=False)
        embed10.add_field(name='***sakura coinflip***',
                          value='**This should be fairly simple**',
                          inline=False)
        embed10.add_field(name='***sakura hack <member>***',
                          value='**Wanna hack your friend? or maybe enemy?**',
                          inline=False)
        embed10.add_field(name='***sakura wiki <search>***',
                          value='**Search wikipedia with ease**',
                          inline=False)
        embed10.add_field(name='***sakura ratewaifu***',
                          value='**Rates you **',
                          inline=False)
        embed10.add_field(name='***sakura howgay***',
                          value='**Rates you**',
                          inline=False)
        embed10.add_field(name='***sakura ovo <text>***',
                          value='**OVO**',
                          inline=False)
        embed10.add_field(name='***sakura choose <choices>***',
                          value='**Chooses random obj**',
                          inline=False)
        embed10.add_field(name='***sakura predict***',
                          value='**Damn!**',
                          inline=False)
        embed10.add_field(name='***sakura reverse <text>***',
                          value='**reverses text**',
                          inline=False)
        embed10.add_field(name='***sakura scramble <text>***',
                          value='**scrambles text**',
                          inline=False)
        embed10.add_field(name='***sakura upsidedown <text>***',
                          value='**upsidedown text**',
                          inline=False)

        embed11 = discord.Embed(title='***Random Commands***', color=0x8E44AD)
        embed11.add_field(name='***sakura meme***',
                          value='**Returns a meme**',
                          inline=False)
        embed11.add_field(name='***sakura srchreddit <subreddit>***',
                          value='**Search Reddit with ease**',
                          inline=False)
        embed11.add_field(name='***sakura fact***',
                          value='**Returns a random fact**',
                          inline=False)
        embed11.add_field(name='***sakura waifu***',
                          value='**You horny today?**',
                          inline=False)
        embed11.add_field(name='***sakura translate <language><text>***',
                          value='**Translator**',
                          inline=False)
        embed11.add_field(name='***sakura detect <language>***',
                          value='**Detects language**',
                          inline=False)
        embed11.add_field(name='***sakura google <Query>***',
                          value='**Returns 3 google search links**',
                          inline=False)
        embed11.add_field(name='***sakura weather <place>***',
                          value='**Tells weather of a location**',
                          inline=False)
        embed11.add_field(
            name='***sakura invite***',
            value='**Returns a invite link to bot and support server**',
            inline=False)

        embed12 = discord.Embed(title='**Sound Board**', color=0x8E44AD)
        embed12.add_field(name="***Sakura bsdk***",
                          value="**Indian meme**",
                          inline=False)
        embed12.add_field(name="***Sakura why***",
                          value="**Why are you gay?**",
                          inline=False)
        embed12.add_field(name="***bombplanted***",
                          value="**Bomb has been planted**",
                          inline=False)
        embed12.add_field(name="***bear_scream***",
                          value="***Sakura just got hit on her balls :O***",
                          inline=False)

        if num == 2:
            return embed1
        elif num == 3:
            return embed2
        elif num == 4:
            return embed3
        if num == 5:
            return embed4
        if num == 6:
            return embed5
        if num == 7:
            return embed6
        if num == 8:
            return embed7
        if num == 9:
            return embed8
        if num == 10:
            return embed9
        if num == 11:
            return embed10
        if num == 12:
            return embed11
        if num == 13:
            return embed12

    num = 1
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add',
                                                timeout=100,
                                                check=check)
            if str(reaction.emoji) == "⏭":
                num = 13
                await m.edit(embed=embeds(num))
            if str(reaction.emoji) == "◀":
                if num < 3:
                    pass
                else:
                    num = num - 1
                await m.edit(embed=embeds(num))
            if str(reaction.emoji) == "▶":
                if num >= 13:
                    pass
                else:
                    num += 1
                    await m.edit(embed=embeds(num))
            if str(reaction.emoji) == "⏮":
                num = 2
                await m.edit(embed=embeds(num))
            if str(reaction.emoji) == "🛑":
                break

        except asyncio.TimeoutError:
            break


@bot.command()
async def weather(ctx, location):
    try:
        response = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={APP_ID}'
        )
        weather = json.loads(response.content)
        icon = weather['weather'][0]['icon']
        description1 = weather['weather'][0]['main']
        description2 = weather['weather'][0]['description']
        avg_temp = weather['main']['temp']
        max_temp = weather['main']['temp_max']
        min_temp = weather['main']['temp_min']
        pressure = weather['main']['pressure']
        Humidity = weather['main']['humidity']
        avg_temp_celcius = round((int(avg_temp) - 273.15))
        min_temp_celcius = round(int(min_temp) - 273.15)
        max_temp_celcius = round(int(max_temp) - 273.15)

        icon_url = f'https://openweathermap.org/img/wn/{icon}@2x.png'

        weather_embed = discord.Embed(
            title=f'Weather of {location}',
            description=f'{description1}:{description2}',
            color=0x8E44AD)
        weather_embed.set_thumbnail(url=icon_url)
        weather_embed.add_field(name='***Location:***',
                                value=f'🌐City: {location}',
                                inline=False)
        weather_embed.add_field(
            name='***weather***',
            value=
            f'***🌡️Current Temp: *** {avg_temp_celcius} Celcius\n*** 🌡️Max Temp: *** {max_temp_celcius} Celcius \n ***🌡️Min Temp: *** {min_temp_celcius} Celcius \n ***💧Humidity: *** {Humidity}%'
        )
        weather_embed.set_footer(icon_url=icon_url,
                                 text=f'Requested by {ctx.author.name}.')
        await ctx.send(embed=weather_embed)
    except:
        await ctx.send('Please enter a valid location')


@bot.command()
async def google(ctx, *, srch):
    embed = discord.Embed(title=f'Results for your search {srch}:',
                          color=0x8E44AD)
    try:
        for j in search(srch, tld="co.in", num=3, stop=3, pause=2):
            embed.add_field(name='Links:', value=j, inline=False)
    except:
        embed.add_field(name='BEEP BOP!',
                        value='Could not process your query',
                        inline=False)
    await ctx.send(embed=embed)


@bot.command(aliases=['support'])
async def invite(ctx):
    link = 'https://discord.gg/bHnnREvEsc'
    invite = 'https://discord.com/api/oauth2/authorize?client_id=805392535660003369&permissions=8&scope=bot'
    embed = discord.Embed(title='***Support***',
                          description='**For support contact the creator @**',
                          color=0x8E44AD)
    embed.add_field(name='**Support Server:**',
                    value=f'[Support server!]({link})',
                    inline=False)
    embed.add_field(name='**Invite link:**',
                    value=f'[Invite Link!]({invite})',
                    inline=False)
    await ctx.send(embed=embed)


keep_alive()
bot.run(token)

# another one bites the dust
