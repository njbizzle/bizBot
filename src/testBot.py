import discord, os, load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__))
ENV_PATH = str(APP_ROOT.split("src", 1)[0]) + ".env"

load_dotenv.load_dotenv(ENV_PATH)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


def start_bot(token: str):
    client.run(token)
