from bs4 import BeautifulSoup
import discord
import requests
import responses
import time
import asyncio
import responses
import random


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

   
    








def run_discord_bot():
    TOKEN = "MTExMDE4Nzg5NTY2NDQxNDcyMQ.GbnJBE.BZIMl3X4kzQ-SVM5BcRibqXPxqa51D0O5Q31dE"
    intents = discord.Intents.default()
    intents.message_content = True
    intents.voice_states = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        
        if "nigga" in message.content:
            await message.guild.kick(message.author)
            await message.channel.send(f"Goodbye {message.author.mention}.")
        
        
    

   
    client.run(TOKEN)