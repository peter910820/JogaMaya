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

    async def on_message(self, message):
        print(message.content)

    async def on_message_edit(self, before, after):
        user = before.author.global_name
        await before.channel.send(f'{user}剛剛更改了訊息:{before.content} => {after.content}')
        
    async def on_message_delete(self, message):
        user = message.author.global_name
        await message.channel.send(f'{user}剛剛刪除了訊息:{message.content}')

    async def setup_hook(self):
        await bot.load_extension('cogs.general')
        await bot.tree.sync(guild = None)

bot = JogaMaya()
bot.run(os.getenv('BOT_TOKEN'))