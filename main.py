# Developed by Vetri Vijay and tested By Allen Zhao and Valabh Korivi

import os
from datetime import datetime

import discord
from dotenv import load_dotenv
import pytz

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CODE = os.environ.get('DISCORD_CODE')
CONFIGCODE = os.environ.get('DISCORD_CONFIGCODE')
FILE = os.environ.get('DISCORD_FILE')
CONFIGFILE = os.environ.get('DISCORD_CONFIGFILE')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
  print("The bot is online")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  global CODE
  global FILE

  msg = message.content
  if '<' in msg:
    msg = msg[msg.find('>') + 1:]

  a = msg.split()

  try:
    name = ""
    f = True
    for elem in a:
      if elem != a[0]:
        if f:
          name += elem
          f = False
        else:
          name += (' ' + elem)
    command = a[0].lower()
    print(f"{command} {name}")
  except:
    await message.delete()
    return

  code = CODE.lower()

  if command == "help":
    await message.channel.send(f"---------------------------| Help |--------------------------\nCommand Usage: @SolarAttendance code name\nExample: @SolarAttendance password123 Vetri Vijay")
    
  elif command == code:
    # await message.channel.send("https://tenor.com/view/kitty-cat-sandwich-cats-sandwich-gif-26112528")
    if name == "":
      await message.channel.send(f"You forgot your name, add it after the code\n")
    else:
      await message.channel.send(f"{name}'s attendence was recorded\n")
      with open(FILE, 'a') as file_object:
        tz_city = pytz.timezone('America/Detroit')
        d1 = datetime.now(tz_city).strftime("%H,%M,%S,%m,%d,%Y")
        file_object.write(f"{name.lower()},{d1}\n")
        
  elif command == CONFIGCODE:
    print()
    CODE = name
    await message.channel.send(f"Code Updated\n")
    
  else:
    await message.channel.send(f"Incorrect Code Entered\n")
  await message.delete()

client.run(TOKEN)