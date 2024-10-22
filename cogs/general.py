import discord

from discord import app_commands
from discord.ext import commands

class GeneralCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name= 'ping', description='ping bot return delay')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'{format(self.bot.latency, ".2f")}ms')


async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))