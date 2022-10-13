##################################################
## Software for the AttendenceBot in the MSU Solar
## Racing Team discord server
##
## Author: Vetri Vijay
## Credits: Allen Zhao and Valabh Korivi
## Email: vetivijay2002@gmail.com
##################################################

import os
from datetime import datetime

import discord
from dotenv import load_dotenv
import pytz
import pandas as pd

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CODE = os.environ.get('DISCORD_CODE')
CONFIGCODE = os.environ.get('DISCORD_CONFIGCODE')
FILE = os.environ.get('DISCORD_FILE')
CONFIGFILE = os.environ.get('DISCORD_CONFIGFILE')

client = discord.Client(intents=discord.Intents.default())

def add_name(df,name):
  if name not in df["name"].tolist():
    df.loc[len(df)] = [name] + [0 for _ in range(df.shape[1]-1)]
  return df["name"].tolist().index(name)

def add_date(df,date):
  if date not in df.columns:
    df[date] = [0 for _ in range(len(df['name']))]

def enter_attendance(df,name,date):
  a = add_name(df=df,name=name)
  add_date(df=df,date=date)
  df.at[a,date] = 1

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
      tz_city = pytz.timezone('America/Detroit')
      d1 = datetime.now(tz_city).strftime("%m,%d,%Y")
      try:
        df = pd.read_csv('attendencesheet.csv')
      except:
        df = pd.DataFrame()
        df['name'] = []
      enter_attendance(df=df,name=name,date=d1)
      df.to_csv('attendencesheet.csv',index=False)
      await message.channel.send(f"{name}'s attendence was recorded\n")
        
  elif command == CONFIGCODE:
    print()
    CODE = name
    await message.channel.send(f"Code Updated\n")
    
  else:
    await message.channel.send(f"Incorrect Code Entered\n")
  await message.delete()

client.run(TOKEN)