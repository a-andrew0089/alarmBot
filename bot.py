import discord
from decouple import config

import alarm

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
        await alarm.alarmProcessing(message)
    
    if message.content.startswith("-listAlarms"):
        await alarm.listAlarms(message)

    if message.content.startswith("-setTZ"):
        await alarm.adjustTimezone(message)

    if message.content.startswith("-delAlarm"):
        await alarm.deleteAlarm(message)

    if message.content.startswith("-test"):
        await alarm.testStuff()

    #command to select alarm music
    #set alarm with unique music
    #set alarm timezone

client.run(config("DISCORD_BOT_TOKEN"))