import discord
import os
import requests
import json
import random
from replit import db

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


client = discord.Client()

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


swear_words = ["fuck", "motherfucker", "nigga", "bitch", "cock"]

warns = [
"u mf u don't swear in this server",
"swearing isnt allowed in dankers op",
"you will get warned if u swear again"
]

if "responding" not in db.keys():
  db["responding"] = True

def warn_update(warns):
  if "warns" in db.keys():
    warns = db["warns"]
    warns.append(warn)
    db["warns"] = warns
  else:
    db["warns"] = [warns]

def delete_encouragment(index):
  warns = db["warns"]
  if len(warns) > index:
    del warns[index]
  db["warns"] = warns

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if db["responding"]:
    options = warns

    if any(word in msg for word in swear_words):
      await message.channel.send(random.choice(options))



client.run(os.getenv('TOKEN'))
