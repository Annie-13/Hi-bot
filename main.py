import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()
"""
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#hello'):
        await message.channel.send('Hello!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#help'):
        await message.channel.send ('```** Hi there ! Its me Hi Bot. M Designed by a Stupid novice coder named Annie (Ananya xD) who hasn\'t even passed her 10th ..Howtf :/ \n Kek All I can do is nothing but this Auto Response T_T \n Type \n #help \n \n For Fun) **```')
"""

swear_words = ["stuff","lel"]
warns = ["you are warned lel", "warned"]

if "responding" not in db.keys():
  db["responding"] = True

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if db["responding"]:
    options = warns

    if any(word in msg for word in swear_words):
      await message.channel.send(random.choice(options))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
msg1 = message.content
a="amart"

if any(word in message for word in a):
  await message.channel.send('who said amart')



client.run(os.getenv('TOKEN'))
