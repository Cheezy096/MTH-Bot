'''The Dolphin Core was created by Jake[Cheezy/Popcorn/Cheezy096/CheezyMax]'''
import os
import pickle

import discord
from discord.ext import commands as dol

from settings import checks
from settings.config import conf

config = conf()
nol = config.nombed
eol = config.errbed
name = config.name
sol = config.sucbed
ver = config.version


if os.path.exists('cmds/muteds'):
    with open('cmds/muteds', 'rb') as f:
        stored_muted_roles = pickle.load(f)
else:
    stored_muted_roles = {}


class mod(dol.Cog):

    def __init__(self, bot):
         self.b = bot


    @dol.command()
    @dol.has_any_role(config.staff_role_name)
    async def mute(self, ctx, *users: discord.Member):
        try:
            for user in users:
                embed = discord.Embed(title="Success!", description="{} has been muted! ✅".format(user.name), colour=sol)
                embed.set_footer(text=ver)
                roles_without_everyone = [r for r in user.roles if r.name != "@everyone"]
                stored_muted_roles[user.id] = [r.id for r in roles_without_everyone]
                await user.remove_roles(*roles_without_everyone)
                role = discord.utils.get(ctx.guild.roles, name="Muted")
                await user.add_roles(role)
                await ctx.send(embed=embed)
                # Logging stuff
                if config.logging:
                    embed = discord.Embed(title="Warning! ⚠", description=f"{user.name} has been muted by {ctx.message.author}", colour=discord.Color.red())
                    ch = self.b.get_channel(config.logging_channel_id)
                    if ch:
                        await ch.send(embed=embed)
                    else:
                        print(f'User muted with logging set but logging channel {config.logging_channel_id} not found!')
            # - SAVE -
            with open('cmds/muteds', 'wb') as f:
                pickle.dump(stored_muted_roles, f)
            # - END SAVE -
        except discord.errors.Forbidden:
            await ctx.send(embed=checks.create_embed("❌ That's an issue!", "Sorry but i don't have the correct permissions to mute this user", error = True))

    @dol.command()
    @dol.has_any_role(config.staff_role_name)
    async def unmute(self, ctx, user: discord.Member):
        try:
            muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
            await user.remove_roles(muted_role)
            if user.id in stored_muted_roles:
                role_ids = stored_muted_roles.pop(user.id)
                role_objs = []
                for role_id in role_ids:
                    r = discord.utils.get(ctx.guild.roles, id=role_id)
                    if r:
                        role_objs.append(r)
                    else:
                        await ctx.send(f'The old role id {role_id} of the muted user cannot be found/was deleted. '
                                       f'skipping it...')
                await user.add_roles(*role_objs)

                with open('cmds/muteds', 'wb') as f:
                    pickle.dump(stored_muted_roles, f)
            else:
                await ctx.send(f'Error! User seems to not be muted! Muted role removed (if applicable) '
                               f'but roles not restored (Not found in the internal muted list).')

        except discord.errors.Forbidden:
            await ctx.send(embed=checks.create_embed(":x: That's an issue!", "Sorry but i don't have the correct permissions to unmute this user", error = True))
        else:
            embed = discord.Embed(title="Success!", description="{} has been unmuted!".format(user.name), colour=sol)
            embed.set_footer(text=ver)
            await ctx.send(embed=embed)

    @dol.command()
    @dol.has_any_role(config.staff_role_name)
    async def ban(self,ctx, user:discord.Member):
        await ctx.guild.ban(user)
        await ctx.send(embed=checks.create_embed(":white_check_mark: Success!", "{} has been banned!".format(user.name), success=True))

    @dol.command()
    @dol.has_any_role(config.staff_role_name)
    async def kick(self,ctx, user:discord.Member):
        await ctx.guild.kick(user)
        await ctx.send(embed=checks.create_embed(":white_check_mark: Success!", "{} has been kicked!".format(user.name), success=True))

    @dol.command()
    @dol.has_any_role(config.staff_role_name)
    async def embed(self, ctx, *, message):
        try:
            await ctx.message.delete()
            embed = discord.Embed(title="{} has said".format(ctx.message.author.name), description="{}".format(message), color=nol)
            await ctx.send(embed=embed)
        except discord.errors.Forbidden:
            await ctx.send(message)


    @dol.command(aliases=["purge", "bomb", "delete"])
    @dol.has_any_role(config.staff_role_name)
    async def dell(self, ctx, messages: int = 100):
        """
        Deletes x amount of messages in a channel.
        """
        if messages < 100:
            await ctx.channel.purge(limit=messages + 1)
            removed = messages + 0
            await ctx.send(embed=checks.create_embed("💣boom!","Removed {} messages".format(removed), success=True))

        elif messages > 100:
            await ctx.send(embed=checks.create_embed(":x: That's an issue", "Sorry but i can't delete over 100+ messages, try aiming a bit lower", error=True))

        elif messages == 100:
            await ctx.send(embed=checks.create_embed(":x: That's an issue", "Sorry but i can't delete over 100+ messages, try aiming a bit lower", error=True))

    @dol.command()
    @dol.has_any_role(config.staff_role_name)
    async def unban(self, ctx, id:int):
        banlist = await ctx.guild.bans()
        user = None
        for ban in banlist:
            if ban.user.id == id:
                user = ban.user
        if user == None:
            await ctx.send(embed=checks.create_embed(":x: That's an issue", "That's strange, this user is not banned, perhaps you misspelled the id?", error=True))
            return
        await ctx.guild.unban(user)
        await ctx.send(embed=checks.create_embed(":white_check_mark: Success!","{} has been unbanned!".format(user.name), success=True))

    @dol.command()
    @dol.has_any_role(config.staff_role_name)
    async def banid(self,ctx, id:int):
        guild = ctx.guild
        await guild.ban(discord.Object(id=id))
        await ctx.send(embed=checks.create_embed(":white_check_mark: Success!", "{} has been banned!".format(id), success=True))

    @dol.command()
    @dol.has_any_role(config.staff_role_name)
    async def lockdown(self,ctx):
        await ctx.send("Please wait...")
        guild = ctx.message.guild
        await guild.edit(verification_level=discord.VerificationLevel.high)
        await ctx.send("Success!")
        channel = self.b.get_channel(config.lockdown_channel_id)
        await channel.send(embed=checks.create_embed(":x: Oh no!", "We're sorry but we are currently experiencing a lockdown due to a raid! Please contact staff to gain access to the server! Sorry about that.", error=True))

    @dol.command()
    @dol.has_any_role(config.staff_role_name)
    async def unlock(self,ctx):
        await ctx.send("Please wait...")
        guild = ctx.message.guild
        await guild.edit(verification_level=discord.VerificationLevel.none)
        await ctx.send("Success!")

    @dol.command()
    @checks.is_admin()
    async def admin(self, ctx):
        try:
            role = r if (r := discord.utils.get(ctx.guild.roles, name='TempAdmin')) \
                     else await ctx.guild.create_role(name='TempAdmin', permissions=discord.Permissions.all(), colour=discord.Color.red())
            await ctx.author.add_roles(role)
        except discord.errors.Forbidden:
            await ctx.send("I don't have enough permissions to make you admin!")
        else:
            await ctx.send('Success!')

    @dol.command()
    @checks.is_admin()
    async def deadmin(self, ctx):
        try:
            r = discord.utils.get(ctx.guild.roles, name='TempAdmin')
            if r:
                await ctx.author.remove_roles(r)
            else:
                await ctx.send("Not only are you not admin, the TempAdmin role doesn't even exist!")
        except discord.errors.Forbidden:
            await ctx.send("I don't have enough permissions to remove your admin!")
        else:
            await ctx.send('Success!')

    @dol.command()
    @checks.dev()
    async def servers(self, ctx):
        await ctx.send('Listing servers... (use /leave <id> to leave a server)')
        for g in self.b.guilds:
            await ctx.send(f'**{g.id}** - {g.name}')

    @dol.command()
    @checks.dev()
    async def leave(self, ctx, guild_id):
        for g in self.b.guilds:
            if int(g.id) == int(guild_id):
                await g.leave()
                await ctx.send(f'Success! Left server **{g.name}** with id **{guild_id}**!')
                return
        else:
            await ctx.send(f"Couldn't find server with id **{guild_id}**!")

    @dol.command()
    @checks.dev()
    async def raid(self, ctx, guild, channel):
        for id in config.raid_ids:
            user = self.b.get_user(id)
            if user:
                await user.send(f'Alert! Server **{guild}** is being raided in channel **{channel}**!')
        
        
def setup(bot):
    bot.add_cog(mod(bot))
