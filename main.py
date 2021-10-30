import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(self_bot=True)

@bot.event
async def on_ready():
    print("User is online")

bot.run(TOKEN, bot=False)
