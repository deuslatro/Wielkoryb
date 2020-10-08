import discord
import asyncio
import threading
from time import sleep

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        #self.bg_task = self.loop.create_task(self.signal("essa"))

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        #await self.signal("xD")

    async def signal(self,msg):
        print("xD")
        await self.wait_until_ready()
        channel = self.get_channel(756525875452706846) # channel ID goes here
        await channel.send(msg)



    def getLoop(self):
        return self.loop

client = MyClient()
def runBot():
    client.run('NzU2NTQwMjE2Mzk4ODM5OTY5.X2TU-w.OCfhfX3b65KdXu3apw7I__Pqv-c')

discordBot = threading.Thread(target=runBot,daemon=True)
discordBot.start()




