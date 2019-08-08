import asyncio
import os
import random

import discord
from discord.ext import commands

import CONFIG

CHANNEL_ID = 607838204468658188  # Eternity Onmyoji
PR_STATUES = CONFIG.PR_STATUES


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=['.'], case_insensitive=True)

    async def init_cogs(self):
        for cog in os.listdir('./cogs'):
            if cog.endswith('.py') and not cog.startswith('_'):
                try:
                    cog = f'cogs.{cog.replace(".py", "")}'
                    self.load_extension(cog)
                    print(f'{cog} is loaded.')
                except Exception as e:
                    print(f'{cog} cannot be loaded.')
                    raise e

    async def on_connect(self):
        await self.init_cogs()

    async def on_ready(self):
        print('Logged in as:')
        print(self.user.name)
        print('------------')
        # await self.change_pr()

    async def change_pr(self):
        await self.wait_until_ready()
        while not self.is_closed():
            status = random.choice(PR_STATUES)
            await self.change_presence(activity=discord.Game(status))
            print(f'Statue = Playing {status}')
            await asyncio.sleep(10)

    async def check_cmd(self, ctx):
        if not ctx.message.channel.id == CHANNEL_ID:
            await ctx.send(f'Only use bot commands at Channel #{self.get_channel(CHANNEL_ID)}.')
        return ctx.message.channel.id == CHANNEL_ID

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found.')
            raise error


if __name__ == '__main__':
    Bot().add_check(Bot.check_cmd(Bot(), commands.Context))
    Bot().loop.create_task(Bot().change_pr())
    Bot().run(CONFIG.DISCORD_TOKEN, reconnect=True)

# @bot.check
# async def check_commands(ctx):
#     if not ctx.message.channel.id == CHANNEL_ID:
#         await ctx.send(f'Only use bot commands at Channel #{bot.get_channel(CHANNEL_ID)}.')
#     return ctx.message.channel.id == CHANNEL_ID
#
#
# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send('Command not found.')
#         raise error
