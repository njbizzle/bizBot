import discord, os, load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__))
ENV_PATH = str(APP_ROOT.split("src", 1)[0]) + ".env"

load_dotenv.load_dotenv(ENV_PATH)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("BOT_TOKEN"))
