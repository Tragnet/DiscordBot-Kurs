# Bottens første kommando

I dette eksemplet skal vi lage en enkel kommando som svarer med "pong" når kommando "ping" sendes.

## Slash-kommando
> **Note**
> Det kan ta litt tid før kommandoene synkroniseres med discord når de ikke er spesifisert til servere.

```py
@client.tree.command(name="ping", description="Ping the bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong!', ephemeral=True)
```
Denne kommandoen gjør slik at vi kan skrive "/ping" i serveren din mens botten kjører, noe som vil få botten til å svare med "Pong!".
I dette eksemplet har kommandoen funksjonen "ephemeral" satt til sann, noe som gjør slik at bare du kan se botten svare på kommandoen din. Dette ser slik ut:

![image](https://user-images.githubusercontent.com/40642234/210766170-c4b4bab3-0ab8-47ae-a8fe-923534b14dd6.png)

Vi kan også se beskrivelsen av kommandoen før vi utfører den når vi har kommandoene synkronisert med discord. Dette er svært nyttig da du slipper å lese dokumentasjon for å finne ut hva hver enkelt kommando gjør. Discord vil også kunne hjelpe deg å autofullføre kommandoer når du bruker slash-kommandoer.

![image](https://user-images.githubusercontent.com/40642234/210766432-4d99f83e-588b-44bf-a677-6c84609d8df9.png)

## Vanlig kommando

```py
@client.command(name="ping")
async def ping(ctx):
    await ctx.reply('Pong!')
```
Denne kommandoen gjør egentlig akkurat det samme som slash-kommandoen, men er mer begrenset.
Som vi har definert i 1.4 skal "client" kommandoer alltid starte med "!". Så hvis vi kjører kommandoen !ping vil vi få følgende resultat

![image](https://user-images.githubusercontent.com/40642234/210767022-53bc3409-ca17-4753-bdd6-89bfe90dce7d.png)

Som du ser er dette nesten identisk slash-kommandoen men i kode skrives de litt annerledes.

# Problemer?
Hvis du har noen problemer med koden din så langt kan du kopiere koden her for å sikre deg at alt er korrekt.
> **Warning** Husk å endre TOKEN variablen til ditt eget token!
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
# Commands ---------------------------
@client.command(name="ping")
async def ping(ctx):
    await ctx.reply('Pong!')

@client.tree.command(name="ping", description="Ping the bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong!', ephemeral=True)


client.run(TOKEN)
```

[![image](https://img.shields.io/badge/back-Forrige%20Side-red?style=for-the-badge&logo=python&logoColor=yellow)](https://github.com/Tragnet/DiscordBot-Kurs/tree/1.4-Kj%C3%B8re-botten)    [![image](https://img.shields.io/badge/next-Neste%20Side-green?style=for-the-badge&logo=python&logoColor=yellow)](https://github.com/Tragnet/DiscordBot-Kurs/tree/1.6-Stilering-av-meldinger-med-embeds)

