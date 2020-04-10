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
		if len(ctx.message.content[6:]) > 0:
			user = await commands.MessageConverter().convert(ctx, ctx.message.content[6:])
		else:
			embed = discord.Embed(color=0xFFFFFF)
			embed.add_field(name="Error: Member not found. Please make sure you provide the correct information of a member.", value="Having problems using the command? Contact a staff member!")
			await ctx.send("An error occurupted this command.", embed=embed)
			return
		if user is None:
			embed = discord.Embed(color=0xFFFFFF)
			embed.add_field(name="Error: Member not found. Please make sure you provide the correct information of a member.", value="Having problems using the command? Contact a staff member!")
			await ctx.send("An error occurupted this command.", embed=embed)
			return
		try:
			await user.kick(reason="By {}".format(ctx.message.author))
		except:
			await ctx.send("Uh! This member has a role higher than mines, I can't kick them.")
			return
		try:
			await user.send("You've been kicked from **{}** by **{}** ({}) for: \n```NO_REASON_PROVIDED```".format(ctx.message.author.guild.name, ctx.message.author, ctx.message.author.id))
		except:
			await ctx.send("**{} has been kicked, but they were not notified due to their DMs being closed.** <a:animated_check_emoji:698107059106742372>".format(user.name))
			return
		await ctx.send("**{} has been kicked.** <a:animated_check_emoji:698107059106742372>".format(user.name))
	elif isinstance(error, commands.CheckFailure):
		embed = discord.Embed(color=0xFFFFFF)
		embed.add_field(name="Error: You're missing required permissions. You require the ``kick_members`` permission.", value="Having problems using the command? Contact a staff member!")
		await ctx.send("An error occurupted this command.", embed=embed)
	else:
		print('Ignoring exception in command av:', file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
		embed = discord.Embed(description="{}".format(error), color=0x000000)
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
		await ctx.send("An error has occured. Detailed information below:", embed=embed)
