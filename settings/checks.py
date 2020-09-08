'''The Dolphin Core was created by Jake[Cheezy/Popcorn/Cheezy096/CheezyMax]'''

import discord
import discord.utils
from discord.ext import commands

from settings.config import conf

config = conf()
ver = config.version
nol=config.nombed
sol=config.sucbed
eol=config.errbed
wol=config.wanbed

#this is where stuff like @checks.is_dev is made, simply put if your id matches the one on a string the command will work right, else nono


class dev_only(commands.CommandError):
    pass


class admin_only(commands.CommandError):
    pass


def dev():
    def predicate(ctx):
        if ctx.author.id in config.dev_id:
            return True
        else:
            raise dev_only
    return commands.check(predicate)


def is_admin():
    def predicate(ctx):
        if ctx.author.id in config.admin_ids:
            return True
        else:
            raise admin_only

    return commands.check(predicate)



def create_embed(title= "", description = "", normal = False, warning = False, success = False, error = False):
    if success:
        c = sol
        e = discord.Embed(title=title, description=description, color=c)
        e.set_footer(text=ver)
        return e
    elif normal:
        c = nol
        e = discord.Embed(title=title, description=description, color=c)
        e.set_footer(text=ver)
        return e
    elif warning:
        c = wol
        e = discord.Embed(title=title, description=description, color=c)
        e.set_footer(text=ver)
        return e
    elif error:
        c = eol
        e = discord.Embed(title=title, description=description, color=c)
        e.set_footer(text=ver)
        return e
    else:
        c = nol
        e = discord.Embed(title=title, description=description, color=c)
        e.set_footer(text=ver)
        return e
