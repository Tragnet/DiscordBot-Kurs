# Utfordring

Nå som du har lært deg en god del grunnleggende kunnskap om hvordan du kan lage en discord-bot, har jeg en siste utfordring til deg. I denne oppgaven skal du prøve å lage en kommando som sender en embed melding med et bilde av en katt. Under vil du se resultatet du burde prøve å få til.

![bilde](https://user-images.githubusercontent.com/40642234/211124833-8c485ff9-bb27-461e-847c-3b848b41fb7a.png)



Under finner du en link til bildet jeg har brukt. Gjerne bruk dette når du prøver utfordringen!

https://user-images.githubusercontent.com/40642234/211124873-20632720-555d-4d66-8664-d2034c678d8b.png

<details>
    <summary>Løsningsforslag</summary>
    
```py
@client.tree.command(name="cat", description="Sends a picture of a cat")
async def cat(interaction: discord.Interaction):
    await interaction.response.send_message(embed=makeEmbed('Have a cat!',
                                                            'meow',
                                                            image="https://user-images.githubusercontent.com/40642234/211124873-20632720-555d-4d66-8664-d2034c678d8b.png",
                                                            footer='Your cat is kinda wonky ngl'))
                                                           
```

</details>


# For lett?

Hvis du syns denne oppgaven blir for lett, kan du prøve å lage en liste med flere bilder som sender tilfeldige bilder hver gang kommandoen kjøres.
Du kan også ta i bruk en [API (cataas.com)](https://cataas.com/#/) for denne oppgaven.
>**Note**
> Det kan være lurt å ta i bruk "Random" biblioteket for denne oppgaven. Dette biblioteket er innebygd i Python installasjonen din så du trenger bare å importere det.

[![image](https://img.shields.io/badge/back-Forrige%20Side-red?style=for-the-badge&logo=python&logoColor=yellow)](https://github.com/Tragnet/DiscordBot-Kurs/tree/1.7-Nedkj%C3%B8ling-av-kommandoer)    
