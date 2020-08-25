from dotenv import load_dotenv
import os
import random
from datetime import datetime
import discord

load_dotenv()

TOKEN = os.getenv("TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('happy birthday'):
        response = "happy birthday!"
        await message.channel.send(response)
    
    elif str.lower(message.content) == '$help':
        e = discord.Embed()
        e.add_field(name = "Commands that you can execute", value = """here are the commands that you can type they are :
                    1) Whenever you wish someone happy birthday it will also respond happy birthday
                    2) Type $help to execute this command which will display the commands that you can execute
                    3) Type $time to show the current time and date
                    4) Type $toss to peform the a coin toss
                    5) Type $date to show current date
                    6) Type $tell me a joke to get a random joke from the internet""" , inline = False)
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
    
    elif str.lower(message.content) == '$tell me a joke':
        e = discord.Embed()
        RandomDate = random.randint(0, 6)
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
        await message.channel.send(embed = e)

    elif message.content.startswith('$') and message.content != '$date' and message.content != '$time' and message.content != '$toss':
       await message.channel.send("That command does not exist")

client.run(TOKEN)
