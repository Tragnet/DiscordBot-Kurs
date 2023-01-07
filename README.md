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



