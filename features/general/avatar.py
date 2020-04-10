import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from storage import *

@bot.command(aliases=["av", "ava", "a", "showmeoffdaddy", "myav"])
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(description="{.mention}".format(user), color=0xFFFFFF)
	embed.set_author(name="Look at this cutie!", icon_url=user.avatar_url)
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@avatar.error
async def avatar_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="{.mention}".format(ctx.message.author), color=0xFFFFFF)
		embed.set_author(name="Look at this cutie!", icon_url=ctx.message.author.avatar_url)
		embed.set_image(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.BadArgument):
		embed = discord.Embed(color=0xFFFFFF)
		embed.add_field(name="Error: Member not found. Please make sure you provide the correct information of a member.", value="Having problems using the command? Contact a staff member!")
		await ctx.send("An error occurupted this command.", embed=embed)
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send("An error has occured. Detailed information below:", embed=embed)
