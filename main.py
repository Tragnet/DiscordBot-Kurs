import discord, asyncio

from discord import app_commands
from discord.ext import commands

TOKEN ="Gå til side for hvordan lage discord BOT bruker og sett inn token her"
prefix = "!"
def check(bot, message):
    if message.content.lower().startswith(prefix):
        return prefix
    return prefix

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

def timeFormat(seconds):
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

intents = discord.Intents.all()
client = commands.AutoShardedBot(check, intents=intents)

@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    print("Bot is ready!")


@client.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        msg = timeFormat(error.retry_after)
        msg2 = timeFormat(error.cooldown.per)
        await interaction.response.send_message(embed=makeEmbed("something is not right", "Try again in {0}. This command has a {1} cooldown.".format(msg, msg2), colour=15746887), ephemeral=True)
    else:
        raise error


@client.tree.command(name="ping", description="Ping the bot")
@app_commands.checks.cooldown(1, 10, key=lambda i: (i.user.id))
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(embed=makeEmbed('Pong!', colour=4895220), ephemeral=True)

@client.command(name="ping")
async def ping(ctx):
    await ctx.reply('Pong!')

client.run(TOKEN)



