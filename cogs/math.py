import discord
from discord.ext import commands


class MathCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='add', aliases=['plus'])
    @commands.guild_only()
    async def do_addition(self, ctx, first: int, second: int):
        """A simple command which does addition on two integer values."""

        total = first + second
        await ctx.send(f'The sum of **{first}** and **{second}**  is  **{total}**')

    @commands.command(name='mx', aliases=['mul'])
    @commands.guild_only()
    async def do_multiplication(self, ctx, first: int, second: int):
        """A simple command which does addition on two integer values."""

        total = first * second
        await ctx.send(f'The sum of **{first}** and **{second}**  is  **{total}**')

    @commands.command(name='sub', aliases=['subtraction'])
    @commands.guild_only()
    async def do_subtraction(self, ctx, first: int, second: int):
        """A simple command which does addition on two integer values."""

        total = first - second
        await ctx.send(f'The sum of **{first}** and **{second}**  is  **{total}**')

    @commands.command(name='div', aliases=['division'])
    @commands.guild_only()
    async def do_division(self, ctx, first: int, second: int):
        """A simple command which does addition on two integer values."""

        total = first / second
        await ctx.send(f'The sum of **{first}** and **{second}**  is  **{total}**')

    
def setup(bot):
    bot.add_cog(MathCog(bot))