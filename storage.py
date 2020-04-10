from discord.ext.commands import Bot
from discord.ext import commands
import discord
import http.client
import requests
import json

bot = commands.Bot(command_prefix="=", case_insensitive=True)

snipe_msgs = {}
snipe_msgs_time = {}
editsnipe_msgs = {}
editsnipe_msgs_time = {}
