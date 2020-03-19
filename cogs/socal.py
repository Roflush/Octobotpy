import discord
from discord.ext import commands
import random

class SocalCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='halpme', aliases=['halp','saveme','askingforafriend'])
    async def SaveMe(self, ctx):

        embed=discord.Embed(title="Talk To Someone Now.", url="https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines", description="If you're thinking about suicide, are worried about a friend or loved one, or would like emotional support reach out. We can help!", color=0x69daf1)
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRP4jCxJ-g401sKfcfa0B-sDVFG0y42ZmzEco0iO3KHDeguLkmi")
        embed.add_field(name="National Suicide Prevention Lifeline", value="1-800-273-8255", inline=False)
        embed.add_field(name="Crisis Text Line", value="text HELLO to 741741", inline=False)
        embed.add_field(name=" Veterans Crisis Line", value="1-800-273-8255 and press 1", inline=True)
        embed.add_field(name="Veterans Crisis Line text ", value="838255", inline=True)
        embed.add_field(name="IMAlive Crisis Chatine", value="imalive.org", inline=False)
        embed.set_footer(text="RoFlush")

        await ctx.send(embed=embed)
    
    @commands.command(name='cool')
    async def coolfams(self, ctx):
        '''Are you cool?'''
        await ctx.send("Your not cool fam.")
 
    @commands.command(name='clean', aliases='remove', pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clean(ctx, limit: int):
        """Cleans out a textchat of trash."""
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))

    @clean.error
    async def clear_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")

    @commands.command(name='repeat')
    async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


def setup(bot):
    bot.add_cog(SocalCog(bot))