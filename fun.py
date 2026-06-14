import random
import requests
import os

hello_messages = ["Howdy!", "Hello!", "Ahoj!", "What's poppin!", "What's crackin'!", "Wazzup!", "Hey!", "Yahoo!"]
coin = ["Head", "Tail"]


async def hello(message):
    await message.channel.send(random.choice(hello_messages))


async def coinflip(message):
    await message.channel.send(random.choice(coin))


async def jet(message):
    url = f"https://api.giphy.com/v1/gifs/random?api_key={os.getenv('GIPHY_TOKEN')}&tag=fighter-plane&rating=g"
    response = requests.get(url)
    data = response.json()
    gif_url = data["data"]["images"]["original"]["url"]
    await message.channel.send(gif_url)


async def gif_67(message):
    url = f"https://api.giphy.com/v1/gifs/random?api_key={os.getenv('GIPHY_TOKEN')}&tag=67&rating=g"
    response = requests.get(url)
    data = response.json()
    gif_url = data["data"]["images"]["original"]["url"]
    await message.channel.send(gif_url)


async def funfact(message):
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
    response = requests.get(url)
    data = response.json()
    await message.channel.send(data["text"])


async def random_choice(message):
    words = message.content.split()
    options = words[1:]
    if len(options) < 2:
        await message.channel.send("You have to write at least 2 options for instance !random George John or !random red blue green")
    else:
        await message.channel.send(random.choice(options))


async def roll(message):
    words = message.content.split()
    if len(words) != 2:
        await message.channel.send("You have to write one number like !roll 20 not !roll 6 7 or just !roll")
    else:
        amount = int(words[1])
        await message.channel.send(f"Bravo! Your number is: {random.randint(1, amount)}")


async def quote(message):
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    data = response.json()
    await message.channel.send(f'"{data[0]["q"]}" - {data[0]["a"]}')


async def meme(message):
    url = "https://meme-api.com/gimme/blackhumor"
    response = requests.get(url)
    data = response.json()
    await message.channel.send(data["url"])


async def bread(message):
    await message.channel.send("I am a bread!")