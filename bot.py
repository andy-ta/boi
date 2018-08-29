import discord
from discord.ext import commands
import argparse
import random

description = '''A controversial bot'''
bot = commands.Bot(command_prefix='boi ', description=description)
parser = argparse.ArgumentParser(description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(description='Decides on what to eat.')
async def eat():
    foods = ['sushi', 'mcdz', 'shawarma', 'italian', 'mandarin', 'greek', 'tacos']
    await bot.say('Y\'all should get some ' + random.choice(foods))


@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices: str):
    await bot.say(random.choice(choices))


@bot.command()
async def joined(member: discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))


# Subcommand Example
@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))


@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')


parser.add_argument('token', type=str, help='Required bot token generated by Discord.')
bot.run(parser.parse_args().token)
