import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix=(">>>"), self_bot=True)

@bot.event
async def on_ready():
    print("Logged in as %s#%s" % (bot.user.name, bot.user.discriminator))
    print("ID: " + str(bot.user.id))

bot.run(TOKEN, bot=False)
