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

# This is where I'll import the different files.

@bot.event
async def on_ready():
	print("Mommy Bot is up!")
	
bot.run()
