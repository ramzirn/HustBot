from bs4 import BeautifulSoup
import discord
import requests
import responses
import time
import asyncio
import responses
import random
from functions.chat import *


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

   
    








def run_discord_bot():
    with open("token.txt", "r") as filin:

     TOKEN=filin.read()

     
    
   
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
        
        
        if message.mentions and any(user.id == 1110187895664414721 for user in message.mentions):
            await message.channel.send(f"{message.author.mention}, {getanswer(message.content)}")
    

    @client.event
    async def on_ready():
                                print(f"Connecté en tant que {client.user.name} (ID: {client.user.id})")
                                print(f"hust actuellement dans {len(client.guilds)} serveurs.")


        
    

   
    client.run(TOKEN)