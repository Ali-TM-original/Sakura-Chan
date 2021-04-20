import discord
from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount + 1)

    @commands.command(pass_context=True, aliases=['kick_member'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if reason is None:
            reason = 'Sorry mate! they did not specify any reason'
        try:
            await member.kick(reason=reason)
            await member.send(f'you have been kicked from server {ctx.guild.name}. Reson={reason}')
            await ctx.send(member.name + ' GET KICKED NOOB XD')
        except:
            await member.kick(reason=reason)
            await ctx.send(member.name + ' GET KICKED NOOB XD')

    @commands.command(pass_context=True, aliases=['ban_hammer', 'ban_member'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):  # 'No Reason Provided, NOOB!'
        if reason is None:
            reason = 'Sorry mate! they did not specify any reason'
        try:
            await member.send(f'you have been banned from server {ctx.guild.name}. Reson={reason}')
            await ctx.send(f'{member.name} has been banned by {ctx.author.mention}')
            await member.ban(reason=reason)
        except:
            await ctx.send(member.name + ' GET BANNED BITCH XD')
            await member.ban(reason=reason)

    @commands.command(pass_context=True, aliases=['count', 'total'])
    async def stats(self, ctx):
        members = 0
        servers = self.bot.guilds
        for server in servers:
            x = server.member_count
            members += x
        embed = discord.Embed(title='Stats',color=0x2ECC71)
        embed.add_field(name='***Server Count:*** ', value=f'**{len(servers)}**', inline=False)    
        embed.add_field(name='***Member Count:*** ', value=f'**{members}**', inline=False)
        embed.add_field(name='***Creator:*** ', value='Ali™#4294', inline=False)

        #await ctx.send(f'**I am in {str(len(servers))} servers. Watching over {members} members**')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban_list(self, ctx):
        banned_user = await ctx.guild.bans()
        for users in banned_user:
            embedVar7 = discord.Embed(title='Banned users', color=0x2ECC71)
            embedVar7.add_field(name=users[1], value=users[0], inline=False)
            await ctx.send(embed=embedVar7)


def setup(bot):
    bot.add_cog(moderation(bot))
