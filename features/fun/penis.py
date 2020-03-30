import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from storage import *

@bot.command(aliases=["pp", "size", "ppsize"])
async def penis(ctx, *, user: discord.Member):
	sizes = ["D (no balls)", "D8 (inverted pp)", "8D", "8=D", "8==D", "8===D", "8====D", "8=====D", "8======D", "8=======D", "8========D", "8=========D", "8==========D", "8===========D", "8============D", "8=============D", "8==============D", "8===============D"]
	size = random.choice(sizes)
	embed = discord.Embed(title="{}".format(size), color=0x000000, timestamp=datetime.utcnow())
	embed.set_author(name="{}'s pp size".format(user.name), icon_url=user.avatar_url)
	embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
	await ctx.send(embed=embed)
	
@penis.error
async def penis_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		sizes = ["D (no balls)", "D8 (inverted pp)", "8D", "8=D", "8==D", "8===D", "8====D", "8=====D", "8======D", "8=======D", "8========D", "8=========D", "8==========D", "8===========D", "8============D", "8=============D", "8==============D", "8===============D"]
		size = random.choice(sizes)
		embed = discord.Embed(title="{}".format(size), color=0x000000, timestamp=datetime.utcnow())
		embed.set_author(name="{}'s pp size".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(color=0xFFFFFF)
        embed.add_field(name="Error: Member not found. Mommy was selected as the default member.", value="Having problems using the command? Contact a staff member!")
		await ctx.send("ngl i would be pretty worried if mommy had a pp", embed=embed)
    else:
        print('Ignoring exception in command av:', file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        embed = discord.Embed(description="{}".format(error), color=0x000000)
        embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
        await ctx.send("An error has occured. Detailed information below:", embed=embed)
