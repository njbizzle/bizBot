import discord

from reaction_role import ReactionRole

intents = discord.Intents.default()
intents.message_content = True


class Bot(discord.Client):
    def __init__(self, intents: discord.Intents):
        super().__init__(intents=intents)

        self.reaction_roles = [

        ]

    async def on_ready(self):
        print(f'We have logged in as {self.user}')


    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("yo"):
            await message.channel.send("hi")

    async def on_message_delete(self, message: discord.Message):
        await message.channel.send(
            f"\"{message.content}\" - {message.author.name}"
        )

    async def on_reaction_add(self, reaction: discord.Reaction, user: discord.User):
        if type(reaction.emoji) == discord.PartialEmoji or type(reaction.emoji) == discord.Emoji:
            reaction = reaction.name
        print(reaction.emoji)
        for reaction_role in self.reaction_roles:
            if reaction_role.message != reaction.message:
                continue
            if reaction_role.reaction != reaction:
                continue

            print("reacted")


def start_bot(token: str):
    Bot(intents=intents).run(token)
