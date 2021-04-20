from asyncio import sleep
import discord
from discord.ext import commands
from discord.utils import get


class Soundboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def why(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            await ctx.send('LOL')
        elif voice:
            try:
                if not channel:
                    await ctx.send("You are not connected to a voice channel")
                    return
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                    voice.play(discord.FFmpegPCMAudio("assets/why-are-you-gay.mp3"))
                    await sleep(10)
                else:
                    voice = await channel.connect()
                    voice.play(discord.FFmpegPCMAudio("assets/why-are-you-gay.mp3"))
                    await sleep(10)
            except:
                await ctx.send(f'{ctx.message.author.name} you need to be in a voice channel to connect me')
        else:
            try:
                if not channel:
                    await ctx.send("You are not connected to a voice channel")
                    return
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                    voice.play(discord.FFmpegPCMAudio("assets/why-are-you-gay.mp3"))
                    await sleep(10)
                    await voice.disconnect()
                else:
                    voice = await channel.connect()
                    voice.play(discord.FFmpegPCMAudio("assets/why-are-you-gay.mp3"))
                    await sleep(10)
                    await voice.disconnect()
            except:
                await ctx.send(f'{ctx.message.author.name} you need to be in a voice channel to connect me')

    @commands.command()
    async def bombplanted(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            await ctx.send('LOL')
        elif voice:
            try:
                if not channel:
                    await ctx.send("You are not connected to a voice channel")
                    return
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                    voice.play(discord.FFmpegPCMAudio("assets/cs.mp3"))
                    await sleep(3)
                else:
                    voice = await channel.connect()
                    voice.play(discord.FFmpegPCMAudio("assets/cs.mp3"))
                    await sleep(3)
            except:
                await ctx.send(f'{ctx.message.author.name} you need to be in a voice channel to connect me')
        else:
            try:
                if not channel:
                    await ctx.send("You are not connected to a voice channel")
                    return
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                    voice.play(discord.FFmpegPCMAudio("assets/cs.mp3"))
                    await sleep(3)
                    await voice.disconnect()
                else:
                    voice = await channel.connect()
                    voice.play(discord.FFmpegPCMAudio("assets/cs.mp3"))
                    await sleep(3)
                    await voice.disconnect()
            except:
                await ctx.send(f'{ctx.message.author.name} you need to be in a voice channel to connect me')

    @commands.command()
    async def bsdk(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            await ctx.send('LOL')
        elif voice:
            try:
                if not channel:
                    await ctx.send("You are not connected to a voice channel")
                    return
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                    voice.play(discord.FFmpegPCMAudio("assets/Chal Bhosdike.mp3"))
                    await sleep(10)
                else:
                    voice = await channel.connect()
                    voice.play(discord.FFmpegPCMAudio("assets/Chal Bhosdike.mp3"))
                    await sleep(10)
            except:
                await ctx.send(f'{ctx.message.author.name} you need to be in a voice channel to connect me')
        else:
            try:
                if not channel:
                    await ctx.send("You are not connected to a voice channel")
                    return
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                    voice.play(discord.FFmpegPCMAudio("assets/Chal Bhosdike.mp3"))
                    await sleep(10)
                    await voice.disconnect()
                else:
                    voice = await channel.connect()
                    voice.play(discord.FFmpegPCMAudio("assets/Chal Bhosdike.mp3"))
                    await sleep(10)
                    await voice.disconnect()
            except:
                await ctx.send(f'{ctx.message.author.name} you need to be in a voice channel to connect me')

    @commands.command()
    async def bear_scream(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            await ctx.send('LOL')
        elif voice:
            try:
                if not channel:
                    await ctx.send("You are not connected to a voice channel")
                    return
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                    voice.play(discord.FFmpegPCMAudio("assets/screaming-beaver.mp3"))
                    await sleep(11)
                else:
                    voice = await channel.connect()
                    voice.play(discord.FFmpegPCMAudio("assets/screaming-beaver.mp3"))
                    await sleep(11)
            except:
                await ctx.send(f'{ctx.message.author.name} you need to be in a voice channel to connect me')
        else:
            try:
                if not channel:
                    await ctx.send("You are not connected to a voice channel")
                    return
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                    voice.play(discord.FFmpegPCMAudio("assets/screaming-beaver.mp3"))
                    await sleep(11)
                    await voice.disconnect()
                else:
                    voice = await channel.connect()
                    voice.play(discord.FFmpegPCMAudio("assets/screaming-beaver.mp3"))
                    await sleep(11)
                    await voice.disconnect()
            except:
                await ctx.send(f'{ctx.message.author.name} you need to be in a voice channel to connect me')

def setup(bot):
    bot.add_cog(Soundboard(bot))
