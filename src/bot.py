import discord

from reaction_role import ReactionRole

intents = discord.Intents.default()
intents.message_content = True


class Bot(discord.Client):
    def __init__(self, intents: discord.Intents):
        super().__init__(intents=intents)

        self.reaction_roles = []

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

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        reaction_id = payload.emoji.id if payload.emoji.id else payload.emoji.name
        message_id = payload.message_id

        for reaction_role in self.reaction_roles:
            if reaction_role.message_id != message_id:
                continue
            if reaction_role.reaction_id != reaction_id:
                continue

            await payload.member.remove_roles(
                self.get_guild(payload.guild_id).get_role(reaction_role.role_id)
            )
            continue

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        reaction_id = payload.emoji.id if payload.emoji.id else payload.emoji.name
        message_id = payload.message_id

        for reaction_role in self.reaction_roles:
            if reaction_role.message_id != message_id:
                continue
            if reaction_role.reaction_id != reaction_id:
                continue

            await payload.member.remove_roles(
                self.get_guild(payload.guild_id).get_role(reaction_role.role_id)
            )

            continue


def start_bot(token: str):
    Bot(intents=intents).run(token)
