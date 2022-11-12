import calendar
import discord
from datetime import datetime
from discord.ext import commands

import CONFIG

MYSTERY_CIRCLE_LIST = CONFIG.MYSTERY_CIRCLE_LIST


class MysteryCircle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['m'])
    async def mystery_circle(self, ctx, month: int = None):
        """
        (.m) Display the mystery amulet summoning circle for the month.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :param month: (int) Optional parameter. Month number (1-12). If empty, function will take current month.
        :return:
        """
        month = datetime.now().month if not month else month

        mystery_circle_image = discord.File(MYSTERY_CIRCLE_LIST[month % 6 - 1], filename="image.png")

        embed_msg = discord.Embed(title=f'{calendar.month_name[month]} Mystery Amulet Circle',
                                  colour=discord.Colour.dark_gold())
        embed_msg.set_image(url="attachment://image.png")
        embed_msg.set_footer(text=f'Requested by {ctx.author.display_name}.', icon_url=ctx.author.avatar_url)
        msg = await ctx.send(embed=embed_msg, file=mystery_circle_image)


def setup(bot):
    bot.add_cog(MysteryCircle(bot))
