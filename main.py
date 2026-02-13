import discord
from discord.ext import commands
import os

# Увімкнення потрібних intents (обов'язково для читання повідомлень і членів)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Створюємо бота з префіксом '!'
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} успішно запущено!')
    print(f'Серверів: {len(bot.guilds)} | Користувачів: {len(bot.users)}')

@bot.command()
async def ping(ctx):
    """Проста тестова команда"""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Понг! Затримка: {latency} мс')

# Запуск бота — саме так, без додаткового asyncio.run()
# Токен беремо з змінної середовища (DISCORD_TOKEN на Railway)
bot.run(os.getenv('b5ab57522ba924f359cdc6d812b58a08e15bcb6f543869e85f3fab379746fb12'))
