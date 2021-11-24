import random
import asyncio
import aiohttp
import discord


client = discord.Client()
game = discord.Game("with Animals")
msg = 0
animal = 0 #0 store, 1 cat, 2 dog, 3 parrot, 4 Iroh, 5 Katara
rannum = 0
messagecount = 0
event = 0
ranmsg = 0
parrotmsg = 0
verb = random.choice(['wear', 'comes', 'thinking', 'were', 'hate', 'die', 'sees', 'bring', 'standing', 'have', 'depends', 'come', 'pack', 'make', 'know', 'looking', 'cheer', 'am', 'cause', 'learned', 'despise', 'reading', 'need', 'want', 'feel', 'be', 'singing', 'dreaming', 'should', 'try', 'calling', 'load', 'taking', 'telling', 'drove', 'look', 'raining', 'going', 'has', 'go', 'guess', 'save', 'running', 'wait', 'follow', 'was', 'went', 'plays', 'think', 'belong', 'wears', 'looks', 'made', 'been', 'tell', 'find', 'say', 'are', 'hope', 'did', 'learns', 'had', 'start', 'built', 'believe', 'crunch', 'understands', 'talk', 'afraid', 'boarding', 'do', 'trying', 'live', 'adore', 'gone', 'speak', 'feeling', 'dislike', 'might', 'take', 'is', 'learning', 'see', 'gave', 'move', 'jumped', 'can', 'said', 'added', 'wake', 'will', 'love'])
noun = random.choice(['everyone', 'emma', 'dog', 'case', 'fortnite', 'dream', 'eye', 'desire', 'nestle', 'trek', 'harry', 'paparazzi', 'conjunction', 'gem', 'butterfly', 'meanie', 'story', 'lapidot', 'popleoma', 'cant', 'emergency', 'city', 'friends', 'taco', '<@302486645754560523>', 'kind', 'rock', 'cesi', 'doing', 'butterflies', 'tester', 'instagram', 'reaper', 'school', 'stevenuniverse', 'lover', 'time', 'fire', 'computer', 'beans', 'star', 'earth', 'exercise', 'habla', 'rain', 'salad', 'gypsum', 'nun', 'random', 'wine', 'ingles', 'tacos', 'word', 'test', 'alien', 'soup', 'sounds', 'thing', 'possesive', 'opinion', 'language', 'end', 'death', 'umbridge', 'noun', 'none', 'kevin', 'baby', 'schools', 'lettuce', 'google', 'peach', 'party', 'peribot', 'police', 'fan', 'preposition', 'forehead', 'ministry', 'update', 'soda', 'aliens', 'banana', 'professor', 'cara', 'potter', 'picture', 'luck', 'adjective', 'pronoun', 'youtube', 'cheese', 'english', 'people', 'others', 'mug', 'house', 'verb', 'us', 'words', 'won', 'cherry', 'question', 'day', 'summer', 'noum', 'god', 'chicken', 'bee', 'melon', 'clod', 'adverb', 'article', 'barbie'])
class MyClient(discord.Client):
    async def on_ready(self):
        global game
        print('We are open!', self.user)
        await client.change_presence(activity=game)
        async for guild in client.fetch_guilds(limit=150):
            print(guild.name)



    async def on_message(self, message):
        global msg
        msg = message.content.lower()
        global animal
        global rannum
        global messagecount
        global event
        global noun
        global ranmsg
        global parrotmsg
        global verb
# we do not want the bot to reply to itself
        if message.author == client.user:
            return
        if msg == "pet emma" and message.author.id == 333724648900657155:
            await message.channel.send("Emma be nice, not everyone has the same opinions, and attacking other people's opinions is not acceptable either! Remember, no one likes rude people!")
        if msg == "pet invite":
            await message.channel.send("https://discordapp.com/api/oauth2/authorize?client_id=712391206298189894&permissions=8&scope=bot")
        if msg == "pet help":
            await message.channel.send("To change animals do... Pet (Animal)! We currently have.. cats, dogs, Iroh, Katara, and parrots!")
        if msg == "uwu":
            await message.channel.send("uwu")
        if msg == "pet off":
            await message.channel.send("Turning Off")
            animal = 0
        if msg == "pet cat":
            await message.channel.send("Meow")
            animal = 1
            await message.guild.me.edit(nick="Cat")
            rannum = random.randint(5, 30)
        if (messagecount == rannum or msg == "cat") and animal == 1:
            noun = random.choice(['everyone', 'emma', 'dog', 'case', 'fortnite', 'dream', 'eye', 'desire', 'nestle', 'trek', 'harry', 'paparazzi', 'conjunction', 'gem', 'butterfly', 'meanie', 'story', 'lapidot', 'popleoma', 'cant', 'emergency', 'city', 'friends', 'taco', '<@302486645754560523>', 'kind', 'rock', 'cesi', 'doing', 'butterflies', 'tester', 'instagram', 'reaper', 'school', 'stevenuniverse', 'lover', 'time', 'fire', 'computer', 'beans', 'star', 'earth', 'exercise', 'habla', 'rain', 'salad', 'gypsum', 'nun', 'random', 'wine', 'ingles', 'tacos', 'word', 'test', 'alien', 'soup', 'sounds', 'thing', 'possesive', 'opinion', 'language', 'end', 'death', 'umbridge', 'noun', 'none', 'kevin', 'baby', 'schools', 'lettuce', 'google', 'peach', 'party', 'peribot', 'police', 'fan', 'preposition', 'forehead', 'ministry', 'update', 'soda', 'aliens', 'banana', 'professor', 'cara', 'potter', 'picture', 'luck', 'adjective', 'pronoun', 'youtube', 'cheese', 'english', 'people', 'others', 'mug', 'house', 'verb', 'us', 'words', 'won', 'cherry', 'question', 'day', 'summer', 'god', 'chicken', 'bee', 'melon', 'clod', 'article', 'barbie'])
            event = random.choice(["https://quotationsquotes.com/wp-content/uploads/2015/09/Top-15-Very-Funny-Cat-GIFs-most-funniest.gif","https://www.pbh2.com/wordpress/wp-content/uploads/2012/05/funniest-cat-gifs-cat-bully.gif","https://i.imgur.com/jKurtIs.gif","https://www.laughtard.com/wp-content/uploads/2019/08/CAT_GIF_Wiske_the_Kitten_fighting_her_own_reflection_in_the_mirror_cute_funny_crazy_large.gif","https://media.giphy.com/media/efHwZH4DeN9ss/giphy.gif","https://www.cutecatgifs.com/wp-content/uploads/2015/11/Funny-Cat-vacuum.gif","https://media.giphy.com/media/ND6xkVPaj8tHO/giphy.gif","https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif","https://media0.giphy.com/media/o0yFJqm2fmgGk/source.gif"])
            await message.channel.send(event)
            await message.channel.send("pushes a {} off the counter".format(noun))
            messagecount = 0
        if msg == "pet parrot":
            await message.channel.send("SQUAK")
            animal = 3
            await message.guild.me.edit(nick="Parrot")
            rannum = random.randint(5, 30)
            ranmsg = random.randint (0,10)
        if ranmsg == messagecount:
            parrotmsg = message.content
        if (rannum == messagecount or msg == "parrot")and animal == 3 :
            event = random.choice(["https://4.bp.blogspot.com/-UANBKxED0Ww/UWLQymAKHQI/AAAAAAAABq4/4eMTJSqV3-g/s1600/Funny-parrot.gif","https://i.pinimg.com/originals/c8/25/c4/c825c44eb29b95413da0f6fd9592ba2d.gif","https://31.media.tumblr.com/18c4ca4550f04a35c0938b89172326e3/tumblr_n5d9f36uV21smhnavo2_400.gif","https://media.giphy.com/media/RJzxfUAEcfFp6/giphy.gif","https://mytebox.com/gif/when-your-friend-is-angry-on-you-funny-parrots-gif.gif","https://i.pinimg.com/originals/71/d7/f8/71d7f8e22940a1b780341d3abddc15eb.gif","https://i.imgur.com/TKRqcUb.gif","https://media.giphy.com/media/6V5h8ucx8q1mo/giphy.gif","https://i.pinimg.com/originals/5b/c8/85/5bc885fbe0f420b4bae1956170ccb758.gif","https://i.pinimg.com/originals/4e/5a/1c/4e5a1ce135ad0735bb1a1bb3ff83d088.gif"])
            await message.channel.send(event)
            await message.channel.send("**Squak** {}".format(parrotmsg))
            messagecount = 0
        if msg == "pet dog":
            await message.channel.send("Bork BOOF BarK")
            animal = 2
            await message.guild.me.edit(nick="Dog")
            rannum = random.randint(5, 30)
        if (rannum == messagecount or msg == "dog")and animal == 2:
            event = random.choice(["https://i.kinja-img.com/gawker-media/image/upload/s--omBQ1AB7--/t_ku-xlarge2/18d43yey83yudgif.gif","https://i.imgur.com/y56ZjXP.gif","https://media.giphy.com/media/Pk20jMIe44bHa/giphy-downsized-medium.gif", "https://i.imgur.com/QEd4cL0.gif", "https://media.giphy.com/media/bswGDO7Rh1ONO/giphy.gif", "https://www.liveabout.com/thmb/riMZsZrsm5LFV29pY4Uqk4HpWKY=/640x640/filters:no_upscale():max_bytes(150000):strip_icc()/stoned-dog-5afaefe70e23d90037d0165e.gif", "https://media3.giphy.com/media/PWP86D0d8kLTO/giphy.gif", "https://assets.memedrop.io/memes/jyryDzw6UW5DozS1yIeD2mjbn1OTqKDLl0MMfjQr.gif"])
            await message.channel.send(event)
            messagecount = 0
        if msg == "vibe check":
            await message.channel.send("Looks like someone needs their vibe checked.. https://media0.giphy.com/media/kyR2VCeATWZ4VCc5Cd/source.gif")

        if msg == "pet iroh":
            await message.channel.send("It's a long long way to Ba Sing Se but the girls in the city they look so pretty!")
            animal = 4
            await message.guild.me.edit(nick="Iroh")
            rannum = random.randint(5, 30)
        if (rannum == messagecount or msg == "iroh")and animal == 4:
            noun = random.choice(["Life happens wherever you are, whether you make it or not.","Pride is not the opposite of shame, but its source.","Sometimes life is like this tunnel. You can’t always see the light at the end of the tunnel, but if you keep moving, you will come to a better place.","You sound like my nephew, always thinking you need to do things on your own without anyone’s support. There is nothing wrong with letting the people who love you help you."," You are not the man you used to be. You are stronger and wiser and freer than you ever used to be. And now you have come at the crossroads of the destiny. Its time for you to choose. Its time for you to choose good.", "You’re looking at the rare white dragon bush. Its leaves make a tea so delicious it’s *heartbreaking!* That, or it’s the white jade bush, which is poisonous.","You have light and peace inside of you. If you let it out, you can change the world around you"])
            event = random.choice(["https://media2.giphy.com/media/ZvJ0bHvAy1N9S/giphy.gif", "https://media.tenor.com/images/67b930c572d96cc219a938be664aabd2/tenor.gif", "https://i.imgur.com/KkFbkKG.gif?noredirect", "https://i.imgur.com/8W9QwyZ.gif", "https://thumbs.gfycat.com/OrangeIgnorantKrill-max-1mb.gif", "https://i.gifer.com/JBQH.gif", "https://media.giphy.com/media/KgUBgEGK2NuSs/giphy.gif", "https://media1.tenor.com/images/110180252120032d8d109ce939ba873c/tenor.gif?itemid=5975668", "https://data.whicdn.com/images/37514119/original.gif", "https://comicvine1.cbsistatic.com/uploads/original/11118/111183530/5273591-animation%20%2881%29.gif","https://qph.fs.quoracdn.net/main-qimg-08d07d8cf75170f3ce36973d75fb0b99","https://grapeshotmq.com.au/wp-content/uploads/2015/03/tumblr_md1c0hnZYA1rulmmfo2_r1_250.gif","https://img.fireden.net/co/image/1536/69/1536699816263.gif"])
            await message.channel.send(event)
            await message.channel.send(noun)
            messagecount = 0

        if msg == "pet katara":
            await message.channel.send("splishy splash :D")
            animal = 5
            await message.guild.me.edit(nick="Katara")
            rannum = random.randint(5, 30)
        if (rannum == messagecount or msg == "katara")and animal == 5:
            verb = random.choice(['wear', 'comes', 'thinking', 'were', 'hate', 'die', 'sees', 'bring', 'standing', 'have', 'depends', 'come', 'pack', 'make', 'know', 'looking', 'cheer', 'am', 'cause', 'learned', 'despise', 'reading', 'need', 'want', 'feel', 'be', 'singing', 'dreaming', 'should', 'try', 'calling', 'load', 'taking', 'telling', 'drove', 'look', 'raining', 'going', 'has', 'go', 'guess', 'save', 'running', 'wait', 'follow', 'was', 'went', 'plays', 'think', 'belong', 'wears', 'looks', 'made', 'been', 'tell', 'find', 'say', 'are', 'hope', 'did', 'learns', 'had', 'start', 'built', 'believe', 'crunch', 'understands', 'talk', 'afraid', 'boarding', 'do', 'trying', 'live', 'adore', 'gone', 'speak', 'feeling', 'dislike', 'might', 'take', 'is', 'learning', 'see', 'gave', 'move', 'jumped', 'can', 'said', 'added', 'wake', 'will', 'love'])
            event = random.choice(["https://media0.giphy.com/media/hIWJ5h3IOmGty/source.gif","https://i.makeagif.com/media/11-27-2015/_TPiRO.gif","https://media.giphy.com/media/i4WFK65oICs36/giphy.gif","https://i.gifer.com/AoKP.gif","https://media.giphy.com/media/5FipnlUgq6ICI/giphy.gif","https://66.media.tumblr.com/79344d0a5b78591132fc7136c106aca2/ea7f655eb0be9dca-14/s400x600/106d954fee5de138419021b6446c510348de92f0.gifv","https://animatedmeta.files.wordpress.com/2015/04/atla-katara-will-never-turn-her-back-on-people-who-need-her.gif","https://25.media.tumblr.com/tumblr_m8brt7NNtm1rss05ao1_500.gif","https://thumbs.gfycat.com/DecimalHeavenlyBergerpicard-size_restricted.gif","https://comicvine1.cbsistatic.com/uploads/original/11129/111292893/5639004-giphy%20%281%29.gif"])
            await message.channel.send(event)
            await message.channel.send("My mother used to {} :cry:".format(verb))
            messagecount = 0

        else:
            messagecount += 1
client = MyClient()
client.run("")
