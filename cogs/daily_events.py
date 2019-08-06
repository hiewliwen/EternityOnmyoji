# Reference: https://stackoverflow.com/questions/53065086/using-apschedule-to-run-awaits-in-background

from datetime import datetime

import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands

GENERAL_CHN_ID: int = 536406529583218701
OFFICER_CHN_ID: int = 536409484285968425
DRAGON_MASK = 'https://i.ibb.co/72k8Tbd/Dragon-Mask.png'
AZURE_WAVE = 'https://i.ibb.co/P5btpS7/Azure-Wave.png'
AZURE_WAVE_EMOJI = '<:AzureWave:540798886403375142>'

# DRAGON_MASK' = 'https://media1.tenor.com/images/5a22184deef81fb772283cf09ef51182/tenor.gif'

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
        self.scheduler = AsyncIOScheduler()

    @commands.command(aliases=['k'])
    async def manual_kirin_hunt_msg(self, ctx):
        await self.kirin_hunt()

    async def kirin_hunt(self):
        channel = self.bot.get_channel(GENERAL_CHN_ID)

        day_of_week = datetime.now().weekday()

        kirin_type, embed_colour, kirin_icon_url, kirin_emoji = kirin_params(day_of_week)

        embed = discord.Embed(title=f'**{kirin_type} Kirin Hunt {kirin_emoji}**',
                              description='**@everyone Get Ready for Kirin Hunt :crossed_swords:**',
                              colour=getattr(discord.Colour, embed_colour)(),
                              timestamp=datetime.utcnow())
        embed.set_thumbnail(url=DRAGON_MASK)
        msg = await channel.send(embed=embed)
        await msg.add_reaction(kirin_emoji)

    @commands.command(aliases=['g'])
    async def manual_guild_raid_msg(self, ctx):
        await self.guild_raid()

    async def guild_raid(self):
        channel = self.bot.get_channel(GENERAL_CHN_ID)
        embed = discord.Embed(title='**:shinto_shrine: Guild Raid Reset**',
                              description="Let's :punch: Somebody",
                              colour=discord.Colour.dark_gold())
        embed.set_thumbnail(url=AZURE_WAVE)
        msg = await channel.send(embed=embed)
        await msg.add_reaction(AZURE_WAVE_EMOJI)

    def start_timer(self):
        self.scheduler.start()

        # Monday, Tuesday & Wednesday Kirin Hunt
        self.scheduler.add_job(self.kirin_hunt, trigger='cron', day_of_week='mon,tue,thu', hour=13, minute=29,
                               second=30)

        # Daily Guild Hunt
        self.scheduler.add_job(self.guild_raid, trigger='cron', hour=4, minute=58, second=00)

        # Wednesday Guild Feast & Kirin Hunt

        # Saturday Guild Feast & Kirin Hunt


def setup(bot):
    DailyEvents(bot).start_timer()
    bot.add_cog(DailyEvents(bot))
