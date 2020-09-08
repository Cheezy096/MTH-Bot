'''The Dolphin Core was created by Jake[Cheezy/Popcorn/Cheezy096/CheezyMax]'''

import platform
import sys
import traceback

import discord
from discord.ext import commands as dol

from settings import checks
from settings.config import conf

config = conf()
cog = config.cog
ver = config.version


nol = config.nombed

class dev(dol.Cog):

    def __init__(self, bot):
         self.b = bot

    if config.developer_tools == True:

        @checks.dev()
        @dol.command(hidden=False)
        async def load(self, ctx, *, cog: str):
            try:
                self.b.load_extension(cog)
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            else:
                embed = discord.Embed(title = "Success!", description ="{} was successfully loaded".format(cog), color = nol)
                embed.set_footer(text=ver)
                await ctx.send(embed=embed)

        @dol.command(hidden=False)
        @checks.dev()
        async def unload(self, ctx, *, cog: str):
            try:
                self.b.unload_extension(cog)
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            else:
                embed = discord.Embed(title = "Success!", description ="{} was successfully unloaded".format(cog), color = nol)
                embed.set_footer(text=ver)
                await ctx.send(embed=embed)

        @dol.command(hidden=False)
        @checks.dev()
        async def reload(self, ctx, *, cog: str):
            try:
                self.b.unload_extension(cog)
                self.b.load_extension(cog)
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            else:
                embed = discord.Embed(title = "Success!", description ="{} was successfully reloaded".format(cog), color = nol)
                embed.set_footer(text=ver)
                await ctx.send(embed=embed)


        @dol.command()
        @checks.dev()
        async def refresh(self, ctx):
            """Re-initialise the cogs folder."""
            await ctx.send("Please wait...")
            initial_extensions = cog

            for extension in initial_extensions:
                try:
                    self.b.unload_extension(extension)
                    self.b.load_extension(extension)
                    print(f'Loaded {extension}.')
                except Exception as e:
                    print(f'Failed to load extension {extension} because fuck you.', file=sys.stderr)
                    traceback.print_exc()

        @dol.command(aliases=["stats"])
        @checks.dev()
        async def usage(self,ctx):
            embed=discord.Embed(title="Just some things i guess", colour=nol)
            embed.set_author(name="{}".format(config.name))
            embed.add_field(name="D.py branch", value=str(discord.__version__), inline=True)
            embed.add_field(name="Platform:", value=str(platform.platform()), inline=True)
            embed.add_field(name="Guild count:", value=len(self.b.guilds), inline=True)
            embed.add_field(name="File location:", value=str(__file__), inline=True)
            #embed.add_field(name="Developer ID's:", value=confug.dev_ids, inline=True)
            embed.add_field(name="Version:", value=config.version, inline=True)
            embed.add_field(name="Name:", value=config.name, inline=True)
            embed.add_field(name="Shard Count:", value=self.b.shard_count, inline=True)
            await ctx.send(embed=embed)

        #@dol.command()
        #@checks.dev()
        #async def leave(self,ctx):
        #    embed = discord.Embed(title = "👋 Bye bye!", description ="I'm sorry but i must leave this server now", color = nol)
        #    embed.set_footer(text=ver)
        #    await ctx.send(embed=embed)
        #    server = ctx.guild
        #    await server.leave()


        @dol.command()
        @checks.dev()
        async def say(self, ctx, *, message):
            try:
                await ctx.message.delete()
                await ctx.send(message)
            except discord.errors.Forbidden:
                await ctx.send(message)

        @dol.command()
        @checks.dev()
        async def dm(self, ctx, user:discord.Member, *, message):
            try:
                await ctx.message.delete() #Requires bot to be able to modify files
                await user.send(message)
            except Exception as e:
                await ctx.send(e)


        @dol.command()
        @checks.dev()
        async def game(self, ctx, *,args):
            args = args or 'no arg provided'
            game = discord.Game(name=''.join(args))
            await self.b.change_presence(activity=game)
            try:
                await ctx.send("My playing status has been updated to: {}".format(args))
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')


        @dol.command()
        @checks.dev()
        async def rgame(self, ctx):
            game = discord.Game(name=config.playing)
            await self.b.change_presence(activity=game)
            try:
                await ctx.send("My playing status has been updated to: {}".format(config.playing))
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')



        @dol.command()
        @checks.dev()
        async def listguild(self,ctx):
            embed = discord.Embed(title = "📬 I sent the list to your DM's", color = nol)
            await ctx.send(embed=embed)
            x = '\n'.join([str(guild) for guild in self.b.guilds])

            y = '\n'.join([str(guild.id) for guild in self.b.guilds])
            embed = discord.Embed(title = "I'm in:", description = x, color = nol)
            embed.set_footer(text=ver)
            await ctx.author.send(y)
            return await ctx.author.send(embed = embed)
    #If developer tools is turned set to false in the config file then none of the dev cog will be completely useless
    else:
        pass


def setup(bot):
    bot.add_cog(dev(bot))
