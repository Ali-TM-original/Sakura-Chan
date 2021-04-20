from gtts import gTTS
from discord.ext import commands
import discord
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


class custom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tts(self, ctx, *,text=None):
        await ctx.trigger_typing()
        if text is None:
            text = "Write some text bitch"
        language = 'en'
        output_audio = gTTS(text=text, lang=language, slow=False)
        output_audio.save('assets/output.mp3')
        file=discord.File('assets/output.mp3')
        await ctx.send(file=file)


def setup(bot):
    bot.add_cog(custom(bot))