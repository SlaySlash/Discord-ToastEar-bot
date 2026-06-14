import os
import requests


async def weather(message):
    words = message.content.split()
    if len(words) != 2:
        await message.channel.send("You have to write one city like !weather London not !weather London Moscow or just !weather")
    else:
        city = words[1]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={os.getenv('WEATHER_KEY')}&units=metric"
        response = requests.get(url)
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        w_city = data["name"]
        await message.channel.send(f"In the {w_city} is {description}. The temperature is {temp}°C and humidity is {humidity}%")