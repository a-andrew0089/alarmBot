# Written by Alex Andrew
# Made to be implemented within the General Discord Bot Project: https://github.com/dudley2y/discord-general-bot

import datetime
import asyncio
from youtube_dl import YoutubeDL
from discord.ext import commands
from discord import FFmpegPCMAudio

alarmList = []
timezoneOffset = 0
hourFormat = False
client = None
voiceClient = None 
url = "https://www.youtube.com/watch?v=y_pedYe52kI"

class alarmData:
    def __init__(self, username, userID, guildID, startTime, alarmTime, alarmURL):
        self.username = username
        self.userID = userID
        self.guildID = guildID
        self.startTime = startTime
        self.alarmTime = alarmTime
        self.alarmURL = alarmURL


async def printTime(hour, minute):
    if (hour + timezoneOffset) > 24:
        hour = hour - 24
    elif (hour + timezoneOffset) < 0:
        hour = hour + 24
        
    global hourFormat
        
    if hourFormat and hour > 12:
        hour = hour-12
    
    if hourFormat and hour is 0:
        hour = hour+12

    result = ("{:02d}".format(hour + timezoneOffset) + ":{:02d}".format(minute))
    return result


async def play(alarmObj):
    guild = client.get_guild(alarmObj.guildID)
    member = guild.get_member(alarmObj.userID)
    if member.voice:

        global voiceClient
        if voiceClient is not None:
            await voiceClient.disconnect()

        voiceClient = await member.voice.channel.connect()

        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        with YoutubeDL(YDL_OPTIONS) as ydl:
            if alarmObj.alarmURL is None:
                info = ydl.extract_info(url, download=False)
            else:
                info = ydl.extract_info(alarmObj.alarmURL, download=False)
        URLz=info['formats'][0]['url']

        voiceClient.play(FFmpegPCMAudio(URLz, **FFMPEG_OPTIONS))


async def checkTime():

    while alarmList:
        if datetime.datetime.utcnow() > alarmList[0].alarmTime:
            await play(alarmList[0])
            del alarmList[0]
        await asyncio.sleep(1)


async def alarmProcessing (message, cli):
    global client
    client = cli

    if len(alarmList) == 0:
        startTimer = True
    else:
        startTimer = False

    alarmURL = None

    msg = message.content.split()
    if len(msg) > 2:
        alarmMsg = msg[1]
        alarmURL = msg[2]
        print(alarmURL)
    else:
        alarmMsg = msg[1]

    if not alarmMsg.isnumeric():
        await message.channel.send("Enter a valid number")
        return
    
    alarmTime = int(alarmMsg)

    if alarmTime < 1 or alarmTime > 180:
        await message.channel.send("Enter a time between 1 and 180 minutes")
        return

    end = message.created_at + datetime.timedelta(minutes=alarmTime)

    for x in alarmList:
        diff = end - x.alarmTime
        if diff.seconds < 30:
            await message.channel.send("There is already an alarm set for this time")
            return

    alarmList.append(alarmData(message.author.display_name, message.author.id, message.guild.id, message.created_at, end, alarmURL))
    alarmDis = await printTime(end.hour, end.minute)
    await message.channel.send("Alarm set for " + alarmDis)
    
    alarmList.sort(key=lambda x:x.alarmTime)

    if startTimer:
        loop = asyncio.get_event_loop()
        loop.create_task(checkTime())


async def listAlarms(message):
    num = 1
    for x in alarmList:
        alarmDis = await printTime(x.alarmTime.hour, x.alarmTime.minute)
        await message.channel.send(("Alarm #: "+ str(num) + "\nUser: " + str(x.username) + 
            "\nAlarm: " + alarmDis ))
        num += 1  


async def clearList(message):
    if len(alarmList) > 0:
        alarmList.clear()
        await message.channel.send("Alarm list cleared")
    else:
        await message.channel.send("Alarm list is empty")


async def adjustTimezone(message):
    global timezoneOffset
    dt = datetime.datetime.utcnow()

    zone = message.content.split("-setTZ ", 1)[1] 
    if zone.isnumeric() or (zone.startswith("-") and zone[1:].isnumeric()):
        zoneInt = int(zone)
        if zoneInt < -12 or zoneInt > 14:
            await message.channel.send("Please enter an offset between -12 and 14")
        else:
            timezoneOffset = zoneInt
            timeDis = await printTime(dt.hour, dt.minute)
            await message.channel.send("Timezone Changed")
            await message.channel.send("The time is now " + timeDis)
    else:
        await message.channel.send("Please enter an integer")


async def deleteAlarm(message):
    alarmNum = message.content.split("-delAlarm ", 1)[1]
    if not alarmNum.isnumeric():
        await message.channel.send("Please enter a number")

    alarmIndex = int(alarmNum)-1
    if alarmIndex > len(alarmList) or alarmIndex < 0:
        await message.channel.send("Please enter a valid alarm number")

    alarm = alarmList[alarmIndex]
    alarmDis = await printTime(alarm.alarmTime.hour, alarm.alarmTime.minute)
    await message.channel.send("Deleting alarm " + alarmNum + "\nTime: " + alarmDis)

    del alarmList[alarmIndex]


async def changeDefaultUrl(message):
    global url
    url = message.content.split("-setDefault ", 1)[1]
    await message.channel.send("Default alarm changed")


async def leave(message):
    if voiceClient is not None:
        await voiceClient.disconnect()
    else:
<<<<<<< HEAD
        await message.channel.send("alarmBot is not in a voice channel")
=======
        await message.channel.send("alarmBot is not in a voice channel")
        

async def testStuff():
    print('Test')
   
async def changeFormat(message):
    global hourFormat
    
    if hourFormat:
        hourFormat = False
        await message.channel.send("Changed to 24-hour display format")
    else:
        hourFormat = True
        await message.channel.send("Changed to 12-hour display format")
        
    
>>>>>>> e308078e3e6f390056af8d5214377dae3f112593
