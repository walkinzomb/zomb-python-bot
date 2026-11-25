
import os
import discord
from discord import app_commands

class ZombPythonBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = ZombPythonBot()

@bot.event
async def on_ready():
    print(f"ZOMB Python online as {bot.user}")

@bot.tree.command(name="ping", description="Check bot response")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🐺 ZOMB Python is online!",
        ephemeral=True
    )

token = os.getenv("DISCORD_TOKEN")

if not token:
    raise RuntimeError("Missing DISCORD_TOKEN environment variable")

bot.run(token)
