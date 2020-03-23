import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from cv import *

kiss_gifs = [
    "https://cdn.discordapp.com/attachments/671404646459244616/672064253225861120/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672064340609990656/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672064417709424670/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672064417709424670/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672064645972099092/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672064718990737428/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672064783452995615/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672065318067372040/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672065411872849930/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672065509176639535/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672065589488910376/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672065656501305355/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672065764739776512/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672065830212730890/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672065877717549066/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672065934793506907/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672066186296688640/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672066335559385088/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672066396124872724/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672066469814730762/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672066569005694976/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672066797284884480/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672067078756499457/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672067227146518539/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672067647793266708/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672067751678050324/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672067827150356480/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672067892984021002/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672067953495375872/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672068178171527188/a.gif"
    ]
    
@bot.command()
async def kiss(ctx, user: discord.Member):
	embed = discord.Embed(description="**{.message.author.name}** kisses **{.name}**. <:kiss_babi:681965003116773471>".format(ctx, user), color=0xFFFFFF, timestamp=datetime.utcnow())
	embed.set_image(url=random.choice(kiss_gifs))
	await ctx.send(embed=embed)
	
@kiss.error
async def kiss_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="**babi** kisses **{.message.author.name}**. <:kiss_babi:681965003116773471>".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
		embed.set_image(url=random.choice(kiss_gifs))
		await ctx.send(embed=embed)
	elif isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="**babi** kisses **{.message.author.name}**. <:kiss_babi:681965003116773471>".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
		embed.set_image(url=random.choice(kiss_gifs))
		await ctx.send(f"**{ctx.message.author.name}** member not found, I kissed you instead.", embed=embed)
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		await ctx.send("An error has occured. Detailed information below:", embed=embed)
