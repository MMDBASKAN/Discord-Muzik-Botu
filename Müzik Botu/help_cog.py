import discord
from discord.ext import commands
#from utils import *

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
Komutlar:
.help - Kullanılabilir tüm komutları görüntüler
.oynat <o> - Youtube'dan seçilen bir şarkıyı çalar     kısayol: o
.kuyruk -    Sıradaki geçerli şarkıları görüntüler      kısayol: k
.geç  -      Çalınan geçerli şarkıyı atlar              kısayol: g
.ktemizle -  Müziği durdurur ve kuyruğu temizler        kısayol: kt
.çık -       Botu Ses Kanalından Atar                   kısayol: ç
.durdur -    Çalınan geçerli şarkıyı duraklatı          
.devam -     Bot Şarkıyı Oynatmaya Devam Eder
```
"""
        self.text_channel_list = []


    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        await self.send_to_all(self.help_message)        

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)