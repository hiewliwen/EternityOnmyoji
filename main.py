import asyncio
import os
import random

import discord
from discord.ext import commands

import CONFIG

bot = commands.Bot(command_prefix=['.'])
CHANNEL_ID = 607838204468658188  # Eternity Onmyoji
PR_STATUES = CONFIG.PR_STATUES


@bot.check
async def check_commands(ctx):
    if not ctx.message.channel.id == CHANNEL_ID:
        await ctx.send(f'Only use bot commands at Channel #{bot.get_channel(CHANNEL_ID)}.')
    return ctx.message.channel.id == CHANNEL_ID


@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print('------------')

    await init_cogs()
    # channel = bot.get_channel(CHANNEL_ID)
    # await channel.send('Ready!')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found.')
        raise error


async def change_pr():
    await bot.wait_until_ready()

    while not bot.is_closed():
        status = random.choice(PR_STATUES)
        await bot.change_presence(activity=discord.Game(status))
        await asyncio.sleep(300)


async def init_cogs():
    for cog in os.listdir('./cogs'):
        if cog.endswith('.py') and not cog.startswith('_'):
            try:
                cog = f'cogs.{cog.replace(".py", "")}'
                bot.load_extension(cog)
                print(f'{cog} is loaded.')
            except Exception as e:
                print(f'{cog} cannot be loaded.')
                raise e


bot.loop.create_task(change_pr())
bot.run(CONFIG.DISCORD_TOKEN)
