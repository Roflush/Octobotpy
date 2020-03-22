import discord
from discord.ext import commands

import sys, traceback

get_token = open('token.txt', 'r').read()

def get_prefixes(bot, message):
    prefixes = ['.', '?', 'ch.', 'ro.', 'sudo ']

    if not message.guild:
        return '?'

    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = [ 'cogs.social', 
                        'cogs.math', 
                        'cogs.dev']


bot = commands.Bot(command_prefix=get_prefixes, description='needs help')

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name='Use ch.help for help!', url='https://www.twitch.tv/monstercat'))
    print(f'Successfully logged in and booted...!')


bot.run(get_token, bot=True, reconnect=True)
