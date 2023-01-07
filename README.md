# Kjøre discord-botten

For å kjøre din nyskapte bot, trenger vi litt Python-kode.
Under har jeg skrevet en kort Python-kode som lar deg kjøre botten på discord. Hvis du ikke allerede har det, lag en python-fil i ditt valg av editor og lim inn koden under.

```py
import discord, asyncio

from discord import app_commands
from discord.ext import commands

TOKEN ="MTA2MDQ5Mjk0NzkyNzM0MzE2NA.GFGQut.wfN7mCuoXXvbQbNx0KEM5taBa2IzoC4SO76glo"
prefix = "!"
def check(bot, message):
    if message.content.lower().startswith(prefix):
        return prefix
    return prefix

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

client.run(TOKEN)
```
Koden gjør ikke så mye av seg selv, den bare starter botten.

Det som er viktig å notere seg fra denne koden er at "TOKEN" som da er nøkkelen til botten, må endres til den du lagret da du lagde deg botten i steg 1.2.

I koden ovenfor er det en del som skjer, men kort fortalt sender den et kall til discord for å kjøre botten. Du legger kanskje merke til biten 
```py
def check(bot, message):
    if message.content.lower().startswith(prefix):
        return prefix
    return prefix
```
Dette er måten botten lytter etter kommandoer. Denne formaten av kommandoer er ganske gammeldags sammenlignet med hva vi skal ta for oss i denne guiden, men det er greit å bruke begge.
Du ser også en kodebit "on_ready():". Dette er kode som utføres med en gang botten er oppe og kjører. Innenfor der har vi koden her:
```py
try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
```
Dette gjør det mulig for oss å synkronisere "slash"-kommandoene våre med discord, slik at de kan brukes. Dette er typen kommandoer vi skal hovedsakelig ta for oss i guiden her, da det er den nye standarden.

> **Warning** 
> Det er viktig at du alltid har "client.run(TOKEN)" på slutten av dokumentet ditt.
> Noter at du også må endre verdien til TOKEN variablen til ditt eget token for at botten skal kunne kjøre
