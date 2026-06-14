import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash-8b")


async def ai_command(message):
    words = message.content.split()
    prompt = " ".join(words[1:])
    try:
        response = model.generate_content(prompt)
        await message.channel.send(response.text)
    except Exception:
        await message.channel.send("AI is currently unavailable, try again later!")