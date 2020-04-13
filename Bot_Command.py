import sys
import discord.utils
import discord.ext.commands
import discord
import random

class Bot_Command():
    def __init__(self,bot):
        self.bot=bot

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

'''
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
'''