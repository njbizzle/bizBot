import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(
    intents=intents,
    status=discord.Status.dnd,
    activity=discord.CustomActivity(
        name="test",
        emoji=discord.PartialEmoji.from_str(":skull:")
    )
)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("yo"):
        await message.channel.send("Hello!")


def start_bot(token: str):
    client.run(token)
