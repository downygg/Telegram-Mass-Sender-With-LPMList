from logging import error
from telethon import TelegramClient
from dotenv import load_dotenv
import os
import json
from telethon.tl.functions.channels import JoinChannelRequest
import time

# import time
# Load environment variables
load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
api_name = os.getenv("API_NAME")

# Account Connection
client = TelegramClient(api_name, api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())
    
    with open("listjoin.json", 'r') as openfile:
        lists = json.load(openfile)

    for grup in lists:
        print("[*] Joining : "+grup)
        try:
            await client(JoinChannelRequest(channel=grup))
            print("[+] Successfully join "+grup+"\n")
        except:
            print("[-] Failed to join "+grup+"\n")
        
        time.sleep(240)

with client:
    client.loop.run_until_complete(main())
