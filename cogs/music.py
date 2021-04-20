import aiosqlite
import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.ext.commands import CommandInvokeError
from discord.utils import get


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def _check_stream(self,guild):
        STREAMING = False
        async with aiosqlite.connect("STREAMS.db") as db:
            cur = await db.cursor()
            await cur.execute('create table if not exists Streams("guild_id" TEXT,"streaming" INTEGER)')
            await cur.execute(f'select guild_id from Streams where guild_id="{guild}"')
            result_userID = await cur.fetchone()
        if not result_userID:
            async with aiosqlite.connect("STREAMS.db") as db:
                cur = await db.cursor()
                await cur.execute('insert into Streams(guild_id,streaming) values(?,?)',(guild, 0))
                await db.commit()
                return STREAMING
        elif result_userID:
            async with aiosqlite.connect("STREAMS.db") as db:
                cur = await db.cursor()
                await cur.execute('insert into Streams(guild_id,streaming) values(?,?)',(guild, 1))
                await db.commit()
                STREAMING = True
                return STREAMING

    async def _check_leave(self,guild):
        async with aiosqlite.connect("STREAMS.db") as db:
            cur = await db.cursor()
            await cur.execute('create table if not exists Streams("guild_id" TEXT,"streaming" INTEGER)')
            await cur.execute(f'select guild_id from Streams where guild_id="{guild}"')
            result_userID = await cur.fetchone()
        if not result_userID:
            async with aiosqlite.connect("STREAMS.db") as db:
                cur = await db.cursor()
                await cur.execute('insert into Streams(guild_id,streaming) values(?,?)',(guild, 0))
                await db.commit()
        elif result_userID:
            async with aiosqlite.connect("STREAMS.db") as db:
                cur = await db.cursor()
                await cur.execute('insert into Streams(guild_id,streaming) values(?,?)',(guild, 0))
                await db.commit()

    @commands.command()
    async def play(self, ctx,*,source=None):
        guild = ctx.guild.id
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        try:
            channel = ctx.message.author.voice.channel
            if not channel:
                await ctx.send("You are not connected to a voice channel")
                return
            if voice and voice.is_connected():
                await ctx.send("Be Patient I am streaming music")
            else:
                await channel.connect()
                check = await self._check_stream(guild)
                if check:
                    voice = get(self.bot.voice_clients, guild=ctx.guild)
                    if source is None or source.lower() == "rock":
                        source = 'http://stream.radioparadise.com/rock-128'
                    elif source.lower() == "chill":     
                        source = 'http://stream.radioparadise.com/'
                    else:
                        source = 'http://stream.radioparadise.com/rock-128'    
                    FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                                'options': '-vn'}
                    voice.play(FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e: print('done', e))
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 0.1
                elif not check:
                    await ctx.send("Added Guild to database Please use the stream command again to Stream")
        except Exception as e:
            print(e)                 

    @commands.command(pass_context=True)
    async def join(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        channel = ctx.message.author.voice.channel
        try:
            if not channel:
                await ctx.send("You are not connected to a voice channel")
                return
            if voice and voice.is_connected() and not voice.is_playing():
                await voice.move_to(channel)
            else:
                await channel.connect()
        except:
            await ctx.send(f'{ctx.message.author.name} Bitch you need to be in a voice channel with me')

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        author = ctx.message.author
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        guild = ctx.guild.id
        try:
            try:
                channel = ctx.message.author.voice.channel
                if not channel:
                    await ctx.send("Bitch you are not connect to a voice channel")                 
                elif self.bot.user in channel.members:
                    await self._check_leave(guild)
                    await ctx.voice_client.disconnect()   
                else:
                    await ctx.send(f'{author.name} Dumb ass i am not connected to a channel')
            except:
                await ctx.send("WTF are you trying to do? lmao")
        except:
            await ctx.send(f'{author.name} you need to be in a voice channel to make me leave')


    @commands.command(pass_context=True)
    async def pause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        voice_state = ctx.message.author.voice
        if voice_state is None:
            await ctx.send('You need to be in a voice channel to use this command')
        elif voice_state.channel == voice.channel:
            if voice and voice.is_playing():
                await ctx.send('**Pausing the music**')
                voice.pause()
            elif voice:
                await ctx.send('**Currently there is no music playing.**')
            else:
                await ctx.send('**Wtf do you want me to pause your life?**')
        elif voice_state.channel != voice.channel:
            await ctx.send(f'**You need to be in Voice channel with me to activate this command bitch**')

    @commands.command(pass_context=True)
    async def resume(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        voice_state = ctx.message.author.voice
        if voice_state is None:
            await ctx.send('You need to be in a voice channel to use this command')
        elif voice_state.channel == voice.channel:
            if voice and voice.is_paused():
                await ctx.send('**Dont worry my mate resuming your Musicaa!**')
                voice.resume()
            elif voice:
                await ctx.send('**Song not playing mate**')
            else:
                await ctx.send(
                    '**Want me to resume fucking you cause i see no song playing.Plus not connected to a VC**')
        elif voice_state.channel != voice.channel:
            await ctx.send(f'**You need to be in Voice channel with me to activate this command bitch**')

    @play.error
    async def skip_error(self, ctx, error):
        if isinstance(error, CommandInvokeError):
            await ctx.send("EITHER STREAM IS DOWN OR YOU ARE STUPID")
        else:
            raise error

    @commands.command()
    async def volume(self, ctx,volume:int = None):
        channel = ctx.message.author.voice.channel
        if volume is None:
            await ctx.send("WTF ARE YOU TRYING TO PROVE?")    
        if ctx.voice_client is None:
            return await ctx.send("Not connected to voice channel")
            await ctx.send("You are not connected to a channel")
        elif self.bot.user in channel.members:    
            try:
                ctx.voice_client.source.volume = volume / 100
                await ctx.send(f"Changed volume to {volume}%")
            except Exception as e:
                print(e)
                await ctx.send("Something unexpected just happened")
        else:
            await ctx.send("Do you want me to fucking abuse?")  

    @volume.error
    async def volume_error(self,ctx,error):
        if isinstance(error, CommandInvokeError):
            await ctx.send("BRAIN.EXE STOPPED WORKING COMMAND INVOKED INCORRECTLY!")

def setup(bot):
    bot.add_cog(Music(bot))


""" 
    https://api.radioparadise.com/api/now_playing
"""