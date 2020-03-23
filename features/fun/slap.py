import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from storage import *

slap_gifs = [
    "https://cdn.discordapp.com/attachments/670153232039018516/674300987120418846/da424ee4ad0dadbb88be107b5c68a58e0ebfe632_hq.gif",
    "https://cdn.discordapp.com/attachments/670153232039018516/674300990194843678/giphy_1.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300987258699808/akari-slap.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300991109201920/giphy_2.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300990836572190/anime-slap-gif-11.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300994120581147/giphy_4.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300994166718464/giphy_5.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674300995794370575/giphy_3.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674301000407973891/giphy_6.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674301000525283346/giphy_7.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674301033002041356/tenor_1.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674301035224760330/source_1.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674301035103256577/source.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674301039242903552/YA7g7h7.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674301041184866304/tenor.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674301048638406696/tenor_2.gif"
    ]
    
@bot.command()
async def slap(ctx, user: discord.Member):
	embed = discord.Embed(description="**{.message.author.display_name}** slaps **{.display_name}**. <:pensive_heart:681955741279715349>".format(ctx, user), color=0xFFFFFF, timestamp=datetime.utcnow())
	embed.set_image(url=random.choice(slap_gifs))
	embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
	await ctx.send(embed=embed)
	
@slap.error
async def slap_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="**Mommy** slaps **{.message.author.display_name}**. <:pensive_heart:681955741279715349>".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
		embed.set_image(url=random.choice(slap_gifs))
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="**Mommy** slaps **{.message.author.display_name}**. <:pensive_heart:681955741279715349>".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
		embed.set_image(url=random.choice(slap_gifs))
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send(f"**{ctx.message.author.display_name}** member not found, I slapped you instead", embed=embed)
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send("An error has occured. Detailed information below:", embed=embed)
