import discord
import subprocess
import asyncio
from config import username
from config import password
client = discord.Client()
@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print('--------------')
@client.event
async def on_message(msg):
    if msg.content == "!mine" and msg.author.id == client.user.id:
        while (1==1):
            await client.send_message(msg.channel, "!mine")
client.run(username,password)
