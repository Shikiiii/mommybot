import discord
from discord.ext import commands
import traceback
import datetime
import asyncio
import random
from datetime import datetime
from storage import *

@bot.command()
async def coinflip(ctx, chosenSide: str):
