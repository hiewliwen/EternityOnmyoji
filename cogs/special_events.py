import discord
from discord.ext import commands
import openpyxl


class SpecialEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['k'])
    async def by_cell(self, ctx, *, cell):
        """
        (.k) Search Kidomaru Color by cell.
        :param ctx: (discord.ext.commands.Context object). Mandatory parameter.
        :param cell: (str) Cell to be searched.
        :return: (discord.Embed object) Embed message of cell colors.
        """

        cell = list(cell)

        if not len(cell) == 2:
            print('Cell is not formatted correctly.')
            await ctx.send(f'Search term [{cell}] is not formatted correctly. For example: A1, B4.')
            return

        try:
            row_letter, col_number = str(cell[0].upper()), int(cell[1])
        except Exception as e:
            await ctx.send(f'Search term [{cell}] is not formatted correctly. For example: A1, B4.')
            raise e
            return

        if row_letter not in ['A', 'B', 'C', 'D', 'E']:
            await ctx.send(f'Row [{row_letter}] is not part of the picture. Only A-E.')
            return
        if 0 > col_number > 78:
            await ctx.send(f'Column [{col_number}] is not part of the picture. Only 1-78.')
            return

        EXCEL_FILE = 'Kidomaru Coloring.xlsx'
        with open(EXCEL_FILE, 'r') as excel_file:
            color_wb = openpyxl.load_workbook(EXCEL_FILE)
        color_row = [color.value for color in color_wb[row_letter][col_number-1]]

        await ctx.send(f'Kidomaru Cell [{str(row_letter)+str(col_number)}] is {color_row}')


def setup(bot):
    bot.add_cog(SpecialEvents(bot))
