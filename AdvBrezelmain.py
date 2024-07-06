import tracemalloc
import discord
from discord.ext import commands, tasks
import asyncio
import os
from dotenv import load_dotenv
import random

tracemalloc.start()

# Load environment variables from .env file
load_dotenv()

# Create bot instances with specific intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.messages = True
intents.presences = True
intents.reactions = True


bot1 = commands.Bot(command_prefix='!', intents=intents)
bot2 = commands.Bot(command_prefix='?', intents=intents)

# Function to load all extensions (cogs) for both bots from the 'cogs' directory
async def load_extensions(bot1, bot2):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot1.load_extension(f'cogs.{filename[:-3]}')
            await bot2.load_extension(f'cogs.{filename[:-3]}')
   
        # Change status every 5 minutes

    
@bot1.event
async def on_ready():
    activity = discord.Game(name="Prefix: !", type=3)
    await bot1.change_presence(status=discord.Status.online, activity=activity)
    print(f'Bot 1 is online as {bot1.user}')
    await load_extensions(bot1, bot2)

    
         
        

# Define event for bot2 (without status update)
@bot2.event
async def on_ready():
    activity = discord.Game(name="Prefix: ?", type=3)
    await bot2.change_presence(status=discord.Status.online, activity=activity)
    print(f'Bot 2 is online as {bot2.user}')
    await load_extensions(bot1, bot2)

# Start both bots simultaneously
async def main():
    await asyncio.gather(
        bot1.start(os.getenv('DISCORD_TOKEN')),
        bot2.start(os.getenv('TOKEN'))
    )

# Start the main function
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is shutting down...')
        asyncio.run(bot1.close())
        asyncio.run(bot2.close())
        print('Bot successfully shut down.')
