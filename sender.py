from telethon import TelegramClient, errors
from dotenv import load_dotenv
import time
import os
import json
from random import randint

# API details
load_dotenv()
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
api_name = os.getenv("API_NAME")
# Account connection
client = TelegramClient(api_name, api_id, api_hash)


async def main():
    me = await client.get_me()
    # Read message from file and send to a list of scraped groups

    while(True):

        with open("groups.json", 'r') as openfile:
            json_object = json.load(openfile)

        for data in json_object:

            with open("message.json", "r") as m:
                msg = json.load(m)
                random_index = randint(0, len(msg)-1)
                message = msg[random_index]

            try:
                # await client.send_message(data['id'], message)
                await client.forward_messages(data['id'],message['msg_id'],message['channel'])
                print(data['name']+" "+str(data['id'])+" send successfully")
            except Exception as e:
                print(data['name']+" "+str(data['id'])+" failed to send. Reason : "+str(e))
        
            time.sleep(90)
        os.system('cls' if os.name == 'nt' else 'clear')
        js = []
    
        print("-- UPDATE GRUP LIST --\n")
        async for dialog in client.iter_dialogs():
            if str(dialog.id).startswith("-100"):
                dt = {"name" : dialog.name,"id" : dialog.id}
                #groups.append(dialog.id)
                js.append(dt)
                
                print(dialog.name, "has ID", dialog.id)
        with open("groups.json", "w") as outfile :
            json.dump(js,outfile)
        print("\nwaiting next loop 60 seconds")
        time.sleep(60)
        os.system('cls' if os.name == 'nt' else 'clear')

with client:
    client.loop.run_until_complete(main())
