# bot.py
import sys
import os
import requests
import youtube_dl
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import emoji
import discord
import random
import asyncio
import time
from itertools import cycle
import json

try:

    TOKEN = 'NjM2NDQzNTk3NTA3Mzk1NjA1.XbBgHg.LiCm5XV-WhcB9VB3uymYL2Xhj_Y'

    bot = commands.Bot(command_prefix='JE-')
    bot.remove_command("help")

    @bot.command(pass_content=True)
    async def help(ctx):
        author =ctx.message.author
        embed=discord.Embed(
            colour=discord.colour.Color.blue()
        )
        embed.set_author(name="Help",icon_url="https://cdn.discordapp.com/emojis/558779481636995094.png?v=1")
        embed.set_image(url="https://cdn.discordapp.com/emojis/558779481636995094.png?v=1")
        embed.add_field(name="Ping",value="Returns Pong",inline=False)
        embed.add_field(name="rnd_emoji", value="Returns Random Emoji", inline=False)
        embed.add_field(name="clear", value="clear <amount> Message", inline=False)
        embed.add_field(name="mention_name", value="Role name <role> to mention role", inline=False)
        await ctx.message.channel.send(author,embed=embed)

    @bot.command(pass_content=True)
    async def Ping(ctx):
        server_name = ctx.message.guild.name
        server_id=ctx.message.guild.id
        await ctx.message.channel.send("Pong")

    @bot.command(pass_content=True)
    async def clear(ctx, amount=100):
        await ctx.channel.purge(limit=amount)

    @bot.command(pass_content=True)
    async def join(ctx):
        channel=ctx.message.author.voice
        voice_channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        if voice and voice.is_connected():
            await voice_channel.move_to(channel)
        else:
            voice = await voice_channel.connect()

    @bot.command(pass_content=True)
    async def leave(ctx):
        channel=ctx.message.author.voice
        voice = get(bot.voice_clients, guild=ctx.guild)
        if not channel:
            await ctx.send("should I connected to a voice channel? use join")
            return
        if voice and voice.is_connected():
            await voice.disconnect()
        else:
            voice = await voice.disconnect()

    @bot.command(pass_content=True)
    async def rnd_emoji(ctx):
        x=random.choice(['🤔','<:bbtcat2:560740329087696906>','<:No:636237585332568064>','<a:cat_party:607428113609261082>','<a:woagcat:615703786413096973>',
              '<a:pippycat:592165061880184862>','<:cat_faceplam:632906256176250880>','<a:CatSleep:625386100445282321>','<a:MadBongoCat:622032933544263681>',
              '<:cat_woag:632863596887670785>','<:cat_wow:632863596216320039>','<:Cat_Wut:622588442672627712>'])
        print(x,'TAG : rnd_emoji')
        await ctx.message.channel.send(x)

    @bot.command(pass_content=True)
    async def mention_name(ctx,rolename='Bot'):
        role = discord.utils.get(ctx.guild.roles, name=rolename)
        await ctx.send(f'{role.mention}')

    @bot.command(pass_content=True)
    async def close(ctx,rolename='Bot'):
        sys.exit()

    @bot.command(pass_content=True)
    async def login_out():
        await bot.logout()

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!','TAG : Bot connect')
        activity = discord.Game(name="JE-",type=discord.ActivityType.streaming)
        await bot.change_presence(status=discord.Status.idle, activity=activity)

    @bot.event
    async def on_reaction_add(reaction,user):

        channel=reaction.message.channel

        print(user.name, ' has  add ', reaction.emoji, ' to ', reaction.message.content,'TAG : reaction')

        await channel.send("{} has added {} to the message {}".format(user.name,reaction.emoji,reaction.message.content))

    @bot.event
    async def on_reaction_remove(reaction,user):

        channel = reaction.message.channel

        print(user.name,' has  removed ',reaction.emoji,' to ',reaction.message.content,'TAG : reaction')

        await channel.send("{} has removed {} to the message {}".format(user.name, reaction.emoji,reaction.message.content))


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

        if message.content.startswith('Hello'):
            msg = 'Hello {0.author.mention}'.format(message)
            await message.channel.send(msg)

        if message.content.startswith('joker' or 'JOKER' or 'Joker'):
            await message.channel.send(emoji.emojize(':black_joker:'))

        if 'mike' in message.content:
            await message.add_reaction(":this_is_bbtcat: 558779481636995094")

        if 'No way'in message.content:
            await message.channel.send("<:No:636237585332568064>")

        if 'bbtcat'in message.content:
            await message.channel.send("<:this_is_bbtcat:558779481636995094>")

        if message!=None:
            print(message.author,':', message.content)

        #await message.channel.send(message.content)
        await bot.process_commands(message)

    @bot.event
    async def on_message_delete(message):

        server_name = message.guild.name
        server_id = message.guild.id
        author = message.author
        content = message.content

        if message.author !=bot.user:
            await message.channel.send("{} Delete the message {}".format(author, content))

        print('TAG : on_message_delete content',content)
        print( 'TAG : Server Name ',server_name, 'TAG : Channels ',channels, ' TAG : Server ID',server_id)
        print('TAG : on_message_delete author',author)


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
    bot.run(TOKEN,bot=True)

