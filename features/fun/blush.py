import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from storage import *

blush_gifs = [
		"https://cdn.discordapp.com/attachments/670153232039018516/674297378454634506/tenor.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297383906967554/tumblr_180b159af06f5854161da3bccaaea1cf_d1d6cd99_540.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297385127641108/tumblr_nfujjdolje1r23i51o1_500.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297393675501591/0d31b6e935a2d9fb94aea46f0a5a5035.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297397060304906/blushing-anime-gif-9.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297406262607882/giphy_1.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297408007700480/df4c5f87d1c1b6ae-which-is-cuter-anime-girls-blushing-or-crying-anime-amino.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297412763779092/da1elnc-2c4bdeb2-c7ae-429e-82f7-64e11b74d41d.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297413166432287/CapitalDenseAcaciarat-small.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297416924790794/giphy_5.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297420905054238/giphy_3.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297426479153152/giphy_12.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297427897090069/giphy_7.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297430446964749/giphy_11.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297431915102208/giphy_2.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297432410030111/giphy_10.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297431697129482/giphy_6.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297441964654602/e777b2a55d4ea6e98ccf8f3589136dd6.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297437027958855/giphy_9.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297468724183060/tenor_1.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297487514796052/original.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297490824101889/b74a5b128b5d65ea1fdb9090c0b3f295.gif",
		"https://cdn.discordapp.com/attachments/670153232039018516/674297493886074922/8TJX.gif"
]

@bot.command()
async def blush(ctx):
	gif = random.choice(blush_gifs)
	embed = discord.Embed(description="**{.author.display_name}** blushes. <a:blush:691588875495145472>".format(ctx), color=0xFFFFFF, timestamp=datetime.utcnow())
	embed.set_image(url=gif)
	await ctx.send(embed=embed)
