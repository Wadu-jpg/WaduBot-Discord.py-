import discord
import random 
import os
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("bot is ready")

@client.command()
async def ping(ctx):
    await ctx.send(f'ms! {round(client.latency * 1000)}ms')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command(name="ip")
async def ip(ctx):
    await ctx.send("Your Local IP is 111.223.11.2")

@client.event 
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('asslicker| .help'))
    print("Bot is ready")

@client.command(name="randimg")
async def randimg(context):

    images = [ "peakfit.png" , "guy.png" , "asexual.png" , "blm.png" , "coins.png" , "goku.png" , "CursedRoblox1.png", "mario.png" , "miku.png" , "unnamed.png"]

    random_image = random.choice(images)

    await context.send(file=discord.File(random_image))

@client.command()
async def load(ctx , extension):
    client.load_extension(f"{cogs.extension}")

@client.command()
async def unload(ctx , extension):
    client.unload_extension(f"{cogs.extension}")

for filename in os.listdir('./cogs'):
    if filename.endwith('.py'):
        client,load_extension(f'cogs.{filename[:-3]}')

client.run("ODAyNjYxNDU5NTM2MjQ4ODYy.YAyevA.4TMngv7gyaTyCtvVadHfmoOOsvo")