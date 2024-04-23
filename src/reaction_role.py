import discord


class ReactionRole():
    def __init__(self,
        client: discord.Client,
        guild_id: int,
        reaction_roles: dict,
        message_id: int,
        channel: discord.TextChannel=None
    ):
        self.client = client
        self.guild_id = guild_id
        self.reaction_roles = reaction_roles

        self.message_id = message_id
        self.channel = channel

    async def create_message(self):
        if not self.channel:
            return

        message = await self.channel.send(content=f"React To Add / Remove Roles: \n {
            "\n".join([f":{
                self.client.get_emoji(rr["reaction"]).name
            }: = {
                self.client.get_guild(self.guild_id).get_role(rr["role"]).name
            }" for rr in self.reaction_roles])
        }")

        self.message_id = message.id

    async def set_reactions(self):
        if not self.message_id:
            return

        for reaction_role in self.reaction_roles:
            reaction_id = reaction_role["reaction"]
            role_id = reaction_role["role"]
            await self.message.add_reaction(self.client.get_emoji(reaction_id));
