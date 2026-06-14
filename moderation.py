from datetime import timedelta


async def kick(message):
    if len(message.mentions) == 0:
        await message.channel.send("You have to mention a user like: !kick @user")
    else:
        member = message.mentions[0]
        try:
            await member.kick()
            await message.channel.send(f"{member.mention} has been kicked.")
        except Exception:
            await message.channel.send("An error occured while trying to kick the user.")


async def ban(message):
    if len(message.mentions) == 0:
        await message.channel.send("You have to mention a user like: !ban @user")
    else:
        member = message.mentions[0]
        try:
            await member.ban()
            await message.channel.send(f"{member.mention} has been banned.")
        except Exception:
            await message.channel.send("An error occured while trying to ban the user.")


async def timeout(message):
    words = message.content.split()
    if len(message.mentions) == 0:
        await message.channel.send("You have to mention a user to timeout like: !timeout @user 10")
    elif len(words) < 3:
        await message.channel.send("You have to write how much minutes to time out user like: !timeout @user 10")
    else:
        member = message.mentions[0]
        time = int(words[2])
        try:
            await member.timeout(timedelta(minutes=time))
            await message.channel.send(f"{member.mention} has been timed out for {time} minutes.")
        except Exception:
            await message.channel.send("An error occured while trying to timeout the user.")


async def untimeout(message):
    if len(message.mentions) == 0:
        await message.channel.send("You have to mention a user to remove timeout like: !untimeout @user")
    else:
        member = message.mentions[0]
        try:
            await member.timeout(None)
            await message.channel.send(f"Timeout removed from {member.mention}.")
        except Exception:
            await message.channel.send("An error occured while trying to remove timeout from the user.")


async def mute(message):
    if len(message.mentions) == 0:
        await message.channel.send("You have to mention a user to mute like: !mute @user")
    else:
        member = message.mentions[0]
        try:
            await member.edit(mute=True)
            await message.channel.send(f"{member.mention} has been muted.")
        except Exception:
            await message.channel.send("An error occured while trying to mute the user.")


async def unmute(message):
    if len(message.mentions) == 0:
        await message.channel.send("You have to mention a user to unmute like: !unmute @user")
    else:
        member = message.mentions[0]
        try:
            await member.edit(mute=False)
            await message.channel.send(f"{member.mention} has been unmuted.")
        except Exception:
            await message.channel.send("An error occured while trying to unmute the user.")


async def clear(message):
    words = message.content.split()
    if len(words) != 2:
        await message.channel.send("You have to write how many messages you want to delete like: !clear 10")
    else:
        amount = int(words[1])
        try:
            await message.channel.purge(limit=amount)
        except Exception:
            await message.channel.send("An error occured while trying to delete messages.")