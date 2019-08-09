from discord.ext import commands

MAX_PURGE_MSG = 20


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command(hidden=True)
    # @commands.has_permissions(kick_members=True)
    # async def kick(self, ctx, member: discord.Member, *, reason='No reason'):
    #     """
    #     Kicks a specific member.
    #     :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
    #     :param member: (discord.Member object). The member to be kicked.
    #     :param reason: (str) The reason for kicking the member.
    #     :return: None.
    #     """
    #     await member.kick(reason=reason)
    #     await ctx.send(f'{member.mention} is kicked by {ctx.author.mention}. [{reason}]')
    #
    # @commands.command(hidden=True)
    # @commands.has_permissions(ban_members=True)
    # async def ban(self, ctx, member: discord.Member, *, reason='No reason'):
    #     """
    #     Bans a specific member.
    #     :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
    #     :param member: (discord.Member object). The member to be banned.
    #     :param reason: (str) The reason for banning the member.
    #     :return:
    #     """
    #     await member.ban(reason=reason)
    #     await ctx.send(f'{member.mention} is banned by {ctx.author.mention}. [{reason}]')

    # @commands.command(aliases=['cl'])
    @commands.command(hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        """
        Clear a specific number of messages from the channel.
        Author must have "manage_message" permission enabled.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :param amount: (int) Number of messages to be deleted. Capped at MAX_PURGE_MSG
        :return: None
        """
        amount = 20 if amount > MAX_PURGE_MSG else amount
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'{amount} messages were deleted.', delete_after=3)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You don't have the permission to do that.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to specify an amount (int) of messages to be clear.')
        if isinstance(error, commands.BadArgument):
            await ctx.send('Requires an integer.')

        raise error


def setup(bot):
    bot.add_cog(Mod(bot))
