import discord
from discord.ext import commands


class DevCog(commands.Cog):

    '''all of the devloper commands'''

    def __init__(self, bot):
        self.bot = bot

    #Doesn't work has of right now.
    @commands.command(name='presence', aliases=['newstat', 'status'] ,hidden=True)
    async def _presence(self, ctx, type=None, *, game=None):
        '''Change the bot's presence'''
        if type is None:
            await ctx.send(f'Usage: `{ctx.prefix}presence [game/stream/watch/listen] [message]`')
        else:
            if type.lower() == 'stream':
                await ctx.change_presence(status=discord.Status.online, activity=discord.Streaming(name='Use ch.help for help!', url='https://www.twitch.tv/monstercat'))
                await ctx.send(f'Set presence to. `Streaming {game}`')
            elif type.lower() == 'game':
                await ctx.change_presence(status=discord.Status.online, activity=discord.Game(name=game))
                await ctx.send(f'Set presence to `Playing {game}`')
            elif type.lower() == 'watch':
                await ctx.change_presence(status=discord.Status.online, activity=discord.Game(name=game, type=3), afk=True)
                await ctx.send(f'Set presence to `Watching {game}`')
            elif type.lower() == 'listen':
                await ctx.change_presence(status=discord.Status.online, activity=discord.Game(name=game, type=2), afk=True)
                await ctx.send(f'Set presence to `Listening to {game}`')
            elif type.lower() == 'clear':
                await self.bot.change_presence(game=None)
                await ctx.send('Cleared Presence')
            else:
                await ctx.send('Usage: `ch.presence [game/stream/watch/listen] [message]`')





def setup(bot):
    bot.add_cog(DevCog(bot))