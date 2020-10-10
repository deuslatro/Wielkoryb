import discord
import asyncio
import threading
from time import sleep
from io import BytesIO
from PIL import Image
from discord.ext import commands
from dotenv import load_dotenv
import os

# Credentials
load_dotenv('.env')


class MyClient(commands.Bot):
	def __init__(self, *args, **kwargs):
		super().__init__(command_prefix='.', *args, **kwargs)

	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)

	async def signal(self, msg):
		await self.wait_until_ready()
		channel = self.get_channel(756525875452706846)  # channel ID goes here
		await channel.send(msg)

	async def sendScreen(self, screen):
		await self.wait_until_ready()
		channel = self.get_channel(756525875452706846)
		with BytesIO() as image_binary:
			screen.save(image_binary, 'PNG')
			image_binary.seek(0)
			await channel.send(file=discord.File(fp=image_binary, filename='screen.png'))

	def getLoop(self):
		return self.loop


client = MyClient()


@client.command()
async def w(ctx, arg, arg2):
	if int(arg):
		print(arg, arg2)


def runBot():
	client.run(os.getenv('TOKEN'))


discordBot = threading.Thread(target=runBot, daemon=True)
discordBot.start()
