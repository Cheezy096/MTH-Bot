'''The Dolphin Core was created by Jake[Cheezy/Popcorn/Cheezy096/CheezyMax]'''

import inspect
import logging

import discord
from discord.ext import commands

from settings import checks
from settings.config import conf

config = conf()

logging.basicConfig(level=logging.INFO)
# Configures logging.

logger = logging.getLogger("MassMessager")
# Defines the logger.


name = config.name
ver = config.version

nol = config.nombed
eol = config.errbed
class Eval(commands.Cog):

    def __init__(self, bot):
        self.b = bot



#change enabled=True to False if you want the command completely disabled so not even you can use it
    @checks.dev()
    @commands.command(enabled=True)
    async def eval(self, ctx, *, code):
        code = code.strip("` ")
        user = discord.Member
        try:
            result = eval(code)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            embed = discord.Embed(title = "❌ Oops!", description ="Input:` {}`\n{}: `{}`".format(code, type(e).__name__, e), color = eol)
            embed.set_footer(text=ver)
            await ctx.send(embed=embed)
   
        else:
            embed = discord.Embed(title = "Your Input:", description ="`{}`".format(code), color = nol)
            embed.add_field(name="Your Output:", value = "`{}`".format(result), inline=False)
            embed.set_footer(text=ver)
            embed.set_author(name="Here's your eval result!")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Eval(bot))
