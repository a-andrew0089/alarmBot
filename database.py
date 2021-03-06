import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
import atexit
import sys
import json
from decouple import config


if "init" in sys.argv:
    if os.path.exists(".env"):
        os.remove(".env") 

    envFile = open(".env", "w")
    print ("Init Setup")
    
    google_credentials_file = input("Enter Google Application Credentials: ")
    with open(google_credentials_file) as gFile:
        data = json.loads(gFile.read())
        jsonData = json.dumps(data)
        envFile.write("GOOGLE_APPLICATION_CREDENTIALS="+ jsonData+ "\n")

    os.remove(google_credentials_file)

    filePath = input("Enter Google File Path: ")
    envFile.write("GOOGLE_FILE_PATH="+filePath+"\n")

    botToken = input("Enter Discord Bot Token: ")
    envFile.write("DISCORD_BOT_TOKEN="+botToken+"\n")

    botTestToken = input("Enter Discord Bot Test Token: ")
    envFile.write("DISCORD_BOT_TEST_TOKEN="+botTestToken+"\n")

    envFile.close()

filePath = config("GOOGLE_FILE_PATH")

with open(filePath, "w") as google_credentials:
    google_credentials.write(config("GOOGLE_APPLICATION_CREDENTIALS"))

atexit.register(os.remove, filePath)
cred = credentials.Certificate(filePath)

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://alarmbot-4df36-default-rtdb.firebaseio.com/'
})
