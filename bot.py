import discord
from dotenv import load_dotenv
import os

load_dotenv()

import fun
import weather
import ai
import moderation
import music
import polls

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

HELP_TEXT = (
    "Here is a list of available commands:\n"
    "!hello - bot say hello,\n"
    "!jet - random gif with fighter jet,\n"
    "!funfact - random fun fact,\n"
    "!random [option1] [option2] - chooses one option,\n"
    "!roll [number] - rolls a random number between 1 and the given number,\n"
    "!quote - random quote,\n"
    "!weather [city] - current weather in the given city,\n"
    "!coinflip - flips a coin,\n"
    "!meme - random meme from reddit,\n"
    "!ai [prompt] - ask AI about anything you want,\n"
    "!join - bot joins your voice channel,\n"
    "!play [link] - bot plays music from youtube link,\n"
    "!stop - bot stops the music,\n"
    "!resume - bot resumes the music,\n"
    "!pause - bot pauses the music,\n"
    "!leave - bot leaves the voice channel,\n"
    "!kick [@user] - kicks the mentioned user,\n"
    "!ban [@user] - bans the mentioned user,\n"
    "!timeout [@user] [minutes] - timeouts the mentioned user,\n"
    "!untimeout [@user] - removes timeout,\n"
    "!mute [@user] - mutes the mentioned user,\n"
    "!unmute [@user] - unmutes the mentioned user,\n"
    "!clear [number] - deletes given number of messages,\n"
    "!poll [question] - creates a discord poll,\n"
    "!poll2 [question] - creates a reaction poll."
)


@client.event
async def on_ready():
    print(f"Bot działa! Zalogowano jako {client.user}")
    await tree.sync()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()

    
    if content == "!hello":
        await fun.hello(message)
    elif content == "!help":
        await message.channel.send(HELP_TEXT)
    elif content == "!jet":
        await fun.jet(message)

   
    if "67" in message.content:
        await fun.gif_67(message)
    elif content == "!funfact":
        await fun.funfact(message)
    elif message.content.startswith("!random"):
        await fun.random_choice(message)
    elif message.content.startswith("!roll"):
        await fun.roll(message)
    elif content == "!quote":
        await fun.quote(message)
    elif message.content.startswith("!weather"):
        await weather.weather(message)
    elif content == "!coinflip":
        await fun.coinflip(message)


    if "bread" in content:
        await fun.bread(message)
    elif content == "!meme":
        await fun.meme(message)
    elif message.content.startswith("!ai"):
        await ai.ai_command(message)
    elif content == "!join":
        await music.join(message)
    elif message.content.startswith("!play"):
        await music.play(message)
    elif content == "!stop":
        await music.stop(message)
    elif content == "!resume":
        await music.resume(message)
    elif content == "!pause":
        await music.pause(message)
    elif content == "!leave":
        await music.leave(message)
    elif message.content.startswith("!kick"):
        await moderation.kick(message)
    elif message.content.startswith("!ban"):
        await moderation.ban(message)
    elif message.content.startswith("!timeout"):
        await moderation.timeout(message)
    elif message.content.startswith("!untimeout"):
        await moderation.untimeout(message)
    elif message.content.startswith("!mute"):
        await moderation.mute(message)
    elif message.content.startswith("!unmute"):
        await moderation.unmute(message)
    elif message.content.startswith("!clear"):
        await moderation.clear(message)
    elif message.content.startswith("!poll2"):
        await polls.poll_reactions(message)
    elif message.content.startswith("!poll"):
        await polls.poll(message)


client.run(os.getenv("DISCORD_TOKEN"))