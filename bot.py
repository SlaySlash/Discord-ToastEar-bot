import discord
import requests
import random
from dotenv import load_dotenv
import os
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
hello = ["Howdy!", "Hello!", "Ahoj!", "What's poppin!", "What's crackin'!", "Wazzup!", "Hey!", "Yahoo!"]
coin = ["Head", "Tail"]

@client.event 
async def on_ready():
    print(f"Bot działa! Zalogowano jako {client.user}")
    await tree.sync()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if(message.content.lower() == "!hello"):
        await message.channel.send(random.choice(hello))
    elif(message.content.lower() == "!help"):
        await message.channel.send("Here is a list of available commands:\n!hello - bot say hello,\n!jet - radnom gif with fighter jet,\n!funfact - random fun fact,\n!random [option1] [option2] - chooses one option,\n!roll [number] - rolls a random number between 1 and the given number,\n!quote - random quote,\n !weather - current weather in the given city,\n!coinflip - flips a coin")
    elif(message.content.lower() == "!jet"):
        url = f"https://api.giphy.com/v1/gifs/random?api_key={os.getenv("GIPHY_TOKEN")}&tag=fighter-plane&rating=g"
        response = requests.get(url)
        data = response.json()
        gif_url = data["data"]["images"]["original"]["url"]
        await message.channel.send(gif_url)
    elif(message.content.lower() == "!funfact"):
        url = f"https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
        response = requests.get(url)
        data = response.json()
        funfact = data["text"]
        await message.channel.send(funfact)
    elif(message.content.startswith("!random")):
        words = message.content.split()
        options = words[1:]
        if len(options) < 2:
            await message.channel.send("You have to write at least 2 options for instance !random George John or !random red blue green")
        else:
            answer = random.choice(options)
            await message.channel.send(answer)
    elif(message.content.startswith("!roll")):
        words = message.content.split()
        if len(words) != 2:
            await message.channel.send("You have to write one number like !roll 20 not !roll 6 7 or just !roll")
        else:
            option = words[1]
            answer = random.randint(1, int(option))
            await message.channel.send(f"Bravo! Your number is: {answer}")
    elif(message.content.lower() == "!quote"):
        url = f"https://zenquotes.io/api/random"
        response = requests.get(url)
        data = response.json()
        quote = data[0]["q"]
        author = data[0]["a"]
        await message.channel.send(f'"{quote}" - {author}')
    elif(message.content.startswith("!weather")):
        words = message.content.split()
        if len(words) != 2:
            await message.channel.send("You have to write one city like !weather Warsaw not !weather Warsaw Krakow or just !weather")
        else:
            city = words[1]
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={os.getenv("WEATHER_KEY")}&units=metric"
            response = requests.get(url)
            data = response.json()
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            w_city = data["name"]
            await message.channel.send(f"In the {w_city} is {description}. The temperature is {temp}°C and humidity is {humidity}%")
    elif(message.content.lower() == "!coinflip"):
        choice = random.choice(coin)
        await message.channel.send(choice)
    
      
      
client.run(os.getenv("DISCORD_TOKEN")) 





