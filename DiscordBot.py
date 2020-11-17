# bot.py
import configparser
import datetime
import sys

import discord
from discord.ext import commands

config = configparser.ConfigParser()
config.read('Token.ini')
TOKEN = (config.get('Token', 'Token'))

try:
    bot = commands.Bot(command_prefix='JE-')
    bot.remove_command("help")


    @bot.command(pass_content=True)
    async def Ping(ctx):
        await ctx.message.channel.send("Pong")


    @bot.command(pass_content=True)
    async def clear(ctx, amount=100):
        await ctx.channel.purge(limit=amount)


    @bot.command(pass_content=True)
    async def close():
        sys.exit()


    @bot.command(pass_content=True)
    async def login_out():
        await bot.logout()


    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!', 'TAG : Bot connect')
        activity = discord.Game(name="JE-", type=discord.ActivityType.streaming)
        await bot.change_presence(status=discord.Status.online, activity=activity)


    @bot.event
    async def on_reaction_add(reaction, user):

        channel = reaction.message.channel

        print(user.name, ' has  add ', reaction.emoji, ' to ', reaction.message.content, 'TAG : reaction')

        await channel.send(
            "{} has added {} to the message {}".format(user.name, reaction.emoji, reaction.message.content))


    @bot.event
    async def on_reaction_remove(reaction, user):

        channel = reaction.message.channel
        print(user.name, ' has  removed ', reaction.emoji, ' to ', reaction.message.content, 'TAG : reaction')
        await channel.send(
            "{} has removed {} to the message {}".format(user.name, reaction.emoji, reaction.message.content))


    @bot.event
    async def on_member_join(member):
        role = discord.utils.get(member.guild.roles, name="Cat")
        await member.add_roles(role)
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to  Discord server!'
        )


    @bot.event
    async def on_message(message):

        if message.author == bot.user:
            return
        if message != None:
            print(datetime.datetime.now(), message.author, ':', message.content, sep=' ')
        await bot.process_commands(message)


    @bot.event
    async def on_message_delete(message):

        author = message.author
        content = message.content
        if message.author != bot.user:
            print(f"{author} Delete the message {content}")
            await message.channel.send("{} Delete the message {}".format(author, content))


    @bot.event
    async def on_error(event, *args, **kwargs):
        with open('err.log', 'a') as f:
            if event == 'on_message':
                f.write(f'Unhandled message: {args[0]}\n')
            else:
                raise

except Exception as Print_Exception:
    print(Print_Exception)

finally:
    bot.run(TOKEN, bot=True)
