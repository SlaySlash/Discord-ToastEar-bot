import discord
from datetime import timedelta


async def poll(message):
    words = message.content.split()
    if len(words) < 2:
        await message.channel.send("You have to ask a question in your poll.")
    else:
        question = " ".join(words[1:])
        new_poll = discord.Poll(question=question, duration=timedelta(hours=1))
        new_poll.add_answer(text="Yes")
        new_poll.add_answer(text="No")
        await message.channel.send(poll=new_poll)


async def poll_reactions(message):
    words = message.content.split()
    if len(words) < 2:
        await message.channel.send("You have to ask a question in your poll.")
    else:
        question = " ".join(words[1:])
        sent_message = await message.channel.send(question)
        await sent_message.add_reaction("👍")
        await sent_message.add_reaction("👎")