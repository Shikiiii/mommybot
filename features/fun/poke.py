import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from storage import *

poke_gifs = [
    "https://cdn.discordapp.com/attachments/670153232039018516/674299333100961813/b.gif",
    "https://cdn.discordapp.com/attachments/670153232039018516/674299332790583306/a.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299336569389056/c.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299344039575582/e.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299342416379934/f.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299340885458954/d.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299344697950249/g.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299346736513046/h.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299354076413982/i.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299356882403358/j.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299376528654346/o.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299375702376478/k.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299374976761886/q.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299394748579874/r.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674299399786070027/s.gif"
    ]
    
@bot.command()
async def poke(ctx, user: discord.Member):
	embed = discord.Embed(description="**{.message.author.display_name}** pokes <a:poke:691589063437844481> **{.display_name}**.".format(ctx, user), color=0xFFFFFF, timestamp=datetime.utcnow())
	embed.set_image(url=random.choice(poke_gifs))
	embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
	await ctx.send(embed=embed)
	
@poke.error
async def poke_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="**Mommy** pokes <a:poke:691589063437844481> **{.message.author.display_name}**.".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
		embed.set_image(url=random.choice(poke_gifs))
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="**Mommy** pokes <a:poke:691589063437844481> **{.message.author.display_name}**.".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
		embed.set_image(url=random.choice(poke_gifs))
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send(f"**{ctx.message.author.display_name}** member not found, I poked you instead.", embed=embed)
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send("An error has occured. Detailed information below:", embed=embed)
