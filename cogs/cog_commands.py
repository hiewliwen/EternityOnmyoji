import os

from discord.ext import commands


class CogCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['l'], hidden=True)
    @commands.is_owner()
    async def load(self, ctx, cog):
        """
        (.l) Load a named cog.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :param cog: (str) Name of the cog to be loaded.
        :return: None
        """
        await ctx.message.delete()

        try:
            self.bot.load_extension(f'cogs.{cog}')
            # await ctx.send(f'{cog} is loaded.')
            print(f'{cog} is loaded.')
        except Exception as e:
            await ctx.send(f'**{cog} cannot be loaded.**')
            print(f'{cog} cannot be loaded.')
            raise e

    @commands.command(aliases=['u'], hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, cog):
        """
        (.u) Unload a named cog.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :param cog: (str) Name of the cog to be unloaded.
        :return: None
        """
        await ctx.message.delete()

        try:
            self.bot.unload_extension(f'cogs.{cog}')
            # await ctx.send(f'{cog} is unloaded.')
            print(f'{cog} is unloaded.')
        except Exception as e:
            await ctx.send(f'{cog} cannot be unloaded.')
            print(f'{cog} cannot be unloaded.')
            raise e

    @commands.command(aliases=['r'], hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, cog):
        """
        (.r) Reload a named cog.
        It will unload, then load.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :param cog: (str) Name of the cog to be reloaded.
        :return: None
        """
        await ctx.message.delete()

        try:
            self.bot.reload_extension(f'cogs.{cog}')
            # await ctx.send(f'{cog} is reloaded.')
            print(f'{cog} is reloaded.')
        except Exception as e:
            await ctx.send(f'{cog} cannot be reloaded.')
            print(f'{cog} cannot be reloaded.')
            raise e

    @commands.command(aliases=['rr'], hidden=True)
    @commands.is_owner()
    async def reload_all(self, ctx):
        """
        (.rr) Reload all the cogs in the cogs folder.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :return: None
        """
        await ctx.message.delete()
        for cog in os.listdir('./cogs'):
            if cog.endswith('.py') and not cog.startswith('_'):
                try:
                    cog = f'cogs.{cog.replace(".py", "")}'
                    self.bot.reload_extension(cog)
                    # await ctx.send(f'{cog} is reloaded.')
                    print(f'{cog} is reloaded.')
                except Exception as e:
                    await ctx.send(f'{cog} cannot be reloaded.')
                    print(f'{cog} cannot be reloaded.')
                    raise e


def setup(bot):
    bot.add_cog(CogCommands(bot))
