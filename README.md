# Discord Alarm Bot

An alarm bot made with the intent to learn different tools


## Installation and Prerequisites  

Use the package manager pip to install

```bash
pip install -r requirements.txt
```

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

Future plan:
1. Allow user to change default URL or set URL by alarm
2. Have a setting to make it a recurring alarm i.e. the Pomodoro technique

One can run the main bot using 
```bash
python bot.py
```

Frist time running in test mode to add config 
```bash
python bot.py init
```