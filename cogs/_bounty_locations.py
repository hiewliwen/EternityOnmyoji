import sqlite3

import discord
from discord.ext import commands

# conn = sqlite3.connect('bounty_locations.db')
conn = sqlite3.connect('bounty_locations_ext.db')
cur = conn.cursor()

"""
input = [A\nB\nC\nD\n]
output = [-A, -B, -C]

split_input = input.splitlines()
for c in split_input:
    c.append(':small_blue_diamond:'.join(c))
    
list(':small_blue_diamond:'.join(c) for c in char.splitlines())
"""


def location_by_name(shiki_name):
    """
    Search the SQLite DB with 'shiki_name' in the table column 'shikigami_names'
    :param shiki_name: str
    :return: list
    """
    cur.execute("SELECT * FROM bounty_locations_ext WHERE shikigami_name LIKE ?",
                ('%' + shiki_name + '%',))  # The comma is intentional
    return cur.fetchall()


def location_by_clues(clue):
    """
    Search the SQLite DB with 'clue' in the table column 'mystery_clues'
    :param clue: str
    :return: list
    """
    cur.execute("SELECT * FROM bounty_locations_ext WHERE mystery_clues LIKE ?",
                ('%' + clue + '%',))  # The comma is intentional
    return cur.fetchall()


def create_embed_message(message):
    """
    Create a discord.Embed message object with the input message.
    :param ctx: discord Context object
    :param message: list of str
    :return: discord.Embed message object.
    """

    shiki_name = message[0]
    shiki_image = message[1]
    clues = message[2]
    locations = message[3]

    embed_msg = discord.Embed(title=f'**<< {shiki_name} >> Bounty Locations**',
                              colour=discord.Colour.gold())
    embed_msg.set_thumbnail(url=shiki_image)
    embed_msg.add_field(name='Clues:', value=clues.replace('\n', ', '), inline=False)
    embed_msg.add_field(name='Locations:', value=locations, inline=False)

    return embed_msg


class BountyLocations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['n'])
    async def bl_name(self, ctx, *, name):
        if not len(name) >= 3:
            print('Search string is too short.')
            await ctx.send(f'Search string [{name}] is too short.')
            return

        results = location_by_name(name)
        if not results:
            print(f'Cannot find {name} in Bounty Locations.')
            await ctx.send(f'Cannot find [{name}] in Bounty Locations.')
            return

        for result in results:
            await ctx.send(result)

    @commands.command(aliases=['c'])
    async def bl_clue(self, ctx, *, clue):
        if not len(clue) >= 3:
            print('Search string is too short.')
            await ctx.send(f'Search string [{clue}] is too short.')
            return

        results = location_by_clues(clue)
        if not results:
            print(f'Cannot find {clue} in Bounty Locations.')
            await ctx.send(f'Cannot find [{clue}] in Bounty Locations.')
            return

        for result in results:
            embed_msg = create_embed_message(result)
            embed_msg.set_footer(text=f'Requested by {ctx.author.name}. Search terms: [{clue}]',
                                 icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed_msg)

            # await ctx.send(embed=create_embed_message(result))

    @bl_name.error
    async def bl_name_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to type a name to search.')

    @bl_clue.error
    async def bl_clue_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to type a clue to search.')


def setup(bot):
    bot.add_cog(BountyLocations(bot))
