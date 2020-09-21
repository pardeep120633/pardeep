import discord
from discord.ext import commands
# from itertools import cycle
import asyncio
import time
prefix = "op"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')
BOT_OWNER_ROLE="owner"

@bot.event
async def on_ready():
    print('Online')
    print(bot.user.name)
    print("Everything's all ready to go~")
    while True:
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Moolah News!"))
    	await asyncio.sleep(3)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with DM BOT!"))
    	await asyncio.sleep(3)


@bot.command(name="++")
@commands.has_role('owner')
async def f(ctx,*,msg):
	await ctx.message.delete()
	author=ctx.message.author
	
	for guild in bot.guilds:
		for member in guild.members:
			try:
				await member.send(msg)
				embed=discord.Embed(title="DISCORD MASS DM",description=f"DM sent to {member.name} \n:white_check_mark:",colour=0x142c9c)
				embed.set_image(url="https://cdn.discordapp.com/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
				embed.set_thumbnail(url = member.avatar_url)
				
				await ctx.send(embed=embed)
			except:
				embed=discord.Embed(title='''DISCORD MASS DM''',description=f'''DM Not sent to {member.name}#{member.discriminator}''' ''' :x: ''',colour=0x142c9c)
				embed.set_image(url="https://cdn.discordapp.com/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
				embed.set_thumbnail(url = member.avatar_url)
				
				await ctx.send(embed=embed)
					
				embed=discord.Embed(title="DM sent to all",description=f" :white_check_mark: ",colour=0x142c9c)
				embed.set_image(url="https://cdn.discordapp.com/attachments/595242286321762326/597758225336631300/Welcome2-1-4-1.gif")
				
				await ctx.send(embed=embed)
        
bot.run("NzQwOTQ3ODk2NjA1NzM3MDkx.XywbgA.EY3wAo-u2ndkSA0-M9PZ2DwTk80")  # Where 'TOKEN' is 
