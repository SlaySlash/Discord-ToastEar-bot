import discord
import yt_dlp

queue = []


async def join(message):
    channel = message.author.voice.channel
    if message.guild.voice_client is None:
        await channel.connect()


async def play(message):
    if message.author.voice is None:
        await message.channel.send("You need to be in a voice channel!")
        return

    ydl_opts = {'format': 'bestaudio'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        words = message.content.split()
        link = words[1]
        info = ydl.extract_info(link, download=False)
        audio_url = info['url']

    try:
        channel = message.author.voice.channel
        if message.guild.voice_client is None:
            await channel.connect()
        voice_client = message.guild.voice_client
        if voice_client.is_playing():
            queue.append(link)
            await message.channel.send("Added to queue but queue doesn't exist yet:3 !")
        else:
            voice_client.play(discord.FFmpegPCMAudio(audio_url))
            await message.channel.send(f"Now playing: {info['title']}")
    except Exception:
        await message.channel.send("An error occurred while trying to play the audio.")


async def stop(message):
    message.guild.voice_client.stop()


async def resume(message):
    message.guild.voice_client.resume()


async def pause(message):
    message.guild.voice_client.pause()


async def leave(message):
    await message.guild.voice_client.disconnect()