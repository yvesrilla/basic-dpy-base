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

client.run("ODY5NzE1ODU4ODUzODgzOTQ1.YQCQAw.mnwe3lCLs86H4mCmFTh5jmzeKRQ")
