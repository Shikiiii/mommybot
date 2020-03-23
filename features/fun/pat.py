import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from cv import *

pat_gifs = [
    "https://cdn.discordapp.com/attachments/670153232039018516/674299983117156362/1edd1db645f55aa7f2923838b5afabfc863fc109_hq.gif",
    "https://cdn.discordapp.com/attachments/670153232039018516/674299989152890881/7MPC.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299989559738378/2e27d5d124bc2a62ddeb5dc9e7a73dd8.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299990386016257/48f70b7f0f0858254d0e50d68ef4bc4f443b74a7_hq.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299995922628628/anime-head-pat-gif.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299997248028712/a.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300008031322114/e3e2588fbae9422f2bd4813c324b1298.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300013492437014/giphy_1.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300014427766801/FlimsyDeafeningGrassspider-small.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300013509214228/giphy.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300026150977563/tenor_1.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300032303759360/tenor.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300033440415754/unnamed.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300032366804992/giphy_2.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300037924126743/tumblr_n9g05o77tU1ttu8odo1_500.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300047004925952/c0c1c5d15f8ad65a9f0aaf6c91a3811e.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300051438305368/giphy_3.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300056601362454/tenor_2.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300062024597514/B7g8Vh.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300069696241684/source_1.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300074557177892/source.gif"
]
    
@bot.command()
async def pat(ctx, user: discord.Member):
	embed = discord.Embed(description="**{.message.author.display_name}** pats **{.display_name}**. <a:pat:691589024774750228>".format(ctx, user), color=0xFFFFFF, timestamp=datetime.utcnow())
	embed.set_image(url=random.choice(pat_gifs))
	embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
	await ctx.send(embed=embed)
	
@pat.error
async def pat_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="**babi** pats **{.message.author.display_name}**. <a:pat:691589024774750228>".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
		embed.set_image(url=random.choice(pat_gifs))
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="**babi** pats **{.message.author.display_name}**. <a:pat:691589024774750228>".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
		embed.set_image(url=random.choice(pat_gifs))
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send(f"**{ctx.message.author.display_name}** member not found, I patted you instead", embed=embed)
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		await ctx.send("An error has occured. Detailed information below:", embed=embed)
