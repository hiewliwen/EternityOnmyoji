from datetime import datetime

import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

DRAGON_MASK = 'https://i.ibb.co/72k8Tbd/Dragon-Mask.png'

# Dummy server
# #               [Kirin Type], [Embed Colour], [Kirin Icon URL], [Kirin_Emoji]
# KIRIN_FIELDS = (['Fire', 'magenta', 'https://i.ibb.co/H2hrjN0/fire.png', '<:FireKirin:606403630437892098>'],  # Monday
#                 ['Wind', 'teal', 'https://i.ibb.co/872CCmW/wind.png', '<:WindKirin:606403631024963587>'],  # Tuesday
#                 ['Water', 'blue', 'https://i.ibb.co/mcbSCtX/water.png', '<:WaterKirin:606403630886682624>'],
#                 # Wednesday
#                 ['Lightning', 'purple', 'https://i.ibb.co/DYfkjzd/lightning.png',
#                  '<:LightningKirin:606403630639087627>'])  # Thursday

#               [Kirin Type], [Embed Colour], [Kirin Icon URL], [Kirin_Emoji]
KIRIN_FIELDS = (['Fire', 'magenta', 'https://i.ibb.co/H2hrjN0/fire.png', '<:FireKirin:606656436415627277>'],  # Monday
                ['Wind', 'teal', 'https://i.ibb.co/872CCmW/wind.png', '<:WindKirin:606656434532515859>'],  # Tuesday
                ['Water', 'blue', 'https://i.ibb.co/mcbSCtX/water.png', '<:WaterKirin:606656436516159501>'],
                # Wednesday
                ['Lightning', 'purple', 'https://i.ibb.co/DYfkjzd/lightning.png',
                 '<:LightningKirin:606656436910686208>'])  # Thursday


def kirin_params(day_of_week):
    kirin_type = KIRIN_FIELDS[day_of_week - 1][0]
    embed_colour = KIRIN_FIELDS[day_of_week - 1][1]
    kirin_icon_url = KIRIN_FIELDS[day_of_week - 1][2]
    kirin_emoji = KIRIN_FIELDS[day_of_week - 1][3]

    return kirin_type, embed_colour, kirin_icon_url, kirin_emoji


class DailyEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['k'], hidden=True)
    async def kirin_hunt(self, ctx, dow=None):
        """
        Creates a Kirin Hunt embed message with the Kirin type for the day.
        Only on Monday - Thursday EST.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :param dow: (int) Day of week. 1 = Monday, 2 = Tuesday .... 0 and 7 = Sunday
        :return: (discord.Embed object) Kirin Hunt embed message.
        """
        day_of_week = datetime.now().weekday() if not dow else int(dow)
        print(day_of_week)

        if not 0 < day_of_week <= 4:
            print('Day of Week is outside of Kirin Hunt days!')
            await ctx.send('Kirin Hunt message is shown outside of event days.')
            return

        # else:
        #     print('Error with Kirin Hunt message.')
        #     await ctx.send('Error with Kirin Hunt message.')
        #     return

        kirin_type, embed_colour, kirin_icon_url, kirin_emoji = kirin_params(day_of_week)

        embed = discord.Embed(title=f'**{kirin_type} Kirin Hunt {kirin_emoji}**',
                              description='**@everyone Get Ready for Kirin Hunt :crossed_swords:**',
                              colour=getattr(discord.Colour, embed_colour)(),
                              timestamp=datetime.utcnow())

        embed.set_thumbnail(url=DRAGON_MASK)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction(kirin_emoji)


def setup(bot):
    bot.add_cog(DailyEvents(bot))
