import discord
from discord.ext import commands


description = '''Komendy to: 
start.{ilosc botow}
stop
write.{text}
'''
bot = commands.Bot(command_prefix='.', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def start(ctx,ilosc):
	await ctx.send(f'startuje {ilosc} botow')

bot.run('NzU2NTQwMjE2Mzk4ODM5OTY5.X2TU-w.7csHxWLMxW503jP5ogVzsnxJ-y8')