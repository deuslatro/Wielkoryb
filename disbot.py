import discord
import asyncio
import wedkarz
import threading
from time import sleep
from io import BytesIO
from PIL import Image
from discord.ext import commands
from dotenv import load_dotenv
import os

# Credentials
load_dotenv('.env')
exitConversationLoop = 0

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
async def w(ctx, arg, *args):
	try:
		if int(arg):
			print("wysylam wiadomosc:",args,"do bota ",arg)
			wedkarz.msgInGame(arg, " ".join(args[:]))
	except ValueError:
		print('poprawna konstrukcja komendy : .w [ktory bot] tresc np: .w 1 elo')
		await client.signal('poprawna konstrukcja komendy : .w [ktory bot] tresc np: .w 1 elo')

@client.command()
async def r(ctx, arg):
	try:
		if int(arg):
			print("pobieram nudesy od bota :",arg)
			await wedkarz.picToDiscord(arg)
	except ValueError:
		print('poprawna konstrukcja komendy : .r [ktory bot] np: .w 1')
		await client.signal('poprawna konstrukcja komendy : .r [ktory bot] np: .w 1')


@client.command()
async def e(ctx, arg):
	try:
		if int(arg):
			print("zamykam chat od bota :",arg)
			wedkarz.closeMsgWindow(arg)
	except ValueError:
		print('poprawna konstrukcja komendy : .e [ktory bot] np: .e 1')
		await client.signal('poprawna konstrukcja komendy : .e [ktory bot] np: .e 1')

@client.command()
async def restart(ctx):
	print("restart botow :")
	global exitConversationLoop
	exitConversationLoop = 0

def runBot():
	client.run(os.getenv('TOKEN'))


discordBot = threading.Thread(target=runBot, daemon=True)
discordBot.start()
