import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from storage import *

hug_gifs = [
    "https://cdn.discordapp.com/attachments/671404646459244616/672068771254632478/a.gif",
    "https://cdn.discordapp.com/attachments/671404646459244616/672068829291085875/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672068948837269555/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672069209173262357/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672069432541052938/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672070035510001684/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672070333360242725/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672070387621691395/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672070449940791306/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672070521466257438/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672070582828924937/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672070783153209394/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672070845761585181/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672070902359261212/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672071318497394688/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672071890516312074/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672072002298707978/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672072270281179156/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672072340867252264/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672072525467090964/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672072623349563402/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672072691137904641/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672072830363631616/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672072915197493268/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672073033263087626/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672073183863767060/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672073255791624192/a.gif",
		"https://cdn.discordapp.com/attachments/671404646459244616/672073393826168842/a.gif"
    ]
    
@bot.command()
async def hug(ctx, user: discord.Member):
	embed = discord.Embed(description="**{.message.author.name}** hugs **{.name}**.".format(ctx, user), color=0xFFFFFF, timestamp=datetime.utcnow())
	embed.set_image(url=random.choice(hug_gifs))
	embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/667221349575688202.gif?v=1")
	embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
	await ctx.send(embed=embed)
	
@hug.error
async def hug_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="**Mommy** hugs **{.message.author.name}**.".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
		embed.set_image(url=random.choice(hug_gifs))
		embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/667221349575688202.gif?v=1")
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="**Mommy** hugs **{.message.author.name}**.".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
		embed.set_image(url=random.choice(hug_gifs))
		embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/667221349575688202.gif?v=1")
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send(f"**{ctx.message.author.name}** member not found, I hugged you instead.", embed=embed)
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="```{}```".format(error), color=0x000000)
		await ctx.send("An error has occured. Detailed information below:", embed=embed)
