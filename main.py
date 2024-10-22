import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

class JogaMaya(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = '$',
            intents = intents
        )

    async def on_ready(self):
        print(f'{bot.user} is online.')
        print(f'{format(bot.latency, ".2f")}ms')

    async def setup_hook(self):
        await bot.load_extension('cogs.general')
        await bot.tree.sync(guild = None)

bot = JogaMaya()
bot.run(os.getenv('BOT_TOKEN'))