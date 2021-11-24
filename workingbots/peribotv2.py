import random
import asyncio
import aiohttp
import discord
import pickle

client = discord.Client()
 
botnum = 0
 
Jboogers = 0
 
haha = 0

macousins = random.choice(["john","jeff","emily","carole"])
 
noun = random.choice(["man", "woman", "dog", "store", "kid", "dog", "cat", "cabinet", "waffle", "car", "llama", "chair", "Pie"])
 
noun2 = random.choice(["man", "woman", "dog", "store", "kid", "dog", "cat", "Fredbear's family diner", "fried chicken", "children", "rock", "Pie"])
 
verb = random.choice(["went", "ran", "swims", "talks", "sits", "cries", "slaps", "kicks", "punch", "drops", "stops", "grows"])
 
verb2 = random.choice(["went", "ran", "swims", "talked", "sits", "cries", "slaps", "kicks", "punch", "drops", "smells", "grows"])
 
adjective = random.choice(["fun", "happy", "scary", "pretty", "fat", "tall", "weird", "red", "tired", "smelly", "dangerous", "funny"])
 
adjective2 = random.choice(["fun", "happy", "scary", "pretty", "fat", "tall", "weird", "dead", "dirty", "sad", "fast", "slow"])
 
article = random.choice(["the", "a", "some"])
 
article2 = random.choice(["the", "a", "some"])
 
preposition = random.choice(["to", "under", "over", "through", "around"])
 
conjunction = random.choice(["and"])
 
adverb = random.choice(["happily", "gloomily", "sadly", "stupidly", "weirdly", "strangly", "slowly", "quickly", "scaredly", "meanly"])
 
adverb2 = random.choice(["happily", "gloomily", "sadly", "stupidly", "weirdly", "strangly", "slowly", "quickly", "forcefully", "worridly"])
 
space = " "
 
sentenceoftheday = random.choice([article + space + noun + space + adverb + space + verb + space + preposition + space + article + space + adjective + space + noun2, article + space + adjective + space + adjective2 + space + noun + space + adverb + space + verb + space + conjunction + space + adverb2 + space + verb2 + space + preposition + space + article2 + space + noun2, macousins + space + adverb + space + verb + space + preposition + space + article + space + adjective + space + noun, noun + space + adverb + space + verb + space + preposition + space + adjective2 + space + noun2])
 
game = discord.Game("with Emotions")
 
annoyingspam = 0
class MyClient(discord.Client):
    async def on_ready(self):
        global game
        print('Logged on as', self.user)
        await client.change_presence(activity=game)
        async for guild in client.fetch_guilds(limit=150):
            print(guild.name)
 
 
 
    async def on_message(self, message):
        global botnum
        global Jboogers
        global macousins
        global sentenceoftheday
        global haha
        global annoyingspam
#we do not want the bot to reply to itself
        if message.author == client.user:
            return
        if message.content.startswith('Peribot'):
            msg = random.choice(["I'm Busy! D:<", "What do you want you Clod?", "Ahh.. I love that name!"]).format(message)
            await message.channel.send(msg)
        elif botnum == 20 and annoyingspam == 0:
            msg = random.choice(["You Clods are so Annoying!!", "EEEE You people talk so Cloddin much!", "What if you CLODS SHUSHSH!"]).format(message)
            await message.channel.send(msg)
            botnum = 0
        elif message.content.startswith('info'):
            msg = "Created by Popleoma with the intent of being a fun bot. Currently at version 1.1.3! Commands are Peribot, info, Lapidot, Peridot, Sentence of the day, All Hail Peri, watermel, How many watermelon, shut up peri and more to come!".format(message)
            await message.channel.send(msg)
        elif message.content.startswith('Lapidot'):
            msg = "Ima be a metal throwing, water spewing, flying machine! :cackles:".format(message)
            await message.channel.send(msg)
        elif message.content.startswith('Peri what is your birthday?'):
            msg = "Hmm, assuming you mean when I was first formed... Earth Month 8.. Earth Day 7th!".format(message)
            await message.channel.send(msg)
        elif message.content.startswith('shut up peri'):
            msg = "You clod, I am offended! You shall wear this hat of shame. https://imgur.com/PXS1z6U".format(message)
            await message.channel.send(msg)
        elif message.content.startswith('Sentence of the day'):
            msg = "The sentence of the day is:  {}".format(sentenceoftheday, message)
            await message.channel.send(msg)
        elif message.content.startswith('Peridot'):
            msg = "I don't know who this 'Peridot' character is but she sounds very un-cloddy :thinking:".format(message)
            await message.channel.send(msg)
        elif message.content.startswith('All Hail Peri'):
            msg = random.choice(["Aha thank you, thank you!", "Yes, Yes! All Hail me!", "Why am I being hailed?? :grimacing: I like it though.. :smile:"]).format(message)
            await message.channel.send(msg)
        elif message.content.startswith('How many watermelon'):
            msg = "{} has {} boogers".format(macousins, Jboogers, message)
            await message.channel.send(msg)
        elif message.content.startswith('findingnemo'):
            msg = "snorkle".format(Jboogers, message)
            await message.channel.send(msg)
        elif message.content.startswith('watermelon'):
            Jboogers += 1
        elif message.content == "Disable Spam":
            annoyingspam = 1
            await message.channel.send("Complete")
        elif message.content == "Enable Spam":
            annoyingspam = 0
            await message.channel.send("Complete")

        counter = 0
        
        if message.content == "Pull Random Picture":
            while counter < 5:
                freevar = message.author
                ranlet1= random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet2=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet3=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet4=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet5=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranseq= ranlet1 + ranlet2 +ranlet3+ranlet4+ranlet5
                await freevar.send("http://i.imgur.com/{}.png".format(ranseq))
                ranlet1= random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet2=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet3=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet4=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet5=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranseq= ranlet1 + ranlet2 +ranlet3+ranlet4+ranlet5
                await freevar.send("http://i.imgur.com/{}.png".format(ranseq))
                ranlet1= random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet2=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet3=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet4=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet5=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranseq= ranlet1 + ranlet2 +ranlet3+ranlet4+ranlet5
                await freevar.send("http://i.imgur.com/{}.png".format(ranseq))
                ranlet1= random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet2=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet3=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet4=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranlet5=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"])
                ranseq= ranlet1 + ranlet2 +ranlet3+ranlet4+ranlet5
                await freevar.send("http://i.imgur.com/{}.png".format(ranseq))
                counter = counter + 1
 
 
 
        else:
            botnum += 1
client = MyClient()
client.run("")
