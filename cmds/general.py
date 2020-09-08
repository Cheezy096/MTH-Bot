'''The Dolphin Core was created by Jake[Cheezy/Popcorn/Cheezy096/CheezyMax]'''

import time
from datetime import datetime

import discord
from discord.ext import commands as dol

from settings.config import conf

config = conf()

ver = config.version
name = config.name

sol = config.sucbed
nol = config.nombed
wol = config.wanbed
eol = config.errbed
class Eval(dol.Cog):

    def __init__(self, bot):
        self.b = bot

    @dol.command(aliases=["accept"])
    @dol.guild_only()
    async def agree(self, ctx):
        try:
            role = discord.utils.get(ctx.guild.roles, name="member")
            user = ctx.message.author
            await user.add_roles(role)
            await ctx.message.delete()
        except Exception:
            embed = discord.Embed(title="❌ That's an issue!", description="I'm sorry but there seems to be no role called 'Member' or there is an issue with the role", colour=eol)
            embed.set_footer(text=ver)
            await ctx.send(embed=embed)

    @dol.command()
    @dol.guild_only()
    async def ping(self,ctx):
        start = time.perf_counter()
        msg = await ctx.send(embed=discord.Embed(title="Please wait",color=nol))
        end = time.perf_counter()
        duration = (end - start) * 1000
        await msg.delete()
        embed=discord.Embed(title="That took me {:.2f}ms.".format(duration), color=nol)
        embed.set_author(name="Pong!", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)



    @dol.command()
    async def about(self,ctx):
        e=discord.Embed(title="{}".format(config.name), description="Hi there, i'm {} a bot designed to be streaky's brand predecessor, i was Created by Cheezy[Jake R.] with the original idea for the bot by Lucas (Max).".format(config.name), color=nol)
        e.add_field(name="Version:", value=str(config.version), inline=True)
        e.add_field(name="Currently Playing:", value=config.playing)
        await ctx.send(embed=e)

    @dol.command()
    async def bugrep(self,ctx, *, report):
        user = ctx.guild.get_member(208027858176704513)
        e = discord.Embed(title=":mailbox_closed: Reported!", description="The bug has been reported to {}".format(user.name), color=sol)
        await ctx.send(embed=e)
        em = discord.Embed(title=":warning: New bug report!", color=wol)
        em.add_field(name="Time Post: ", value="`{}`".format(datetime.now()), inline=False)
        em.add_field(name="Bug Report: ", value="`{}`".format(report), inline=False)
        em.add_field(name="Reported by: ", value="{}".format(ctx.author.name), inline=False)
        await user.send(embed=em)

def setup(bot):
    bot.add_cog(Eval(bot))
