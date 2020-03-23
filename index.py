import discord
from discord import Message, Guild, Member
from typing import Optional
from discord.ext import commands
import os
import sys
import traceback
import asyncio
from datetime import datetime
import datetime
import random
import json
import requests

from storage import *

# FUN
import features.fun.blush
import features.fun.facepalm
import features.fun.hug
import features.fun.kiss
import features.fun.pat
import features.fun.poke
import features.fun.slap

@bot.event
async def on_ready():
	print("Mommy Bot is up!")
	
bot.run(os.environ.get("token"))
