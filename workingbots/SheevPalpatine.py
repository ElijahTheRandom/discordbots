import discord
import random
import datetime
import asyncio
import pickle

typingtimer = 0
game = discord.Game("with Democracy")
date = datetime.datetime
name = "Chancellor Palpatine"
timer = 0
character = 1
reset = 0
gifss = 0
reactionnums = 0
popleoma = 0
macousins = random.choice(["bob","george","linda","crayola"])

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
testnum = 0 
sentenceoftheday = random.choice([article + space + noun + space + adverb + space + verb + space + preposition + space + article + space + adjective + space + noun2, article + space + adjective + space + adjective2 + space + noun + space + adverb + space + verb + space + conjunction + space + adverb2 + space + verb2 + space + preposition + space + article2 + space + noun2, noun2 + space + adverb + space + verb + space + preposition + space + article + space + adjective + space + noun, noun + space + adverb + space + verb + space + preposition + space + adjective2 + space + noun2])
senatornum1 = 0
senatornum2 = 0
senatorset = {"Senators"}
senatorsetnums = {0}
senatorauthors = {0}
chancellor = {"Chancellors"}
senatorleaders = {"Senate Leaders"}
senateleadernum = 0
senateleadernum2 = 0
senateleadernum3 = 0
chancellornum = 0
chancellornum2 = 0
loremaster = {0}
sentenceoftheday2 = 0
sentenceoftheday3 = 0
class MyClient(discord.Client):
    global date
    global game
    global typingtimer
    async def on_ready(self):
        global senatornum1
        global senatornum2
        print('Logged on as', self.user)
        await client.change_presence(activity=game)
        async for guild in client.fetch_guilds(limit=150):
            print(guild.name)
       # senatornum1 = random.randint(0, 500)
        #senatornum2 = random.randint(0, 500)
       # senatorset = pickle.load(open(r"C:\Users\pople\Desktop\Python Bots\Palpatine\sennum1.pkl", "rb"))
  #      senatorsetnums = pickle.load(open(r"C:\Users\pople\Desktop\Python Bots\Palpatine\sensetnums.pkl", "rb"))
   #     senatorauthors = pickle.load(open(r"C:\Users\pople\Desktop\Python Bots\Palpatine\senauthors.pkl", "rb"))


    async def on_message(self, message):
        # don't respond to ourselves
        global typingtimer
        global name
        global timer
        global character
        global reset
        global gifss
        global reactionnums
        global popleoma
        global noun
        global noun2
        global verb
        global verb2
        global adjective
        global adjective2
        global article
        global article2
        global preposition
        global conjunction
        global adverb
        global adverb2
        global space
        global testnum
        global sentenceoftheday
        global senatornum1
        global senatornum2
        global senatorset
        global senatorsetnums
        global senatorauthors
        global chancellor
        global senatorleaders
        global senateleadernum
        global senateleadernum2
        global senateleadernum3
        global chancellornum
        global chancellornum2
        global sentenceoftheday2
        global sentenceoftheday3
        if message.author == self.user:
            return
            
        if message.content == "Clones":
            gifss = random.choice(["https://media.giphy.com/media/1lznA4FFhnyJiUYIip/giphy.gif","https://media3.giphy.com/media/EgUfjmaWvwD0Q/source.gif","https://media3.giphy.com/media/43VnvrEmxehGM/giphy.gif","https://em.wattpad.com/fb5cbb713a906c69dd4c632f4175bd7794b9a490/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f4a46474a2d6d716b714b49315a773d3d2d3339343132363830342e313462323463373438323531663533373231333133373937333431332e676966","https://memestatic.fjcdn.com/gifs/Star_df7d35_6423532.gif","https://78.media.tumblr.com/34f1a853d6ac5c8018f7289cbaea4d20/tumblr_ndb47r8DBJ1tjjuglo2_500.gif","https://media2.giphy.com/media/gr3rGWS6c7pKM/giphy.gif",""])
            await message.channel.send(gifss)

        if message.content == "Palpatine":
            gifss = random.choice(["https://media.giphy.com/media/ePL05nRDzwCXe/giphy.gif", "https://media.giphy.com/media/9g8PH1MbwTy4o/giphy.gif", "https://media.giphy.com/media/C89ePJHZWq6FmvGAsj/giphy.gif", "https://media.giphy.com/media/B6Jr28VwfxUFa/giphy.gif", "https://tenor.com/view/emperor-palpatine-luke-skywalker-shock-gif-13110792", "https://media.giphy.com/media/4gxOxfuL0QHQY/giphy.gif", "https://media.giphy.com/media/xTiIzBS80Jx9nMwmME/giphy.gif", "https://media.giphy.com/media/SJb0vHduIW8wM/giphy.gif", "https://media.giphy.com/media/mxJAwFqouAqo8/giphy.gif","https://media.giphy.com/media/qf4zM1Ne6ZTji/giphy.gif", "https://media.giphy.com/media/oZWhOWcEQh84M/giphy.gif", "https://media.giphy.com/media/l0HlRqd6Quh2HiXks/giphy.gif", "https://media.giphy.com/media/3o84sDfCF4mZR7aFYk/giphy.gif", "https://media.giphy.com/media/xTiIzIhgJ6ZrY3cZeo/giphy.gif", "https://media.giphy.com/media/3o84sIQ7S5BLsvETIc/giphy.gif", "https://media.giphy.com/media/kJWYrH269RK8M/giphy.gif", "https://tenor.com/view/threatning-jedi-palpatine-chancellor-gif-14403782", "https://tenor.com/view/sheev-palpatine-emperor-chancellor-kill-him-now-gif-14424446", "https://tenor.com/view/star-wars-palpatine-senate-gif-13095904", "https://tenor.com/view/palpatine-treason-star-wars-emperor-gif-8547403", "https://tenor.com/view/plan-b-star-wars-palpatine-obiwan-anakin-gif-10785572"])
            await message.channel.send(gifss)

        if message.content == "Appoint Senator Leaders" and message.author in chancellor:
            senateleadernum = random.randint(0, 1000000)
            senateleadernum2 = random.randint(0, 1000000)
            senateleadernum3 = random.randint(0, 1000000)
            chancellorperson = message.author
            await chancellorperson.send("Your lead senator codes are.. {}, {}, and {}. They can claim their rank with Senate Lead Claim (code)".format(senateleadernum, senateleadernum2, senateleadernum3))

        if message.content == "Senate Lead Claim " + str(senateleadernum) and senateleadernum != 0:
            senatornum2 = "Lead Senator {}".format(message.author)
            senateleaders.add(message.author)
            persons = message.author
            await persons.send("Congrats Senate Leader. You can authorize votes now! To authorize a vote do.. Vote: (insert the complete vote here)")

        if message.content == "Senate Lead Claim " + str(senateleadernum2) and senateleadernum2 != 0:
            senatornum2 = "Lead Senator {}".format(message.author)
            senateleaders.add(message.author)
            persons = message.author
            await persons.send("Congrats Senate Leader. You can authorize votes now! To authorize a vote do.. Vote: (insert the complete vote here)")

        if message.content == "Senate Lead Claim " + str(senateleadernum3) and senateleadernum3 != 0:
            senatornum2 = "Lead Senator {}".format(message.author)
            senateleaders.add(message.author)
            persons = message.author
            await persons.send("Congrats Senate Leader. You can authorize votes now! To authorize a vote do.. Vote: (insert the complete vote here)")

        if message.content.startswith("Vote:") and message.author in senateleaders:
            msgg = message.content
            channel = client.get_channel(668145300120010762)
            await channel.send(msgg)
            
        if message.content == "Chancellor Run" and chancellornum == 2:
            msgg = message.author
            channel = client.get_channel(668145502554161162)
            await channel.send(msgg)

        if message.content == "Im a sucker" and message.author == popleoma:
            msgg = "Chancellor Elections are Open!"
            channel = client.get_channel(668145502554161162)
            chancellor.clear
            await channel.send(msgg)
            chancellornum = 2

        if message.content == "Chancellor Generate" and message.author == popleoma:
            chancellornum2 = random.randint(0, 100000000)
            await message.channel.send("Chancellor code is: {}".format(chancellornum2))
            chancellornum = 1

        if message.content == "Chancellor Claim " + str(chancellornum2) and chancellornum == 1:
            senatornum2 = "Chancellor {}".format(message.author)
            chancellor.add(message.author)
            persons = message.author
            await persons.send("As Chancellor you can Appoint Senator Leads with 'Appoint Senator Leaders'. You also announce the results of votes. But the Senate also has a possibility to impeach you.. ")
            chancellornum = 0
            msgg = "Congrats to Chancellor {}!".format(message.author)
            channel = client.get_channel(668145502554161162)
            await channel.send(msgg)

        if message.content == "Palpatine Invite":
            await message.channel.send("https://discordapp.com/api/oauth2/authorize?client_id=665667402331062313&permissions=8&scope=bot")




        if message.content == "Senator Generate":
            senatornum1 = random.randint(0, 10000)
            if senatornum1 in senatorsetnums:
                senatornum1 = random.randint(0, 10000)
            if senatornum1 in senatorsetnums:
                senatornum1 = random.randint(0, 10000)
            await message.channel.send("Your Senate Code.. {}".format(senatornum1))

        if message.content == "Senator Claim " + str(senatornum1) and message.author in senatorauthors:
            await message.channel.send("Good Try Senator")

        if message.content == "Senator Claim " + str(senatornum1) and senatornum1 not in senatorsetnums:
            senatornum2 = "Senator {}, {}".format(message.author, senatornum1)
            senatorset.add(senatornum2)
            senatorsetnums.add(senatornum1)
            senatorauthors.add(message.author)
            persons = message.author
            await message.channel.send("Senator {}, {}; Welcome to the Republic.".format(message.author, senatornum1))
            await persons.send("Congrats Senator, Feel free to join https://discord.gg/hyZvwTG! Here we will have server votes, events, and more!")
          #  pickle.dump(senatorset, open(r"C:\Users\pople\Desktop\Python Bots\Palpatine\sennum1.pkl", "wb"))
       #     pickle.dump(senatorsetnums, open(r"C:\Users\pople\Desktop\Python Bots\Palpatine\sensetnums.pkl", "wb"))
        #    pickle.dump(senatorauthors, open(r"C:\Users\pople\Desktop\Python Bots\Palpatine\senauthors.pkl", "wb"))
            
        if message.content == "Senators":
            await message.channel.send("{}".format(senatorset))
            
        if message.content == "Palpatine Decree":
            macousins = random.choice(["Ruby", "Cara", "Anna", "Allie", "Pop2", "Elijah"])
            noun = random.choice(["man", "woman", "dog", "store", "kid", "dog", "cat", "cabinet", "waffle", "car", "llama", "chair", "pie", "Jedi", "Empire", "Republic", "Sith", "baby", "child", "goat","cow","chicken"])
            noun2 = random.choice(["man", "woman", "dog", "store", "kid", "dog", "cat", "alien", "fried chicken", "children", "rock", "pie", "Jedi", "Republic", "Sith", "Empire","baby","bucket","car","fly","beetle","worm"])
            verb = random.choice(["went", "ran", "swims", "talks", "sits", "cries", "slaps", "kicks", "punch", "drops", "stops", "grows","poots","kills","sighs","stabs","dances","shakes"])
            verb2 = random.choice(["went", "ran", "swims", "talked", "sits", "cries", "slaps", "kicks", "punch", "drops", "smells", "grows", "gags", "screams"])
            adjective = random.choice(["fun", "happy", "scary", "pretty", "fat", "tall", "weird", "red", "tired", "smelly", "dangerous", "funny", "creepy","young","small","giant","tall"])
            adjective2 = random.choice(["fun", "happy", "scary", "pretty", "fat", "tall", "weird", "dead", "dirty", "sad", "fast", "slow"])
            article = random.choice(["the", "a", "some"])
            article2 = random.choice(["the", "a", "some"])
            preposition = random.choice(["to", "under", "over", "through", "around", "at"])
            conjunction = random.choice(["and"])
            adverb = random.choice(["happily", "gloomily", "sadly", "stupidly", "weirdly", "strangly", "slowly", "quickly", "scaredly", "meanly"])
            adverb2 = random.choice(["happily", "gloomily", "sadly", "stupidly", "weirdly", "strangly", "slowly", "quickly", "forcefully", "worridly"])
            space = " "
            sentenceoftheday = random.choice([article + space + noun + space + adverb + space + verb + space + preposition + space + article + space + adjective + space + noun2, article + space + adjective + space + adjective2 + space + noun + space + adverb + space + verb + space + conjunction + space + adverb2 + space + verb2 + space + preposition + space + article2 + space + noun2, noun2 + space + adverb + space + verb + space + preposition + space + article + space + adjective + space + noun, noun + space + adverb + space + verb + space + preposition + space + adjective2 + space + noun2])
            await message.channel.send(sentenceoftheday)

        if message.content == "Fam Fun" or message.content == "famfun":
            macousins = random.choice(["Ruby", "Cara", "Anna", "Allie", "Pop2", "Elijah", "Titus", "Luke", "Kallie"])
            macousins2 = random.choice(["Ruby", "Cara", "Anna", "Allie", "Pop2", "Elijah", "Titus", "Luke", "Kallie"])
            noun = random.choice(["man", "woman", "dog", "store", "kid", "dog", "cat", "cabinet", "waffle", "car", "llama", "chair", "pie", "baby", "child", "goat","cow","chicken"])
            noun2 = random.choice(["man", "woman", "dog", "store", "kid", "dog", "cat", "alien", "fried chicken", "children", "rock", "pie", "baby","bucket","car","fly","beetle","worm"])
            verb = random.choice(["went", "ran", "swims", "talks", "sits", "cries", "slaps", "kicks", "punch", "drops", "stops", "grows","poots","kills","sighs","stabs","dances","shakes"])
            verb2 = random.choice(["went", "ran", "swims", "talked", "sits", "cries", "slaps", "kicks", "punch", "drops", "smells", "grows", "gags", "screams"])
            adjective = random.choice(["fun", "happy", "scary", "pretty", "fat", "tall", "weird", "red", "tired", "smelly", "dangerous", "funny", "creepy","young","small","giant","tall"])
            adjective2 = random.choice(["fun", "happy", "scary", "pretty", "fat", "tall", "weird", "dead", "dirty", "sad", "fast", "slow"])
            article = random.choice(["the", "a", "some"])
            article2 = random.choice(["the", "a", "some"])
            preposition = random.choice(["to", "under", "over", "through", "around", "at"])
            conjunction = random.choice(["and"])
            adverb = random.choice(["happily", "gloomily", "sadly", "stupidly", "weirdly", "strangly", "slowly", "quickly", "scaredly", "meanly"])
            adverb2 = random.choice(["happily", "gloomily", "sadly", "stupidly", "weirdly", "strangly", "slowly", "quickly", "forcefully", "worridly"])
            space = " "
            sentenceoftheday = random.choice([article + space + macousins + space + adverb + space + verb + space + space + article + space + adjective + space + noun2, article + space + adjective + space + adjective2 + space + macousins + space + adverb + space + verb + space + conjunction + space + adverb2 + space + verb2 + space + space + article2 + space + noun2, macousins + space + adverb + space + verb + space + space + article + space + adjective + space + noun, noun + space + adverb + space + verb + space + preposition + space + adjective2 + space + macousins])
            sentenceoftheday2 = random.choice([macousins + space + verb +space+ preposition+ space +macousins2, article + space +adjective+ space + noun + space + adverb +space+ verb +space+ macousins, article+ space +adjective + space + macousins +space +adverb + space + verb+ space +macousins2, adjective+ space +noun+ space +adverb+ space +verb+ space +macousins,article+ space + adjective+ space +macousins+ space +adverb+ space +verb+ space +adjective+ space +macousins2,macousins+ space +verb+ space +noun,macousins+ space +verb+ space +macousins2, macousins+ space +verb+ space +adjective])
            sentenceoftheday3= random.choice([sentenceoftheday, sentenceoftheday2])
            await message.channel.send(sentenceoftheday3)
            
        if message.content.startswith(".") and message.author == popleoma:
            msgg = message.content
            channel = client.get_channel(366289483592630272)
            await channel.send(msgg)

        if message.content.startswith("News:") and message.author == popleoma:
            msgg = message.content
            channel = client.get_channel(668173203411042336)
            await channel.send(msgg)

        if message.content == "I am Popleoma the Great!":
            popleoma = message.author

    #    if message.content == "hmmmmm":
     #       role = 668142019352199188
      #      await message.author.add_roles(role)

        if message.content == "Yoda":
            gifss = random.choice(["https://i.imgur.com/1ieDc7A.gif","https://media3.giphy.com/media/3ohuAxV0DfcLTxVh6w/giphy.gif", "https://media1.giphy.com/media/ArrVyXcjSzzxe/giphy.gif", "https://media2.giphy.com/media/GnNtz3c1Ni8Ba/giphy.gif", "https://media.giphy.com/media/l1KufYZKGTPq89cQ0/giphy.gif", "https://www.unibetcommunity.com/t5/image/serverpage/image-id/37941iCA17C10E2C6060DD/image-size/large/is-moderation-mode/true?v=1.0&px=999", "https://media2.giphy.com/media/nZGIDIHQtimBO/source.gif", "https://media2.giphy.com/media/HvqvsVQAbJ4M8/source.gif"])
            await message.channel.send(gifss)

       # if message.content == 'Emperor Palpatine' and character == 1:
        #    pfp_path =r'C:\Users\pople\Desktop\Python Bots\Bot pfp\emperorpalpatine.jpg'
         #   fp = open(pfp_path, 'rb')
          #  pfp = fp.read()
        #    name = "Emperor Palpatine"
         #   gifss = random.choice(["https://media.giphy.com/media/ePL05nRDzwCXe/giphy.gif", "https://media.giphy.com/media/9g8PH1MbwTy4o/giphy.gif", "https://media.giphy.com/media/C89ePJHZWq6FmvGAsj/giphy.gif", "https://media.giphy.com/media/B6Jr28VwfxUFa/giphy.gif", "https://tenor.com/view/emperor-palpatine-luke-skywalker-shock-gif-13110792", "https://media.giphy.com/media/4gxOxfuL0QHQY/giphy.gif", "https://media.giphy.com/media/xTiIzBS80Jx9nMwmME/giphy.gif", "https://media.giphy.com/media/SJb0vHduIW8wM/giphy.gif", "https://media.giphy.com/media/mxJAwFqouAqo8/giphy.gif"])
          #  await client.user.edit(avatar=pfp)
           # await message.guild.me.edit(nick=name)
            #await message.channel.send(gifss)
          #  character = 0
    #    if message.content == 'Chancellor Palpatine' and character == 1:
    #        pfp_path =r'C:\Users\pople\Desktop\Python Bots\Bot pfp\palpatine.jpg'
     #       fp = open(pfp_path, 'rb')
      #      pfp = fp.read()
       #     name = "Chancellor Palpatine"
        #    gifss = random.choice(["https://media.giphy.com/media/qf4zM1Ne6ZTji/giphy.gif", "https://media.giphy.com/media/oZWhOWcEQh84M/giphy.gif", "https://media.giphy.com/media/l0HlRqd6Quh2HiXks/giphy.gif", "https://media.giphy.com/media/3o84sDfCF4mZR7aFYk/giphy.gif", "https://media.giphy.com/media/xTiIzIhgJ6ZrY3cZeo/giphy.gif", "https://media.giphy.com/media/3o84sIQ7S5BLsvETIc/giphy.gif", "https://media.giphy.com/media/kJWYrH269RK8M/giphy.gif", "https://tenor.com/view/threatning-jedi-palpatine-chancellor-gif-14403782", "https://tenor.com/view/sheev-palpatine-emperor-chancellor-kill-him-now-gif-14424446", "https://tenor.com/view/star-wars-palpatine-senate-gif-13095904", "https://tenor.com/view/palpatine-treason-star-wars-emperor-gif-8547403", "https://tenor.com/view/plan-b-star-wars-palpatine-obiwan-anakin-gif-10785572"])
         #   await client.user.edit(avatar=pfp)
          #  await message.guild.me.edit(nick=name)
           # await message.channel.send(gifss)
            #character = 0

        #if message.content == 'Grand Master Yoda' and character == 1:
    #        pfp_path =r'C:\Users\pople\Desktop\Python Bots\Bot pfp\yoda.jpg'
     #       fp = open(pfp_path, 'rb')
      #      pfp = fp.read()
       #     name = "Grand Master Yoda"
        #    gifss = random.choice(["https://media3.giphy.com/media/3ohuAxV0DfcLTxVh6w/giphy.gif", "https://media1.giphy.com/media/ArrVyXcjSzzxe/giphy.gif", "https://media2.giphy.com/media/GnNtz3c1Ni8Ba/giphy.gif", "https://media.giphy.com/media/l1KufYZKGTPq89cQ0/giphy.gif", "https://www.unibetcommunity.com/t5/image/serverpage/image-id/37941iCA17C10E2C6060DD/image-size/large/is-moderation-mode/true?v=1.0&px=999", "https://media2.giphy.com/media/nZGIDIHQtimBO/source.gif", "https://media2.giphy.com/media/HvqvsVQAbJ4M8/source.gif"])
         #   await client.user.edit(avatar=pfp)
          #  await message.guild.me.edit(nick=name)
           # await message.channel.send(gifss)
            #character = 0

       # if message.content == 'Resetteroni!' and reset == 0:
    #        pfp_path =r'C:\Users\pople\Desktop\Python Bots\Bot pfp\palpatine.jpg'
     #       fp = open(pfp_path, 'rb')
      #      pfp = fp.read()
       #     name = "Chancellor Palpatine"
        #    await client.user.edit(avatar=pfp)
       #  3   await client.user.edit(nick=name)
          #  reset = 1
        if message.content == 'Gimme the nums':
            await message.channel.send('typing timer-ish:{}, name:{}, character num:{}, reactionnums:{}'.format(typingtimer, name, character, reactionnums))
            
 #       if character == 1 and reactionnums == 0:
 #           await message.add_reaction(emoji="👍")
  #          reactionnums = 1

    
  #  async def on_typing(self, channel, date, user):
  #      global typingtimer
   #     global character
    #    global reactionnums
     #   if typingtimer == 2:
      #      await asyncio.sleep(1800)
       #     typingtimer = 1
        #    character = 1
         #   reactionnums = 0
       # else:
            #await channel.send('I know your every move... A message is being sent.. Soon.')
       #     typingtimer = 2

#
#
#

#git commit -am "tt"
#git add .
#git push heroku master
client = MyClient()
client.run('')
