import discord
import os
import sys
import database
import datetime
from decouple import config

import alarm

alarmList = []

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.messages = True
intents.voice_states = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot Ready")

@client.event
async def on_message(message): 
    if message.author == client.user:
        return 

    if message.content.startswith("-setAlarm"):
        await alarm.alarmProcessing(alarmList, message)
    
    if message.content.startswith("-listAlarms"):
        await alarm.listAlarms(alarmList, message)           

client.run(config("DISCORD_BOT_TOKEN"))