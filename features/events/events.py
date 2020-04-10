import discord
from discord.ext import commands
import random
import sys
import traceback
import asyncio
import datetime
import json
from datetime import datetime
from storage import *

@bot.event
async def on_message_delete(message):
	snipe_msgs[str(message.channel.id)] = "{}|{}".format(message.content, message.author.id)
	snipe_msgs_time[str(message.channel.id)] = datetime.utcnow()

@bot.event
async def on_message_edit(before, after):
	editsnipe_msgs[str(before.channel.id)] = "{}|{}".format(before.content, before.author.id)
	editsnipe_msgs_time[str(after.channel.id)] = datetime.utcnow()
