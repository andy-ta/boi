import discord

TOKEN = 'NDg0MDQzMjEwMTU5ODE2NzA2.DmeVaw.9zt9AaaGPlV7RIRx3Z6AzOwWxUc'

client = discord.Client()


@client.event
async def on_message(message):
    # Prevent the bot from replying to itself
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
