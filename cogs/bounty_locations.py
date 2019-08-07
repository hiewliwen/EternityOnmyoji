import sqlite3

import discord
from discord.ext import commands

BOUNTY_LOCATION_DB = 'eternity.db'
conn = sqlite3.connect(BOUNTY_LOCATION_DB)
cur = conn.cursor()


def location_by_name(shiki_name):
    """
    Query the SQLite DB with 'shiki_name' (str) in the table column 'shikigami_name'
    :param shiki_name: (str) Name of the shikigami to be searched.
    :return: List of results from DB query.
    """
    cur.execute("SELECT * FROM bounty_locations WHERE shikigami_name LIKE ?",
                ('%' + shiki_name + '%',))  # The comma is intentional
    return cur.fetchall()


def location_by_clues(clue):
    """
    Query the SQLite DB with 'clue' (str) in the table column 'clues'
    :param clue: (str) The clue(s) to be searched.
    :return: List of results from DB query.
    """
    cur.execute("SELECT * FROM bounty_locations WHERE mystery_clues LIKE ?",
                ('%' + clue + '%',))  # The comma is intentional
    return cur.fetchall()


def create_embed_message(result):
    """
    Create a discord.Embed object with 'result'.
    :param result: (str) Query result(s).
    :return: (discord.Embed object) Embed message.
    """
    shiki_name, shiki_image, clues, chapters, secrets, souls, encounters, others = result

    embed_msg = discord.Embed(title=f'**<< {shiki_name} >> Bounty Locations**',
                              colour=discord.Colour.gold())
    embed_msg.set_thumbnail(url=shiki_image)

    """
    Some of these fields could have '' string. Script will fail if '' is passed in.
    To overcome this, each of these fields are checked. If '', it will skip the assignment.
    """
    if clues:
        embed_msg.add_field(name='Clues:', value=clues.replace('\n', ', '), inline=False)
    if chapters:
        embed_msg.add_field(name='Chapters:', value=chapters, inline=False)
    if secrets:
        embed_msg.add_field(name='Secrets:', value=secrets, inline=False)
    if souls:
        embed_msg.add_field(name='Souls:', value=souls, inline=False)
    if encounters:
        embed_msg.add_field(name='Encounters:', value=encounters, inline=False)
    if others:
        embed_msg.add_field(name='Others:', value=others, inline=False)
    return embed_msg


class BountyLocations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['n'])
    async def by_name(self, ctx, *, name):
        """
        (.n) Search bounty locations by shikigami name.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :param name: (str) Shikigami name to be searched.
        :return: (discord.Embed object) Embed message of bounty location(s).
        """
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
            embed_msg = create_embed_message(result)
            embed_msg.set_footer(text=f'Requested by {ctx.author.name}. Search terms: [{name}]',
                                 icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed_msg)

    @commands.command(aliases=['c'])
    async def by_clue(self, ctx, *, clue):
        """
        (.c) Search bounty locations by clue(s).
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :param clue: (str) Clue(s) to be searched.
        :return: (discord.Embed object) Embed message of bounty location(s).
        """
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

    @by_name.error
    async def by_name_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to type a name to search.')

    @by_clue.error
    async def by_clue_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to type a clue to search.')


def setup(bot):
    bot.add_cog(BountyLocations(bot))
