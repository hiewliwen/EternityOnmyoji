import os

from discord.ext import commands

import CONFIG

bot = commands.Bot(command_prefix=['.'])
# CHANNEL_ID = 607829309305913355 #dummy_server
CHANNEL_ID = 607838204468658188  # Eternity Onmyoji


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

    # channel = bot.get_channel(CHANNEL_ID)
    # await channel.send('Ready!')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found.')
        raise error


for cog in os.listdir('./cogs'):
    if cog.endswith('.py') and not cog.startswith('_'):
        try:
            cog = f'cogs.{cog.replace(".py", "")}'
            bot.load_extension(cog)
        except Exception as e:
            print(f'{cog} cannot be loaded.')
            raise e

bot.run(CONFIG.DISCORD_TOKEN)
