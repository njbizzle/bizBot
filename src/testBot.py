import os, random

import discord
from discord.ext import commands
from dotenv import load_dotenv



class BizBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()  # gives the bot total control over everything i think
        super().__init__(command_prefix='!', intents=intents)

    async def on_ready(self):
        print(f'{self.user.name} has connected.')
        await self.change_presence(activity=discord.Game("test 1"))

    @commands.command(name="test")
    async def test(self, context: commands.Context, *args):
        await context.send("test")


def start_bot(BOT_TOKEN):
    biz_bot = BizBot()
    biz_bot.run(BOT_TOKEN)
