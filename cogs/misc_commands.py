import discord
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['ui'])
    async def userinfo(self, ctx, member: discord.Member = None):
        """
        Display the information of a specific user.
        If no user param is given, the script will use author's ID.
        :param ctx: (discord.ext.commands.Context object) Mandatory parameter.
        :param member: (discord.Member object) @so_and_so. If 'None', then author ID will be used.
        :return: (discord.Embed object) User information.
        """
        member = ctx.author if not member else member

        roles = [role for role in member.roles]

        embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f'User Info = {member}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Request by {ctx.author}', icon_url=ctx.author.avatar_url)

        embed.add_field(name='ID', value=member.id)
        embed.add_field(name='Guild Name', value=member.display_name)
        embed.add_field(name='Created At', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
        embed.add_field(name='Joined At', value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
        embed.add_field(name=f'Roles ({len(roles)})', value=' '.join([role.mention for role in roles]))
        embed.add_field(name='Top Role', value=member.top_role.mention)
        embed.add_field(name='Bot?', value=member.bot)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))
