import os
import asyncio
import discord
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv
import json
import re

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ACTIVITY1 = os.getenv('ACTIVITY1')
ACTIVITY2 = os.getenv('ACTIVITY2')
ACTIVITY3 = os.getenv('ACTIVITY3')
TEST = os.getenv('TEST')
bot = commands.Bot(command_prefix=(">>>"), self_bot=True)
client = discord.Client()

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    if config["activity"] == True:
      my_background_task.start()

    print("Logged in as %s#%s" % (bot.user.name, bot.user.discriminator))
    print("ID: " + str(bot.user.id))

if config["activity"] == True:
  @tasks.loop(seconds=40)
  async def my_background_task():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=(ACTIVITY1)))
    await asyncio.sleep(40)
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=(ACTIVITY2)))
    await asyncio.sleep(40)
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=(ACTIVITY3)))
else:
  print("Not using activity")

bot.run(TOKEN, bot=False)
