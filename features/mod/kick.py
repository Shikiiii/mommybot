import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from storage import *

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reasonn: str):
	try:
		await user.kick(reason="{} | by {}".format(reasonn, ctx.message.author))
	except:
		await ctx.send("Uh! This member has a role higher than mines, I can't kick them.")
		return
	try:
		await user.send("You've been kicked from **{}** by **{}** ({}) for: \n```{}```".format(ctx.message.author.guild.name, ctx.message.author, ctx.message.author.id, reasonn))
	except:
		await ctx.send("**{} has been kicked, but they were not notified due to their DMs being closed.** <a:animated_check_emoji:698107059106742372>".format(user.name))
		return
	await ctx.send("**{} has been kicked.** <a:animated_check_emoji:698107059106742372>".format(user.name))
	
@kick.error
async def kick_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(color=0xFFFFFF)
		embed.add_field(name="Error: Member not found. Please make sure you provide the correct information of a member.", value="Having problems using the command? Contact a staff member!")
		await ctx.send("An error occurupted this command.", embed=embed)
		return
	elif isinstance(error, commands.MissingRequiredArgument):
		
	elif isinstance(error, commands.CheckFailure):
	
