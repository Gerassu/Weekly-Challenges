import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


from discord.ui import Button, View



@client.event
async def on_ready():
    print(f"logged in as {client.user}")



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if(message.content.startswith("!")):

        buttonsa = Button(style=discord.ButtonStyle.blurple, emoji="😢")
        buttonha = Button(style=discord.ButtonStyle.blurple, emoji="🙂")
        buttonth = Button(style=discord.ButtonStyle.blurple, emoji="🤔")
        buttonlo = Button(style=discord.ButtonStyle.blurple, emoji="😍")
        buttonco = Button(style=discord.ButtonStyle.blurple, emoji="😕")

        async def button_callbacksa(interaction):
            #datasa = datasa + 1
            #print(datasa)
            await interaction.response.send_message(view=view)

        async def button_callbackha(interaction):
            #dataha = dataha + 1
           # print(dataha)
            await interaction.response.send_message(view=view)

        async def button_callbackth(interaction):
           # datath = datath + 1
            #print(datath)
            await interaction.response.send_message(view=view)

        async def button_callbacklo(interaction):
            #datalo = datalo + 1
            #print(datalo)
            await interaction.response.send_message(view=view)

        async def button_callbackco(interaction):
           # dataco = dataco + 1
            #print(dataco)
            await interaction.response.send_message(view=view)

        buttonsa.callback = button_callbacksa
        buttonha.callback = button_callbackha
        buttonth.callback = button_callbackth
        buttonlo.callback = button_callbacklo
        buttonco.callback = button_callbackco

        view = View()

        view.add_item(buttonsa)
        view.add_item(buttonha)
        view.add_item(buttonth)
        view.add_item(buttonlo)
        view.add_item(buttonco)

        await message.channel.send(view=view)



client.run('OTk4Nzc1NDQ0MzM1NzY3NjQy.GzKJi1.BF8YXlOAZONNutcp7ZtzkmTWXuLzVZvqyP-DvM')
