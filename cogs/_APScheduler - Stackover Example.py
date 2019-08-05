import os
from datetime import date

from apscheduler.schedulers.background import BackgroundScheduler


class CostumeCog:
    """CostumeCog is a cog that automagically changes the profile picture of Cueball for the holiday."""

    def __init__(self, bot):
        self.bot = bot
        self.sched = BackgroundScheduler()

    async def check_costume(self):
        print("Spook.")
        picture = open('cogs/costumecog/standard.png')
        for file in [f.strip('.png').split('-') for f in os.listdir('cogs/costumecog/costumes/')
                     if os.path.isfile(os.path.join('cogs/costumecog/costumes/', f))]:
            if int(file[0]) <= int(date.today().strftime("%m%d")) <= int(file[2]):
                picture = open(f'{"-".join(file)}.png', 'rb')
        await self.bot.edit_profile(avatar=picture.read())
        print("Costume checked.")

    def start_timer(self):
        self.sched.start()
        self.sched.add_job(self.check_costume, trigger='cron', hour=20, minute=27, id='check_costume',
                           executor='asyncio')


def setup(bot):
    CostumeCog(bot).start_timer()
    bot.add_cog(CostumeCog(bot))
