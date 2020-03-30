import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from storage import *

@bot.command(aliases=["cf"])
async def coinflip(ctx, chosenSide: str):
	side = " "
	if chosenSide.lower() != "heads" and chosenSide.lower() != "h" and chosenSide.lower() != "tails" and chosenSide.lower() != "t":
		await ctx.send(f"**{ctx.message.author.name}**, you must specify either heads or tails. ``{chosenSide}`` is not a valid option. Please choose either ``heads``/``h`` or ``tails``/``t``.")
		return
	elif chosenSide.lower() == "heads" or chosenSide.lower() == "h":
		side = "HEADS"
	elif chosenSide.lower() == "tails" or chosenSide.lower() == "t":
		side = "TAILS"
	beforeFlip = discord.Embed(color=0xFFFFFF)
	beforeFlip.add_field(name="Your choice: {}".format(side), value="The coin landed on...")
	message = await ctx.send("The coin is being flipped...")
	await asyncio.sleep(3)
	possibleChoices = ["HEADS", "TAILS"]
	flippedSide = random.choice(possibleChoices)
	if side == flippedSide:
		afterFlip = discord.Embed(color=0x58ff3b)
		afterFlip.add_field(name="Your choice: {}".format(side), value="The coin landed on **{}**.".format(flippedSide))
		await message.edit(content="You win!", embed=afterFlip)
	elif side != flippedSide:
		afterFlip = discord.Embed(color=0xff3b30)
		afterFlip.add_field(name="Your choice: {}".format(side), value="The coin landed on **{}**.".format(flippedSide))
		await message.edit(content="You lose!", embed=afterFlip)
		
@coinflip.error
async def coinflip_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		beforeFlip = discord.Embed(description="The coin landed on...", color=0xFFFFFF)
		message = await ctx.send("The coin is being flipped...")
		await asyncio.sleep(3)
		possibleChoices = ["HEADS", "TAILS"]
		flippedSide = random.choice(possibleChoices)
		afterFlip = discord.Embed(description="The coin landed on **{}**.".format(flippedSide), color=0x000000)
		await message.edit(content="The coin has been flipped.\n\n**__FUN FACT:__** You can specify a side on the coinflip command! For example: ``=coinflip heads``.", embed=afterFlip)
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send("An error has occured. Detailed information below:", embed=embed)
