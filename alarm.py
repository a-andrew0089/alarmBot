import datetime
import asyncio

alarmList = []

class alarmData:
    def __init__(self, userID, startTime, alarmTime):
        self.userID = userID
        self.startTime = startTime
        self.alarmTime = alarmTime
        #add alarm music track to each object

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
    alarmList.append(alarmData(message.author.display_name, message.created_at, end))
    #sort alarmList by datetime

    if startTimer:
        loop = asyncio.get_event_loop()
        loop.create_task(checkTime(message))

    return


async def listAlarms(message):
    num = 1
    for x in alarmList:
        await message.channel.send(("Alarm #: "+ str(num) + "\nUser: " + str(x.userID) + 
                                     "\nAlarm: {:02d}".format(x.alarmTime.hour) +":{:02d}".format(x.alarmTime.minute)))
        num += 1    