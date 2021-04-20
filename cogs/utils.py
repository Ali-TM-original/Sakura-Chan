import discord
from discord.ext import commands


class UTILS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        embed_var4 = discord.Embed(title='info', color=0x222222)
        embed_var4.add_field(name='Version', value='Beta', inline=True)
        embed_var4.add_field(name='Creator', value='Ali™#4294', inline=True)
        embed_var4.set_image(url='https://cdn.discordapp.com/attachments/805458192166420480/807536955675508766/100ms_last_gif.gif')
        # embed_var4.set_image(url=discord.File('100ms last gif.gif'))
        await ctx.send(embed=embed_var4)
        # await ctx.send(file= discord.File('100ms last gif.gif'))

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        embed_var3 = discord.Embed(color=0x222222)
        embed_var3.set_image(url=member.avatar_url)
        await ctx.send(embed=embed_var3)

    @commands.command(aliases=['user', 'userinfo'])
    async def whois(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        roles = [role.name for role in member.roles]
        created_at = member.created_at.strftime("%b, %d, %Y")
        joined_at = member.joined_at.strftime("%b, %d, %Y")
        embed_var2 = discord.Embed(title=member.name, description=member.mention, color=0x2ECC71)  # 2ECC71
        embed_var2.add_field(name='Account Created:', value=created_at, inline=False)
        embed_var2.add_field(name='Joined:', value=joined_at, inline=False)
        embed_var2.add_field(name=f'Roles[{len(roles)}]', value=str(roles), inline=False)
        embed_var2.add_field(name='ID:', value=member.id, inline=False)
        embed_var2.add_field(name='Status:', value=str(member.status).title(), inline=False)
        embed_var2.add_field(name='Top Role:', value=member.top_role, inline=False)
        embed_var2.set_thumbnail(url=member.avatar_url)
        embed_var2.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}.')
        embed_var2.timestamp = ctx.message.created_at
        await ctx.send(embed=embed_var2)

    @commands.command(pass_context=True)
    async def sv(self, ctx):
        guild = ctx.guild
        server_name = guild.name
        bot_guild_info = ctx.guild.members
        number_of_members = bot_guild_info[0].guild.member_count
        owner = self.bot.get_user(ctx.guild.owner_id)
        embedVar = discord.Embed(title="Server Info", description="Details about the server",
                                 color=0x8E44AD)  # 0x00ff00
        embedVar.add_field(name="Server Name", value=server_name, inline=False)
        embedVar.add_field(name="Number of Members", value=number_of_members, inline=False)
        embedVar.add_field(name="Owner name", value=owner, inline=False)
        embedVar.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embedVar)


def setup(bot):
    bot.add_cog(UTILS(bot))
