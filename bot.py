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

    if message.channel.name != "bot-commands":
        return

    if message.content.startswith("-setAlarm"):
        await alarm.alarmProcessing(message, client)
    
    if message.content.startswith("-listAlarms"):
        await alarm.listAlarms(message)

    if message.content.startswith("-clearList"):
        await alarm.clearList(message)

    if message.content.startswith("-setTZ"):
        await alarm.adjustTimezone(message)

    if message.content.startswith("-delAlarm"):
        await alarm.deleteAlarm(message)

    if message.content.startswith("-setDefault"):
        await alarm.changeDefaultUrl(message)

    if message.content.startswith("-leave"):
        await alarm.leave(message)
        
    if message.content.startswith("-displayFormat"):
        await alarm.changeFormat(message)

client.run(config("DISCORD_BOT_TOKEN"))
