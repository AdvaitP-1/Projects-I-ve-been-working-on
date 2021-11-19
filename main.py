import discord
from discord.ext import commands
import music

cogs= [music]

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())

for i in range(len(cogs)):
	cogs[i].setup(client)


client.run("OTA4NzQzNTIwNDQ0MDg4MzUx.YY6LWg.vBU3nE5mIIZxgZx6-rjfw85GjLA")
