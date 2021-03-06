from dotenv import load_dotenv
from discord.utils import get
import os
import random
from datetime import datetime
import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

ROLE = "member"

bot = commands.Bot(command_prefix="~")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TOKEN = os.getenv("TOKEN")
CHANNEL = os.getenv("CHANNEL")
channels = int(CHANNEL)
client = discord.Client()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="CLIENT_ID",
                                                           client_secret="CLIENT_SECRET"))

@bot.command()
async def test(message, *, text):
  await message.channel.send(f"You text, sir:\n{text}")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("Helping in Great People")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_member_join(member: discord.Member, ctx):
    channel = client.get_channel(channels)
    await channel.send(f'Welcome to my server **{member.name}** you have now become one of the great people of discord.')
    await member.create_dm()
    await member.dm_channel.send(
        f"""Welcome **{member.name}** to the 9D server. It is the server for the Grade 9 Vibgyor High and here are the rules:
The random messages will be sent in #time-pass-chatting-😀.
Songs will be played in the #💿-muscic-and-bot-commands-👾.
The entire coding questions will be played in the coding section of the server
If you want to talk about doubts or show your ricing it will be in the linux section
Anything about minecraft in the minecraft section
And if you want to test your discord bot please in the #👾-bot-stuff-👾"""
)



@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('happy birthday'):
        response = "happy birthday!"
        await message.channel.send(response)
    
    elif str.lower(message.content) == "$send":
        response = ""
        while response != "$send":
            response = message.content
        await message.channel.send(response)

    elif str.lower(message.content) == '$help':
        e = discord.Embed()
        e.add_field(name = "Commands that you can execute", value = """here are the commands that you can type they are :
                    1) Whenever you wish someone happy birthday it will also respond happy birthday
                    2) Type $help to execute this command which will display the commands that you can execute
                    3) Type $time to show the current time and date
                    4) Type $toss to peform the a coin toss
                    5) Type $date to show current date
                    6) Type $tell me a joke or $tmj to get a random joke from the internet""" , inline = False)
        await message.channel.send(embed=e)

    elif str.lower(message.content) == '$toss':
        response = "Coin tossed"
        await message.channel.send(response)
        TossNum = random.randint(0, 1)
        if TossNum == 0:
            await message.channel.send("Heads")
        else :
            await message.channel.send("Tails")

    elif str.lower(message.content) == 'execute order 66':
        e = discord.Embed()
        e.set_image(url = "https://img.cinemablend.com/filter:scale/quill/e/d/3/d/3/0/ed3d3077e9a6da391dd23249345cba386a826399.jpg?mw=600")
        await message.channel.send(embed = e)

    elif str.lower(message.content) == '$time':
        time = "The current time is " + str(datetime.now().time())
        await message.channel.send(time)
    
    elif str.lower(message.content) == '$date':
        date = "Today's date is " + str(datetime.now().date())
        await message.channel.send(date)
    
    elif message.content.startswith('bye'):
        await message.channel.send('Bye see you soon')
   
    elif str.lower(message.content) == 'yeet':
        await message.channel.send('Yeet!')
    
    elif message.content == '$verify':
            member = message.author
            role = discord.utils.get(message.guild.roles, name = "member")
            await member.add_roles(role)
            await message.channel.send(f"{member.name} has been verified")



    elif str.lower(message.content) == '$tell me a joke image' or str.lower(message.content) == '$tmji':
        e = discord.Embed()
        RandomDate = random.randint(0, 10)
        if RandomDate == 0:
            e.set_image(url = "https://i.pinimg.com/originals/63/fa/0e/63fa0ed29577611ffe5afa43bc298708.jpg")
        elif RandomDate == 1:
            e.set_image(url = "https://i.pinimg.com/originals/f1/4e/9c/f14e9c95b60ec398978c73cdec45d682.jpg")
        elif RandomDate == 2:
            e.set_image(url = "https://i.pinimg.com/originals/16/46/49/1646496ee03b89f3764b2e06629e693d.jpg")
        elif RandomDate == 3:
            e.set_image(url = "https://i.pinimg.com/originals/e0/04/7e/e0047ee0793602795410723a654c8826.jpg")
        elif RandomDate == 4:
            e.set_image(url="https://www.jokescoff.com/wp-content/uploads/2017/12/Very-Funny-Jokes-for-Kids-in-English.jpg")
        elif RandomDate == 5:
            e.set_image(url = "https://i.pinimg.com/originals/13/ba/20/13ba20c03fef8b6df337916e17e51d94.jpg")
        elif RandomDate == 6:
            e.set_image(url = "https://i.pinimg.com/originals/58/d8/41/58d841c873cdb9afe199f7ad7bb6ceae.jpg")
        elif RandomDate == 7:
            e.set_image(url = "https://imgs.xkcd.com/comics/python.png")
        elif RandomDate == 8:
            e.set_image(url = "https://i.redd.it/tep9xw80lhs51.png")
        elif RandomDate == 9:
            e.set_image(url = "https://external-preview.redd.it/R1ycGzRU2BJfStiYgQ7vtTW_fVUZdxo2OKY-Od-t_kE.jpg?width=640&crop=smart&auto=webp&s=1ffa8c5eb7c44e2d8f416faaa7392d5a5782ae64")
        elif RandomDate == 10:
            e.set_image(url="https://preview.redd.it/kxeexaamhes51.jpg?width=640&crop=smart&auto=webp&s=6b17f0736f948628f1bd03d1bd6e49dbccc1da21")
        await message.channel.send(embed = e)
    
    elif message.content == '$send':
        await message.channel.send('Say the message!')
        msg = ""
        while msg == "" and msg == "$send":
            msg = message.content
        response = "**{.author}** says", msg
        res = str.format(response)
        await message.channel.send(res)

    elif message.content.startswith('$'):
       await message.channel.send("That command does not exist")
    
client.run(TOKEN)
