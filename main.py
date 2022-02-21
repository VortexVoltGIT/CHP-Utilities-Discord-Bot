import nextcord
from nextcord.ext import commands
import os
import json

#############################################################

if os.path.exists(os.getcwd() + "/config.json"):
    #pass
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+" ) as f:
        json.dump(configTemplate, f)

token = configData["Token"]
################################################################

guilds = [934531644570878013]

activity = nextcord.Activity(type=nextcord.ActivityType.listening, name = "CHPS Students")

client = commands.Bot(command_prefix="c!", activity=activity, status=nextcord.Status.do_not_disturb)

@client.event
async def on_ready():
    
    print(f"Running as {client}!")

@client.command()
async def test(ctx):
    await ctx.reply("Can't do nothin, <@687785530750271549> is being to gay")

for fn in os.listdir("./cogs"):
    if fn.endswith("py"):
        client.load_extension(f"cogs.{fn[:-3]}")

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send("Loaded Cog!")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send("Unloaded Cog!")

@client.command()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    await ctx.send("Reloaded Cog!")


client.run(token)