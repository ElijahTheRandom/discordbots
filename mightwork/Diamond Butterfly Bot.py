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
from time import sleep



client = discord.Client()

#pfp_path = r"/home/pi/Desktop/Eclipsa/Eclipsa2.jpg"

#fp = open(#pfp_path, 'rb')
#p#fp = fp.read()
me = "<@586998711415078952>"
new_username='Eclipsa'
change = 0
dialog = 1
messagechoice  = random.randint(100,300)
messagenumber = 0
#servername = "beep boop bots"
#server = discord.utils.get(client.servers, name=servername)
discordgame = discord.Game("with Magic")
game = 0
game2 = 0
game3 = 0
game4 = 0
game5 = 0
moongametitle = "the Strange"
moonstatsmon = 10
moonstatsmew = 10
moonstatshighcom = 10
currentqueen = 0
currentqueenname = 0
currentqueennum = 0
turns = 0
currentqueenknight1 = 0
currentqueenknight2 = 0
currentqueenknight3 = 0
currentqueensquire = 0
currentqueenknight1name = 0
currentqueenknight2name = 0
currentqueenknight3name = 0
currentqueensquirename = 0
queennews = "blank"
squirenews = "blank"
currentqueenking = 0
currentqueenkingname = 0
currentnotqueen = 0
game6 = 0
spiderbites = 0
monsters = 0
ponyheads = 0
underworld = 0
strength = 0
intel = 0
fanswapnum = 0
fanswapcount = 0
diamond = 0
notdiamond = 0
diamondnum = 0
diamondname = 0
diamond2 = 0
notdiamond2 = 0
diamondnum2 = 0
diamondname2 = 0
diamond3 = 0
notdiamond3 = 0
diamondnum3 = 0
diamondname3 = 0
diamond4 = 0
notdiamond4 = 0
diamondnum4 = 0
diamondname4 = 0
class MyClient(discord.Client):
    async def on_ready(self):
        global discordgame
        print('Logged on as', self.user)
        await client.change_presence(activity=discordgame)
        print("------------")
        async for guild in client.fetch_guilds(limit=150):
            print(guild.name)

    async def on_message(self, message):
    # we do not want the bot to reply to itself
        #global #pfp_path
        #global fp
        #global pfp
        global me
        global new_username
        global dialog
        global change
        global messagenumber
        global messagechoice
        global servername
        global server
        global game
        global game2
        global game3
        global game4
        global moonstatshighcom
        global moonstatsmew
        global moonstatsmon
        global turns
        global currentqueen
        global game5
        global currentqueenname
        global currentqueennum
        global moongametitle
        global currentqueenknight1
        global currentqueenknight2
        global currentqueenknight3
        global currentqueensquire
        global currentqueenknight1name
        global currentqueenknight2name
        global currentqueenknight3name
        global currentqueensquirename
        global queennews
        global squirenews
        global currentqueenking
        global currentqueenkingname
        global currentnotqueen
        global game6
        global monsters
        global ponyheads
        global spiderbites
        global underworld
        global fanswapnum
        global fanswapcount
        global diamond
        global notdiamond
        global diamondnum
        global diamondname
        global diamond2
        global notdiamond2
        global diamondnum2
        global diamondname2
        global diamond3
        global notdiamond3
        global diamondnum3
        global diamondname3
        global diamond4
        global notdiamond4
        global diamondnum4
        global diamondname4
        if message.author == client.user:
            return
        elif message.content == 'fun fun' and dialog == 2 and fanswapnum == 0:
            msg = "I am Festivia the Fun!".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly Server':
            msg = "https://discord.gg/6ZMK74Q".format(message)
            await message.channel.send(msg)
        elif message.content == 'magic' and dialog == 1 and fanswapnum == 0:
            msg = "I am Eclipsa the Queen of Darkness. Creator of Spells!".format(message)
            await message.channel.send(msg)
        elif message.content == 'Cleave the Bond, Break the Magic. Queens shall die.':
            currentqueenname = 0
            currentqueen = 0
            currentqueennum = 0
            currentqueenknight1 = 0
            currentqueenknight2 = 0
            currentqueenknight3 = 0
            currentqueensquire = 0
            currentqueenknight1name = 0
            currentqueenknight2name = 0
            currentqueenknight3name = 0
            currentqueensquirename = 0
            queennews = 0
            squirenews = 0
            currentqueenking = 0
            currentqueenkingname = 0
        elif message.content == 'Cleave the Bond, Break the Magic. Squires shall die.':
            currentqueensquire = 0
        elif message.content == 'Butterfly Info':
            msg = "Butterfly Bot was created by Popleoma#2491 and is coded in Python! It was a fun bot originally. It has taught me tons about Python and I appreciate everyone who uses it!".format(message)
            await message.channel.send(msg)
        elif message.content.startswith('News:') and message.author == currentqueen:
            queennews = message.content
            await client.send_message(client.get_channel('613503880277524490'), 'Queen {}'.format(queennews,message))
            await client.send_message(client.get_channel('614216403503022120'), 'Queen {}'.format(queennews,message))
        elif message.content.startswith('News:') and message.author == currentqueensquire:
            squirenews = message.content
            await client.send_message(client.get_channel('613503880277524490'), 'Squire {}'.format(squirenews,message))
            await client.send_message(client.get_channel('614216403503022120'), 'Squire {}'.format(squirenews,message))
        elif message.content == 'Butterfly Current Queen News':
            msg = "**QueenNews** {}".format(queennews,message)
            await message.channel.send(msg)
            msg = "**SquireNews** {}".format(squirenews,message)
            await message.channel.send(msg)

        elif message.content == 'Butterfly Knight Claim 354' and currentqueenknight1 == 0:
            currentqueenknight1 = message.author
            msg = "Knight {}".format(currentqueenknight1,message)
            await message.channel.send(msg)
            await client.send_message(currentqueenknight1, "You can choose your knight name with 'Name:(name)'")
        elif message.content.startswith('Name:') and message.author == currentqueenknight1 and currentqueennum == 1:
            currentqueenknight1name = message.content
            await client.send_message(client.get_channel('613495754534944780'), 'Rise Knight {}, {}!'.format(currentqueenknight1name, currentqueenknight1))
            msg = "You are now Knight: {}!".format(currentqueenknight1name,message)
            await message.channel.send(msg)

        elif message.content == 'Butterfly King Claim 1040' and currentqueenking == 0:
            currentqueenking = message.author
            msg = "King {}".format(currentqueenking,message)
            await message.channel.send(msg)
            await client.send_message(currentqueenking, "You can choose your King name with 'Name:(name)'")
        elif message.content.startswith('Name:') and message.author == currentqueenking and currentqueennum == 1:
            currentqueenkingname = message.content
            await client.send_message(client.get_channel('613495754534944780'), 'King {}, {}!'.format(currentqueenkingname, currentqueenking))
            await client.send_message(client.get_channel('614204564958347288'), 'King {}, {}! Wedded to {}'.format(currentqueenkingname, currentqueenking, currentqueenname))
            msg = "You are now King: {}!".format(currentqueenkingname,message)
            await message.channel.send(msg)

        elif message.content == 'Butterfly Knight Claim 543' and currentqueenknight2 == 0:
            currentqueenknight2 = message.author
            msg = "Knight {}".format(currentqueenknight2,message)
            await message.channel.send(msg)
            await client.send_message(currentqueenknight2, "You can choose your knight name with 'Name:(name)'")
        elif message.content.startswith('Name:') and message.author == currentqueenknight2 and currentqueennum == 1:
            currentqueenknight2name = message.content
            await client.send_message(client.get_channel('613495754534944780'), 'Rise Knight {}, {}!'.format(currentqueenknight2name, currentqueenknight2))
            msg = "You are now Knight: {}!".format(currentqueenknight2name,message)
            await message.channel.send(msg)

        elif message.content == 'Butterfly Knight Claim 564' and currentqueenknight3 == 0:
            currentqueenknight3 = message.author
            msg = "Knight {}".format(currentqueenknight3,message)
            await message.channel.send(msg)
            await client.send_message(currentqueenknight3, "You can choose your knight name with 'Name:(name)'")
        elif message.content.startswith('Name:') and message.author == currentqueenknight3 and currentqueennum == 1:
            currentqueenknight3name = message.content
            await client.send_message(client.get_channel('613495754534944780'), 'Rise Knight {}, {}!'.format(currentqueenknight3name, currentqueenknight3))
            msg = "You are now Knight: {}!".format(currentqueenknight3name,message)
            await message.channel.send(msg)

        elif message.content == 'Butterfly Squire Claim 123' and currentqueensquire == 0:
            currentqueensquire = message.author
            msg = "Squire {}".format(currentqueensquire,message)
            await message.channel.send(msg)
            await client.send_message(currentqueensquire, "You can choose your squire name with 'Name:(name)' . You can also write into the Queen News! Just say 'News: (news)'")
        elif message.content.startswith('Name:') and message.author == currentqueensquire and currentqueennum == 1 and fanswapnum == 0:
            currentqueensquirename = message.content
            await client.send_message(client.get_channel('613495754534944780'), 'Rise Squire {}, {}!'.format(currentqueensquirename, currentqueensquire))
            msg = "You are now Squire: {}!".format(currentqueensquirename,message)
            await message.channel.send(msg)

        elif message.content == 'Butterfly Divorce' and message.author == currentqueen:
            currentqueenking = 0
            currentqueenkingname = 0
            msg = "Successfully Divorced!"
            await client.send_message(message.channel,msg)

        elif message.content == 'Butterfly Claim' and currentqueen == 0:
            currentqueen = message.author
            currentnotqueen = message.author
            msg = "Long live the Queen! {}".format(currentqueen,message)
            await message.channel.send(msg)
            await client.send_message(currentqueen, "As Queen you can automatically change the queen. If you change the queen too many times the picture will stop changing due to discord limitations. Try to limit yourself to once or twice per hour! You lose your Queen rank whenever the Bot Resets But your name is Recorded! **Choose your name with 'Name:(your name and a title (you dont have to have a title))'**")   
            await client.send_message(currentqueen, "You can also have Entries. **Use 'Entry: (entry)' to put something in the book of spells!**")
            await client.send_message(currentqueen, "As Queen you can pick a Squire a King and 3 Knights! Use the command 'Butterfly Court Creation' to get codes!")
            await client.send_message(currentqueen, "You can also make a News statement! Just Send 'News: (news)' you can see the News with 'Butterfly Current Queen News'")

        elif message.content == 'Butterfly Claim' and message.author == currentnotqueen:
            msg = "You had your shot!".format(currentqueen,message)
            await message.channel.send(msg)

        elif message.content == 'Butterfly Court Creation' and message.author == currentqueen:
            await client.send_message(currentqueen, "King Command and code: 'Butterfly King Claim (code)' Current Codes: 1040")
            await client.send_message(currentqueen, "Squire Command and code: 'Butterfly Squire Claim (code)' Current Codes: 123")
            await client.send_message(currentqueen, "Knight Commands and code: 'Butterfly Knight Claim (code)' Current Codes: 354, 543, and 564")
        elif message.content == 'Butterfly Current Queen':
            msg = "Current Queen Butterfly: {}; {}".format(currentqueenname,currentqueen,message)
            await message.channel.send(msg)
            msg = "Current Royal Court: King: {}; Squire: {}; Knights: {}, {}, {}".format(currentqueenkingname,currentqueensquirename,currentqueenknight1name,currentqueenknight2name,currentqueenknight3name,message)
            await message.channel.send(msg)
        elif message.content.startswith('Name:') and message.author == currentqueen and currentqueennum == 0:
            currentqueenname = message.content
            await client.send_message(client.get_channel('612362848554975245'), 'All Hail Queen {}, {}!'.format(currentqueenname, currentqueen))
            await client.send_message(client.get_channel('614204564958347288'), 'All Hail Queen {}, {}!'.format(currentqueenname, currentqueen))
            msg = "You are now Queen: {}!".format(currentqueenname,message)
            await message.channel.send(msg)
            currentqueennum = 1


        elif message.content == 'Butterfly Suggestion':
            msg = "Send your Suggestion with the format: 'Suggestion: (suggestion)'".format(message)
            await message.channel.send(msg)
        elif message.content.startswith('Suggestion:'):
            game4 = message.content
            await client.send_message(client.get_channel('612351642146177024'), '{}'.format(game4))
            game4 = 0
            msg = "Suggestion Sent!".format(message)
            await message.channel.send(msg)
        elif message.content.startswith('Entry:') and message.author == currentqueen:
            game4 = message.content
            await client.send_message(client.get_channel('612377720726487040'), '{} by **{}**'.format(game4, currentqueenname))
            await client.send_message(client.get_channel('614204438457876498'), '{} by **{}**'.format(game4, currentqueenname))
            await client.send_message(currentqueen, "Entry Recorded! You can make more entries if you want!")
            game4 = 0
        elif message.content == 'Butterfly Version':
            msg = "Version 1.6.0".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly Changelog':
           # msg = "```1.5.0 8/17/19: Updated Butterfly Messages, Worked on Moon Game (not finished), added new commands (Butterfly Help for the list), fixed some minor bugs, changed Eclipsa's picture```".format(message)
            #await message.channel.send(msg)
            #msg = "```1.5.1 8/17/19: Added a Suggestion command```".format(message)
            #await message.channel.send(msg)
            #msg = "```1.5.2 8/17/19: Added Current Queen Commands and Abilities. Squished some major bugs```".format(message)
            #await message.channel.send(msg)
            #msg = "```1.5.3 8/18/19: Squished some bugs, fixed some mistakes, ate 23 pizza rolls.. Finished Moon's Game```".format(message)
            #await message.channel.send(msg)
            #msg = "```1.5.4 8/19/19: Tweaked some Moon game stuff. Suffered through school... Fixed some bugs.. Added Green the Diamond's chapter```".format(message)
            #await message.channel.send(msg)
            #msg = "```1.5.5 8/20/19: Added 'Butterfly Info' (completely forgot to make it). Added Royal Titles/Court and the Queen News ```".format(message)
            #await message.channel.send(msg)
            #msg = "```1.5.5 8/21/19: Fixed some minor bugs. Added Devon the Dead Rose's chapter ```".format(message)
            #await message.channel.send(msg)
            msg = "```1.5.5 8/23/19: Added Breezenia's chapter. Added a Butterfly Server command. Fixed some bugs~ ```".format(message)
            await message.channel.send(msg)
            msg = "```1.5.6 8/23/19: Added two chapters! Added Festivias game ```".format(message)
            await message.channel.send(msg)
            msg = "```1.5.6 8/23/19: Added Oli's chapter. Fixed Festivia's game! Fixed Kings```".format(message)
            await message.channel.send(msg)
            msg = "```1.6.0 10/19/19: Added New Chapters, Added SU section, Added all Diamond commands```".format(message)
            await message.channel.send(msg)
        elif message.content == 'Who are you?':
            msg = "I am.. {}".format(new_username, message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly Invite':
            msg = "https://discordapp.com/api/oauth2/authorize?client_id=586998711415078952&permissions=8&scope=bot".format(message)
            await message.channel.send(msg)
        elif message.content == 'Passcode: 8675309':
            messagenumber = messagechoice
            msg = "Time.. Speeding.. Up! needed messages: {}; message amount: {};".format(messagechoice,messagenumber,new_username, message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly Values':
            msg = "dialog: {}; name: {}; needed messages: {}; message amount: {}; turns: {}; overall message amount {};".format(dialog,new_username,messagechoice,messagenumber, turns, fanswapcount,message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly Help':
            msg = "Queen Butterflys, Butterfly Server, Butterfly Values, Butterfly Info, Butterfly Version, Butterfly Claim, Butterfly Current Queen, Butterfly Suggestion, Butterfly, Butterfly Invite, Butterfly Changelog, Butterfly Current Queen News, and Butterfly Game (not all queens have a game yet). Whenever in Values message needed is equal to message count you can do 'Summon (Queen's title)' for example 'Summon the Fun' Everything is Case Sensitive! WE HAVE A HELP FOR THE DIAMOND SECTION TOO 'Diamond Help', **'Butterfly Help 2' for more Help** ".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly Help 2':
            msg = "Each Canon Queen will have their own Game. You can swap fandoms to SU from SVTFOE or vise versa by 'Fandom Swap (SU or SVTFOE)' **'Butterfly Help 3' for more help**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly Help 3':
            msg = "Every time the bot restarts someone can become the Current Queen by sending 'Butterfly Claim' before anyone else. This person can swap queens without having to meet the message requirement. They also get a name that will go into the book of spells. **'Butterfly Help 4' for more help**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly Help 4':
            msg = "Each Current Queen will have a chapter in the Book of Spells. This is done manually so it may take a bit for the entries to be put in for good. To see the Book of Spells Index send 'Book of Spells'. To see a specific chapter do 'Book of Spells (number of chapter)' to see their court do 'Book of Spells (chapter number) Court'! To see the old Book of Spells say 'Old Book of Spells'".format(message)
            await message.channel.send(msg)

        elif message.content == 'Diamond Help':
            msg = "Diamonds , Butterfly Server, Butterfly Values, Butterfly Info, Butterfly Version, Diamond Claim, Diamond Current Leader, Butterfly Suggestion, Diamond, Butterfly Invite, and Butterfly Changelog. Whenever in Values message needed is equal to message count you can do 'Summon (Diamond's color)' for example 'Summon White' Everything is Case Sensitive! Use 'Diamond Log' to see the past Gem Overlords and their logging. Gem Overlords work the same as Queen. ".format(message)
            await message.channel.send(msg)















    #@client.event
    #async def changes():
       # global change
     #   global #pfp_path
      #  global fp
       # global pfp
        #global me
        #global new_username
        elif message.content == 'Summon the Queen of Darkness' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 1
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Eclipsa2.jpg"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Eclipsa"
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Eclipsa")
            time.sleep(2)
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing..".format(message)
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1hour
            msg = "I am Eclipsa Butterfly".format(message)
            await message.channel.send(msg)
            #change = 0
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Fun' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 2
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Festivia.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Festivia"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Festivia")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Festivia Butterfly!!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Shy' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 3
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Celena.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Celena"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Celena")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Celena Butterfly...".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Chef' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 4
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Comet.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Comet"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Comet")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Comet Butterfly!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Eager' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 5
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Crescenta.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Crescenta"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Crescenta")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Crescenta Butterfly!!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Heaped' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 6
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Dirhhuennia.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Dirhhuennia"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Dirhhuennia")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Dirhhuennia Butterfly..".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Drafted' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 7
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Estrella.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Estrella"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Estrella")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Estrella Butterfly..".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Uncalculated' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 8
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Jushtin.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Jushtin"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Jushtin")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Jushtin Butterfly!!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon Meteora' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 9
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Meteora.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Meteora"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Meteora")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "Meteora Butterfly!? Ghaahgoogoo".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Undaunted' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 10
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Moon.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Moon"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Moon")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Moon Butterfly!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Riddled' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 11
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Rhina.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Rhina"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Rhina")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Rhina Butterfly..?".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Queen of Hours' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 12
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Skywynne.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Skywynne"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Skywynne")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Skywynne Butterfly.".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Monster Carver' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 13
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Solaria.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Solaria"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Solaria")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Solaria Butterfly! Die ungreatful monsters!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Underestimated' and messagechoice <= messagenumber and fanswapnum == 0:
            dialog = 14
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Star.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Star"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Star")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Star Butterfly!!!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Butterfly' and dialog == 1: #Eclipsa
            msg = "I am Eclipsa the Queen of Darkness. Creator of the Dark Chapter of Spells!".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly' and dialog == 2: #Festivia
            msg = "I am Festivia the Fun! The Beginning of a Broken Family Line.. Pie Folk Rock! Let's Party Till We're Purple!".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly' and dialog == 3: #Celena
            msg = "I am.. Celena the Shy.. uhum bye..".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly' and dialog == 4: #Comet
            msg = "I am Comet the Chef! I'll bake my way into your heart! Gotta love the pies".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly' and dialog == 5: #Crescenta
            msg = "I am Crescenta the Eager! Unlike my sister.. Dirhhuennia.. I will fight for this Kingdom! Don't like me? Too Bad!".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly' and dialog == 6: #Dirhhuennia
            msg = "*grunts* im that Dirhhuennia the Heaped... I had rather do my own thing. Pfft kingdom smingdom no one cares Crescenta! Circles are the best o o O o o O o o O o o O O O".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly' and dialog == 7: #Estrella
            msg = "I am Estrella the Drafted. Queen? I'd rather draw..".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly' and dialog == 8: #Jushtin
            msg = "I am Jushtin the Uncalculated! Love me! Adore me! The Only Male Ruler of Mewni! Ahh Take a Picture It Lasts Longer! Math Rules!".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly' and dialog == 9: #Meteroa
            msg = "Meteora. Hfblabla! goo goo!".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly' and dialog == 10: #Moon
            msg = "I am Moon the Undaunted! I betrayed my kingdom and the Queen.. I will never forget what I have done.".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly' and dialog == 11: #Rhina
            msg = "I am Rhina the Riddled. Riddles are for me.. Have a riddle huh huh? no. okay bye.".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly' and dialog == 12: #Skywynne
            msg = "I am Skywynne the Queen of Hours! Limited by time? Hah. I have created tons of powerful spells! I even destroyed a dimension.. Butterfly Form is too strong.".format(message)
            await message.channel.send(msg)
        elif message.content == 'Butterfly' and dialog == 13: #Solaria
            msg = "I am Solaria the Monster Carver! Monsters are what makes this kingdom WEAK! We will DESTROY them ALL.".format(message)
            await message.channel.send(msg) #Game DONE
        elif message.content == 'Butterfly' and dialog == 14: #Star
            msg = "I am Star the Underestimated! I loveee Narwhals and Unicorns and Rainbows!!! I also might have destroyed magic but IT WAS FOR THE BEST".format(message)
            await message.channel.send(msg)
        elif message.content == 'Queen Butterflys':
            msg = "Star the Underestimated, Solaria the Monster Carver, Skywynne the Queen of Hours, Rhina the Riddled, Moon the Undaunted, Meteora, Jushtin the Uncalculated, Estrella the Drafted, Dirhhuennia the Heaped, Crescenta the Eager, Comet the Chef, Celena the Shy, Festivia the Fun, and Eclipsa the Queen of Darkness".format(message)
            await message.channel.send(msg)




    #CURRENT QUEEN SPECIFICS




        elif message.content == 'Summon the Queen of Darkness' and currentqueen == message.author and fanswapnum == 0:
            dialog = 1
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Eclipsa2.jpg"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Eclipsa"
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Eclipsa")
            time.sleep(2)
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing..".format(message)
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1hour
            msg = "I am Eclipsa Butterfly".format(message)
            await message.channel.send(msg)
            #change = 0
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Fun' and currentqueen == message.author and fanswapnum == 0:
            dialog = 2
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Festivia.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Festivia"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Festivia")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Festivia Butterfly!!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Shy' and currentqueen == message.author and fanswapnum == 0:
            dialog = 3
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Celena.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Celena"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Celena")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Celena Butterfly...".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Chef' and currentqueen == message.author and fanswapnum == 0:
            dialog = 4
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Comet.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Comet"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Comet")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Comet Butterfly!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Eager' and currentqueen == message.author and fanswapnum == 0:
            dialog = 5
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Crescenta.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Crescenta"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Crescenta")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Crescenta Butterfly!!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Heaped' and currentqueen == message.author and fanswapnum == 0:
            dialog = 6
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Dirhhuennia.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Dirhhuennia"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Dirhhuennia")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Dirhhuennia Butterfly..".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Drafted' and currentqueen == message.author and fanswapnum == 0:
            dialog = 7
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Estrella.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Estrella"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Estrella")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Estrella Butterfly..".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Uncalculated' and currentqueen == message.author and fanswapnum == 0:
            dialog = 8
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Jushtin.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Jushtin"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Jushtin")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Jushtin Butterfly!!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon Meteora' and currentqueen == message.author and fanswapnum == 0:
            dialog = 9
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Meteora.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Meteora"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Meteora")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "Meteora Butterfly!? Ghaahgoogoo".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Undaunted' and currentqueen == message.author and fanswapnum == 0:
            dialog = 10
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Moon.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Moon"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Moon")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Moon Butterfly!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Riddled' and currentqueen == message.author and fanswapnum == 0:
            dialog = 11
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Rhina.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Rhina"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Rhina")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Rhina Butterfly..?".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Queen of Hours' and currentqueen == message.author and fanswapnum == 0:
            dialog = 12
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Skywynne.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Skywynne"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Skywynne")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Skywynne Butterfly.".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Monster Carver' and currentqueen == message.author and fanswapnum == 0:
            dialog = 13
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Solaria.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Solaria"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Solaria")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Solaria Butterfly! Die ungreatful monsters!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon the Underestimated' and currentqueen == message.author and fanswapnum == 0:
            dialog = 14
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Star.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Star"
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing...".format(message)
            time.sleep(2)
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Star")
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1 hour
            #change = 0
            msg = "I am Star Butterfly!!!".format(message)
            await message.channel.send(msg)
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)


    #NEW BOOK OF SPELLS

        elif message.content == 'Book of Spells':
            msg = "Index: Chapter 1 - Reavina the Whisperer :speaking_head: (X) 0 - 67 ".format(message)
            await message.channel.send(msg)












    #DIAMOND LOG

        elif message.content == 'Diamond Log':
            msg = "Index: Log 1 - Maroon Diamond".format(message)
            await message.channel.send(msg)
        elif message.content == 'Diamond Log 1':
            msg = "Entry: Log Date 0000: To all my dear gems who read this, welcome to your new home of Dimension:0000,Planet:0! Or as the organics call it... Mewni. Allow me to tell you the story of this glorious empires beginning, so that all of the future generations of gem may lead our kingdom to greatness! A long long long time ago. There were three diamonds. White, Yellow, and Blue. Each one playing a crucial role in the great empire known as homeworld! As Homeworld conquered more and more worlds, and made more and more gems. Our technology grew as well. Eventually we discovered something amazing, Different Dimensions! A whole realm of them! stemming from infinite possibilities, and infinite room to grow our empire! Blinded by the possibilities the Diamonds quickly went to world on forming a new Diamond to conquer one of these glorious Dimensions. Me, Maroon Diamond. They sent my Injector through the dimensional portal to go to what we considered to be the easiest one to conquer, Mewini. But as my injector traveled something terrible happened. It seemed as if the strange properties of dimensional travel were breaking down, the portal started to close before they could send in reinforcements, and it seemed as if there was no longer a way to connect to this strange universe. My Injector, confused, and without orders, Quickly Crashed into a mountain side with a shattering boom! Organic life started to die for miles as i was being created. As i emerged the only thing I could find of my origin were the instruction i naturally had, my injector, and the information logs on it. Letting me know how this all happened in the first place. No Matter, I shall continue on with my Homeworld's orders to construct a new army of gems and take over this pitiful world. So, Mewni, Welcome to Gem kind. We do not come in peace.".format(message)
            await message.channel.send(msg)
            msg = "Entry: Log Date 0001: You would not believe how boring it is to construct a colony from a single injector. I have to produce every gem one by one until i finally get a (non-defective) construction force. Did i mention that nearly every gem i make in this gem forsaken ground is defective? My formation took a large chunk of the organic resources from this area, leading to some truly disgusting abominations. One of the Pyropes came out with four arms! Can you believe it? I would be shattering half my court on the spot if it weren't for my current lack of resources. That isn't to say i can't make their lives miserable... I should also mention that we've been detecting some of the sentient organics huddling around the edge of the area that was destroyed of all life. No doubt wondering what caused it... Well, no worries my dear little insignificant annoying terrible... I mean organics. you'll all see the cause soon enough... (Note to future gems, don't inject pyropes into organic drained granite.)".format(message)
            await message.channel.send(msg)


















    #OLD BOOK OF SPELLS






        elif message.content == 'Old Book of Spells':
            msg = "Index: Chapter 1 - Leafan the First :leaves: (X) 0 - 67 ".format(message)
            await message.channel.send(msg)
            msg = "Chapter 2 - Brody the Gifted :two_hearts: (X) 32 - 114".format(message)
            await message.channel.send(msg)
            msg = "Chapter 3 - Green the Diamond :green_heart: (X) 67 - 92".format(message)
            await message.channel.send(msg)
            msg = "Chapter 4 - Brody the Gifted.. Again  :two_hearts: (X) 32 - 114".format(message)
            await message.channel.send(msg)
            msg = "Chapter 5 - Om1nous the Determinaded :dolphin: (X) 91 - 136".format(message)
            await message.channel.send(msg)
            msg = "Chapter 6 - Devon The Dead Rose :rose: (/) 126 - 350".format(message)
            await message.channel.send(msg)
            msg = "Chapter 7 - Breezenia the Free Willed :cloud: 140 - 350".format(message)
            await message.channel.send(msg)
            msg = "Chapter 8 - Fat the Confusing :peach: (/) 150 - 350".format(message)
            await message.channel.send(msg)
            msg = "Chapter 9 -  OhYeah the Mystery Fan :heart_exclamation: (X) 181 - 202".format(message)
            await message.channel.send(msg)
            msg = "Chapter 10 -  Solareo the New :star2: (/) 193 - 350".format(message)
            await message.channel.send(msg)
            msg = "Chapter 11 -  Oli the Funny :joy: (X) 208 - 290".format(message)
            await message.channel.send(msg)
            msg = "Chapter 12 -  Lorde the Volcanic :fire: (?) 240 - 350".format(message)
            await message.channel.send(msg)
            msg = "Chapter 13 -  Dusk the Spirited :skull: (X) 258 - 312".format(message)
            await message.channel.send(msg)
            msg = "Chapter 14 -  Reavina the Whisperer :speaking_head: 282 - ".format(message)
            await message.channel.send(msg)
            msg = "Chapter 15 -  Sabrina the Voided :comet: (?) 318 - 350".format(message)
            await message.channel.send(msg)
            msg = "Chapter 16 -  Breezenia the Free Willed :cloud: 140 - 350".format(message)
            await message.channel.send(msg)
            msg = "Chapter 17 -  Marlowe the King of Edible :chocolate_bar: 330 - 350".format(message)
            await message.channel.send(msg)
            msg = "Chapter 18 -  Breezenia the Free Willed :cloud: 140 - 350".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 1':
            msg = "Chapter 1 - Leafan the First: Entry: Being a Queen is going to be hard. Good thing I have Glossaryk to help me along the way.. Here I will write in the book of spells my chapter, my story, my life. I was born to an Unknown Queen who was hidden from the public and murdered. But not before I was born. I was raised by the Magic High Comission to be a strong 'Queen' figure. I am actually the only boy queen besides one of my super great uncles Jushtin the Uncalculated. My wife is pregnate with a new queen but I can write a few of my spells down..".format(message)
            await message.channel.send(msg)
            msg = "Homework Finisher - A spell to instantly do your homework, Cheese Blast - Blasts only the most exquisit cheese ever!, Balloon Animal Army - Creates a fun army of balloon animals!(they dont work well against sharp monsters.. heh), and Tick Tock Back Stop, Stops time and teleports you back to the time of your wish! My great grandmother-ish Skywynne would be proud!".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 2':
            msg = "Chapter 2 - Brody the Gifted: Entry: uwu".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryk Notes -  Brody was a.. unique queen.. reign was short..? Definitly competeing with Star for shortest queen time!*".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 3':
            msg = "Chapter 3 - Green the Diamond: Entry: Hello Dear Reader I am Green , As you see i am The Curent Owner Of the Magic Book of spells! And you think you will find some Past History About me...Well...You wont , I want to ... Hide some things from my Past  so from now on youl see whats going on in my life xP , Well I was Always Wondering About Writing spells...So Why not try? [Alergy Sprouts] This Spell Can creat Special Plants that activate Anyonese Alergy at any moment , Point your wand At the ground under your Enemy , Then Point it at them then Spin One Time and point at them with your wand again and Say 'Alergy...SPROUTS!!' And then they will be Traped in Plants that Might Activate Or even Give Alergy to them! (I uses it onese On Grey...it was kinda funny...teehee) [Trap Vines] To Use this spell Remember to always be around a Tree Or Grass (i usually Do it around a Tree , But when there is no Tree In my sight then i just use the spell where grass is around) After you found a good spot for this spell , Point your Wand at the place you want to trap to be placed , Then Hold your Wand Up High up your head and Say 'Trap-' Then point at the spot with your wand again and continue with 'Vines!' Then lets say you ware near a Tree , from it Glowing green Vines Well go around your Hand and when they reach the wand , They Will Shot at the Spot you wanted the Trap Creating a Little Circle that cmauflage's , And when its done you wait for some one or someting to step in it and get Traped!".format(message)
            await message.channel.send(msg)
            msg = "Entry: Hello! ... Again So I Was testing out my Vine spell...It Acidently traped One of the Mewmans ... it wasent as funny as i thought it would be... Well atleast i think that was... good... The spell is also Usefull for getting well 'pets' , I also Noticed that Glossyrick isnt as...active in the book...Well While i was Reading thgrought this book...I saw 'Brody The Gifted'...Well....His ... Chapter was... Intresting...I still need to learn more spells! I Asked Glossy if he can Open the Forbiden Chapter for me (he did it after giving him 9 Plates Of Pudding ...) Well ... I also Used one of Skywyenn's Spells ... and... I saw my Tabustry...I wont say it but it involves my ... Mothere and Fathere... cuz they arent my parents . by Name:Green the Diamond".format(message)
            await message.channel.send(msg)
            msg = "Entry: Hello Dear Reader , I will propably create less spells due to some Problems at Mewni , well I do have some spells I wanted to create for a long time , [Crystal Wings] If you havent gone thgrought mewbertty (Like me :P) then this might be usefull for you! Hold your wand with both of your hands and Point it right infront of you then Put it Way up your head then point to your right , then to the left and point your wand up your head then Jump and say 'Crystal-' then when you are at the ground then put your wand infront of you again and say '-Wings!' Then Colorfull Crystal wings will grow out of yur back! (But suprisingly wont break your shirt from the back) [Crystal Jail] This will create a Cage from Powerfull and strong Crystals that hardly anyone can get out of , to cast the spell you simply point your wand up and to your right side then up to your left then point your wand at your enemy and say 'Crystal...Jail!' And they will become traped in the crystal Cage! [Crystal Shield] Point your want up your head , then move it to the ground and 'Draw a Circle Around you , then point it up your head after you are done , and say 'Crystal-' and point it at the ground and say '-Shield!' This is it for now , I dont think i am safe , i hear someone walking down the hall way , i dont know if i might be able to write in here for long , i should Run , Maybe my last entry".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 3 Part 2' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 3 Part 2':
            msg = "Entry: I am Back Dear  Reader , its been some time...alot of time...well this book was Full of dust , i wanted to note that i have a...child...comming soon but i still have some Time to write!".format(message)
            await message.channel.send(msg)
            msg = "Entry: The Ruling is hard , i dont know if i will be able to write that mutch... ".format(message)
            await message.channel.send(msg)
            msg = "Entry:Hello , you might remeber ... the time that i wrote my 'last' entry...well the one that broke in the castle was this Lizard kinda monster , we got him today , he was crystalized , i also found this thing with this 'Toffe' name , i think its a name , it dose sound like it , or some one is just opsesd with Candy ,i also found a pice of paper , but its so hard to read from it i dont understand whats on it , i think this wont be a good idea , but i will write a spell i made , and use it on this Lizard person , the spell is [Crystal Melter] point your wand at a crystalized person and Say 'Crystal-' then point at the part of the Crystalized  body you want to uncrystalize and say '-Melter!' It works...it works I... Talked with Toffe...I dont think He will be fully out,  but after i got what i needed i did the spell in reverse and got back to mewni , i think i will be safe now , at least i Hope.   [Crystal Fear Ilusion] This spell will make an Ilosion that the one that you used this spell on will see othere people as the thing he/she fears ,to use it you need to point your wand to the right , then to the left then up infront of you then spin , and point your wand at the enemy and say 'Crystal Fear Ilusion!'".format(message)
            await message.channel.send(msg)
            msg = "Entry:A war started , an Rebelion Group of Monsters atracked mewni and some othere villages , we are very weakend but i can use my magic to win ... right? Well If things might get to dangerus... ill send the Diamond Cut Guardians...I will be only able to make 4...i am afreaid i might use to mutch magic and...well...fell in (acoma) a Long sleep...well here is the spell for the Guardians [《》Diamond Cut Guardians 《》] Cross your Arms while holding your wand in your right hand , then point the wand with both arms to the right , then the same but to the left , then back away a little , and spin (the number of Guardians you want to summon is the number you want to spin) then point your wand above your head and say 'Diamond!-' then point the wand infront of you and say 'Cut!-' then jump while pointing the wand down and say 'Guardians!' Then you would see the Guardians comming out of the ground at attacking all of your enemys! ".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryk Notes - Now this was a respectable Queen. She was strong.. It was too bad the way she.. died.. She was shot during a war by an arrow..*".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 4':
            msg = "Chapter 4 - Brody the Gifted: Entry: HeE hEe".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryk Notes -  After Green the Diamond's untimely death, Brody the Gifted took back the book. Alas they are as unimpressive as ever.. Hopefully this is the end of their reign..*".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 5':
            msg = "Chapter 5 - Om1nous the Determinaded: Entry: Ok, mom died and my grandmother took the wand and the throne, again, but i guess i can end with this war, one for all, i will be working on this for a bunch of time, i sent some spells that could be useful for who needs to heal or for summon an army, this army can be alive forever, their own weakness is your heart, it is inside of their heads, but remmmeber, if u destroy one they will attack the murder until it dies, and when it dies, they stop until the 2nd command, so it's better you dont kill one of them.".format(message)
            await message.channel.send(msg)
            msg = "Entry: I'M SO EXCITED, THE SPELLS WORKED, but it i more strong than ithinked, the spells name is 'Determination Forever' this spell is the most dengerouse spell ever, accidentally i destroyed the catle of mewni, the Magi High Comition was mad at me, but i saved mewn, for my lucky i used skywynne's spell of the time for build a new mewni, it took a little time and was REALLY boring because the day was going to reapeat, repeat, repeat, and again and again, UUUUGH, also i did a new spell better than solaria's spell of breaking Rhombulus' crystals, i hate Rhombulus, he act like a child! I'm glad that Glossaryck put his hands as snakes".format(message)
            await message.channel.send(msg)
            msg = "Entry: Some random spells: Determination Army and Determination Healing".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 5 Part 2' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 5 Part 2':
            msg = "Entry: Now i will list my new spells:Determinaded Crystal Break: U can break any crystal with it, u need to focus on the crystal and say 'crystal pain' and the crystal dies too; Determinaded Army: U can make a giant army for battle and protection, this army wont attack the user, even if u kill one of them, fpr make this spell u just need to focus on all your determination and for do an ARMY u need to hand the wand and u need to shake it until make how much armys u want; Determinaded Heal: U can heal every single person, but caution, if u do this with someone that died more than 10 minutes before, preper for  be jailed in time FOREVER, fot this spell think on one GOOD thing about the person ur healing, because if u think on BAD things thaat person will die forever; Determinaded Portal: With this spell, simple but useful, u can pass for any dimension u want with out a dimension sisor! For complet this spell u just need to thing on the place u want to go, and then say 'PORTAL ON' poof the protal appers, for close u just need to say 'PORTAL OFF'; Determinaded Armor: U can do an Armor for protect you for any time, but if u use this more than 24H u can have chances to die l u need to do is close your eyes, point the wand anywhere and say 'ARMOR ACTIVATE' and then the armor appers on you".format(message)
            await message.channel.send(msg)
            msg = "Entry: Determination Forever: CAUTION IF U DO ANY WRONG MOVIMENT U WILL LOSE ALL YOUR FEELINGS, with this sell u can use all determination that is used on your army, suck all determination OF THE MULTIVERSE, dont worry their determination will come back when u end this spell, with him u can DESTROY anyone or ANYTHING u want, this spell is to much DENGEROUSE, uccan be like 'u say it is dengerouse but ur lieing' I'M NOT JOKING, JUST FOR CENTIMETRS I DONT DESTROY ALL MEWNI, the spell will continue floating and attacking everything it touch, for end this spell u need to focus on your determination and say 'FINISH ALL!' and then the spell will explode and then anything next there will turn into dust, depending of how much determination u used it can destroy 100% of one dimension ".format(message)
            await message.channel.send(msg)
            msg = "Entry:When i ended with the war usin Determination Forever i used the Determination army for protect the kingdom, i created another spell, its not thaaat thing of 'OMG ITS SAVING ALL OF OUR LIFES' it calls, Determinaded Shield, and if u say, 'ITS ALL WITH DETERMINATION', dude, I'm Ominus the DETERMINADED, dont judge me ;P, welp, for use it u just need to think in protection and say 'shields up' and for cancel 'shields down' done, i was thinking, when my mom dead, and she had a lot of power, maybe she didnt died for an accident, maybe she just, wanted to die? NEVERMIND!".format(message)
            await message.channel.send(msg)
            msg = "Entry: For my last spell from this book, i will make the future vision, this spells will let u see 5 minutes of the future, just 5 minutes ok? u just need to look up point ur wand to the sky and say 'future activate', i tested on Mnafred V, he said he was going to visit the supermarket tomorrow......I guess it worked, i will test by my own now.".format(message)
            await message.channel.send(msg)
            msg = " IT WORKED, MY SPELL IS DONE, and if ur my grand grand grand grand grand grand grand grand daughter, go for the pony head dimension, i will let a gift for you there, and if ur not, dont try to go there for the gift, please, the time need this ok?".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryk Notes -  I don't understand Green's idea to put a number in their name.. Or maybe it was Brody? Oh btw RIP Brody. Died of old age. Some of this magic is pretty strong! dark too though.. Oh I gave her one of my buggy friends!*".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 6':
            msg = "Chapter 6 - Devon The Dead Rose: Entry:Hello , I am Devon Butterfly , Welcome to my Chapter in this great book! I am not as liked in mewni...i bearly have friends..well i do have 4! Logan , Denro , Mark (Yes , thats a real name on mewni...) , Fiare (One of the lucitor family) and Lucy , her brothere is Logan , they are twins , I also Noticed the garden , every time i come there , all roses die , but one time when i was sad and started crying , i noticed that the roses started to coming to life  again! Well i didnt say something yet...My Mom dissapeared after I was born and my dad left , leaving the high commision to taking care of me .. I dont even know how my mom looks , but all of her things are gone or locked , i dont know why , but they are ... Well I realy like Glossy! He is very helpfull and funny ! But...his pet bugs aee kinda...odd..i dont like then that mutch but if glossy likes them , i guess ill have to rely on his decisions.".format(message)
            await message.channel.send(msg)
            msg = "Entry:so i have been reading throught the book and this odd forbidden chapter...it was so odd , i didnt read it tho , I was in the garden again , well this time there was someone there , they ware taking the roses , and some othere flowers , but when they saw me they amidently runed away , i have been noticing them around the candy shop , but they always runned when they saw me , othere mewmans useually talk to me or ignore me or just act like i am some sort of King of the world , i was also talking with Glossy about spells , he is really Into pudding! Just like me! Well i do preffer Vanilla Pudding buut Choclate is good to , Glossy telld me to Make some spells in here so here we go! Heh. 》Warping Spell《Point your wand above your head , and close your eyes and think of where you want to go , Then point your wand under you and say 'Warp!' And then you will be warped! To go back simply point your wand at the ground and say 'Back!' 》Thorn Forcefeild《 Point your wand infront of you , then spin around while slowly rising your wand above your head then when its perfectly above your head stop spining , then point it to the right , to the left and above your head again and say 'Thorn-' then spin once and point your wand infront of you and say '-Forcefeild!' Then throns will creat a forcefeild , that follows you around , it only is spikey on the outside. I think this is a good for now , ill continue later!".format(message)
            await message.channel.send(msg)
            msg = "Entry:I comlpletly forgot about the book! I am so sorry! Its been a year...i feel bad that i left glossy alone for so long...well! This dose mean i will write...but ill work on it later.".format(message)
            await message.channel.send(msg)
            msg = "Entry:I got an gift! I dont know from who , but they have a Crush on me ;3 they send flowers , candy and a letter! Its so sweet! Especialy the candy , well i wont say the whats in the letter buuut you know , romantic stuff :3 , Well i hope that i will meet them some day , well anyway i also got a pet ! Its a little cute Rabbit! I called him Mistter flufs , cuz he is sooo flufy! And likes to be petted , i created a spell that will make any kind of pet happy and energetic! 》Joyfull《Point your wand above your head , then spin onece and point at your pet! And say 'Joyfull!' And then they will start to look happyer ! (If the pet looked sad) and will want to play! Okay but enought whit this childish stuff , i am almost 16 after all! Well my bithday is in 2 months and a weak...but that is still close!".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 6 Part 2' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 6 Part 2':
            msg = "Entry:...I...It was Fiare...I am...so...suprised...i realized how H O T he is!! Omg omg omg!! I am so happy that we are togethere now! He is just so nice! And lovely , Glossy Cobgratulated me! And I think that Glossy is the best from the MHC ! He is almost like a...like a dad? No well maybe more like a very close friend! Glossy has been always so helpfull! Well today there wont be anyspells , just some talking , When i was Wallking around Mewni with Fiare , we tallked and even tried to fly togehtere . Heh. He fell when he tried to fly with me on his back , he is so awsome! Well we also played cards , i won 4 rounds >:3 and he won just 2...Well it was still fun!".format(message)
            await message.channel.send(msg)
            msg = "Entry:Well some Years Past...i am Actually meried to Fiare! We are so happy togethere! Well...Monsters want a war..we are under stress...we dont know what to do yet , well for now we wont do anything...we shall celebrate! I will inform all mewmans of the weddings Party!!".format(message)
            await message.channel.send(msg)
            msg = "Entry:The war will start...But we will fight till we win! We will never give up! All Haill the Era of The Dead Rose!".format(message)
            await message.channel.send(msg)
            msg = "Entry:After the war ... Fiare... he... he didnt make it...he died... ... what will i do..? He was everything to me...".format(message)
            await message.channel.send(msg)
            msg = "Entry:-after 3 Years- I was Meried to This Girl Lunayla , she isnt the best...i dont even love her...she is horible!".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 6 Part 3' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 6 Part 3':
            msg = "Entry:Hi , I will ... do Something fullish...but its for the best》Forced Love《point your wand at your chesy then at your not loved partner , and say'Forced-' and then spin while having your wand above your head , then stop spining and say '-Love!'".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryck Notes - Sadly depressed sadly died. Her powers were none he could hide. Rest in peace Devon.. -- oh?*".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 6 Part 4' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 6 Part 4':
            msg = "Entry: Ⱨł , ł ₳₥ Ʉ₴ł₦₲ ₮ⱧɆ ⱤɆ₴₮ Ø₣ ₥Ɏ ₥₳₲ł₵ ł₦ ₥Ɏ ₴ØɄⱠ ₣ØⱤ₥ ₮Ø ₵Ø₥₥łɄ₦ł₵₳₮Ɇ ₮Ⱨł₴ Ø₦Ɇ Ⱡ₳₴₮ ₮ł₥Ɇ , ₥Ɏ ₵ⱧłⱠĐ , ł₣ ɎØɄ ₳ⱤɆ ⱤɆ₳Đł₦₲ ₮Ⱨł₴ , ł ⱧØ₱Ɇ , ɎØɄⱠⱠ ฿Ɇ ₳ ₲ⱤɆ₳₮ ⱤɄⱠɆⱤ, ฿Ʉ₮ ł ĐØ₦₮ Ⱨ₳VɆ ₥Ʉ₮₵Ⱨ ₮ł₥Ɇ ₳₴ ₮Ⱨł₴ ł₴ VɆⱤɎ Ⱨ₳ⱤĐ ₳₦Đ ł ₩₳₦₮ ₮Ø ₮ɆⱠⱠ ɎØɄ ₮Ⱨ₳₮ ₣ł₳ⱤɆ ł₴₦₮ ĐɆ₳-".format(message)
            await message.channel.send(msg)
            msg = "Entry:ł ₳₥ Ʉ₴ł₦₲ Ø₦Ɇ Ø₣ ₮ⱧɆ ⱤØɎ₳Ⱡ ₴₮₳₣₣ ₮Ø ₩Ɽł₮Ɇ , ł₮ ₥ł₲Ⱨ₮ ฿Ɇ ĐɆ₥Ɇ₦₮ɆĐ ₳₴ ₮Ⱨł₴ ₴ⱧØɄⱠĐ₦₮ ฿Ɇ Ⱨ₳₱₱Ɇ₦ł₦₲ ₳₦Đ ₮ⱧɆ ₥₳₲ł₵ ł₴ ₥₳₭ł₦₲ ł₮ ⱠØØ₭ Ⱡł₭Ɇ ł₮...₳₦Đ ł ₩Ø₦₮ ⱠɆ₮ ₥Ɏ Ⱨł₴₮ØⱤɎ ĐłɆ Ⱡł₭Ɇ ₮Ⱨ₳₮! ł₮ ₩₳₴ ĐɄ₥฿ Ø₣ ₥Ɇ ₮Ø Ɇ₦Đ ł₮! ฿Ʉ₮ ɎØɄ ₭₦Ø₩...ł ₭₦Ø₩ ₴Ø₥Ɇ₮Ⱨł₦₲...ł ₳₥ JɄ₴₮ Ⱡł₭Ɇ ₥Ɏ Đ₳Đ! ł ₩łⱠⱠ ₳Ⱡ₩₳Ɏ₴ ⱠłVɆ Ø₦! ₳₴ ₥Ɏ ĐɆ₮ɆⱤ₥ł₦₳₮łØ₦ ł₴ ₦Ø₦Ɇ Ɇ₦Đł₦₲! ł ₩łⱠⱠ ⱠłVɆ Ø₦ ₩ł₮Ⱨ ₮ⱧɆ ₥₳₲ł₵!".format(message)
            await message.channel.send(msg)
            msg = "Entry:ɆVɆⱤɎ ₮ł₥Ɇ..ɎØɄ ₴ɆɆ ₳ ⱤØ₴Ɇ ł₦ ₥₳₲ł₵ , ł₮₴ ₥Ɇ! ! ł ⱧɆ₳Ɽ ₴Ø₥Ɇ Ø₦Ɇ.. ł ₦ɆɆĐ ₮Ø ₲Ø! ₴ØⱤⱤɎ ₣ØⱤ ₮Ⱨł₴ ฿Ɇł₦₲ ₴ⱧØⱤ₮...฿Ʉ₮... ɆVɆⱤɎ ₴₮ØⱤɎ...Ɇ₦Đ₴...".format(message)
            await message.channel.send(msg)
            msg = "Entry:вυт мιɢнт ɴever coмe вαcĸ".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 7':
            msg = "Chapter 7 - Breezenia the Free Willed Entry: My mother was wayyy too depressed. I do not have time for that! I am breezy peazy floating easyyy".format(message)
            await message.channel.send(msg)
            msg = "Entry: Keeping the citizens at rest is getting to difficult.. I am appointing One-One as my Squire to take care of this junk for me!".format(message)
            await message.channel.send(msg)
            msg = "Entry: Ive been told I need to save my spells in here... So uh here it goess..".format(message)
            await message.channel.send(msg)
            msg = "Entry: Floaty Breeze - Lets you float wherever you wish; WishyWashy - instantly cleans anything...; Swift Breeze - makes you move faster while floating... and yea thats all my spells..".format(message)
            await message.channel.send(msg)
            msg = "Entry: I just found a child on the road.. She is mine now!!! Love is for losers!! Adoption rules ".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryck Notes - It's nice to have a relaxed queen after these crazy past few queens..*".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 8':
            msg = "Chapter 8 - Fat the Confusing Entry: hi i am fat the confusing the opposite of the skinnies".format(message)
            await message.channel.send(msg)
            msg = "Entry: day 2 of being the fattest thiccest queen i got bored asf of being queen so i made a species name skinnies".format(message)
            await message.channel.send(msg)
            msg = "Entry: how come the queen of skinnylandia dont like me like you better respect me i made you guys i am ur jesus".format(message)
            await message.channel.send(msg)
            msg = "Entry: she said she wanna fight me :sob:".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 8 Part 2' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 8 Part 2':
            msg = "Entry:skinnies are so problematic".format(message)
            await message.channel.send(msg)
            msg = "Entry: for future queens do not side with the skinnies they will betray and scam you ".format(message)
            await message.channel.send(msg)
            msg = "Entry:i feel like im not living up to my name all i do is sit and write in this stupid book".format(message)
            await message.channel.send(msg)
            msg = "Entry: ik im like supposed to do this but i have to do alot as the queen you have to do so much so instead of writing in this book imma just put bible verses and be done with it".format(message)
            await message.channel.send(msg)
            msg = "Entry: just found out im adopted yolo swag".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 8 Part 3' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 8 Part 3':
            msg = "Entry: so far the skinnies havent been a problem since i threatened to turn them into pebbles".format(message)
            await message.channel.send(msg)
            msg = "Entry: tbh i think i should turn the queen into another blue blood makeup palette not sponsored by jeffree star".format(message)
            await message.channel.send(msg)
            msg = "Entry: Today the skinnies started some stuff with me i got over it tho *cries epically*".format(message)
            await message.channel.send(msg)
            msg = "Entry: i decided to travel to earth queen stuff was just way to hard".format(message)
            await message.channel.send(msg)
            msg = "Entry: while on earth i played a 'game' called minecraft i met alot of ppl on there i told them about being a queen and stuff they thought it was fake so i wanted to cast a spell on themthe GET IT RIGHT SPELL BGXFHUDSFHADYHHFUEAHDSDF".format(message)
            await message.channel.send(msg)
            msg = "Entry: did i just do something right? holy frigg  i dIDIDIDIDDIDIDID".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 8 Part 4' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 8 Part 4':
            msg = "Entry: while sleeping i saw something staring at me in the window it looked like a giant heart but it crawled up and it was just black i think i should be worried".format(message)
            await message.channel.send(msg)
            msg = "Entry: maybe its one of the Cuprites i created".format(message)
            await message.channel.send(msg)
            msg = "Entry: i was thinking about it and maybe they jumped out of my makeup box and fused? eh its ok as long as it wasnt with the Kyanites..".format(message)
            await message.channel.send(msg)
            msg = "Entry: I saw it again but it opened its eyes this time the where BIG im talking  H O O G E the pupils where purple which is? unexpected idrk i think i should tell somebody about this".format(message)
            await message.channel.send(msg)
            msg = "Entry: While walking my 3560234554824904837548273 dogs i found a green colored human with a gem on its forehead it couldnt be literally it could not be nobody else knows how to make gems besides ME and im sure of that i talked to this thing i asked it about its thing I was being a little bit TO straight forward idk if thats bad or not one of my little toy gems 'Spinel' told me that i was being very straight forward in my entries and just in general tbh it made me mad at first and i just really wanted to crush that toy with my foot i should learn to take constructive criticism".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 8 Part 5' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 8 Part 5':
            msg = "Entry: been a while since i've written a spell".format(message)
            await message.channel.send(msg)
            msg = "Entry: im dumb rlly dumb so i created a spell its called 'whatever the frick it is spell' its like google im only allowed to use it when im TRULY confused i guess that spell will be used alot ".format(message)
            await message.channel.send(msg)
            msg = "Entry: 'heck'".format(message)
            await message.channel.send(msg)
            msg = "Entry: These skinnies really tried it I’ve found out that the head heart shaped stalker that was in my window nights ago was sent by Nora the skintea that’s the skinnies queen I’ve really had it with these skinnies I’m going up there and turning Nora into a tool wish me luck".format(message)
            await message.channel.send(msg)
            msg = "Entry: as I entered I was immediately greeted with a warm welcome the bone kick which could only be kicked by the scamming backstabbing flipping flop flip Nora she’s just mad that nothing sticks out".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 8 Part 6' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 8 Part 6':
            msg = "Entry: I had my kindergarteners stop the production of skinnies ITS OVER FOR YOU now to pick you off one by one".format(message)
            await message.channel.send(msg)
            msg = "Entry: is there a kindergarten I should know of? Cuz today my village was RAIDED I know what the skinnies army looks like it’s definitely not as huge".format(message)
            await message.channel.send(msg)
            msg = "Entry: I decided to allow cross fusion just for now these skinnies wanna cause surprises well here’s one :>".format(message)
            await message.channel.send(msg)
            msg = "Entry: you know that green colored human I talked about a lot of entries ago? Well she’s interested in what I’ve done says she wants to assist me in dealing with these skinnies I’ll see how this goes I guess".format(message)
            await message.channel.send(msg)
            msg = "Entry: is fat really my name".format(message)
            await message.channel.send(msg)
            msg = "Entry: a skinny just told me that being fat is disgusting my thicc gaurd Obsidian turned them into stone".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 8 Part 7' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 8 Part 7':
            msg = "Entry: I just used the whatever the frigg it is spell to look up my families history only to find that im the reason Devon died.".format(message)
            await message.channel.send(msg)
            msg = "Entry: From the tippity top of my castle as i was singing the ultimate thicc song Anaconda i got shooketh the shook shookethed my voice maybe it was an earthquake?".format(message)
            await message.channel.send(msg)
            msg = "Entry: I couldnt speak for days almost a week the doctor says that I may be mute for a while that's not good since i am the queen..queens have to talkwhile i was suffering from muteness my best friend which  i learned her name was 'Star Emerald' accompanied me she really is a best friend apparently she can read lips that's frigging amazing I've been trying to make some new spells that would help me become unmute i guess I DID IT! but did i really? Well i made a spell that helps me see into the future i called it Confuture Vision i haven't tried it out but hopefully it works.. well it definitely does work...While looking into the future i saw some good bad and unexpected things Star Emerald and i grow closer to each other i was way to embarrassed to tell her that.. Good news I  can speak again! but its going to be a long time..Bad news the skinnies attack us again leaving marks that are almost impossible to recover from I've seen that that's going to happen soon..".format(message)
            await message.channel.send(msg)
            msg = "Entry: The shaking that damaged my voice was not an earth quake those where steps! How come I didn't see this with Confuture Vision the steps came from the skinnies they are coming i've equipped my soldiers with Helmets called Brain Confusion its just a helmet with a Brain Confusion spell I made them use these helmets to confuse what ever is coming as dangerous threats like Zombies and stuff".format(message)
            await message.channel.send(msg)
            msg = "Entry: I used the Confuture Vision spell to figure out what was coming of course i had to go through the routine of unexpected good and bad news. Bad news is they are coming in  small versions of the Diamond Mech kinda amazing how they made them work together  but i dont know if its going to be like that. Every species i've created is different well this time that has to change I equipped my soldiers with necklace gems so they will be able to fuse with each other. Does originality really matter when you are preparing for a battle?".format(message)
            await message.channel.send(msg)
            msg = "Entry: I saw that head heart shaped thing again this time it was day if I don’t survive this I’m a failure'".format(message)
            await message.channel.send(msg)
            msg = "Entry: massive fusions lined up along side singular smaller taller gems and me. Panic starts to consume me as I see the first Diamond Mech head pops up. War is outside the castle nobody knows where Fat and Star are hopefully they are ok- ".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 8 Part 8' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 8 Part 8':
            msg = "Entry: I found out! It’s me Fat I have no idea where I am but I just heard a loud boom and found the book covered by a bunch of rubble the skinnies are destroying the castle by room they have just destroyed my room. To stop the from destroying anymore I might have to consider using the Blinding Spell it won’t do any damage but it’ll give us time to attack we have the weapons and the skill hopefully we can do this.'".format(message)
            await message.channel.send(msg)
            msg = "Entry: The Blinding Spell took all of me literally all of me I’m skinny now this isn’t like me. But I can’t lose focus or I’m going to die. If you consider using the Blinding Spell do NOT it will scar you double time by losing weight and gaining an extra pair of eyes it may be cool but PLEASE do not. I’m in a very bad position most of my spells aren’t even offensive. Wish me luck".format(message)
            await message.channel.send(msg)
            msg = "Entry: I dedicate this spell to the skinnies gO TO HELL AND BE A MEMORY BACKSTABBING TRAITORS- used to make enemies fight themselves ".format(message)
            await message.channel.send(msg)
            msg = "Entry: I feel like that’s the only smart move to use against the Diamond Mechs powerful technology against themselves can’t go right for the person using one. I guess they called for back up cause Backstabbing Traitors did work. As soon as Nora came out of the Diamond Mech she called for more help. I heard the loudest boom I ever could’ve heard. A Diamond Mech the size of an actual Diamond Mech.".format(message)
            await message.channel.send(msg)
            msg = "Entry: I was way to tired to use another Backstabbing Traitor spell. So I did something that I knew wouldn’t end it all. I used the Redirect spell to well redirect them. The Diamond Mechs marched towards a Volcano my scouts had told me about. I used another spell once some of them where in the volcano which was almost about to burst meaning break. The volcano was about to break. Anyways I used the Mannequin spell so they couldn’t leave the volcano at all. I couldn’t see myself using those 2 spells again I was already about to fall on my face. Luckily the mechs didn’t survive the volcano and sadly the volcano didn’t survive having 4 Diamond Mechs inside of it.".format(message)
            await message.channel.send(msg)
            msg = "Entry: My best friend Star Emerald saw that I was way to tired to save us all from the lava. She took my wand and used it to create the Shield Of Vines spell. The spell wrapped the kingdom up in vines hoping to save us from the lava. I’m writing this now so of course she did. But Star had to use all of her energy to save the kingdom..".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 8 Part 9' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 8 Part 9':
            msg = "Entry: My best gem Obsidian accompanied me while I was recovering from the loss of Star he also helped rebuild the kingdom and village. To this day I feel like a part of me is missing. I needed somebody to fill in that part very unexpected but Obsidian filled it. I still never understood why the Confuture Vision made me see a future that wasn’t possible today maybe I should add a warning hmm..".format(message)
            await message.channel.send(msg)
            msg = "Entry: oh btw obsidian made me a child out of stone".format(message)
            await message.channel.send(msg)
            msg = "Entry: Fate: Stoned as that was her last dying wish".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryck Notes - Definitly one of my favorite queens. I almost thought this queen was going to be a dud when their mom picked their name... 'fat'*".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 9':
            msg = "*Glossaryck Notes - Her chapters were quickly ripped out by the Magic High Commission to prevent future queens from behaving this way..*".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 10':
            msg = "Chapter 10 - Solareo The New ".format(message)
            await message.channel.send(msg)
            msg = "Entry:Hello Reader...I am Solar , Solar is a shorter version of my name , Solareo so...Eh i dont know,  well my Family Hates me ... so i made a spell , that can make me not their actuall blood line .. so here i go , Blood Line Change Take a Pice of DNa from a familly member of an family you want to be in , then place it infront of you (I grabed a Bone of this person called Devon they are dead) Then point your wabd at your self , then at the DNA pice , then point your wand above your head , and think of a Red Line , being cut and conected to an difrent line , then open your eyes , the DNA pice should be gone  , it means that you changed your DNA! , so i tested it,  and it worked!! Yay! So ... i found this weird part in 'Devon The Dead Rose's' Chapter , its kinda creepy...well i think Ill go rest a bit".format(message)
            await message.channel.send(msg)
            msg = "Entry:Hello Again! Sooo I dont Know What Happend but rn the MHC is taking care of me .. so i guess my dad is gone? Eh i Dont Care!The MHC is so Cool! They are funny and just so great!! And glossy can be so cute and silly ! I just love it now! Its like by that spell i changed every thing!! Oh and talking of spells! I do have some Ideas but ill get Pudding for Glossy!".format(message)
            await message.channel.send(msg)
            msg = "Entry:Okay , there might be some pudding on the pages tho...hm..Oh! I have an Idea! Mess Cleaning Spell Point your wand at the dirty or Messy place or Object and say 'Clean-' then point above your head and say '-Up!' Then the Object/Place should be clean as Ever! Okay so the book is looking niceee , Glossy is also happy that his room in the book got finaly Cleaned up since..it was messy..Solar Armor point your wand at yourself or at the person you want to give the Solar Armor , then point your wand to the right and up , then the same to the left , then above , then spin , and point it at the one you are go a give the armor to and say 'Solar ... Armor!' Then a Galactic or space like transparent Armor would apear suraounding them , Okay so it works the best on yourself , Solar Boost Point your wand above your head , and say 'Solar-' then spin and point infront of you saying '-boost!' Then a Space like Aura would make an Orb like forcefeild around you , and every one thats in it is healthier , stronger and happier".format(message)
            await message.channel.send(msg)
            msg = "Entry:I was Exploring the Castle , and i found the Dungeons , and found bones...one of the skeletons head...it...it had cheak marks...just like The one in the book , Om1nous...why are their bones  here? Shoudlnt they be at the royal Grave place?? I need to talk to the MHC! But before that...ill invastigate...By reading!!".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 10 Part 2' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 10 Part 2':
            msg = "Entry:Okay i have readed Green the Diamonds , Om1nouss and Devons Chapters , and i think i might now...whats going on , so Green Died by an arrow , and Om1n was making healing spells to prevent that of happening , but also created a BIGG dark Magic spell , so they got locked up in the dungeon when Devon was born , and ware not given food at all , cuz the bones are weak , yes i checked ... dont look so weirded out (if you do right now) or disgusted... well still! , okay so i asked the Crystal Guy , i never cant remember his name... if anyone was inprisoned before in the royal family , he dinied but i insisted , then after some time he told me the truth...i am suprised that i was right , they even wanted to aperently lock devon up since they ware thinking that devon would make even stronger and darker Magic ... but he died long before it , later ill talk to the MHC about this".format(message)
            await message.channel.send(msg)
            msg = "Entry:eh , Maybe not Right now...I am MAD tired".format(message)
            await message.channel.send(msg)
            msg = "Entry:I am up! Good Morning Glossy , well i was wondering if i could make a truth spell...for the talk with the MHC , I porpably should , Truth Spell point your wand at the person that you want the truth out off , then say 'Truth-' and then spin and point above your head and say '-Teller!' Then ask them questions and they will always anwser with truth .... I am Back From the talk with MHC .. and this is getting more and more intresting , so aperently DEVON isnt dead...  they said he was crystalized,  as he posesd a mewman , well that...sucks...i wanted to talk them into my idea but they didnt want to liscen as i am to young , so i got angry ... and I acidently... Deeped Down.. when i was done , half of the castle was ... well gone , Glossy manegde to save the book of spells in time , the MHC didnt say anything...i am curently writing at a restrouant , well i think i might use a spell from my great great great great great great (... um i dont know how many greats but lets say its that amount) GREAT Grandmothere Skywynne's chapter , so cya when its done Iguess.".format(message)
            await message.channel.send(msg)
            msg = "Entry:So the Castle is Repaired , i actually made my own spell! Building Spell Point your wand at the place you want to build something , then cross your arms with your wand in your right hand,  then spin , and point your wand to the right and up , then the same for the left  then jump and say 'Building-' then when you are on the ground point your wand above your head and think of how you want your Build to look , when you are done say '-Madness!' Then the building you thinked off should start to slowly apear , the process takes a Month tho.. Sooo ... cya then! ".format(message)
            await message.channel.send(msg)
            msg = "Entry:Okay so after the Month the castle is done , i am 16 and pretty proud , i also got rid of MHC's Power ... in most of things , now i fully control War Things and some othere things , the war is STILL going on...and i think i should fight alone... ---(for now lets say all of this is in Low Mewman)  i wont give this spell a name due to me being highly ... none liking of this spell , to do it you simply point your wand above your head and say 'Chaotic Unleash' then you will feel the darkesd darkness from the deepesd Shadows coming down your hand and you would start to lose your wand , then the wand would do something on its own , then a portal Opens! Then ... sonething ... comes out of it , It looks like a purpleish blackish Monster ghost like smoke , it just attacked the monsters..all of them..ware Inahilated , just Bones , But the spell got on! IT AWKANED THE DIAMOND GUARDIANS! and the fastes battle begined .. the chaos just broke the guardians .. just like its NOTHING... only ... it was gone then , the MHC are shocked and want to not be around me as posible , only Glossy is there for me... well i will take a break from the book , but before that , ill make some spells Black Pheonix Sky Attack point your wand above your head and say 'Black-' then turn around and jump then spin while jumped , point infront of you when on the ground and say '-Pheonix-' then point to the right , then to the left with your wand , then point your wand above your head again and jumo while saying '-Sky-' then when you are at the ground , spin and say '-Attack!' Then watch as the black Pheonixs attack your enemys from the sky! Phew , thats a big one..maybe ill write more later".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 10 Part 3' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 10 Part 3':
            msg = "Entry:Hi! again ... ia m back after...some years , heh Still i have No one to date or love...So i dont think that..the OG blood line will stay...But! I hope ill find someone to love...Well I dont have that mutch time to...well...Talk about this? I am having a meeting with the MHC".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryck Notes - This queen brought the old bloodline back.. Maybe for the best? Rather sad that Rhombus crystalized him".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 11':
            msg = "Chapter 11 - Oli the Funny Entry: Uhmm.. heeey this is Oli the Funny! I'm not really a queen, more of a king cough cough.. but since I'm next one to the throne here I am! ".format(message)
            await message.channel.send(msg)
            msg = "Entry: I want to first start out about how it's so hard to be a queen! I have to do this and this, and I all I want to do is make people laugh!".format(message)
            await message.channel.send(msg)
            msg = "Entry: Glossy isn't much help either.. he's kinda there..".format(message)
            await message.channel.send(msg)
            msg = "Entry: When I was growing up I used to be the class clown and make everyone laugh and smile in my.. sword fighting class.. UGH! Why did she sign me up for that!?".format(message)
            await message.channel.send(msg)
            msg = "Entry: I don't even like fighting with other people! It just makes me feel guilty if I beat them up..".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 11 Part 2' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Book of Spells 11 Part 2':
            msg = "Entry: Hey! It's been some time since I last wrote in this. I kinda left it off in a cliffhanger, just because I'm really tired with celebrating and laughing with my friends I'm just gonna tell you what happened. So recently I was given the role of Queen and married my new husband.. :heart: Yes I know I'm a gay queen, then we partied until we dropped! That's really all..".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryck Notes - Oli was a Fun queen! Probably one of the more relaxed.. It was Nice I must say!*".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 12':
            msg = "Chapter 12 - Lorde the Volcanic Entry: Sooo i heard my grandparent messed up the bloodline kinda selfish tbh you get what you get why would you change that? eh idrc im ROYAL i dont want to worry about family stuff although fat the confusing was a good queen and i hate to not be related to her i might just mess with the bloodline hmm so after thinking about this bloodline stuff i decided to create a spell to change it Blood Line Burn i use it to burn the connection i have with my parents i really wanted to  be related to Fat i mean who wouldnt? Except for Solar e.e".format(message)
            await message.channel.send(msg)
            msg = "Entry: My great grandmom had to deal with a volcano bursting and almost burning down the kingdom. I always wondered why there was a mysterious volcano in the distance being rebuilt. I decided to name that volcano BurgLurgLunger I also made that a spell and another name for what the spell creates. BurgLurgLunger creates a fire dragon to ride on it may be difficult to ride on because it lunges you around sometimes i could never get on it! I've always kinda felt a connection to that volcano and so has BurgLurg".format(message)
            await message.channel.send(msg)
            msg = "Entry: Tbh Oh Yeah is kinda a flop I regret changing the blood line..Maybe if I used  Blood Line Burn again and erase Oh Yeah.. Oh yeah that sounds like a good plan.. I did it and I feel GREAT I can feel the greatness of not being a failures grand child it’s sad how Fat could give birth to something like that ".format(message)
            await message.channel.send(msg)
            msg = "Entry: I had a bit of a problem today I found a Kyanite my grandmother (Fat) had left behind usually Kyanites are small atleast that how my grandmom created them but this Kyanite came out bigger and stronger. You may be wondering how i found this huge problem well i found it through a little mouse hole on the side of my bed. You again may be wondering how this Kyanite came out of the hole well it didnt it broke a wall ;-; thats good tho! it was the perfect time to use a new spell Lava Burst! Its in the name its a burst of lava in the process i may have melted a wall  >-< oh well i'll have the Stoners clean that up. Stoners use to be called Obsidian sometimes my mom can be a little bit dumb cause...Obsidian is purple and black sometimes that...thats a huge hunk of rock. Oh i also made the BurgLurgLunger (the volcano) a punishment along with Brain Melt which melts your brain and can also be used to wipe memories and stuff".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 12 Part 2' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 12 Part 2':
            msg = "Entry: Breeze said I should sign up for anger management classes and i used Volcanic Outburst on them (similar to lava burst but does more damage) that didnt go over to well it left a mark on them and probably a grave idk i didnt really care so xD i also melted a huge part of the castle and thats my bad but idrc".format(message)
            await message.channel.send(msg)
            msg = "Entry: The cleaners builders whatever you call em have had enough of me well if you have had enough of me then leave thats the reason i created the Lava Portal used for travelling dimensions and stuff of course i did let those cleaners or builders off so easily I used the Lava Portal and kicked them into the volcano oh well shouldnt turn on me /shrug Breeze has also had enough of me I tried to fight it literally and conversationally but that didnt work i was sent to the dungeons and for a long time. While i was down there i covered myself in lava to keep myself warm.  I got a little lonely and created a friend named Tuff Puff TP was like a child to me. I learned to use the magma to my advantage to  burst out of the dungeons. I escaped and never looked back.".format(message)
            await message.channel.send(msg)
            msg = "Entry: Tuff Puff was kinda annoying being a child and all so i created another TP to assist me with taking care of small TP I dont know if thats making a family but to me it was.".format(message)
            await message.channel.send(msg)
            msg = "Entry: I created a fire pit with the spell Fire Pit (creates a fire pit can be used without a wand) I burned the book of spells but continued writing on a piece of paper. I decided to go back to the kingdom but without small TP  and TP I wanted that castle gone after what they did to me. So i lit the castle on fire idk what else happened to the castle cuz i never looked back but TP built me a smaller castle to live in. This is my life now 3w3".format(message)
            await message.channel.send(msg)
            msg = "Entry: oh i wanted to tell you more of my spells before i go here are some uwu Fire Fist summons a barrage of fists that are on fire 3w3 Firenado summons a Fire Tornado to protect the user Fire Bird summons a bird made out of fire the bird can also breathe fire owo by Name: Lorde the Volcanic".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryck Notes - Firey in Magic, Firey in Spirit! I wonder what happened to this Queen?*".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 13':
            msg = "Chapter 13 - Dusk the Spirited Entry:Hello There , I am Dusk , I am the Curent Prince- I mean ""Princess"" uhg i hate that they do the gender thing!! Its ao rude! Maybe i want to be prince? Maybe king? MAYBE EVEN BOTH!??? Kueeing would sound great for someone that dosent have a set gender for them, well enought with that , as i was meeting the Blue guy called Glossaryck , i am gona call him Glossy due to the name being pretty annoying to say , in the full form , well i noticed that the castle is very pretty  ...  but ... the Town of mewni...its disgusting...its so ugly , when i become the right age and will have enought power , ill do Something about it! I need to.. i dont want my people to suffer like that...this needs to be fixed".format(message)
            await message.channel.send(msg)
            msg = 'Entry:well i am back again , i dont understand my cheak marks , they are skulls while i dont see anything else to be conected with skulls than ...death  will i die in some sort of horible way??? Or will some one close to me will??? I am afreaid yet curios , well I got my favorite CHOCLATE .. PUDDING!! Ahh those are the best , glossy loves them too! We sheard :D well , he ate more , Okay so i am suposed to write spells here sooo [Sleepy Sheep] - Step 1- Point your wand at your target Step 2 - Point your wand to the right , then to the left then point at the target again and say "Sleepy .. Sheep!" Then your target will fall a sleep in a second! , this spell worked on one of the guards , ha , [Dusk Forceild] Step 1-spin around Step 2-point your wand above your head Step 3- say "Dusk...Forcefeild!" Then you should be in a dusk forcefeild! [Levitaion] Step 1- point your wand above your head Step 2- Spin Step 3-say "Levitation!" Then you will be able to lavitate  , okay so i think ill write 3 spells in every so two entries'.format(message)
            await message.channel.send(msg)
            msg = 'Entry:So , I was actually thinking of my familiy alot latley , I was Gona talk to the MHCs but i dont want to talk with them , i am afreaid,  after i used one of my spells , Dusk Forcefeild , i have been getting shyer and shyer...ill read those chapters..and see what i can find'.format(message)
            await message.channel.send(msg)
            msg = 'Entry:I found out alot , so aperently my grandma- wait can i even call her that...well breezenia , she broke the blood line , BUT Solareo Bringed the Reall Royal Blood Line Back , but then my mom changed it to "Fats" blood...uhg , that name is disgusting,  why not i use , one of ... Bones ... I cant , i have it already in my room , i am gona puke , it stinkssss , it belonged to green , uhg , ill get it over with , time to use a spell thats not mine...'.format(message)
            await message.channel.send(msg)
            msg = 'Entry:It worked , it worked!! And...i think this is new , my cheak marks started glowing , and i blacked out , then i Woke up , i saw ... Breezenia , I talked with her , i asked her so many questions , she even explained that I aperently deeped down and came here , she said that it sometimes takes back to the orgins...she asked me about thr blood line i said i changed it , but , then , i woke up , but i knew it wasent a dream , there was a paper saying "no problemb for bringing you back" ... intresting '.format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 13 Part 2' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 13 Part 2':
            msg = 'Entry:Glossy told me he wanted to take a nap but he couldnt fall a sleep , so he asked me to help him...and i did i used my spell and , its been 3 days , he is STILL sleaping...i am getting anxienty , what if i acidebtly killed him , what if he is in a sleep forever or what if..he is just an lazy Bug again... well ill still think about the spell , [Wakeing Up]- Step 1 Point your wand above your head Step 2 Point your wand at your sleepy target , Step 3 say "Wake Up Sleepy-" then spin and then say "-head!" [Night Vision]- Step 1 Point your wand infront of you Step 2 Point your wand above Your head Step 3 spin around twice Step 4 Say "Night-" Step 5 Jump while pointing Your wand down Step 6 Point your wand at yourself  and say "-Vision!" [Finding Spell]-Step 1 Point your wand above your head Step 2 think of what or who then say "Find!" (They should start to glow)'.format(message)
            await message.channel.send(msg)
            msg = "Entry:I want to write about my old Personal problems but... I feel like they might be a tad bit TO PERSONAL so no.".format(message)
            await message.channel.send(msg)
            msg = "Entry:So i found out that humans made an Rebel group , I dont know why and for what reason , they started to make their own little town and even tried to attack me , But i Used my new spell [Nighting blast]- Step 1 Point your wand above your head Step 2 Point your wand at your traget Step 3 Say 'Nighting-' then spin and say '-Blast!' I've also found out some intresting Dimension's , well also , i will be turning 18 this weak , so i will be almost queen or Kueeing , ha , well I am gona rest for a bit now...".format(message)
            await message.channel.send(msg)
            msg = 'Entry:[Castle Renovate] Point your Wand at your castle , then above your head spin around 5 times then point your wand to the right then to the left and point at your castle again and say "Castle-" then close your eyes and think of how you want the castle to look like then say "-Renovate!'.format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 13 Part 3' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 13 Part 3':
            msg = "Entry:I dont want to be alone...I didnt found anyone to love...I want to be my self , i took a break from the book...I am 20...I dont know what am i suposed to do...I dont love any girl or boy ... I dont love... maybe .. Adoption is the anwser..? ... hm...Maybe Ill do Solar's Spell difrently and make it on the child i Adopt! Ill write more after".format(message)
            await message.channel.send(msg)
            msg = "Entry:I did it , It worked ... the Baby has cheak marks! I am I N LOVE with it! its so nice and so pretty , I hope they will be a great Ruler , for now i dont have mutch time to write i am a Kueening , I think ill do some updates Daily? i still dont know...".format(message)
            await message.channel.send(msg)
            msg = "Entry: Okay so i forgot about the book again , Glossy dosent even reminded me of it when i asked him to... and when i asked him , he said that i look horible and need sleep i am overworking , well i understand him..and maybe he's right...".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryck Notes - He fell into a coma and was assasinated.. Also why is everyone changing bloodlines? I wish someone would stop that hah!*".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryck Notes 2.0 - This queen.. No one can remember them..*".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 14':
            msg = "Chapter 14 - Reavina the Whisperer Entry: All I did was create the 'Whispering Spell of Destruction', don't think to much of it. All it does is makes any spell you want to go away, but somehow you can only use it once. So like, choose wisely or something. That's all. ".format(message)
            await message.channel.send(msg)
            msg = "Entry: People also say I'm creepy. I just like creepy things, okay?".format(message)
            await message.channel.send(msg)
            msg = "Entry: Another spell I created was, 'The Silence Spell', it just makes any person you want to be quiet.".format(message)
            await message.channel.send(msg)
            msg = "Entry: Side Note: Don't go over to Lorde's house. He was the worst grandpa ever.".format(message)
            await message.channel.send(msg)
            msg = "Entry: I also used the Whispering Spell of Destruction on the Bloodline spells or whatever.. It just came to me in a dream or whatever. ".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryck Notes - Im just glad someone put a stop to these bloodline spells!*".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 15':
            msg = "Chapter 15 - Sabrina the Voided Entry: I'd like to tell you about myself :> My name is: Sabrina Butterfly:, I am: 17, Cheek Marks: :comet:, I'm not really friends with anybody i'm just kinda in my mind all day".format(message)
            await message.channel.send(msg)
            msg = "Entry: I created 2 spells they are called 'Void Portal' allows the user to create a portal to the void which is just nothing but space and 'Void Creation' while you are in the void you can create anything you want! People places animals spells to destroy the world and other stuff.".format(message)
            await message.channel.send(msg)
            msg = "Entry: I've been reading about my families history.. we arent even royal.. that sucks".format(message)
            await message.channel.send(msg)
            msg = "Entry: To me its kinda unfair how alot of my great greats didnt get to say anything about the bloodline spells maybe because they didnt make a bloodline spell or just werent- I got an idea ;> I could use Void Creation and summon the butterflies so they could say something about what happened OR I could fix this messed up family by recreating the bloodline spell in the Void by doing that I could use the spell to fix everything maybe make Fat related to breeze and other  stuff I'll see what happens when i use it".format(message)
            await message.channel.send(msg)
            msg = "Entry: I summoned everybody affected by the bloodline spell then I used all their magic to summon the bloodline spell as a person it kinda looked like Globgor i noticed that it was slowly fading away probably because it was destroyed I brought up Breeze and Fat to make them related to each other and i think it worked.. I dont know tho".format(message)
            await message.channel.send(msg)
            msg = "Entry: I kept the Bloodline spell alive in the Void and named it 'Ayuna Bloodline'  I grew to Ayuna and tried to bring her out of the void a few times but every time it would hurt her badly So i became her and ran away from the Kingdom for a while while I was gone i discovered many monster kingdoms and became friends with a lot of them I wasn't lonely anymore I didn't feel like Sabrina anymore probably because I really wasn't I became  Charlotte and I liked it. I revealed to Breeze who i actually was and she accepted me I was allowed to be queen but after a while I didn't like it. So I trapped myself in the Void and created my own life. A life where I wasn't two people. Well Bye!".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryck Notes - Wait wait.. they didn't have a heir? Now they're gone.. They screwed with history bloodlines! I guess Breezenia gets the book back?*".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 16':
            msg = "Chapter 16 - Breezenia the Free Willed Entry: Why would Sabrina not have a kid before running off into the void? Ugh. Now I am queen again! I wish I could be as free willed as I was in my youth but alas I am now Glossaryk 2.0 (no offense Glossaryk) Now that I have the wand back though I can try out some of my more extensive magic.. Do I need to pick another heir? I could stay Queen Forever! Since I am made of magic I'm immortal! Is that a curse or a blessing? Depends. Ive had some pretty crazy grandchildren.. I'm looking over their chapters and some of them are better than others for sure! Lorde the Volcanic was an angry queen. They even attacked me one time! OhYeah was a horrible queen. I played a HUGE part in their chapter being ripped out. These queens were soooo caught up in bloodlines. I am soooo thankful that Reavina destroyed bloodline spells! Im afraid if I use the whispering spell I will destroy myself.. ".format(message)
            await message.channel.send(msg)
            msg = "Entry: Oh my.. I got wayyyyyyy to over excited with my wand heh! I accidently blasted a hole into the side of the Monster Castle... They have declared war on us! After the past few queens our armies are weak because of mismanagement! I really need to find a strong heir and soon! Or maybe.. I am the best choice? For now I am putting Mewni on lockdown. I must be calm and collective. I am reorganizing the Magic High Commission but I am not giving them their power back over war. My late grandson Solareo already took their power for me!".format(message)
            await message.channel.send(msg)
            msg = "Entry: So I think we have made peace with the monsters. Which is very good.. I have opened Mewni back up! The Magic High Commission and I are starting to not get along as well.. Glossaryk and I are having a great time though! Ive started to extend my magic therefore I need to start writing my spells! First up is 'Cloudy Blast' which makes a really big explosion.. May or may not also be what started the magic war.. Next up is 'Floofy Poofy Cloud Cover' which makes you either have a cloud armor or creates a comfy blanket!".format(message)
            await message.channel.send(msg)
            msg = "Entry: I really wish I wasnt queen right now! I got a letter actually.. It says 'From Heckapoo: Someone has replicated the magic high commission and made them like puppets for the rebellion! Currently the real magic high commission is hiding. Im using my last portal powers to send this.. Please hel--' The letter was cut off and kinda burned. Silly Heckapoo not being very careful with her fire! Oh wait.. Wait! That means the Inwem leaders are fake.. Who could lead a rebellion like this AND use magic to make such convincing and powerful puppets?! On a different note I am still looking for the next Queen! But I will not force them to be queen until AFTER this mess is over!".format(message)
            await message.channel.send(msg)
            msg = "*Glossaryck Notes - Im just glad someone put a stop to these bloodline spells!*".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 16 Part 2' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 16 Part 2':
            msg = "Entry: I was doing a scout of the Rebel land and.. the puppeteer is actually the LAST SKINNY. The skinnies that were created by Fat the Confusing were thought to be all killed.. Turns out we missed the last one.. I am currently gathering and army to attack the Rebels of Inwem. The Pony Heads and Spiderbites are joining me in attacking! Oh I hope the Magic High Commission gets found soon...".format(message)
            await message.channel.send(msg)
            msg = "We are actually losing... I need to find some other magic support.. Lets see.. Sabrina is lost in the void and Reavina is in the woods! I'm going to get Reavina to help me. After using the whispering spell she's been weakened but somehow made herself immortal? Oh well I am going to get her to help me raise a magic army similar to Solaria's!".format(message)
            await message.channel.send(msg)
            msg = "Entry: Combined Reavina and I were finally able to remember her daughter's void spell. We are using it soon to get her... I wonder how she will react to being pulled out of the void.. Reavina seems a little hesitant to pull her daughter out of the void. Mother daughter conflicts :rolling_eyes: ! My father was nothing but creepy but I still liked him! My, adopted, daughter was a little strange but we usually got along.. Then again I am kinda go with the flow! Oh an update on the war.. Well we are still losing.. The SpiderBites have pulled out of the war due to lack of resources.. So thats all for now..".format(message)
            await message.channel.send(msg)
            msg = "Entry: So we have successfully brought Sabrina out of the void. But during that long process we lost track of time.. Iwnem forces have forced through our defenses and the pony heads have retreated. The real Magic High Commission still has not been found. Reavina, Sabrina, and I are all attempting to reinforce the castle and bring Mewmans to safety. If we make it through to tonight I will write more...".format(message)
            await message.channel.send(msg)
            msg = "Entry: So we have pushed the rebels out of Mewni.. We aren't exactly winning.. In the process of getting the rebels away from the castle, the castle was destroyed.. My second reign hasn't been just great but I have done my best.. One of my more promising Generals would make a great Queen! Therefore I am passing the wand down to a much more military capable queen. Sabrina and Reavina both returned to their homes/realms and fully support my decision!".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 17':
            msg = "Chapter 17 - Marlowe the King of Edible Entry: I will be the king that is dedicated to the food bots life".format(message)
            await message.channel.send(msg)
            msg = "Entry: the great gods Reavina and Breezenia created Food Bot which is me".format(message)
            await message.channel.send(msg)
            msg = "Entry: I have traveled to dimensions and like everything to steal everything- mostly food to make myself stronger".format(message)
            await message.channel.send(msg)
            msg = "Entry: my plan is to side with the rebels and feed them poisonous food to kill them ".format(message)
            await message.channel.send(msg)
            msg = "Entry: i've created a spell to disguise myself its called 'Transformation Recipe' its a wip but for now it can transform you into a random human you see or think of Sabrina the Voided she was just kinda in my mind it wouldnt be the best choice bc the Mewmans would be wondering why an old queen is the queen again but Breezenia did it so idrk what would happen ".format(message)
            await message.channel.send(msg)
            msg = "**Send 'Book of Spells 17 Part 2' for more**".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 17 Part 2':
            msg = "Entry: I honestly dont care about the magic high comission i'll do my part as the king and whoever i make out of food can handle it i dont care".format(message)
            await message.channel.send(msg)
            msg = "Entry: I made my army out of bread and hamburgers i had food bot help me by Name: Marley".format(message)
            await message.channel.send(msg)
        elif message.content == 'Old Book of Spells 18':
            msg = "Chapter 18 - Breezenia the Free Willed Entry: I have taken the book back from Marley the Edible King.. I needed to put a protection spell on it. Glossaryk will keep this book, and the new book! I don't have much time. Marley turned out to not be a very good general and the forces of evil have taken over. This is my last written entry.. maybe the last of a bloodline? After I use this spell every queen up to Leafan the First will be erased from history and time will be reset. This line of queens has been amazing! I have found a spell called 'speech to text, so I will be narrating the end of times..".format(message)
            await message.channel.send(msg)
            msg = "Entry: I am now beginning a spell I shall not write down... The Queens of Old Days are appearing! Now the more recent queens.. Leafan, Brody, Om1nous, Devon (Father!!), Fat, OhYeah (gross), Solareo, Oli, Lorde, Dusk, Reavina, Sabrina, and Marley. Seems that this spell has dragged living queens, crystalized queens, and partially dead queens out of their places to here.. The spell is working! I am finally reaching my full potential of being made of magic.. Wings? 4 arms now.. Oh I feel a draining sensation.. Since I am magic I will disappear soon.. This is my final entry: Thank you for everything! May Mewni Live Forever!".format(message)
            await message.channel.send(msg)








    #SOLARIA GAME










        elif message.content == 'Butterfly Game' and dialog == 13:
            msg = "I am Solaria! Pick Between 'Monster Battle' or 'MMQ'".format(message)
            await message.channel.send(msg)
            game2 = 2
        elif message.content == 'Monster Battle' and dialog == 13 and game2 == 2:
            msg = "A Battle has broken out between monsters and Mewmans! Send 'Go' to start!".format(message)
            await message.channel.send(msg)
            game2 = 1
        elif message.content == 'MMQ' and dialog == 13 and game2 == 2:
            msg = "A great war has been waged! A neighboring kingdom has challeged you to a game of Monsters, Mewmans, Queens! Dont forget Queens beat Monsters, Monsters Beat Mewmans, and Mewmans beat Queens! Choose one to continue!".format(message)
            await message.channel.send(msg)
            game2 = 3
        elif message.content == 'Queens' and dialog == 13 and game2 == 3:
            game = random.randint(1,3) # Queens = 1, Monsters = 2, Mewmans = 3
            game3 = 1
            #if game == 1:
            #    game4 = "Queens"
            #if game == 2:
            #    game4 = "Monsters"
            #if game == 3:
            #    game4 = "Mewmans"
            if game == game3:
                msg = "Well. This is strange.. A tie! Your pick: Queens; Enemy's pick: Queens".format(message)
                await message.channel.send(msg)
            elif game == 2:
                msg = "BAHAHA You won! Show them your power hahaha!! Your pick: Queens; Enemy's pick: Monsters".format(message)
                await message.channel.send(msg)
            elif game == 3:
                msg = "You. Lost. For shame upon you. Your pick: Queens; Enemy's pick: Mewmans".format(message)
                await message.channel.send(msg)
            game2 = 0
        elif message.content == 'Monsters' and dialog == 13 and game2 == 3:
            game = random.randint(1,3) # Queens = 1, Monsters = 2, Mewmans = 3
            game3 = 2
            #if game == 1:
            #    game4 = "Queens"
            #if game == 2:
            #    game4 = "Monsters"
            #if game == 3:
            #    game4 = "Mewmans"
            if game == game3:
                msg = "Well. This is strange.. A tie! Your pick: Monsters; Enemy's pick: Monsters".format(message)
                await message.channel.send(msg)
            elif game == 1:
                msg = "BAHAHA You won! Show them your power hahaha!! Your pick: Monsters; Enemy's pick: Mewmans".format(message)
                await message.channel.send(msg)
            elif game == 3:
                msg = "You. Lost. For shame upon you. Your pick: Monsters; Enemy's pick: Queens".format(message)
                await message.channel.send(msg)
            game2 = 0
        elif message.content == 'Mewmans' and dialog == 13 and game2 == 3:
            game = random.randint(1,3) # Queens = 1, Monsters = 2, Mewmans = 3
            game3 = 3
            #if game == 1:
            #    game4 = "Queens"
            #if game == 2:
            #    game4 = "Monsters"
            #if game == 3:
            #    game4 = "Mewmans"
            if game == game3:
                msg = "Well. This is strange.. A tie! Your pick: Mewmans; Enemy's pick: Mewmans".format(message)
                await message.channel.send(msg)
            elif game == 1:
                msg = "BAHAHA You won! Show them your power hahaha!! Your pick: Mewmans; Enemy's pick: Queens".format(message)
                await message.channel.send(msg)
            elif game == 2:
                msg = "You. Lost. For shame upon you. Your pick: Mewmans; Enemy's pick: Monsters".format(message)
                await message.channel.send(msg)
            game2 = 0
        elif message.content == 'Go' and dialog == 13 and game2 == 1:
            game = random.randint(1,4)
            game3 = random.randint(1,4)
            if game > game3:
                msg = "Hmph! The monsters have won this time. Your pick {}; Monster pick {}".format(game3, game, message)
                await message.channel.send(msg)
            elif game < game3:
                msg = "HAH! IN YOUR FACE MONSTER SCUM!! Your pick {}; Monster pick {}".format(game3, game, message)
                await message.channel.send(msg)
            elif game == game3:
                msg = "A tie..? This is unusual.. Your pick {}; Monster pick {}".format(game3, game, message)
                await message.channel.send(msg)
            game2 = 0










    #FESTIVIA GAME





        elif message.content == 'Butterfly Game' and dialog == 2:
            msg = 'I am Festivia Butterfly!! Want to play Party Planner? Send "Start" to begin'.format(message)
            await message.channel.send(msg)
            game2 = 2
            game3 = random.randint(1000,10000)
            turns = 0
            game = 0
            game4 = 0
            game5 = 0
        elif message.content == 'Start' and dialog == 2 and game2 == 2:
            msg = 'You have to plan a party! You have {} money! You have 5 turns to make a great party! Send "Go" !'.format(game3,message)
            await message.channel.send(msg)
            turns = 1
        elif message.content == 'Go' and dialog == 2 and game2 == 2 and turns == 1:
            msg = 'You have {}$ What will you do? Start a Fundraiser? Buy Party Supplies? Send Invites?'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Fundraiser", "Party", or "Invites" to choose your option!'
            await message.channel.send(msg)
        elif message.content == 'Fundraiser' and dialog == 2 and game2 == 2 and turns == 1:
            game = random.randint(100,2000)
            msg = 'You started a Fundraiser! You made {}'.format(game,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to continue!'
            await message.channel.send(msg)
            turns = 2
        elif message.content == 'Party' and dialog == 2 and game2 == 2 and turns == 1:
            msg = 'You are going Shopping! You have {}!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Do you buy: "Diamonds" $6000 for decoration, "Confetti" $500, "Live Animals" $5000, "Live Preformance" $2500 ,or "Snacks" $1000'
            await message.channel.send(msg)
            game4 = 1
        elif message.content == 'Diamonds' and dialog == 2 and game2 == 2 and turns == 1 and game4 == 1 and game3 <= 6000:
            msg = 'You Bought Diamonds!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 2
            game4 = 0
            game5 += 5
            game3 -= 6000
        elif message.content == 'Confetti' and dialog == 2 and game2 == 2 and turns == 1 and game4 == 1 and game3 <= 500:
            msg = 'You Bought Confetti!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 2
            game4 = 0
            game5 += 1
            game3 -= 500
        elif message.content == 'Live Animals' and dialog == 2 and game2 == 2 and turns == 1 and game4 == 1 and game3 <= 5000:
            msg = 'You Rented a Live Animal Show'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 2
            game4 = 0
            game5 += 4
            game3 -= 5000
        elif message.content == 'Live Preformance' and dialog == 2 and game2 == 2 and turns == 1 and game4 == 1 and game3 <= 2500:
            msg = 'You Rented a Live Preformance'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 2
            game4 = 0
            game5 += 3
            game3 -= 2500
        elif message.content == 'Snacks' and dialog == 2 and game2 == 2 and turns == 1 and game4 == 1 and game3 <= 1000:
            msg = 'You Bought Snacks!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 2
            game4 = 0
            game5 += 2
            game3 -= 1000
        elif message.content == 'Invites' and dialog == 2 and game2 == 2 and turns == 1:
            msg = 'You sent invites!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 2
            game5 += 4

        elif message.content == 'Next' and dialog == 2 and game2 == 2 and turns == 2:
            msg = 'You have {}$ What will you do? Start a Fundraiser? Buy Party Supplies? Send Invites?'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Fundraiser", "Party", or "Invites" to choose your option!'
            await message.channel.send(msg)

        elif message.content == 'Fundraiser' and dialog == 2 and game2 == 2 and turns == 2:
            game = random.randint(100,2000)
            msg = 'You started a Fundraiser! You made {}'.format(game,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to continue!'
            await message.channel.send(msg)
            turns = 3
        elif message.content == 'Party' and dialog == 2 and game2 == 2 and turns == 2:
            msg = 'You are going Shopping! You have {}!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Do you buy: "Diamonds" $6000 for decoration, "Confetti" $500, "Live Animals" $5000, "Live Preformance" $2500 ,or "Snacks" $1000'
            await message.channel.send(msg)
            game4 = 1
        elif message.content == 'Diamonds' and dialog == 2 and game2 == 2 and turns == 2 and game4 == 1 and game3 <= 6000:
            msg = 'You Bought Diamonds!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 3
            game4 = 0
            game5 += 5
            game3 -= 6000
        elif message.content == 'Confetti' and dialog == 2 and game2 == 2 and turns == 2 and game4 == 1 and game3 <= 500:
            msg = 'You Bought Confetti!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 3
            game4 = 0
            game5 += 1
            game3 -= 500
        elif message.content == 'Live Animals' and dialog == 2 and game2 == 2 and turns == 2 and game4 == 1 and game3 <= 5000:
            msg = 'You Rented a Live Animal Show'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 3
            game4 = 0
            game5 += 4
            game3 -= 5000
        elif message.content == 'Live Preformance' and dialog == 2 and game2 == 2 and turns == 2 and game4 == 1 and game3 <= 2500:
            msg = 'You Rented a Live Preformance'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 3
            game4 = 0
            game5 += 3
            game3 -= 2500
        elif message.content == 'Snacks' and dialog == 2 and game2 == 2 and turns == 2 and game4 == 1 and game3 <= 1000:
            msg = 'You Bought Snacks!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 3
            game4 = 0
            game5 += 2
            game3 -= 1000
        elif message.content == 'Invites' and dialog == 2 and game2 == 2 and turns == 2:
            msg = 'You sent invites!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 3
            game4 = 0
            game5 += 4

        elif message.content == 'Next' and dialog == 2 and game2 == 2 and turns == 3:
            msg = 'You have {}$ What will you do? Start a Fundraiser? Buy Party Supplies? Send Invites?'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Fundraiser", "Party", or "Invites" to choose your option!'
            await message.channel.send(msg)

        elif message.content == 'Fundraiser' and dialog == 2 and game2 == 2 and turns == 3:
            game = random.randint(100,2000)
            msg = 'You started a Fundraiser! You made {}'.format(game,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to continue!'
            await message.channel.send(msg)
            turns = 4
        elif message.content == 'Party' and dialog == 2 and game2 == 2 and turns == 3:
            msg = 'You are going Shopping! You have {}!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Do you buy: "Diamonds" $6000 for decoration, "Confetti" $500, "Live Animals" $5000, "Live Preformance" $2500 ,or "Snacks" $1000'
            await message.channel.send(msg)
            game4 = 1
        elif message.content == 'Diamonds' and dialog == 2 and game2 == 2 and turns == 3 and game4 == 1 and game3 <= 6000:
            msg = 'You Bought Diamonds!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 4
            game4 = 0
            game5 += 5
            game3 -= 6000
        elif message.content == 'Confetti' and dialog == 2 and game2 == 2 and turns == 3 and game4 == 1 and game3 <= 500:
            msg = 'You Bought Confetti!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 4
            game4 = 0
            game5 += 1
            game3 -= 500
        elif message.content == 'Live Animals' and dialog == 2 and game2 == 2 and turns == 3 and game4 == 1 and game3 <= 5000:
            msg = 'You Rented a Live Animal Show'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 4
            game4 = 0
            game5 += 4
            game3 -= 5000
        elif message.content == 'Live Preformance' and dialog == 2 and game2 == 2 and turns == 3 and game4 == 1 and game3 <= 2500:
            msg = 'You Rented a Live Preformance'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 4
            game4 = 0
            game5 += 3
            game3 -= 2500
        elif message.content == 'Snacks' and dialog == 2 and game2 == 2 and turns == 3 and game4 == 1 and game3 <= 1000:
            msg = 'You Bought Snacks!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 4
            game4 = 0
            game5 += 2
            game3 -= 1000
        elif message.content == 'Invites' and dialog == 2 and game2 == 2 and turns == 3:
            msg = 'You sent invites!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 4
            game4 = 0
            game5 += 4

        elif message.content == 'Next' and dialog == 2 and game2 == 2 and turns == 4:
            msg = 'You have {}$ What will you do? Start a Fundraiser? Buy Party Supplies? Send Invites?'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Fundraiser", "Party", or "Invites" to choose your option!'
            await message.channel.send(msg)

        elif message.content == 'Fundraiser' and dialog == 2 and game2 == 2 and turns == 4:
            game = random.randint(100,2000)
            msg = 'You started a Fundraiser! You made {}'.format(game,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to continue!'
            await message.channel.send(msg)
            turns = 5
        elif message.content == 'Party' and dialog == 2 and game2 == 2 and turns == 4:
            msg = 'You are going Shopping! You have {}!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Do you buy: "Diamonds" $6000 for decoration, "Confetti" $500, "Live Animals" $5000, "Live Preformance" $2500 ,or "Snacks" $1000'
            await message.channel.send(msg)
            game4 = 1
        elif message.content == 'Diamonds' and dialog == 2 and game2 == 2 and turns == 4 and game4 == 1 and game3 <= 6000:
            msg = 'You Bought Diamonds!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 5
            game4 = 0
            game5 += 5
            game3 -= 6000
        elif message.content == 'Confetti' and dialog == 2 and game2 == 2 and turns == 4 and game4 == 1 and game3 <= 500:
            msg = 'You Bought Confetti!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 5
            game4 = 0
            game5 += 1
            game3 -= 500
        elif message.content == 'Live Animals' and dialog == 2 and game2 == 2 and turns == 4 and game4 == 1 and game3 <= 5000:
            msg = 'You Rented a Live Animal Show'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 5
            game4 = 0
            game5 += 4
            game3 -= 5000
        elif message.content == 'Live Preformance' and dialog == 2 and game2 == 2 and turns == 4 and game4 == 1 and game3 <= 2500:
            msg = 'You Rented a Live Preformance'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 5
            game4 = 0
            game5 += 3
            game3 -= 2500
        elif message.content == 'Snacks' and dialog == 2 and game2 == 2 and turns == 4 and game4 == 1 and game3 <= 1000:
            msg = 'You Bought Snacks!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 5
            game4 = 0
            game5 += 2
            game3 -= 1000
        elif message.content == 'Invites' and dialog == 2 and game2 == 2 and turns == 4:
            msg = 'You sent invites!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 5
            game4 = 0
            game5 += 4

        elif message.content == 'Next' and dialog == 2 and game2 == 2 and turns == 5:
            msg = 'You have {}$ What will you do? Start a Fundraiser? Buy Party Supplies? Send Invites?'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Fundraiser", "Party", or "Invites" to choose your option!'
            await message.channel.send(msg)

        elif message.content == 'Fundraiser' and dialog == 2 and game2 == 2 and turns == 5:
            game = random.randint(100,2000)
            msg = 'You started a Fundraiser! You made {}'.format(game,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to continue!'
            await message.channel.send(msg)
            turns = 6
        elif message.content == 'Party' and dialog == 2 and game2 == 2 and turns == 5:
            msg = 'You are going Shopping! You have {}!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Do you buy: "Diamonds" $6000 for decoration, "Confetti" $500, "Live Animals" $5000, "Live Preformance" $2500 ,or "Snacks" $1000'
            await message.channel.send(msg)
            game4 = 1
        elif message.content == 'Diamonds' and dialog == 2 and game2 == 2 and turns == 5 and game4 == 1 and game3 <= 6000:
            msg = 'You Bought Diamonds!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 6
            game4 = 0
            game5 += 5
            game3 -= 6000
        elif message.content == 'Confetti' and dialog == 2 and game2 == 2 and turns == 5 and game4 == 1 and game3 <= 500:
            msg = 'You Bought Confetti!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 6
            game4 = 0
            game5 += 1
            game3 -= 500
        elif message.content == 'Live Animals' and dialog == 2 and game2 == 2 and turns == 5 and game4 == 1 and game3 <= 5000:
            msg = 'You Rented a Live Animal Show'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 6
            game4 = 0
            game5 += 4
            game3 -= 5000
        elif message.content == 'Live Preformance' and dialog == 2 and game2 == 2 and turns == 5 and game4 == 1 and game3 <= 2500:
            msg = 'You Rented a Live Preformance'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 6
            game4 = 0
            game5 += 3
            game3 -= 2500
        elif message.content == 'Snacks' and dialog == 2 and game2 == 2 and turns == 5 and game4 == 1 and game3 <= 1000:
            msg = 'You Bought Snacks!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 6
            game4 = 0
            game5 += 2
            game3 -= 1000
        elif message.content == 'Invites' and dialog == 2 and game2 == 2 and turns == 5:
            msg = 'You sent invites!'.format(game3,message)
            await message.channel.send(msg)
            msg = 'Send "Next" to Continue'
            await message.channel.send(msg)
            turns = 6
            game4 = 0
            game5 += 4

        elif message.content == 'Next' and dialog == 2 and game2 == 2 and turns == 6 and game5 <=10:
            msg = 'You ended with {} dollars!'.format(game3,message)
            await message.channel.send(msg)
            game6 = random.randint(1,10)
            msg = 'You had {} people show up!'.format(game6,message)
            await message.channel.send(msg)
            turns = 0
            game = 0
            game4 = 0
            game5 = 0
            game2 = 0
            game6 = 0
            game3 = 0
        elif message.content == 'Next' and dialog == 2 and game2 == 2 and turns == 6 and game5 >10 and game5 <=15:
            msg = 'You ended with {} dollars!'.format(game3,message)
            await message.channel.send(msg)
            game6 = random.randint(15,50)
            msg = 'You had {} people show up!'.format(game6,message)
            await message.channel.send(msg)
            turns = 0
            game = 0
            game4 = 0
            game5 = 0
            game2 = 0
            game6 = 0
            game3 = 0
        elif message.content == 'Next' and dialog == 2 and game2 == 2 and turns == 6 and game5 >15:
            msg = 'You ended with {} dollars!'.format(game3,message)
            await message.channel.send(msg)
            game6 = random.randint(60, 200)
            msg = 'You had {} people show up!'.format(game6,message)
            await message.channel.send(msg)
            turns = 0
            game = 0
            game4 = 0
            game5 = 0
            game2 = 0
            game6 = 0
            game3 = 0




    #MOON GAME 












        elif message.content == 'Butterfly Game' and dialog == 10:
            msg = 'I am Moon Butterfly! Want to play Run a Kingdom? Send "Start" to begin'.format(message)
            await message.channel.send(msg)
            game2 = 2
            game = 0
            game3 = 0
            game4 = random.randint(1, 5)
        elif message.content == 'Start' and dialog == 10 and game2 == 2:
            msg = 'Make the right choices and build your kingdom! Try not to get the points too high (20) or too low (0) in 10 Turns'.format(message)
            await message.channel.send(msg)
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            if game4 == 1 and turns == 0:
                msg = 'The monsters want more land for farming. Really Badly. But it would require you to give some of your land! Will you give them some? Yes/No'.format(message)
                await message.channel.send(msg)
                game3 = 1
            elif game4 == 2 and turns == 0:
                msg = 'The Mewmans demand that you create a wall between the Monsters and Mewmans! Will you create a Wall? Yes/No'.format(message)
                await message.channel.send(msg)
                game3 = 2
            elif game4 == 3 and turns == 0:
                msg = 'The Magic High Commission wants you to be more strict and control the Mewmans and Monsters with an Iron Fist. Will you be more strict? Yes/No'.format(message)
                await message.channel.send(msg)
                game3 = 3
            elif game4 == 4 and turns == 0:
                msg = 'You have an Opportunity to throw a Ball! Invite everyone or just Mewmans and the Magic High Commission. The MHC and Mewmans do not want the monsters to come! Will you invite the Monsters? Yes/No'.format(message)
                await message.channel.send(msg)
                game3 = 4
            elif game4 == 5 and turns == 0:
                msg = 'There is a famine. All the corn crops have died! Everyone is starving. Will you share your corn? Yes/No'.format(message)
                await message.channel.send(msg)
                game3 = 5
        
        elif message.content == 'Yes' and game4 == 1 and turns == 0 and game3 == 1:
            game = 15
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            turns = 1
        elif message.content == 'No' and game4 == 1 and turns == 0 and game3 == 1:
            game = 16
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            turns = 1
        elif message.content == 'Yes' and game4 == 2 and turns == 0 and game3 == 2:
            game = 16
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            turns = 1
        elif message.content == 'No' and game4 == 2 and turns == 0 and game3 == 2:
            game = 15
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            turns = 1
        elif message.content == 'Yes' and game4 == 3 and turns == 0 and game3 == 3:
            game = 17
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            turns = 1
        elif message.content == 'No' and game4 == 3 and turns == 0 and game3 == 3:
            game = 18
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            turns = 1
        elif message.content == 'Yes' and game4 == 4 and turns == 0 and game3 == 4:
            game = 15
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            turns = 1
        elif message.content == 'No' and game4 == 4 and turns == 0 and game3 == 4:
            game = 16
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            turns = 1
        elif message.content == 'Yes' and game4 == 5 and turns == 0 and game3 == 5:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            turns = 1
        elif message.content == 'No' and game4 == 5 and turns == 0 and game3 == 5:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            turns = 1

        elif message.content == 'Next' and game4 == 1 and turns == 1:
            msg = 'The Mewmans are complaining that the Magic High Commission has too much Power! They ask you to weaken the Commission. Will you weaken the Commission? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 1
            turns = 2
        elif message.content == 'Next' and game4 == 2 and turns == 1:
            msg = 'You hear of a Monster invasion by a random Mewman. Will you fight back on impulse? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 2
            turns = 2
        elif message.content == 'Next' and game4 == 3 and turns == 1:
            msg = 'While roaming around your kingdom you see extreme poverty. Will you innitiate efforts to help your people? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 3
            turns = 2
        elif message.content == 'Next' and game4 == 4 and turns == 1:
            msg = 'The Magic High Commission and your mother have requested you write in the magic spell book more. Keeping a more detailed description of your reign! Will you write more? Yes/No '.format(message)
            await message.channel.send(msg)
            game3 = 4
            turns = 2
        elif message.content == 'Next' and game4 == 5 and turns == 1:
            msg = 'The Magic High Commission is trying to take more power from the Queen. Will you stop them? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 5
            turns = 2
        
        elif message.content == 'Yes' and game4 == 1 and turns == 2 and game3 == 1:
            game = 18
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 1 and turns == 2 and game3 == 1:
            game = 1
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 2 and turns == 2 and game3 == 2:
            game = 2
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 2 and turns == 2 and game3 == 2:
            game = 7
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 3 and turns == 2 and game3 == 3:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 3 and turns == 2 and game3 == 3:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 4 and turns == 2 and game3 == 4:
            game = 10
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 4 and turns == 2 and game3 == 4:
            game = 3
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 5 and turns == 2 and game3 == 5:
            game = 18
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 5 and turns == 2 and game3 == 5:
            game = 17
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Next' and game4 == 1 and turns == 2:
            msg = 'While checking on the Corn Fields you are attacked by rouge monsters. Will you invade monster land after this attempted assassination? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 1
            turns = 3
        elif message.content == 'Next' and game4 == 2 and turns == 2:
            msg = 'The Magic High Commission and your Mother want you make more spells! It might help the future of Mewni or it might Destory it. Will you make more spells? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 2
            turns = 3
        elif message.content == 'Next' and game4 == 3 and turns == 2:
            msg = 'The Magic High Commission and your Mother want you to pick a spouse! Will you agree to pick a spouse? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 3
            turns = 3
        elif message.content == 'Next' and game4 == 4 and turns == 2:
            msg = 'The Magic High Commission wants you to raise the taxes on all food. And start taxing monsters. Will you impose these new taxes? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 4
            turns = 3
        elif message.content == 'Next' and game4 == 5 and turns == 2:
            msg = 'The monsters request that you make peace with them for now. The Magic High Commission does not approve. Will you negotiate with the monsters? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 5
            turns = 3
        
        elif message.content == 'Yes' and game4 == 1 and turns == 3 and game3 == 1:
            game = 2
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 1 and turns == 3 and game3 == 1:
            game = 7
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 2 and turns == 3 and game3 == 2:
            game = 10
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 2 and turns == 3 and game3 == 2:
            game = 3
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 3 and turns == 3 and game3 == 3:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 3 and turns == 3 and game3 == 3:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 4 and turns == 3 and game3 == 4:
            game = 17
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 4 and turns == 3 and game3 == 4:
            game = 3
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 5 and turns == 3 and game3 == 5:
            game = 7
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 5 and turns == 3 and game3 == 5:
            game = 2
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Next' and game4 == 1 and turns == 3:
            msg = 'Surprise! It is your Birthday! Will you throw an Extravangant party for Royals at the expense of Mewmans or a Fun party with your people? Yes for Royal Party. No for Fun Party. Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 1
            turns = 4
        elif message.content == 'Next' and game4 == 2 and turns == 3:
            msg = 'You have been advised by the Magic High Comission to hire a royal food tester! The Monsters and Mewmans will be hurt at the amount of trust you show them! Will you hire a food tester? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 2
            turns = 4
        elif message.content == 'Next' and game4 == 3 and turns == 3:
            msg = 'Blood Moon Ball time! Will you invite the royal monster family? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 3
            turns = 4
        elif message.content == 'Next' and game4 == 4 and turns == 3:
            msg = 'The Mewmans want you to give them food for no cost. It would make them lazy. Will you give them food? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 4
            turns = 4
        elif message.content == 'Next' and game4 == 5 and turns == 3:
            msg = 'While buying corn you stumble apon a baby monster. It turns out to be a royal monster. Will you murder it? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 5
            turns = 4
        
        elif message.content == 'Yes' and game4 == 1 and turns == 4 and game3 == 1:
            game = 17
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 1 and turns == 4 and game3 == 1:
            game = 18
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 2 and turns == 4 and game3 == 2:
            game = 17
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 2 and turns == 4 and game3 == 2:
            game = 18
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 3 and turns == 4 and game3 == 3:
            game = 7
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 3 and turns == 4 and game3 == 3:
            game = 2
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 4 and turns == 4 and game3 == 4:
            game = 1
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 4 and turns == 4 and game3 == 4:
            game = 8
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 5 and turns == 4 and game3 == 5:
            game = 2
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 5 and turns == 4 and game3 == 5:
            game = 7
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Next' and game4 == 1 and turns == 4:
            msg = 'You are sitting around waiting on something to happen when a letter falls from the sky saying mewmans are revolting. This letter may not be true. Will you fight them? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 1
            turns = 5
        elif message.content == 'Next' and game4 == 2 and turns == 4:
            msg = 'Your mother is trying to make you eat more exoctic foods. It may make you sick and not able to do anything. Will you eat this food? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 2
            turns = 5
        elif message.content == 'Next' and game4 == 3 and turns == 4:
            msg = 'Suddenly you have an urge to be a ruthless dictator. Will you become a dictator? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 3
            turns = 5
        elif message.content == 'Next' and game4 == 4 and turns == 4:
            msg = 'Monsters are coming to the caslte. Will you greet them? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 4
            turns = 5
        elif message.content == 'Next' and game4 == 5 and turns == 4:
            msg = 'While bathing you see a mewman taking photos through your window. Will you blast him out? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 5
            turns = 5
        
        elif message.content == 'Yes' and game4 == 1 and turns == 5 and game3 == 1:
            game = 1
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 1 and turns == 5 and game3 == 1:
            game = 8
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 2 and turns == 5 and game3 == 2:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 2 and turns == 5 and game3 == 2:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 3 and turns == 5 and game3 == 3:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 3 and turns == 5 and game3 == 3:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 4 and turns == 5 and game3 == 4:
            game = 7
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 4 and turns == 5 and game3 == 4:
            game = 2
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 5 and turns == 5 and game3 == 5:
            game = 1
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 5 and turns == 5 and game3 == 5:
            game = 18
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Next' and game4 == 1 and turns == 5:
            msg = 'Heckapoo things the Queen should have to pass a dimensional scissors test. This means you would have to give up your dimensional scissors. Will you give them up? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 1
            turns = 6
        elif message.content == 'Next' and game4 == 2 and turns == 5:
            msg = 'An opportunity to become a more risk taking queen arises. This could be bad for the Mewmans and High Commission if you get hurt. Will you be a risk taker? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 2
            turns = 6
        elif message.content == 'Next' and game4 == 3 and turns == 5:
            msg = 'Your mother and the Magic High Commission wants you to go to a Queen School for Wayward Queens. Will you go? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 3
            turns = 6
        elif message.content == 'Next' and game4 == 4 and turns == 5:
            msg = 'While eating some corn you bite into a hard spot. Will you take your anger out on the Monsters and Mewmas? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 4
            turns = 6
        elif message.content == 'Next' and game4 == 5 and turns == 5:
            msg = 'The Monsters want you to make an appearence at a festivial celebrating monsters. The Magic High Commission things this is a horrible idea. Will you go? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 5
            turns = 6
        
        elif message.content == 'Yes' and game4 == 1 and turns == 6 and game3 == 1:
            game = 17
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 1 and turns == 6 and game3 == 1:
            game = 3
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 2 and turns == 6 and game3 == 2:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 2 and turns == 6 and game3 == 2:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 3 and turns == 6 and game3 == 3:
            game = 3
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 3 and turns == 6 and game3 == 3:
            game = 10
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 4 and turns == 6 and game3 == 4:
            game = 4
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 4 and turns == 6 and game3 == 4:
            game = 9
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 5 and turns == 6 and game3 == 5:
            game = 18
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 5 and turns == 6 and game3 == 5:
            game = 2
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Next' and game4 == 1 and turns == 6:
            msg = 'You see a fancy necklace on a Mewmans neck. You really like it. Will you force the Mewman to give it to you? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 1
            turns = 7
        elif message.content == 'Next' and game4 == 2 and turns == 6:
            msg = 'You can throw a festival and invite everyone! Everyone will enjoy it! Will you? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 2
            turns = 7
        elif message.content == 'Next' and game4 == 3 and turns == 6:
            msg = 'While baking your corn bread you see hungry mewmans and monsters outside your window. Will you feed the poor monsters and mewmans? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 3
            turns = 7
        elif message.content == 'Next' and game4 == 4 and turns == 6:
            msg = 'Your mother is about to die. The Magic High Commission wants you to have a quiet funeral. This would hurt Mewman moral though. Will you have a quiet funeral? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 4
            turns = 7
        elif message.content == 'Next' and game4 == 5 and turns == 6:
            msg = 'You misplaced the book of spells. The Magic High Commission will be mad. Mewmans will get scared. You will probably find it soon. Will you tell anyone? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 5
            turns = 7
        
        elif message.content == 'Yes' and game4 == 1 and turns == 7 and game3 == 1:
            game = 1
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 1 and turns == 7 and game3 == 1:
            game = 8
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 2 and turns == 7 and game3 == 2:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 2 and turns == 7 and game3 == 2:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 3 and turns == 7 and game3 == 3:
            game = 17
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 3 and turns == 7 and game3 == 3:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 4 and turns == 7 and game3 == 4:
            game = 17
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 4 and turns == 7 and game3 == 4:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 5 and turns == 7 and game3 == 5:
            game = 5
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 5 and turns == 7 and game3 == 5:
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Next' and game4 == 1 and turns == 7:
            msg = 'Your child wants you to eat some berries they picked. It is possible they are poisoned.. Do they want to be queen sooner? These berries will probably make you sick which will lower Mewman moral. Will you eat the berries? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 1
            turns = 8
        elif message.content == 'Next' and game4 == 2 and turns == 7:
            msg = 'While on a boat you see a strange monster in the water. You get worried. Will you murder the monster? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 2
            turns = 8
        elif message.content == 'Next' and game4 == 3 and turns == 7:
            msg = 'It is stump day! Will you throw a festival for the whole kingdom of Mewni? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 3
            turns = 8
        elif message.content == 'Next' and game4 == 4 and turns == 7:
            msg = 'The Monster come to make some negotiations. The Magic High Commission wants you to say no to everything. Will you make your own judgements? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 4
            turns = 8
        elif message.content == 'Next' and game4 == 5 and turns == 7:
            msg = 'The Magic High Comission and Glossaryk wants you to learn how to dip down. Will you learn? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 5
            turns = 8
        
        elif message.content == 'Yes' and game4 == 1 and turns == 8 and game3 == 1:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 1 and turns == 8 and game3 == 1:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 2 and turns == 8 and game3 == 2:
            game = 2
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 2 and turns == 8 and game3 == 2:
            game = 7
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 3 and turns == 8 and game3 == 3:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 3 and turns == 8 and game3 == 3:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 4 and turns == 8 and game3 == 4:
            game = 18
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 4 and turns == 8 and game3 == 4:
            game = 17
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 5 and turns == 8 and game3 == 5:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 5 and turns == 8 and game3 == 5:
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Next' and game4 == 1 and turns == 8:
            msg = 'Your oldest child turned 14! You can give them the wand or you can break traditions and keep the wand. Will you give them the wand? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 1
            turns = 9
        elif message.content == 'Next' and game4 == 2 and turns == 8:
            msg = 'A rebellious monster clan is attacking Butterfly Castle. Will you punish all monsters for attack? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 2
            turns = 9
        elif message.content == 'Next' and game4 == 3 and turns == 8:
            msg = 'Your child accidently blasts a hole into the side of the castle. You can hire mewni workers to fix it creating jobs, or fix it yourself with dip down magic. Will you hire mewmans? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 3
            turns = 9
        elif message.content == 'Next' and game4 == 4 and turns == 8:
            msg = 'You are in a generous mood. You can give money and the mewmans or monsters. Will you give money? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 4
            turns = 9
        elif message.content == 'Next' and game4 == 5 and turns == 8:
            msg = 'You discover a new type of food.. Ice Cream. Will you share with Mewni your creation? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 5
            turns = 9
        
        elif message.content == 'Yes' and game4 == 1 and turns == 9 and game3 == 1:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 1 and turns == 9 and game3 == 1:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 2 and turns == 9 and game3 == 2:
            game = 2
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 2 and turns == 9 and game3 == 2:
            game = 7
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 3 and turns == 9 and game3 == 3:
            game = 8
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 3 and turns == 9 and game3 == 3:
            game = 1
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 4 and turns == 9 and game3 == 4:
            game = 9
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 4 and turns == 9 and game3 == 4:
            game = 4
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Yes' and game4 == 5 and turns == 9 and game3 == 5:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'No' and game4 == 5 and turns == 9 and game3 == 5:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
        elif message.content == 'Next' and game4 == 1 and turns == 9:
            msg = 'You smell a bad smell coming from the caslte grounds. Will you blame the monsters? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 1
            turns = 10
        elif message.content == 'Next' and game4 == 2 and turns == 9:
            msg = 'Someone laced your drink with drugs. Will you punish all of Mewni? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 2
            turns = 10
        elif message.content == 'Next' and game4 == 3 and turns == 9:
            msg = 'While practicing dipping down you break a priceless Magical High Commission atifact. Will you tell them you did it? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 3
            turns = 10
        elif message.content == 'Next' and game4 == 4 and turns == 9:
            msg = 'Someone stole the royal crown. It could have been the monsters. Will you blame the monsters? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 4
            turns = 10
        elif message.content == 'Next' and game4 == 5 and turns == 9:
            msg = 'A song writer wants to create you a beautiful song to sing throughout Mewni. Will you let him create a song? Yes/No'.format(message)
            await message.channel.send(msg)
            game3 = 5
            turns = 10
        
        elif message.content == 'Yes' and game4 == 1 and turns == 10 and game3 == 1:
            game = 2
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            game2 = 3
        elif message.content == 'No' and game4 == 1 and turns == 10 and game3 == 1:
            game = 7
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            game2 = 3
        elif message.content == 'Yes' and game4 == 2 and turns == 10 and game3 == 2:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            game2 = 3
        elif message.content == 'No' and game4 == 2 and turns == 10 and game3 == 2:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            game2 = 3
        elif message.content == 'Yes' and game4 == 3 and turns == 10 and game3 == 3:
            game = 3
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            game2 = 3
        elif message.content == 'No' and game4 == 3 and turns == 10 and game3 == 3:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            game2 = 3
        elif message.content == 'Yes' and game4 == 4 and turns == 10 and game3 == 4:
            game = 2
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            game2 = 3
        elif message.content == 'No' and game4 == 4 and turns == 10 and game3 == 4:
            game = 7
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            game2 = 3
        elif message.content == 'Yes' and game4 == 5 and turns == 10 and game3 == 5:
            game = 14
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            game2 = 3
        elif message.content == 'No' and game4 == 5 and turns == 10 and game3 == 5:
            game = 13
            moongame()
            msg = 'Current Stats.. Mewmans:{}, Monsters:{}, Magic High Commission:{}. Say "Next"'.format(moonstatsmew, moonstatsmon, moonstatshighcom, message)
            await message.channel.send(msg)
            game4 = random.randint(1, 5)
            game2 = 3
        elif dialog == 10 and game2 == 3:
            msg = "The Queen is Dead! Your line continues.. Your Final Scores Were.. Mewmans:{}, Monsters:{}, Magic High Commission:{}.. Your title {}".format(moonstatsmew, moonstatsmon, moonstatshighcom, moongametitle, message)
            await message.channel.send(msg)
            game = 0
            game2 = 0
            game3 = 0
            game4 = 0
            turns = 0
            game5 = 0
            moonstatshighcom = 10
            moonstatsmew = 10
            moonstatsmon = 10
            moongametitle = "the Strange"


    #STEVEN UNIVERSE SECTION





        elif message.content == "Fandom Swap SU" and fanswapcount >= 1000:
            fanswapnum = 1
            dialog = 20
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Steven.jpg"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Steven"
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Eclipsa")
            time.sleep(2)
            #await client.edit_profile(password=None, username=new_username)
            msg = "Forming..".format(message)
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1hour
            msg = "I am Steven Quartz.. Diamond Universe!".format(message)
            await message.channel.send(msg)
            #change = 0
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
            msg = "Fandom Swapped to SU, Hi I'm Steven and my Life it's pretty crazy"
            await client.send_message (message.channel, msg)
            fanswapcount = 0
        elif message.content == "Fandom Swap SVTFOE" and fanswapcount >= 1000:
            fanswapnum = 0
            dialog = 1
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Eclipsa2.jpg"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Eclipsa"
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Eclipsa")
            time.sleep(2)
            #await client.edit_profile(password=None, username=new_username)
            msg = "Changing..".format(message)
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1hour
            msg = "I am Eclipsa Butterfly".format(message)
            await message.channel.send(msg)
            #change = 0
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
            msg = "Fandom Swapped to SVTFOE, Hello I'm Eclipsa and my Life it's pretty crazy"
            await client.send_message (message.channel, msg)
            fanswapcount = 0
        elif message.content == "Fandom Swap SU" and fanswapcount < 1000:
            msg = "Not enough messages yet! You need 1000! You have {}!".format(fanswapcount, message)
            await client.send_message (message.channel, msg)
        elif message.content == "Fandom Swap SVTFOE" and fanswapcount < 1000:
            msg = "Not enough messages yet! You need 1000! You have {}!".format(fanswapcount, message)
            await client.send_message (message.channel, msg)
        elif message.content == "Diamond" and dialog == 20:
            msg = "Steven Quartz.. Diamond Universe! Saved the galaxy and grew a neck!"
            await client.send_message (message.channel, msg)
        elif message.content == "I don't have time for this Steven!":
            msg = "Woah time is going fast zooom"
            await client.send_message (message.channel, msg)






        elif message.content == 'Diamond Claim Mewni' and (message.author == notdiamond or message.author == notdiamond2 or message.author == notdiamond3 or message.author == notdiamond4):
            msg = "You had your shot!".format(notdiamond,message)
            await message.channel.send(msg)
        elif message.content == 'Diamond Claim Mewni' and message.author == currentqueen:
            msg = "Stick to your Kingdom sweetie".format(diamond,message)
            await message.channel.send(msg)
        elif message.content == 'Diamond Claim Mewni' and diamond == 0:
            diamond = message.author
            notdiamond = message.author
            msg = "Long live the Mewni Gem Overlord! {}".format(diamond,message)
            await message.channel.send(msg)
            await client.send_message(diamond, "As a Gem Overlord you can automatically change the bot's diamond (as long as it is in SU mode!). If you change the queen too many times the picture will stop changing due to discord limitations. Try to limit yourself to once or twice per hour! You lose your Overlord rank whenever the Bot Resets But your name is Recorded! **Choose your name with 'Name:(your name and a title (you dont have to have a title))'** tip! You don't have to be a diamond!")   
            await client.send_message(diamond, "You can also have Entries. **Use 'Log: (entry)' to put something in the Diamond Log**")
            await client.send_message(diamond, "As a Overlord you can declare war and peace on other colonies and kingdoms. Do this by: 'Declare (War/Peace) (Mewni Diamond, Mewni, Earth Diamond, Boogaooga Diamond, Homeworld Diamond)'")


        elif message.content.startswith('Name:') and message.author == diamond and diamondnum == 0:
            diamondname = message.content
            await client.send_message(client.get_channel('612362848554975245'), 'All Hail the Mewni Gem Overlord {}, {}!'.format(diamondname, diamond))
            await client.send_message(client.get_channel('614204564958347288'), 'All Hail the Mewni Gem Overlord {}, {}!'.format(diamondname, diamond))
            msg = "You are now Overlord: {}!".format(diamondname,message)
            await message.channel.send(msg)
            diamondnum = 1




        elif message.content == 'Summon Yellow' and messagechoice <= messagenumber and fanswapnum == 1:
            fanswapnum = 1
            dialog = 21
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Yellow.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Yellow Diamond"
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Eclipsa")
            time.sleep(2)
            #await client.edit_profile(password=None, username=new_username)
            msg = "Forming..".format(message)
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1hour
            msg = "Rise for your all-mighty YELLOW DIAMOND!".format(message)
            await message.channel.send(msg)
            #change = 0
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon White' and messagechoice <= messagenumber and fanswapnum == 1:
            fanswapnum = 1
            dialog = 22
            #pfp_path =r"/home/pi/Desktop/Eclipsa/White.jpg"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "White Diamond"
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Eclipsa")
            time.sleep(2)
            #await client.edit_profile(password=None, username=new_username)
            msg = "Forming..".format(message)
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1hour
            msg = "Rise for your radient WHITE DIAMOND!".format(message)
            await message.channel.send(msg)
            #change = 0
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon Blue' and messagechoice <= messagenumber and fanswapnum == 1:
            fanswapnum = 1
            dialog = 23
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Blue2.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Blue Diamond"
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Eclipsa")
            time.sleep(2)
            #await client.edit_profile(password=None, username=new_username)
            msg = "Forming..".format(message)
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1hour
            msg = "Rise for your weary BLUE DIAMOND".format(message)
            await message.channel.send(msg)
            #change = 0
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon Steven' and messagechoice <= messagenumber and fanswapnum == 1:
            fanswapnum = 1
            dialog = 20
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Steven.jpg"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Steven Quartz (Diamond) Universe"
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Eclipsa")
            time.sleep(2)
            #await client.edit_profile(password=None, username=new_username)
            msg = "Forming..".format(message)
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1hour
            msg = "All rise for Pink Lasagna!".format(message)
            await message.channel.send(msg)
            #change = 0
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)

        elif message.content == 'Summon Yellow' and message.author == diamond and fanswapnum == 1:
            fanswapnum = 1
            dialog = 21
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Yellow.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Yellow Diamond"
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Eclipsa")
            time.sleep(2)
            #await client.edit_profile(password=None, username=new_username)
            msg = "Forming..".format(message)
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1hour
            msg = "Rise for your all-mighty YELLOW DIAMOND!".format(message)
            await message.channel.send(msg)
            #change = 0
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon White' and message.author == diamond and fanswapnum == 1:
            fanswapnum = 1
            dialog = 22
            #pfp_path =r"/home/pi/Desktop/Eclipsa/White.jpg"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "White Diamond"
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Eclipsa")
            time.sleep(2)
            #await client.edit_profile(password=None, username=new_username)
            msg = "Forming..".format(message)
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1hour
            msg = "Rise for your radient WHITE DIAMOND!".format(message)
            await message.channel.send(msg)
            #change = 0
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon Blue' and message.author == diamond and fanswapnum == 1:
            fanswapnum = 1
            dialog = 23
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Blue2.png"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Blue Diamond"
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Eclipsa")
            time.sleep(2)
            #await client.edit_profile(password=None, username=new_username)
            msg = "Forming..".format(message)
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1hour
            msg = "Rise for your weary BLUE DIAMOND".format(message)
            await message.channel.send(msg)
            #change = 0
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)
        elif message.content == 'Summon Steven' and message.author == diamond and fanswapnum == 1:
            fanswapnum = 1
            dialog = 20
            #pfp_path =r"/home/pi/Desktop/Eclipsa/Steven.jpg"
            #fp = open(#pfp_path, 'rb')
            #p#fp = fp.read()
            new_username = "Steven Quartz (Diamond) Universe"
            await client.edit_profile(password=None, avatar=pfp)
            #await client.change_nickname(me, "Eclipsa")
            time.sleep(2)
            #await client.edit_profile(password=None, username=new_username)
            msg = "Forming..".format(message)
            await message.channel.send(msg)
            time.sleep(2) #3600 = 1hour
            msg = "All rise for Pink Lasagna!".format(message)
            await message.channel.send(msg)
            #change = 0
            time.sleep(5)
            messagenumber = 0
            messagechoice  = random.randint(50,200)

        elif message.content.startswith('Log:') and message.author == diamond:
            game4 = message.content
            await client.send_message(client.get_channel('635139680018497536'), '{} by **{}**'.format(game4, diamondname))
            await client.send_message(client.get_channel('635140459089362954'), '{} by **{}**'.format(game4, diamondname))
            await client.send_message(diamond, "Entry Recorded! You can make more entries if you want!")
        elif message.content.startswith('Log:') and message.author == diamond2:
            game4 = message.content
            await client.send_message(client.get_channel('635139680018497536'), '{} by **{}**'.format(game4, diamondname2))
            await client.send_message(client.get_channel('635140459089362954'), '{} by **{}**'.format(game4, diamondname2))
            await client.send_message(diamond2, "Entry Recorded! You can make more entries if you want!")
        elif message.content.startswith('Log:') and message.author == diamond3:
            game4 = message.content
            await client.send_message(client.get_channel('635139680018497536'), '{} by **{}**'.format(game4, diamondname3))
            await client.send_message(client.get_channel('635140459089362954'), '{} by **{}**'.format(game4, diamondname3))
            await client.send_message(diamond3, "Entry Recorded! You can make more entries if you want!")
        elif message.content.startswith('Log:') and message.author == diamond4:
            game4 = message.content
            await client.send_message(client.get_channel('635139680018497536'), '{} by **{}**'.format(game4, diamondname4))
            await client.send_message(client.get_channel('635140459089362954'), '{} by **{}**'.format(game4, diamondname4))
            await client.send_message(diamond4, "Entry Recorded! You can make more entries if you want!")

        elif message.content == 'Diamond' and dialog == 20:
            msg = "Universe, Steven Universe is my name and I loveeeeee donuts.. Oh yea I saved the galaxy and junk".format(diamondname,diamond,message)
            await message.channel.send(msg)
        elif message.content == 'Diamond' and dialog == 21:
            msg = "I am Yellow Diamond. *zap zap*".format(diamondname,diamond,message)
            await message.channel.send(msg)
        elif message.content == 'Diamond' and dialog == 22:
            msg = "I am White Diamond. I say please and thank you to lower lifeforms.. Equal Life forms..!".format(diamondname,diamond,message)
            await message.channel.send(msg)
        elif message.content == 'Diamond' and dialog == 23:
            msg = "I am Blue Diamond, and I dont kill people anymore :D".format(diamondname,diamond,message)
            await message.channel.send(msg)
        elif message.content == 'Diamonds':
            msg = "Yellow Diamond, Blue Diamond, White Diamond, Steven".format(diamondname,diamond,message)
            await message.channel.send(msg)

        elif message.content == 'Diamond Current Leader':
            msg = "Current Mewni Gem Overlord: {}; {}".format(diamondname,diamond,message)
            await message.channel.send(msg)
            msg = "Current Boogaooga Gem Overlord: {}; {}".format(diamondname2,diamond2,message)
            await message.channel.send(msg)
            msg = "Current Earth Gem Overlord: {}; {}".format(diamondname3,diamond3,message)
            await message.channel.send(msg)
            msg = "Current Homewold Gem Overlord: {}; {}".format(diamondname4,diamond4,message)
            await message.channel.send(msg)

    #Mewni, Boogaooga, Earth, Homeworld


        elif message.content == 'Shatter them! Insulent Fools. Mewni Diamond shall die.':
            diamondname = 0
            diamond = 0
            diamondnum = 0
        elif message.content == 'Shatter them! Insulent Fools. Homeworld Diamond shall die.':
            diamondname = 4
            diamond = 4
            diamondnum = 4
        elif message.content == 'Shatter them! Insulent Fools. Earth Diamond shall die.':
            diamondname = 3
            diamond = 3
            diamondnum = 3
        elif message.content == 'Shatter them! Insulent Fools. Boogaooga Diamond shall die.':
            diamondname = 2
            diamond = 2
            diamondnum = 2

        elif message.content == 'Diamond Claim Boogaooga' and (message.author == notdiamond or message.author == notdiamond2 or message.author == notdiamond3 or message.author == notdiamond4):
            msg = "You had your shot!".format(notdiamond,message)
            await message.channel.send(msg)
        elif message.content == 'Diamond Claim Boogaooga' and message.author == currentqueen:
            msg = "Stick to your Kingdom sweetie".format(diamond,message)
            await message.channel.send(msg)
        elif message.content == 'Diamond Claim Boogaooga' and diamond2 == 0:
            diamond2 = message.author
            notdiamond2 = message.author
            msg = "Long live the Gem Overlord! {}".format(diamond2,message)
            await message.channel.send(msg)
            await client.send_message(diamond2, "As a Gem Overlord you can automatically change the bot's diamond (as long as it is in SU mode!). If you change the queen too many times the picture will stop changing due to discord limitations. Try to limit yourself to once or twice per hour! You lose your Overlord rank whenever the Bot Resets But your name is Recorded! **Choose your name with 'Name:(your name and a title (you dont have to have a title))'** tip! You don't have to be a diamond!")   
            await client.send_message(diamond2, "You can also have Entries. **Use 'Log: (entry)' to put something in the Diamond Log**")
            await client.send_message(diamond, "As a Overlord you can declare war and peace on other colonies and kingdoms. Do this by: 'Declare (War/Peace) (Mewni Diamond, Mewni, Earth Diamond, Boogaooga Diamond, Homeworld Diamond)'")



        elif message.content.startswith('Name:') and message.author == diamond2 and diamondnum2 == 0:
            diamondname2 = message.content
            await client.send_message(client.get_channel('612362848554975245'), 'All Hail Gem Overlord {}, {}!'.format(diamondname2, diamond2))
            await client.send_message(client.get_channel('614204564958347288'), 'All Hail Gem Overlord {}, {}!'.format(diamondname2, diamond2))
            msg = "You are now Overlord: {}!".format(diamondname2,message)
            await message.channel.send(msg)
            diamondnum2 = 1
        elif message.content == 'Diamond Claim Earth' and (message.author == notdiamond or message.author == notdiamond2 or message.author == notdiamond3 or message.author == notdiamond4):
            msg = "You had your shot!".format(notdiamond,message)
            await message.channel.send(msg)
        elif message.content == 'Diamond Claim Earth' and message.author == currentqueen:
            msg = "Stick to your Kingdom sweetie".format(diamond,message)
            await message.channel.send(msg)
        elif message.content == 'Diamond Claim Earth' and diamond3 == 0:
            diamond3 = message.author
            notdiamond3 = message.author
            msg = "Long live the Gem Overlord! {}".format(diamond3,message)
            await message.channel.send(msg)
            await client.send_message(diamond3, "As a Gem Overlord you can automatically change the bot's diamond (as long as it is in SU mode!). If you change the queen too many times the picture will stop changing due to discord limitations. Try to limit yourself to once or twice per hour! You lose your Overlord rank whenever the Bot Resets But your name is Recorded! **Choose your name with 'Name:(your name and a title (you dont have to have a title))'** tip! You don't have to be a diamond!")   
            await client.send_message(diamond3, "You can also have Entries. **Use 'Log: (entry)' to put something in the Diamond Log**")
            await client.send_message(diamond, "As a Overlord you can declare war and peace on other colonies and kingdoms. Do this by: 'Declare (War/Peace) (Mewni Diamond, Mewni, Earth Diamond, Boogaooga Diamond, Homeworld Diamond)'")



        elif message.content.startswith('Name:') and message.author == diamond3 and diamondnum3 == 0:
            diamondname3 = message.content
            await client.send_message(client.get_channel('612362848554975245'), 'All Hail Gem Overlord {}, {}!'.format(diamondname3, diamond3))
            await client.send_message(client.get_channel('614204564958347288'), 'All Hail Gem Overlord {}, {}!'.format(diamondname3, diamond3))
            msg = "You are now Overlord: {}!".format(diamondname3,message)
            await message.channel.send(msg)
            diamondnum3 = 1
        elif message.content == 'Diamond Claim Homeworld' and (message.author == notdiamond or message.author == notdiamond2 or message.author == notdiamond3 or message.author == notdiamond4):
            msg = "You had your shot!".format(notdiamond,message)
            await message.channel.send(msg)
        elif message.content == 'Diamond Claim Homeworld' and message.author == currentqueen:
            msg = "Stick to your Kingdom sweetie".format(diamond,message)
            await message.channel.send(msg)
        elif message.content == 'Diamond Claim Homeworld' and diamond4 == 0:
            diamond4 = message.author
            notdiamond4 = message.author
            msg = "Long live the Gem Overlord! {}".format(diamond4,message)
            await message.channel.send(msg)
            await client.send_message(diamond4, "As a Gem Overlord you can automatically change the bot's diamond (as long as it is in SU mode!). If you change the queen too many times the picture will stop changing due to discord limitations. Try to limit yourself to once or twice per hour! You lose your Overlord rank whenever the Bot Resets But your name is Recorded! **Choose your name with 'Name:(your name and a title (you dont have to have a title))'** tip! You don't have to be a diamond!")   
            await client.send_message(diamond4, "You can also have Entries. **Use 'Log: (entry)' to put something in the Diamond Log**")
            await client.send_message(diamond, "As a Overlord you can declare war and peace on other colonies and kingdoms. Do this by: 'Declare (War/Peace) (Mewni Diamond, Mewni, Earth Diamond, Boogaooga Diamond, Homeworld Diamond)'")



        elif message.content.startswith('Name:') and message.author == diamond4 and diamondnum4 == 0:
            diamondname4 = message.content
            await client.send_message(client.get_channel('612362848554975245'), 'All Hail Gem Overlord {}, {}!'.format(diamondname4, diamond4))
            await client.send_message(client.get_channel('614204564958347288'), 'All Hail Gem Overlord {}, {}!'.format(diamondname4, diamond4))
            msg = "You are now Overlord: {}!".format(diamondname4,message)
            await message.channel.send(msg)
            diamondnum4 = 1










    #Declaring War / Peace / Neautrality

        elif message.content == 'Declare War on Mewni Diamond' and message.author == currentqueen:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(currentqueenname, diamondname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(currentqueenname, diamondname))
        elif message.content == 'Declare War on Earth Diamond' and message.author == currentqueen:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(currentqueenname, diamondname3))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(currentqueenname, diamondname3))
        elif message.content == 'Declare War on Homeworld Diamond' and message.author == currentqueen:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(currentqueenname, diamondname4))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(currentqueenname, diamondname4))
        elif message.content == 'Declare War on Boogaooga Diamond' and message.author == currentqueen:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(currentqueenname, diamondname2))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(currentqueenname, diamondname2))

        elif message.content == 'Declare War on Mewni' and message.author == diamond:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname, currentqueenname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname, currentqueenname))
        elif message.content == 'Declare War on Earth Diamond' and message.author == diamond:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname, diamondname3))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname, diamondname3))
        elif message.content == 'Declare War on Homeworld Diamond' and message.author == diamond:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname, diamondname4))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname, diamondname4))
        elif message.content == 'Declare War on Boogaooga Diamond' and message.author == diamond:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname, diamondname2))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname, diamondname2))

        elif message.content == 'Declare War on Mewni Diamond' and message.author == diamond2:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname2, diamondname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname2, diamondname))
        elif message.content == 'Declare War on Earth Diamond' and message.author == diamond2:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname2, diamondname3))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname2, diamondname3))
        elif message.content == 'Declare War on Homeworld Diamond' and message.author == diamond2:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname2, diamondname4))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname2, diamondname4))
        elif message.content == 'Declare War on Mewni' and message.author == diamond2:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname2, currentqueenname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname2, currentqueenname))

        elif message.content == 'Declare War on Mewni Diamond' and message.author == diamond3:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname3, diamondname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname3, diamondname))
        elif message.content == 'Declare War on Mewni' and message.author == diamond3:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname3, currentqueenname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname3, currentqueenname))
        elif message.content == 'Declare War on Homeworld Diamond' and message.author == diamond3:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname3, diamondname4))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname3, diamondname4))
        elif message.content == 'Declare War on Boogaooga Diamond' and message.author == diamond3:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname3, diamondname2))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname3, diamondname2))

        elif message.content == 'Declare War on Mewni Diamond' and message.author == diamond4:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname4, diamondname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname4, diamondname))
        elif message.content == 'Declare War on Mewni' and message.author == diamond4:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname4, currentqueenname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname4, currentqueenname))
        elif message.content == 'Declare War on Earth' and message.author == diamond4:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname4, diamondname3))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname4, diamondname3))
        elif message.content == 'Declare War on Boogaooga Diamond' and message.author == diamond4:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares war on **{}**'.format(diamondname4, diamondname2))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares war on **{}**'.format(diamondname4, diamondname2))
        elif message.content == 'Declare Peace on Mewni Diamond' and message.author == currentqueen:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(currentqueenname, diamondname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(currentqueenname, diamondname))
        elif message.content == 'Declare Peace on Earth Diamond' and message.author == currentqueen:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(currentqueenname, diamondname3))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(currentqueenname, diamondname3))
        elif message.content == 'Declare Peace on Homeworld Diamond' and message.author == currentqueen:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(currentqueenname, diamondname4))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(currentqueenname, diamondname4))
        elif message.content == 'Declare Peace on Boogaooga Diamond' and message.author == currentqueen:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(currentqueenname, diamondname2))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(currentqueenname, diamondname2))

        elif message.content == 'Declare Peace on Mewni' and message.author == diamond:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname, currentqueenname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname, currentqueenname))
        elif message.content == 'Declare Peace on Earth Diamond' and message.author == diamond:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname, diamondname3))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname, diamondname3))
        elif message.content == 'Declare Peace on Homeworld Diamond' and message.author == diamond:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname, diamondname4))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname, diamondname4))
        elif message.content == 'Declare Peace on Boogaooga Diamond' and message.author == diamond:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname, diamondname2))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname, diamondname2))

        elif message.content == 'Declare Peace on Mewni Diamond' and message.author == diamond2:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname2, diamondname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname2, diamondname))
        elif message.content == 'Declare Peace on Earth Diamond' and message.author == diamond2:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname2, diamondname3))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname2, diamondname3))
        elif message.content == 'Declare Peace on Homeworld Diamond' and message.author == diamond2:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname2, diamondname4))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname2, diamondname4))
        elif message.content == 'Declare Peace on Mewni' and message.author == diamond2:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname2, currentqueenname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname2, currentqueenname))

        elif message.content == 'Declare Peace on Mewni Diamond' and message.author == diamond3:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname3, diamondname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname3, diamondname))
        elif message.content == 'Declare Peace on Mewni' and message.author == diamond3:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname3, currentqueenname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname3, currentqueenname))
        elif message.content == 'Declare Peace on Homeworld Diamond' and message.author == diamond3:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname3, diamondname4))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname3, diamondname4))
        elif message.content == 'Declare Peace on Boogaooga Diamond' and message.author == diamond3:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname3, diamondname2))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname3, diamondname2))

        elif message.content == 'Declare Peace on Mewni Diamond' and message.author == diamond4:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname4, diamondname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname4, diamondname))
        elif message.content == 'Declare Peace on Mewni' and message.author == diamond4:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname4, currentqueenname))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname4, currentqueenname))
        elif message.content == 'Declare Peace on Earth' and message.author == diamond4:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname4, diamondname3))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname4, diamondname3))
        elif message.content == 'Declare Peace on Boogaooga Diamond' and message.author == diamond4:
            await client.send_message(client.get_channel('614216403503022120'), '**{}** Declares Peace on **{}**'.format(diamondname4, diamondname2))
            await client.send_message(client.get_channel('635607988295696384'), '**{}** Declares Peace on **{}**'.format(diamondname4, diamondname2))










        else:
            messagenumber += 1
            fanswapcount += 1

def moongame():
    global game # 1 is -Mewmans, 2 is -Monsters, 3 is -MHC, 4 is -Mewmans and -Monsters, 5 is -Mewmans and -MHC, 6 is -Monsters and -MHC, 7 is +Monsters
    global game2 # 8 is +Mewmans, 9 is +Monsters and +Mewmans, 10 is +MHC, 11 is +Monsters and +MHC, 12 is +Mewmans and +MHC, 13 is -all 3, 14 is +all
    global game3 # 15 is +Monsters -Mewmans -MHC, 16 is -Monsters +Mewmans +MHC, 17 +MHC -Mewmans -Monsters, 18 is -MHC +Monsters +Mewmans
    global game4
    global moonstatshighcom
    global moonstatsmew
    global moonstatsmon
    global game5
    global moongametitle
    #turns += 1
#    if turns == 9:
#        game = 0
#        game2 = 3
#        game3 = 0
#        game4 = 0
#        moonstatshighcom = 10
#        moonstatsmew = 10
#        moonstatsmon = 10
    if moonstatshighcom >= 10 and moonstatsmew < 10 and moonstatsmon < 10:
        moongametitle = "the Suckup"
    if moonstatshighcom < 10 and moonstatsmew >= 10 and moonstatsmon < 10:
        moongametitle = "the People Queen"
    if moonstatshighcom < 10 and moonstatsmew < 10 and moonstatsmon >= 10:
        moongametitle = "the Monster Lover"
    if moonstatshighcom < 10 and moonstatsmew < 10 and moonstatsmon <= 10:
        moongametitle = "the Underachiever"
    if moonstatshighcom >= 10 and moonstatsmew >= 10 and moonstatsmon > 10:
        moongametitle = "the Happy Maker"
    if moonstatshighcom == 10 and moonstatsmew == 10 and moonstatsmon == 10:
        moongametitle = "the Ultimate Neutral"
    if moonstatshighcom >= 10 and moonstatsmew >= 10 and moonstatsmon < 10:
        moongametitle = "the Monster Eater"
    if game == 1:
        moonstatsmew -= 2
    if game == 2:
        moonstatsmon -= 2
    if game == 3:
        moonstatshighcom -= 2
    if game == 4:
        moonstatsmew -= 2
        moonstatsmon -= 2
    if game == 5:
        moonstatsmew -= 2
        moonstatshighcom -= 2
    if game == 6:
        moonstatshighcom -= 2
        moonstatsmon -= 2
    if game == 7:
        moonstatsmon += 2
    if game == 8:
        moonstatsmew += 2
    if game == 9:
        moonstatsmew += 2
        moonstatsmon += 2
    if game == 10:
        moonstatshighcom += 2
    if game == 11:
        moonstatsmon += 2
        moonstatshighcom += 2
    if game == 12:
        moonstatsmew += 2
        moonstatshighcom += 2
    if game == 13:
        moonstatsmew -= 2
        moonstatshighcom -= 2
        moonstatsmon -= 2
    if game == 14:
        moonstatsmew += 2
        moonstatsmon += 2
        moonstatshighcom += 2
    if game == 15:
        moonstatsmew -= 2
        moonstatsmon += 2
        moonstatshighcom -= 2
    if game == 16:
        moonstatsmew += 2
        moonstatsmon -= 2
        moonstatshighcom += 2
    if game == 17:
        moonstatsmew -= 2
        moonstatsmon -= 2
        moonstatshighcom += 2
    if game == 18:
        moonstatsmew += 2
        moonstatsmon += 2
        moonstatshighcom -= 2
client = MyClient()
client.run("")
