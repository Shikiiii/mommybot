import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from storage import *

facepalm_gifs = [
    "https://cdn.discordapp.com/attachments/671404646459244616/672073885943857182/a.gif",
    "https://cdn.discordapp.com/attachments/671404646459244616/672074297845743620/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672074391068082197/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672075087976857600/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672075181925335061/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672075479016275979/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672075574214262784/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672075995288961034/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672076165007015944/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672076263556644883/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672076407345512459/a.gif"
]

@bot.command()
async def facepalm(ctx):
	gif = random.choice(facepalm_gifs)
	embed = discord.Embed(description="**{.author.display_name}** facepalms. <a:facepalm:691588917501100053>".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
	embed.set_image(url=gif)
	await ctx.send(embed=embed)
