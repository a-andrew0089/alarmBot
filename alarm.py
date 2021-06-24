import datetime

class alarmData:
    def __init__(self, userID, startTime, alarmTime):
        self.userID = userID
        self.startTime = startTime
        self.alarmTime = alarmTime

async def alarmProcessing (alarms, message):
    alarmMsg = message.content.split("-setAlarm ", 1)[1]

    if not alarmMsg.isnumeric():
        await message.channel.send("Enter a valid number")
        return
    
    alarmTime = int(alarmMsg)

    if alarmTime < 1 or alarmTime > 180:
        await message.channel.send("Enter a time between 1 and 180 minutes")
        return

    end = message.created_at + datetime.timedelta(minutes=alarmTime)
    alarms.append(alarmData(message.author.display_name, message.created_at.time(), end.time()))

    return

async def listAlarms(alarms, message):
    num = 1
    for x in alarms:
        await message.channel.send(("Alarm #: "+ str(num) + "\nUser: " + str(x.userID) + 
                                     "\nAlarm: {:02d}".format(x.alarmTime.hour) +":{:02d}".format(x.alarmTime.minute)))
        num += 1