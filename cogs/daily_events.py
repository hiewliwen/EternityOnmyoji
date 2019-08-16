# Reference: https://stackoverflow.com/questions/53065086/using-apschedule-to-run-awaits-in-background

from datetime import datetime

import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands

GENERAL_CHN_ID: int = 536406529583218701
OFFICER_CHN_ID: int = 536409484285968425
BOTTEST_CHN_ID: int = 607838204468658188
OFFICER_ROLE_ID: int = 536408787272204289
DRAGON_MASK = 'https://i.ibb.co/72k8Tbd/Dragon-Mask.png'
AZURE_WAVE = 'https://i.ibb.co/P5btpS7/Azure-Wave.png'
AZURE_WAVE_EMOJI = '<:AzureWave:540798886403375142>'
DAILY_EVENT_DB = 'databases/daily.db'

# DRAGON_MASK' = 'https://media1.tenor.com/images/5a22184deef81fb772283cf09ef51182/tenor.gif'

#               [Kirin Type], [Embed Colour], [Kirin Icon URL], [Kirin_Emoji]
KIRIN_FIELDS = (['Fire', 'magenta', 'https://i.ibb.co/H2hrjN0/fire.png', '<:FireKirin:606656436415627277>'],  # Monday
                ['Wind', 'teal', 'https://i.ibb.co/872CCmW/wind.png', '<:WindKirin:606656434532515859>'],  # Tuesday
                ['Water', 'blue', 'https://i.ibb.co/mcbSCtX/water.png', '<:WaterKirin:606656436516159501>'],
                # Wednesday
                ['Lightning', 'purple', 'https://i.ibb.co/DYfkjzd/lightning.png',
                 '<:LightningKirin:606656436910686208>'])  # Thursday


def kirin_params(day_of_week):
    kirin_type = KIRIN_FIELDS[day_of_week][0]
    embed_colour = KIRIN_FIELDS[day_of_week][1]
    kirin_icon_url = KIRIN_FIELDS[day_of_week][2]
    kirin_emoji = KIRIN_FIELDS[day_of_week][3]

    return kirin_type, embed_colour, kirin_icon_url, kirin_emoji


class DailyEvents(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.scheduler = AsyncIOScheduler()
        # self.scheduler.add_jobstore('sqlalchemy', url=f'sqlite:///{DAILY_EVENT_DB}')

    @commands.command(aliases=['k'], hidden=True)
    @commands.has_role('Officers')
    async def manual_kirin_hunt_msg(self, ctx):
        """
        (.k) Manually trigger the Kirin Hunt message.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :return: None
        """
        await self.kirin_hunt()

    # @manual_kirin_hunt_msg.error
    # async def manual_kirin_hunt_msg_error(self, ctx, error):
    #     if isinstance(error, commands.MissingRole):
    #         await ctx.send(f'"{ctx.command}" is limited to {get(ctx.message.guild.roles, id=OFFICER_ROLE_ID)} only.')

    async def kirin_hunt(self):
        channel = self.bot.get_channel(GENERAL_CHN_ID)

        day_of_week = datetime.now().weekday()

        if day_of_week >= 4:
            await channel.send(f'There is no Kirin Hunt today ({datetime.now().strftime("%A")}).')
            return

        kirin_type, embed_colour, kirin_icon_url, kirin_emoji = kirin_params(day_of_week)

        embed = discord.Embed(title=f'**{kirin_type} Kirin Hunt {kirin_emoji}**',
                              description='**Get Ready for Kirin Hunt :crossed_swords:**',
                              colour=getattr(discord.Colour, embed_colour)())
        embed.set_thumbnail(url=DRAGON_MASK)
        msg = await channel.send(f'@everyone {kirin_type} Kirin Hunt', embed=embed)
        await msg.add_reaction(kirin_emoji)

    @commands.command(aliases=['g'], hidden=True)
    @commands.has_role('Officers')
    async def manual_guild_raid_msg(self, ctx):
        """
        (.g) Manually trigger the Guild Raid message.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :return: None
        """
        await self.guild_raid()

    # @manual_guild_raid_msg.error
    # async def manual_guild_raid_msg_error(self, ctx, error):
    #     if isinstance(error, commands.MissingRole):
    #         await ctx.send(f'"{ctx.command}" is limited to {get(ctx.message.guild.roles, id=OFFICER_ROLE_ID)} only.')

    async def guild_raid(self):
        channel = self.bot.get_channel(OFFICER_CHN_ID)
        embed = discord.Embed(title='**:shinto_shrine: Guild Raid Reset**',
                              description="Let's :punch: Somebody",
                              colour=discord.Colour.dark_gold())
        embed.set_thumbnail(url=AZURE_WAVE)
        msg = await channel.send(embed=embed)
        await msg.add_reaction(AZURE_WAVE_EMOJI)

    def start_timer(self):
        self.scheduler.start()

        # Monday, Tuesday & Wednesday Kirin Hunt
        self.scheduler.add_job(self.kirin_hunt, trigger='cron', day_of_week='mon-thu', hour=20, minute=0, second=0)

        # Daily Guild Hunt
        self.scheduler.add_job(self.guild_raid, trigger='cron', hour=4, minute=58, second=0)

        # Wednesday Guild Feast & Kirin Hunt

        # Saturday Guild Feast & Kirin Hunt


def setup(bot):
    DailyEvents(bot).start_timer()
    bot.add_cog(DailyEvents(bot))
