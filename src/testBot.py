import discord

intents = discord.Intents.default()
intents.message_content = True

class BizBot(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("yo"):
            await message.channel.send("Hello!")

    async def on_message_delete(self, message):
        await message.channel.send(
            f"\"{message.content}\" - {message.author.name}"
        )


def start_bot(token: str):
    BizBot().run(token)
