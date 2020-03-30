import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from storage import *
 
@bot.command(aliases=["howgay", "rategay"])
async def gayrate(ctx, user: discord.Member):
    await ctx.send(f"**{user.name}** is **__{int(random.randint(0, 100))}__**% gay! 🏳️‍🌈")

@gayrate.error
async def gayrate_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"**{ctx.message.author.name}** is **__{int(random.randint(0, 100))}__**% gay! 🏳️‍🌈")
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(color=0xFFFFFF)
        embed.add_field(name="Error: Member not found. Mommy was selected as the default member.")
        await ctx.send(f"**Mommy** is **__not gay__**, duh.", embed=embed)
    else:
        print('Ignoring exception in command av:', file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        embed = discord.Embed(description="{}".format(error), color=0x000000)
		embed.set_footer(text="© MommyBot by Shiki.", icon_url=bot.user.avatar_url)
        await ctx.send("An error has occured. Detailed information below:", embed=embed)
