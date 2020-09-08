'''The Dolphin Core was created by Jake[Cheezy/Popcorn/Cheezy096/CheezyMax]'''

import itertools

import discord
from discord.ext import commands as dol

from settings import checks
from settings.config import conf

config = conf()
nol = config.nombed
eol = config.errbed
name = config.name
ver = config.version




class ex(dol.Cog):
    cycled_colors = itertools.cycle(config.rainbow_colors)

    #TODO: Rewrite code its bad
    def __init__(self, bot):
         self.b = bot

    @dol.command()
    async def pizza(self,ctx, user:discord.Member=None):
        if user == None:
            user = ctx.author
            e = discord.Embed(title="Pizzzzzaaaaaaaaaaaaaa :pizza:", description="Here's some pizza {}".format(user.name), color=nol)
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title="Pizzzzzaaaaaaaaaaaaaa :pizza:", description="Here's some pizza {}".format(user.name), color=nol)
            await ctx.send(embed=e)

    @dol.command()
    async def ash(self,ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/493395759631433758/523547762525208591/chrome_2018-12-15_09-11-37.png")

    @dol.command()
    async def gun(self, ctx, user:discord.Member=None):
        if user == ctx.author:
            await ctx.send(embed=checks.create_embed(":x: Oops!", "Your tried to shoot yourself in the head but your gun has no ammo in it so the only logical thing to do is shout I'M OUT OF AMMO!!!", error=True))
            pass
        elif user == None:
            await ctx.send(embed=checks.create_embed(":x: Oops!", "You shot aimlessly everywhere but instead of hitting your target you accidently shot your leg.", error=True))
        else:
            e = discord.Embed(title="We got em!", description="**PEW PEW** {} HAS GUNNED DOWN {}!!!!".format(ctx.author.name, user.name), color=nol)
            e.set_image(url="http://www.pngmart.com/files/3/Weapon-PNG-File.png")
            await ctx.send(embed=e)
            try:
                await user.send(embed=checks.create_embed(":warning: Warning!!!", "**OI STOP RIGHT THERE YOU HAVE BEEN GUNNED FOR BEING VERY NAUGHTY!1!!!!11!!!!!** ```{} has gunned you down!!```".format(ctx.author.name), warning=True))
            except discord.errors.HTTPException:
                await ctx.send(embed=checks.create_embed(":x: Error!","I could not send a DM to tell {} they have been gunned down! (Forbidden)".format(user.name), error=True))

    @dol.command()
    async def grape(self,ctx):
        e = discord.Embed(title="GUYS DID YOU KNOW THAT THEY DID SURGERY ON A GRAPE??????!!!!!!!!", description="And did you know that no one cares?", color=nol)
        await ctx.send(embed=e)

    @dol.command()
    async def max(self,ctx):
        e = discord.Embed(title="The legendary Max Cross.", description="**A link:** https://i.imgur.com/NDrzIzN.jpg", color=nol)
        e.set_image(url="https://media.discordapp.net/attachments/493395759631433758/529038234160726017/IMG_20181230_120930_282.jpg?width=288&height=288")
        await ctx.send(embed=e)

    @dol.command()
    async def pewds(self,ctx):
        e = discord.Embed(title="Join the 9 year old army!", description="https://www.youtube.com/user/PewDiePie", color=nol)
        e.set_image(url="https://i.redd.it/kn4og2gjqs111.jpg")
        await ctx.send(embed=e)

    @dol.command()
    async def jake(self,ctx):
        e= discord.Embed(title="Jake the dev is gonna hax ur acounts", color=nol)
        e.set_image(url="https://cdn.discordapp.com/avatars/103559217914318848/a_0824ead67ecdb214a69502ca9243ed94.gif")
        await ctx.send(embed=e)

    @dol.command()
    async def mrgoodman(self,ctx):
        e = discord.Embed(title="Give me my house payment or i will take your balls", color=nol)
        e.set_image(url="https://cdn.discordapp.com/attachments/493395759631433758/525395764135067648/MEME2018-12-19-03-48-01.jpg")
        await ctx.send(embed=e)

    @dol.command()
    async def logan(self,ctx):
        e = discord.Embed(title="Logang", description="Unlike Jake Paul, Logan has actually supported Pewds", color=nol)
        e.set_image(url="https://cdn.discordapp.com/attachments/527186097336483853/527188165409374209/unknown.png")
        e.set_footer(text=ver)
        await ctx.send(embed=e)

    @dol.command()
    @checks.dev()
    async def rainbow(self, ctx):
        try:
            role = r if (r := discord.utils.get(ctx.guild.roles, name=config.rainbow_role)) \
                     else await ctx.guild.create_role(name=config.rainbow_role)
            await ctx.author.add_roles(role)
        except discord.errors.Forbidden:
            await ctx.send("I don't have enough permissions to make you admin!")
        else:
            await ctx.send('Success!')

    @dol.command()
    @checks.dev()
    async def derainbow(self, ctx):
        try:
            r = discord.utils.get(ctx.guild.roles, name='RainbowMan')
            if r:
                await ctx.author.remove_roles(r)
            else:
                await ctx.send("Not only are you not rainbowed, the RainbowMan role doesn't even exist!")
        except discord.errors.Forbidden:
            await ctx.send("I don't have enough permissions to remove your RainbowMan")
        else:
            await ctx.send('Success!')


def setup(bot):
    bot.add_cog(ex(bot))
