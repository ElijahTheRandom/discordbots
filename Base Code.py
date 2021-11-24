#THIS IS ALMOST THE MOST BASIC DISCORD BOT CODE YOU CAN BREAK IT DOWN TO. FEEL FREE TO USE THIS. LET YOUR CREATIVITY FREE.

import discord
import random
import asyncio

game = discord.Game("with your Money") #You can change this to make it play anything


class MyClient(discord.Client):
    global game
    async def on_ready(self):
        print('Logged on as', self.user) #you can change the words in this
        await client.change_presence(activity=game)
        async for guild in client.fetch_guilds(limit=150): #This just prints the names of all the servers the bot is in
            print(guild.name)


    async def on_message(self, message):
        if message.content == "Test": #you can write whatever message you want it to respond to here
            await message.channel.send("hahahaha you can write whatever here")





client = MyClient()
client.run('') #You put your token here
