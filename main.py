import asyncio, discord, random

from discord import app_commands
from discord.ext import commands

#Token
TOKEN = "Gå til side for hvordan lage discord BOT bruker og sett inn token her"

#Embed
def makeEmbed(title = "", desc = "", image = "", footer = "", colour = None, thumb=""):
    if colour != None:
        e = discord.Embed(title=title, description=desc, colour=colour)
    else:
        e = discord.Embed(title=title, description=desc)
    if thumb != None:
        e.set_thumbnail(url=thumb)
    if image != None:
        e.set_image(url=image)
    if footer != None:
        e.set_footer(text=footer)
    return e
intents = discord.Intents.all()
client = commands.AutoShardedBot(check, intents=intents,)

looping = False

#Startup logging
@client.event
async def on_ready():
    global looping
    print("All shards ready")
    print("Checking for restart message..")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    if not looping:
        looping = True
    print("Process started")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("being held hostage by devs")))
    
@client.event
async def on_shard_ready(id):
    print("Shard {0} ready".format(id))
 
#Formattering for å gjøre tid mer leselig
def readableTime(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    s = round(s, 2)
    msg = ""
    if h != 0:
        msg = msg+" {0}h".format(int(h))
    if m != 0:
        msg = msg+" {0}m".format(int(m))
    if s != 0:
        msg = msg+" {0}s".format(s)
    return msg[1:]
  
#Errorhandling for slash kommandoer
@client.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        msg = readableTime(error.retry_after)
        msg2 = readableTime(error.cooldown.per)
        await interaction.response.send_message(embed=makeEmbed(random.choice(["????", "Not a command", "Try something else", "No."]),
                                       "Try again in {0}. This command has a {1} cooldown.".format(msg, msg2), colour=15746887), ephemeral=True)
    else:
        raise error
  
#Første kommando
@client.tree.command(name="ping", description="Ping the bot to see how long it takes for the server to respond!")
@app_commands.checks.cooldown(1, 10, key=lambda i: (i.user.id))
async def pingslash(interaction: discord.Interaction):
    await interaction.response.send_message(embed=makeEmbed(f'Pong! In `{round(client.latency * 1000)}ms`', colour=4895220), ephemeral=True)
    await ctx.reply(embed=makeEmbed(f'Pong! In `{round(client.latency * 1000)}ms`', colour=4895220))
    
    
    
client.run(TOKEN)
