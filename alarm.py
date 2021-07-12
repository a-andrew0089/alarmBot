import datetime
import asyncio

alarmList = []
timezoneOffset = 0

#set 12-hour or 24-hour time display

class alarmData:
    def __init__(self, userID, startTime, alarmTime):
        self.userID = userID
        self.startTime = startTime
        self.alarmTime = alarmTime
        #add alarm music track to each object


async def printTime(hour, minute):
    if (hour + timezoneOffset) > 24:
        hour = hour - 24
    elif (hour + timezoneOffset) < 0:
        hour = hour + 24

    result = ("{:02d}".format(hour + timezoneOffset) + ":{:02d}".format(minute))
    return result


#elminiate 'message' variable
async def checkTime(message):
    
    while alarmList:
        if datetime.datetime.utcnow() > alarmList[0].alarmTime:
            #join server and play some music shit
            await message.channel.send("AHHHHHHHH!")
            del alarmList[0]
        await asyncio.sleep(1)


async def alarmProcessing (message):
    
    if len(alarmList) == 0:
        startTimer = True
    else:
        startTimer = False

    alarmMsg = message.content.split("-setAlarm ", 1)[1]

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

    alarmList.append(alarmData(message.author.display_name, message.created_at, end))
    alarmDis = await printTime(end.hour, end.minute)
    await message.channel.send("Alarm set for " + alarmDis)
    
    alarmList.sort(key=lambda x:x.alarmTime)

    if startTimer:
        loop = asyncio.get_event_loop()
        loop.create_task(checkTime(message))


async def listAlarms(message):
    num = 1
    for x in alarmList:
        alarmDis = await printTime(x.alarmTime.hour, x.alarmTime.minute)
        await message.channel.send(("Alarm #: "+ str(num) + "\nUser: " + str(x.userID) + 
            "\nAlarm: " + alarmDis ))
        num += 1  


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
        

async def testStuff():
    print(timezoneOffset)
    print(alarmList[0].alarmTime.hour)
    print(alarmList[0].alarmTime.hour + timezoneOffset)