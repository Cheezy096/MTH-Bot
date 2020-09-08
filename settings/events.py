'''The Dolphin Core was created by Jake[Cheezy/Popcorn/Cheezy096/CheezyMax]'''

import discord
from discord.ext import commands as dol

from settings.config import conf

config = conf()
nol = config.nombed
eol = config.errbed
name = config.name
ver = config.version
playing = config.playing

class Event(dol.Cog):

    def __init__(self, bot):
         self.b = bot

    @dol.Cog.listener()
    async def on_ready(self):
        print("Ready!")
        try:
            if config.watermark == "01a":
                ver = config.version
                pass
        except Exception:
            ver = config.version+" Created by Cheezy[Jake R.]"
            print("Please pay for this product to remove the watermarks.")

        
         
        if config.playing_status == True:
            game = discord.Game(name=playing)
            await self.b.change_presence(activity=game,status=discord.Status.online)
        elif config.playing_status == False:
            pass
        else:
            pass

    @dol.Cog.listener()
    async def on_member_join(self,member: discord.Member):
        for channel in member.guild.channels:
            if channel.name == config.welcome_msg_channel:
                embed = discord.Embed(title = ":wave: Hi there!", description = "{} has joined {}".format(member.name, member.guild.name), color = nol)
                await channel.send(embed=embed)
                return

    @dol.Cog.listener()        
    async def on_member_remove(self,member):
        for channel in member.guild.channels:
            if channel.name == config.welcome_msg_channel:
                embed = discord.Embed(title = ":wave: Shame to see you go! :", description = "{} has left this server".format(member.name), color = nol)
                await channel.send(embed=embed)

    @dol.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot and config.logging:
            if message.guild:
                s = f'[{message.guild.name}/{message.channel.name}] **{message.author.name}:** {message.content}'
            else:
                s = f'[DM] **{message.author.name}:** {message.content}'  # Assume it's a DM if there's no guild here.
            ch = self.b.get_channel(config.logging_channel_id)
            if ch:
                await ch.send(s)
            else:
                print(f'Logging is turned on but logging channel with id {config.logging_channel_id} not found! '
                      f'This message was supposed to be sent:')
                print('-' * 10 + '\n' + s + '\n' + '-' * 10)

def setup(bot):
    bot.add_cog(Event(bot))
