# Discord Alarm Bot

A Discord bot that allows users to set alarms which will play audio in voice channels.Made with the intention to learn different tools and try stuff out.


## Installation and Prerequisites  

Use the package manager pip to install

```bash
pip install -r requirements.txt
```

Install FFMPEG from https://www.ffmpeg.org/download.html

When running for the first time, there will be 3 environment variables necessary:
1. DISCORD_BOT_TOKEN = THE DISCORD BOT TOKEN
2. GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account-file.json
3. GOOGLE_FILE_PATH="file name to when running store credentials" 

Make sure you do run the first time with a `init` flag


## Usage 

Currently the bot can:
1. Join a discord server
2. Save user created alarms in minutes
3. List current set alarms
4. Notify user when alarm time has elapsed and remove the alarm from the list
5. Change the timezone when displaying times
6. Delete alarms by alarm #
7. Bot will join voice channel of user who set alarm and play a default song
8. User can change the default alarm URL or set URL by alarm
9. Toggle between 12 and 24 hour formats when displaying times

Future plan:
1. Have a setting to make it a recurring alarm i.e. the Pomodoro technique

One can run the main bot using 
```bash
python bot.py
```

Frist time running in test mode to add config 
```bash
python bot.py init
```


## Commands

You must first create a text channel called `bot-commands` in order to use any
of the following commands. This can be changed in `bot.py`

#### -setAlarm (minutes) (youtube URL)    
Input a time in minute between 1 and 180 and sets the bot to activate an alarm once the selected time has passed. You can also put a youtube URL after the minutes to select a unique video for the alarm.

#### -listAlarms
List all alarms currently in the queue and provides alarm number, the name of the user who made it, and the time the alarm will go off. The time listed is based on the timezone set, default is UTC.

#### -delAlarm (alarm number)
Delete the alarm specified by the user. Alarm number is dictated by placement in the alarm list.

#### -clearList    
Clears the entire alarm list.

#### -setTZ (timezone offset)
Changes the displayed time according to the offset given. Based on UTC timezones, only offsets between -12 and 14 are allowed.

#### -setDefault (youtube URL)
Changes the default video that plays after the alarm time has elapsed.

#### -displayFormat
Toggle between 12 and 24-hour display format

#### -silence
Disconnects the bot from the voice channel it is currently connected to.


## Credits
https://discord.com/
https://www.ffmpeg.org/
https://www.youtube.com/