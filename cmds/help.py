'''The Dolphin Core was created by Jake[Cheezy/Popcorn/Cheezy096/CheezyMax]'''

import discord
from discord.ext import commands

from settings import checks
from settings.config import conf

config = conf()
name = config.name
ver = config.version

nol = config.nombed
eol = config.errbed
pre = config.prefix
class Help(commands.Cog):

    def __init__(self, bot):
        self.b = bot

    @commands.group()
    async def help(self,ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title="To see a catergory please do {}help catergory".format(pre), colour=nol)
            embed.set_author(name="{}'s help ting".format(name), icon_url=ctx.message.author.avatar_url)
            embed.add_field(name="general".format(pre), value="general commands", inline=True)
            embed.add_field(name="fun".format(pre), value="fun commands", inline=True)
            embed.add_field(name="mod", value="mod commands", inline=True)
            embed.set_footer(text=ver)
            await ctx.send(embed=embed)



    @help.command()
    async def fun(self,ctx):
        embed = discord.Embed(title="General commands", colour=nol)
        embed.set_footer(text=ver)
        embed.set_author(name="{}'s help ting".format(name))
        embed.add_field(name=pre+"pewds", value="Pewwwwwdiepieeeeeeee", inline=False)
        embed.add_field(name=pre+"pizza", value="pizza", inline=False)
        embed.add_field(name=pre+"ash", value="A picture of ash", inline=False)
        embed.add_field(name=pre+"max", value="A picture of Max Cross", inline=False)
        embed.add_field(name=pre+"gun", value="Gun someone down", inline=False)
        embed.add_field(name=pre+"grape", value="They did surgery on a grape", inline=False)
        embed.add_field(name=pre+"jake", value="ONO", inline=False)

        await ctx.author.send(embed=embed)




    @help.command()
    async def general(self,ctx):
        embed = discord.Embed(title="General commands", colour=nol)
        embed.set_footer(text=ver)
        embed.set_author(name="{}'s help ting".format(name))
        embed.add_field(name=pre+"agree", value="Gives you the 'member' role", inline=False)
        embed.add_field(name=pre+"ping", value="Just a ping command", inline=False)
        embed.add_field(name=pre+"about", value="Some info about the bot", inline=False)
        embed.add_field(name=pre+"bugrep", value="Report a bug (it will be sent to a developers DM's)", inline=False)
        embed.add_field(name=pre+"logan", value="Epic", inline=False)

        await ctx.author.send(embed=embed)


    @help.command()
    async def mod(self,ctx):
        embed = discord.Embed(title="Mod commands", colour=nol)
        embed.set_footer(text=ver)
        embed.set_author(name="{}'s help ting".format(name))
        embed.add_field(name=pre+"ban", value="Bans a user", inline=False)
        embed.add_field(name=pre+"kick", value="Kicks a uer", inline=False)
        embed.add_field(name=pre+"mute", value="Mute a user", inline=False)
        embed.add_field(name=pre+"unmute", value="Unmute", inline=False)
        embed.add_field(name=pre+"embed", value="Make the bot embed the given argument", inline=False)
        embed.add_field(name=pre+"bomb", value="Allows you to delete a certain amount of messages", inline=False)
        embed.add_field(name=pre+"unban", value="Unbans a user via the user's ID", inline=False)
        embed.add_field(name=pre+"banid", value="Bans a user via the user's ID (doesn't require them to be in the server)", inline=False)
        embed.add_field(name=pre+"lockdown", value="Sets the serveres verification level to high", inline=False)
        embed.add_field(name=pre+"unlock", value="Sets the serveres verification level to none", inline=False)

        await ctx.author.send(embed=embed)


    @help.command()
    @checks.dev()
    async def dev(self,ctx):
        embed = discord.Embed(title="Developer commands", colour=nol)
        embed.set_footer(text=ver)
        embed.set_author(name="{}'s help ting".format(name))
        embed.add_field(name=pre+"eval", value="Evaluates code", inline=False)
        embed.add_field(name=pre+"reload", value="Reload a cog", inline=False)
        embed.add_field(name=pre+"load", value="Load a cog", inline=False)
        embed.add_field(name=pre+"unload", value="Unload a cog", inline=False)
        embed.add_field(name=pre+"leave", value="Leaves a server", inline=False)
        embed.add_field(name=pre+"shutdown", value="Shutdown the bot", inline=False)
        embed.add_field(name=pre+"refresh", value="Reloads all cogs that are normally loaded", inline=False)
        embed.add_field(name=pre+"usage", value="See some info about your instance", inline=False)
        embed.add_field(name=pre+"say", value="Make the bot say the given argument", inline=False)
        embed.add_field(name=pre+"dm", value="Make the bot dm a user the given argument", inline=False)
        embed.add_field(name=pre+"debug", value="An expermiental command/mode i'm making for the dolphin core (Dolphin core's debugging mode)", inline=False)

        await ctx.author.send(embed=embed)


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))
