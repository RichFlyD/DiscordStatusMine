import discord
from discord.ext import commands, tasks
import requests
import time
import asyncio

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)






@bot.event
async def on_ready():
    print('Bot is ready')

    update_status.start()

@tasks.loop(seconds=10)
async def update_status():
    response = requests.get('https://minecraft-api.com/api/ping/online/ServerIp/ServerPort')

    if response.status_code == 200:
        data = response.text.strip()
        your_data = int(data)
        status = f'{your_data} Players'
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name="ServerIp"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Server Online🟢"))
        await asyncio.sleep(10)

bot.run('Token_BOT_Here')