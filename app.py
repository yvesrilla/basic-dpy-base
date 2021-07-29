import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")
client.remove_command('help')


@client.event
async def on_ready():
    print("i am online and ready!")

@client.command()
async def ping(ctx):
    await ctx.send("pong!")

client.run("PASTE_YOUR_BOT_TOKEN_HERE")
