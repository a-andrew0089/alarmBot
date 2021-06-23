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

Future plan:
1. Take in a time in minutes and let the user know the time has elapsed

One can run the main bot using 
```bash
python bot.py
```

Frist time running in test mode to add config 
```bash
python bot.py init
```