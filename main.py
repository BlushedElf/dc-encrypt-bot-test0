# ChatGPT - 13/05/2026

import discord
from discord import app_commands
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")  # IMPORTANT: don't hardcode this
KEY = 3

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, key):
    return encrypt(text, -key)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="encrypt", description="Encrypt a message")
async def encrypt_cmd(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(f"🔒 {encrypt(message, KEY)}")

@bot.tree.command(name="decrypt", description="Decrypt a message")
async def decrypt_cmd(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(f"🔓 {decrypt(message, KEY)}")

bot.run(TOKEN)
