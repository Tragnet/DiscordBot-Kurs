# Stilering av bot-svar

Når har vi fått til å sende en kommando som gir oss et svar. Dette er greit nok men det ser ganske kjedelig. Med discord embeds kan vi stilere meldinger for å gjøre de mer attraktive. For å gjøre dette lett å ta bruk av, har jeg laget en funksjon som kan brukes for å generere embeds.

```py
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
```

Du kan lime inn denne kodebiten under "check" funksjonen vi lagde tidligere.

## Hvordan ta i bruk denne funksjonen

I eksemplet under har jeg fornyet ping-kommandoen vi lagde i forrige steg. 

```py
@client.tree.command(name="ping", description="Ping the bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(embed=makeEmbed('Pong!', colour=4895220), ephemeral=True)
```
Her har vi definert at meldingen skal bli vist som en embed, og vil ha en farge med verdi 4895220 (48 rød, 95 grønn, 220 blå). Den vil se slik ut.

![image](https://user-images.githubusercontent.com/40642234/210956947-6fbfdb08-eff7-4535-96ac-3ba5c222e4eb.png)

Vi har også andre verdier vi kan endre, da gjør du bare som vi gjorde med "colour" og skriver inn f.eks "image"

> **Note** 
> Noen av verdiene krever en URL mens andre krever en tekstverdi.


# Problemer?

Her er koden så langt om du har noen problemer. 

```py
import discord, asyncio

from discord import app_commands
from discord.ext import commands

TOKEN ="YOUR TOKEN"
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


```
