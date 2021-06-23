from datetime import datetime
import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

async def alarmPreProcessing (client, message, users_ref)
    alarmMsg = message.content.split("-setAlarm ", 1)[1]

    if not isnumeric(alarmMsg)
        await message.channel.send("Enter a valid number")
        return
    
    alarmTime = int(alarmMsg)

    if alarmTime < 1 or alarmTime > 180
        await message.channel.send("Enter a time between 1 and 180 minutes")
        return

    newAlarm = users_ref.child(str(client))

    if newAlarm.get() is None
        newAlarm.set({
            'user_name': client.user.name,
            'alarm': 
        })