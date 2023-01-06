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
async def pingslash(interaction: discord.Interaction):
    await interaction.response.send_message(embed=makeEmbed('Pong!', colour=4895220), ephemeral=True)
```
Her har vi definert at meldingen skal bli vist som en embed, og vil ha en farge med verdi 4895220 (48 rød, 95 grønn, 220 blå). Den vil se slik ut.

![image](https://user-images.githubusercontent.com/40642234/210956947-6fbfdb08-eff7-4535-96ac-3ba5c222e4eb.png)

Vi har også andre verdier vi kan endre, da gjør du bare som vi gjorde med "colour" og skriver inn f.eks "image"

> **Note** 
> Noen av verdiene krever en URL mens andre krever en tekstverdi.
