import discord
import os
import sys
from firebase_admin import db 

import database
from decouple import config

class alarmData:
    def __init__(self, userID, startTime, alarmTime):
        self.userID = userID
        self.startTime = startTime
        self.alarmTime = alarmTime

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.messages = True
intents.voice_states = True
client = discord.Client(intents=intents)

ref = db.reference('/')
users_ref = ref.child('users')
liveUsers_ref = ref.child('live')

@client.event
async def on_ready():
    print("Bot Ready")

@client.event
async def on_message(message): 
    if message.author == client.user:
        return 

    if message.content.startswith("-setAlarm"):
        await notifyMe.alarmPreProcessing(client, message, users_ref)

client.run(config("DISCORD_BOT_TOKEN"))