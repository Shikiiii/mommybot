import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from storage import *

@bot.command()
async def snipe(ctx):
	try:
		to_slice = snipe_msgs[str(ctx.message.channel.id)]
		sniping = to_slice.split("|")
	except:
		embed = discord.Embed(color=0xFFFFFF)
		embed.add_field(name="Error: No snipeable message was found. Was anything deleted?", value="Having problems using the command? Contact a staff member!")
		await ctx.send("An error occurupted this command.", embed=embed)
	try:
		author = ctx.guild.get_member(int(sniping[1]))
	except:
		embed = discord.Embed(description="{}".format(sniping[0]), color=0xFFFFFF, timestamp=snipe_msgs_time[str(ctx.message.channel.id)])
		embed.set_author(name="User has left the server.".format(author.name), icon_url="https://cdn.discordapp.com/attachments/680647068770893847/698100598930669578/14-147016_question-mark-transparent-png-transparent-background-black-and.png")
		await ctx.send("**Note:** The member who sent this message has left the server.", embed=embed)
		return
	embed = discord.Embed(description="{}".format(sniping[0]), color=0xFFFFFF, timestamp=snipe_msgs_time[str(ctx.message.channel.id)])
	embed.set_author(name="{}".format(author.name), icon_url=author.avatar_url)
	await ctx.send(embed=embed)
