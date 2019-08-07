import calendar
from datetime import datetime

import discord
from discord.ext import commands

MYSTERY_CIRCLE_LIST = ['https://i.ibb.co/MsGgyYm/m1.png', 'https://i.ibb.co/5vgRd6z/m2.png',
                       'https://i.ibb.co/Tbpc3y6/m3.png', 'https://i.ibb.co/tBtQ8kg/m4.png',
                       'https://i.ibb.co/fCZPWkW/m5.png', 'https://i.ibb.co/ns882JK/m6.png']


class MysteryCircle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['m'])
    async def mystery_circle(self, ctx, month: int = None):
        """
        Display the mystery amulet summoning circle for the month.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :param month: (int) Optional parameter. Month number (1-12). If empty, function will take current month.
        :return:
        """
        month = datetime.now().month if not month else month

        mystery_circle_image = MYSTERY_CIRCLE_LIST[month % 6 - 1]

        embed_msg = discord.Embed(title=f'{calendar.month_name[month]} Mystery Amulet Circle',
                                  colour=discord.Colour.dark_gold())
        embed_msg.set_image(url=mystery_circle_image)
        embed_msg.set_footer(text=f'Requested by {ctx.author.name}.')
        await ctx.send(embed=embed_msg)


def setup(bot):
    bot.add_cog(MysteryCircle(bot))
