import os, random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv() # loads the .env file so it can now be accessed with os.getenv("var_name")

BOT_TOKEN = os.getenv("BOT_TOKEN")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


class BizBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()  # gives the bot total control over everything i think
        super().__init__(command_prefix='!', intents=intents)

    async def on_ready(self):
        print(f'{self.user.name} has connected.')
        await self.change_presence(activity=discord.Game("Hollow Knight: Silksong"))


def start_bot():
    biz_bot = BizBot()
    biz_bot.run(BOT_TOKEN)
