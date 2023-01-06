# Formatering av tid

Noen ganger vil vi ha nedkjølingsperioder på kommandoer. For å gjøre dette lett lesbart for brukeren trenger vi en ny funksjon.
```py
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
```
Funksjonen her tar i mot sekunder som en verdi og konverterer den til et lesbart format slik at isteden for 121s vil vi få tilbake 2m 1s.

Alene vil dette ikke gjøre mye, så vi trenger en måte å behandle kommandoer som ikke regnes som gyldig (I dette tilfeldet at den har en nedkjølingsperiode som ikke er ferdig)
For å behandle disse errorene kan vi legge inn denne koden

```py
@client.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        msg = timeFormat(error.retry_after)
        msg2 = timeFormat(error.cooldown.per)
        await interaction.response.send_message(embed=makeEmbed("something is not right", "Try again in {0}. This command has a {1} cooldown.".format(msg, msg2), colour=15746887), ephemeral=True)
    else:
        raise error
```

Når vi skal ta i bruk dette i kommandoene våre, bruker vi en sjekk for å se om den som sender spørringen oppfyller kravene som blir stilt. I ping-kommandoen vår kan dette se slik ut:

```py
@client.tree.command(name="ping", description="Ping the bot")
@app_commands.checks.cooldown(1, 10, key=lambda i: (i.user.id))
async def pingslash(interaction: discord.Interaction):
    await interaction.response.send_message(embed=makeEmbed('Pong!', colour=4895220), ephemeral=True)
```
Her har vi lagt inn en cooldown sjekk. Den ser etter hvor mange ganger kommandoen har blitt brukt innenfor en tidsperiode, hvor lang nedkjølingsperioden er og hvor sjekken skal være gyldig. I dette tilfellet har hver bruker en kommando hvert tiende sekund. Vi kan også legge inn en sjekk for hver kanal eller hele serveren.

Når vi ikke oppfyller kravene for kommandoens sjekk vil vi få følgende resultat:

![image](https://user-images.githubusercontent.com/40642234/210960156-3e143770-9d66-49c9-9973-0676d5debba3.png)

Som du kan se sendes feilsjekkmeldingen vi lagde istedenfor det resultatet vi vanligvis forventet.
