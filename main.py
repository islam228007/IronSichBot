import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} успішно запущено на Render!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Понг! Затримка: {round(bot.latency * 1000)} мс')

# Запуск бота (токен беремо з змінної середовища на Render)
bot.run(os.getenv('b5ab57522ba924f359cdc6d812b58a08e15bcb6f543869e85f3fab379746fb12'))
