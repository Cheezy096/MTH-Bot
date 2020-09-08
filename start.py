import asyncio
import itertools
import logging
import subprocess
import sys
import traceback

import discord
from discord.ext import commands

from settings import checks
from settings.config import conf

config = conf()
pre = config.prefix
dol = commands.Bot(command_prefix=pre, status=discord.Status.do_not_disturb, activity=discord.Game(name="Starting..."))
cog = config.cog
nol = config.nombed
name = config.name
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name)

if __name__ == '__main__':
    for extension in cog:
        try:
            dol.load_extension(extension)
            print(f'Loaded {extension}', file=sys.stderr)
        except Exception as e:
            print(f'Failed to load extension {extension} because fuck you.', file=sys.stderr)
            traceback.print_exc()

@dol.command()
@checks.dev()
async def shutdown(ctx):
    embed = discord.Embed(title = ":wave: Bye!", description = "I will now Shut down.", color = nol)
    await ctx.send(embed=embed)
    await dol.change_presence(activity=discord.Game(name="Shutting down..."),status=discord.Status.do_not_disturb)
    await dol.logout()
    await quit()

@dol.command()
@checks.dev()
async def restart(ctx):
    embed = discord.Embed(title = ":wave: Bye!", description = "I will now Restart.", color = nol)
    await ctx.send(embed=embed)
    await dol.change_presence(activity=discord.Game(name="Restarting..."),status=discord.Status.do_not_disturb)
    subprocess.call([sys.executable, "start.py"])
    await dol.logout()

cycled_colors = itertools.cycle(config.rainbow_colors)


async def cycle_rainbow():
    await dol.wait_until_ready()
    while not dol.is_closed():
        for g in dol.guilds:
            r = discord.utils.get(g.roles, name='RainbowMan')
            if r:
                await r.edit(color=discord.Color.from_rgb(*next(cycled_colors)))
        await asyncio.sleep(config.rainbow_speed)

dol.loop.create_task(cycle_rainbow())


dol.run(config.token)

#TODO: Clean up bot 
