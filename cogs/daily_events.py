# Reference: https://stackoverflow.com/questions/53065086/using-apschedule-to-run-awaits-in-background

import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from discord.ext import commands

import CONFIG

GENERAL_CHN_ID: int = CONFIG.GENERAL_CHN_ID
OFFICER_CHN_ID: int = CONFIG.OFFICER_CHN_ID
BOTTEST_CHN_ID: int = CONFIG.BOTTEST_CHN_ID
OFFICER_ROLE_ID: int = CONFIG.OFFICER_ROLE_ID

DRAGON_MASK = CONFIG.DRAGON_MASK
AZURE_WAVE = CONFIG.AZURE_WAVE
AZURE_WAVE_EMOJI = CONFIG.AZURE_WAVE_EMOJI
DAILY_EVENT_DB = CONFIG.DAILY_EVENT_DB

KIRIN_FIELDS = CONFIG.KIRIN_FIELDS

PREV_RAID_MSG = []
PREV_RAID_REMINDER_MSG = []


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

    @commands.command(aliases=['km'], hidden=True)
    @commands.has_role('Officers')
    async def manual_kirin_hunt_msg(self, ctx):
        """
        (.km) Manually trigger the Kirin Hunt message.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :return: None
        """
        await ctx.message.delete()
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

    @commands.command(aliases=['gm'], hidden=True)
    @commands.has_role('Officers')
    async def manual_guild_raid_msg(self, ctx):
        """
        (.gm) Manually trigger the Guild Raid message.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :return: None
        """
        await ctx.message.delete()
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

        try:
            await PREV_RAID_MSG.pop().delete()
        except:
            pass
        PREV_RAID_MSG.append(msg)

    async def guild_raid_reminder(self):
        channel = self.bot.get_channel(GENERAL_CHN_ID)
        embed = discord.Embed(title='**:shinto_shrine: Guild Raid Progress Reminder**',
                              description="2 more hours to reset. Have we cleared raid?",
                              colour=discord.Colour.dark_gold())
        embed.set_thumbnail(url=AZURE_WAVE)
        msg = await channel.send(embed=embed)
        await msg.add_reaction(AZURE_WAVE_EMOJI)

        try:
            await PREV_RAID_REMINDER_MSG.pop().delete()
        except:
            pass
        PREV_RAID_REMINDER_MSG.append(msg)

    @commands.command(aliases=['gmr'], hidden=True)
    @commands.has_role('Officers')
    async def manual_guild_raid_msg(self, ctx):
        """
        (.gmr) Manually trigger the Guild Raid Reminder message.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :return: None
        """
        await ctx.message.delete()
        await self.guild_raid_reminder()

    def start_timer(self):
        self.scheduler.start()

        # Monday - Thursday Kirin Hunt
        self.scheduler.add_job(self.kirin_hunt, trigger='cron', day_of_week='mon-thu', hour=20, minute=0, second=0)

        # Daily Guild Raid
        self.scheduler.add_job(self.guild_raid_reminder, trigger='cron', hour=3, minute=0, second=0)
        self.scheduler.add_job(self.guild_raid, trigger='cron', hour=4, minute=58, second=0)


def setup(bot):
    # DailyEvents(bot).start_timer()
    bot.add_cog(DailyEvents(bot))
