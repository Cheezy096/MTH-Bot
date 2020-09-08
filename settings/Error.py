import math
import sys
import traceback

import discord
from discord.ext import commands

from settings import checks
from settings.config import conf

config = conf()
name = config.name
ver = config.version
eol = config.errbed


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, commands.DisabledCommand):
            embed = discord.Embed(title="❌ Error!", description="I'm sorry but that command is disabled.", colour=eol)
            embed.set_footer(text=ver)
            return await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.NoPrivateMessage):
            try:
                embed=discord.Embed(title="❌ Error!", description=f"{ctx.command} can not be used in DM's.", colour=eol)
                embed.set_footer(text=ver)
                return await ctx.author.send(embed=embed)
            except:
                pass
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(title="❌ Error!", description="BadArgument", colour=eol)
            embed.set_footer(text=ver)
            return await ctx.send(embed=embed)
        elif isinstance(error, commands.NotOwner):
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="❌ Error!", description="MissingRequiredArgument.", colour=eol)
            embed.set_footer(text=ver)
            return await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(title="❌ Error!", description="I'm sorry but i don't have the correct permissions to do that.", colour=eol)
            embed.set_footer(text=ver)
            return await ctx.send(embed=embed)
        elif isinstance(error, checks.dev_only):
            embed = discord.Embed(title="❌ Error!", description="Developer only!", colour=eol)
            embed.set_footer(text=ver)
            return await ctx.send(embed=embed)
        elif isinstance(error, commands.CheckFailure):
            embed = discord.Embed(title="❌ Error!", description="Sorry bud but you don't have the correct permissions to run this command.", colour=eol)
            embed.set_footer(text=ver)
            return await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title="❌ Error!", description="This command is on cooldown, retry after {} seconds".format(math.ceil(error.retry_after)), colour=eol)
            embed.set_footer(text=ver)
            return await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="❌ Error!", description="Sorry bud but you can't use that", colour=eol)
            embed.set_footer(text=ver)
            return await ctx.send(embed=embed)
        else:
            tra = traceback.format_exception_only(type(error), error)
            embed = discord.Embed(title="❌ Error!", description="Whoops. I ran into an error i don't know! Here's the error: ```py\n%s\n```" % ''.join(tra), file=sys.stderr, colour=eol)
            embed.set_footer(text=ver)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
