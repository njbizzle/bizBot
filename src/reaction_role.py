import discord


class ReactionRole():
    def __init__(self,
        client: discord.Client,
        reaction_roles: dict,
        message: discord.Message=None,
        channel: discord.TextChannel=None
    ):
        self.client = client
        self.reaction_roles = reaction_roles

        self.message = message
        self.channel = channel

    async def create_message(self):
        if not self.channel:
            return

        self.message = await self.channel.send("test")

    async def set_reactions(self):
        if not self.message:
            return

        for reaction in self.reaction_roles.keys():
            await self.message.add_reaction(reaction)
