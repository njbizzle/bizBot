import discord

from reaction_role import ReactionRole

intents = discord.Intents.default()
intents.message_content = True


class Bot(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

        self.reaction_roles = [

        ]

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("yo"):
            await message.channel.send("Hello!")

    async def on_message_delete(self, message: discord.Message):
        await message.channel.send(
            f"\"{message.content}\" - {message.author.name}"
        )

    async def on_reaction_add(self, message: discord.Message, reaction: discord.Reaction):
        for reaction_role in self.reaction_roles:
            print(reaction)
            if reaction_role.message != message:
                continue
            if reaction_role.reaction != reaction:
                continue

            print("reacted")


def start_bot(token: str):
    Bot(intents=intents).run(token)
