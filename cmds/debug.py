'''The Dolphin Core was created by Jake[Cheezy/Popcorn/Cheezy096/CheezyMax]'''

import logging
import platform

from discord.ext import commands

from settings import checks
from settings.config import conf

'''This is the debug command for the dolphin core'''



config = conf()

logging.basicConfig(level=logging.INFO)
# Configures logging.

logger = logging.getLogger("MassMessager")
# Defines the logger.


name = config.name
ver = config.version

nol = config.nombed
cog = config.cog
eol = config.errbed
class Eval(commands.Cog):

    def __init__(self, bot):
        self.b = bot

    def _list_cogs(self):
        cogs = [os.path.basename(f) for f in glob.glob("cmds/*.py")]
        return ["cogs." + os.path.splitext(f)[0] for f in cogs] 



#Is usually enabled however if needed then you can disbale this command by changing enabled=True to enabled=False
    @checks.dev()
    @commands.command(enabled=True)
    async def  debug(self, ctx):
        cmd = ""
        await ctx.send("```Entering debugmode```")
        debug = True
        while debug:
            def check(m):
                return m.author == ctx.message.author and m.channel == ctx.message.channel
            msg2 = await self.b.wait_for('message',check=check, timeout=300)
            if msg2 is None:
                debug = False
            else:
                cmd = msg2.content.split(' ')[0].lower()

                if cmd == "token":
                    await ctx.author.send("```Token: {}```".format(config.token))
                elif cmd == "version":
                    await ctx.send("```Version: {}```".format(config.version))
                elif cmd == "dolphin":
                    await ctx.send('''```Developer Tools: {}
Playing Status: {}
Playing Message: {}
Prefix: {}
Name: {}
Version: {}
Dolphin Core Version: {}```'''.format(config.developer_tools, config.playing_status, config.playing, config.prefix, config.name, config.version, config.dolver))
                elif cmd == "exit":
                    await ctx.send("```Exiting debugmode```")
                    debug = False
                elif cmd == "cog":
                    cog = config.cog
                    await ctx.send("```There are {} cogs present in the config file```".format(len(cog)))
                elif cmd == "devl":
                    await ctx.send("```There are {} users who have full (admin) access to the bot```".format(len(config.dev_id)))
                elif cmd == "dolphin_version":
                    await ctx.send("```Dolphin Core Version: {}```".format(config.dolver))
                elif cmd == "dev_tools":
                    if config.developer_tools == True:	
                        await ctx.send("```Developer Tools: Enabled```")
                    elif config.developer_tools == False:
                        await ctx.send("``` Developer Tools: Disabled```")
                elif cmd == "quit":
                    await ctx.send("```Closing this instance```")
                    quit()
                elif cmd == "file":
                    await ctx.send(f"```Command location: {__file__}```")
                elif cmd == "platform":
                    await ctx.send(f"```Platform: {platform.platform()}```")
                elif cmd == "cogl":
                    loaded = [c.__module__.split(".")[1] for c in self.b.cogs.values()]
                    unloaded = [c.split(".")[1] for c in self._list_cogs()
                                if c.split(".")[1] not in loaded]
                    await ctx.send(loaded)

                 
                elif cmd == None:
                    await ctx.send("No command was given")
                else:
                    await ctx.send('```Command not found.```')
                    debug = True

        else:
            pass


def setup(bot):
    bot.add_cog(Eval(bot))
