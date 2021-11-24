import random
import asyncio
import aiohttp
import discord
import json
from discord.ext import commands
from discord import Game
from discord.ext.commands import Bot
import datetime
from discord.utils import get
import time

TOKEN = ''
 
client = discord.Client()
server2 = "server 2"
botnum = 0
servers1 = "server 1"
Jboogers = 0
say = 0
msg1 = ""
msg2 = ""
msg3 = ""
msg4 = ""
msg5 = ""
msg6 = ""
msg7 = ""
spaces = " "
thevoice = random.choice(["I have observed..", "It seems..", "My research concludes to.."])
quotes = '"'
ran1 = random.randint(1,6)
ran2 = random.randint(7,10)
ran3 = random.randint(11,15)
ran4 = random.randint(16,18)
ran5 = random.randint(19,20)
emoji = ""
ran6 = random.randint(21,24)
game = "with Rocks"
class MyClient(discord.Client):
    async def on_ready(self):
        global game
        print('Logged on as', self.user)
        await client.change_presence(activity=game)
        print("------------")
        async for guild in client.fetch_guilds(limit=150):
            print(guild.name)
 
 

    async def on_message(self, message):
        global botnum
        global Jboogers
        global msg1
        global msg2
        global msg3
        global msg4
        global msg5
        global msg6
        global msg7
        global spaces
        global thevoice
        global quotes
        global ran1
        global ran2
        global ran3
        global ran4
        global ran5
        global ran6
        global say
        global servers1
        global servers2
        global emoji
# we do not want the bot to reply to itself
        if message.author == client.user:
            return
        elif message.content == 'Opportunity':
            msg = random.choice(["Beep boop", "RIP Opportunity 2019"]).format(message)
            await message.channel.send(msg)
        elif message.content == 'Opportunity Number':
            msg = "Message number: {}".format(botnum, message)
            await message.channel.send(msg)
        elif message.content == 'Opportunity Version':
            msg = "Version 1.5.1".format(botnum, message)
            await message.channel.send(msg)
        elif message.content == 'Opportunity Now':
            msg4 = random.choice([thevoice + quotes + msg1 + spaces + msg2 + spaces + msg3 + quotes, thevoice + quotes + msg5 + spaces + msg2 + spaces + msg6 + quotes, thevoice + quotes + msg2 + spaces + msg5 + spaces + msg7 + quotes]).format(message)
            await message.channel.send(msg)
        elif message.content == 'Opportunity Servers':
            servers = list(client.servers)
            servers1 = (f"Connected on {str(len(servers))} servers:")
            servers2 =('\n'.join(server.name for server in servers))
            msg = "{}{}".format(servers1,servers2,message)
            await message.channel.send(msg)
        elif botnum == ran1:
            msg1 = message.content
            botnum += 1 
            await client.add_reaction(message, "👍")
        elif botnum == ran2:
            msg2 = message.content
            await client.add_reaction(message, "👍")
            botnum += 1
        elif botnum == ran3:
            msg3 = message.content
            await client.add_reaction(message, "👍")
            botnum += 1
        elif botnum == ran4:
            msg5 = message.content
            await client.add_reaction(message, "👍")
            botnum += 1 
        elif botnum == ran5:
            msg6 = message.content
            await client.add_reaction(message, "👍")
            botnum += 1 
        elif botnum == ran6:
            msg7 = message.content
            await client.add_reaction(message, "👍")
            botnum += 1 
        elif botnum == 25:
            msg4 = random.choice([thevoice + quotes + msg1 + spaces + msg2 + spaces + msg3 + quotes, thevoice + quotes + msg5 + spaces + msg2 + spaces + msg6 + quotes, thevoice + quotes + msg2 + spaces + msg5 + spaces + msg7 + quotes]).format(message)
            await message.channel.send(msg4)
            botnum = 0
        elif message.content.startswith('watermelon'):
            Jboogers += 1
        else:
            botnum += 1
client.run("")
