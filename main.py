import discord, os
from discord.ext import commands

# This bot made with discord.py 2.2.3 by Milyaket#9669
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# All cog folders comes here
cogs = ["Ticket_System", "Flag_Quiz"]

@bot.event
async def setup_hook():
    for cog in cogs:
        for file in os.listdir(cog):
            if file.endswith(".py"):
                await bot.load_extension(f"{cog}.{file[:-3]}")

    print(bot.user.name + " is online.")

# Run your bot
bot.run(token=os.getenv("TOKEN"))
