# bot.py
import os
import random

import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = ""

client = discord.Client()

bot = commands.Bot(command_prefix='!')

@client.event
async def on_member_join(member):
    await member.send()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!help':
        response = "..."
        await message.channel.send(response)
    
    if message.content == '!here':
        response = "ok i will do it here"
        await message.channel.send(response)
        channelID = message.channel.id

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = client.get_channel(689989416667709589)
    while not client.is_closed():
        counter += 1
        await channel.send("WASH YOUR HANDS")
        await asyncio.sleep(1800)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.loop.create_task(my_background_task())
client.run(TOKEN)