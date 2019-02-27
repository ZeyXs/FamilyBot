import discord
import time
from discord.ext import commands
import random
import os

TOKEN = "NTQ2NjY4OTYxNTQzMjI1MzU0.D0tQAw.X4L4b8-rLWT5Bun_9DpkjSVzcWE"

client = commands.Bot(command_prefix= "/")


@client.event
async def on_ready():
    print("Bot is ready.")
    print("Loading ready. Command is ready.")
    await client.change_presence(game=discord.Game(name='/help'))


@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))

    if (message.channel.id == "546624265206890507"):
        await client.add_reaction(message, "✅")
        await client.add_reaction(message, "❎")

    if message.content.upper().startswith("/PING"):
        timePing = time.monotonic()
        pinger = await client.send_message(message.channel, ":ping_pong: **Pong !**")
        ping = "%.2f" % (1000 * (time.monotonic() - timePing))
        await client.edit_message(pinger, ":ping_pong: **Pong !**\n\
    `Ping: " + ping + "`")

    if message.content.upper().startswith("/PONG"):
        timePing = time.monotonic()
        pinger = await client.send_message(message.channel, ":ping_pong: **Ping !**")
        ping = "%.2f" % (1000 * (time.monotonic() - timePing))
        await client.edit_message(pinger, ":ping_pong: **Ping !**\n\
    `Ping: " + ping + "`")

    if message.content.upper().startswith("/SAY"):
        args = message.content.split(" ")
        await client.send_message(message.channel, (" ".join(args[1:])))
        await client.delete_message(message)

    if message.content.upper().startswith("/GIF"):
        await client.send_message(message.channel, random.choice(["https://giphy.com/gifs/AuIvUrZpzBl04",
                                                                  "https://giphy.com/gifs/hello-hey-big-brother-l0MYBbEvqqi1kfuyA",
                                                                  "https://giphy.com/gifs/wow-amazing-l4FGETcwLzIZ1IaGs",
                                                                  "https://giphy.com/gifs/trump-donald-eclipse-xUNen16DFqlM6v6DEQ",
                                                                  "https://tenor.com/view/ok-okay-gif-5307535",
                                                                  "https://gph.is/2iUaL8y",
                                                                  "https://gph.is/19aLnvI",
                                                                  "https://gph.is/2fiQFj1",
                                                                  "https://gph.is/1rr0eCj",
                                                                  "https://media.giphy.com/media/joPQLwo2kbXe8/giphy.gif",
                                                                  "https://media.giphy.com/media/QGzPdYCcBbbZm/giphy.gif",
                                                                  "https://media.giphy.com/media/w1XrYq5PsCbyE/giphy.gif",
                                                                  "https://gph.is/2tBvKBE",
                                                                  "https://tenor.com/view/smile-golden-retriever-break-neck-gif-7733809",
                                                                  "https://tenor.com/view/pinguino-furbo-frozen-excited-gif-13388703",
                                                                  "https://gph.is/2lnp32Z",
                                                                  "https://gph.is/2rwmnmy",
                                                                  "https://tenor.com/4iLj.gif",
                                                                  "https://tenor.com/4gdR.gif",
                                                                  "https://tenor.com/yFDW.gif",
                                                                  "https://tenor.com/4n8e.gif",
                                                                  "https://tenor.com/yiQN.gif",
                                                                  "https://tenor.com/view/cobie-smulders-sad-crying-wine-upset-gif-3550883",
                                                                  "https://tenor.com/view/ted-teddy-bear-bear-hump-humping-gif-4762693",
                                                                  "https://tenor.com/view/shocked-omg-australiasgottalent-noway-gif-5027549",
                                                                  "https://tenor.com/view/dur-dumb-huh-durrr-stupid-gif-5042504",
                                                                  "https://tenor.com/view/surprise-chris-pratt-parks-and-recreation-parks-and-rec-shocked-gif-5571450",
                                                                  "https://giphy.com/gifs/excited-pikachu-U2nN0ridM4lXy",
                                                                  "https://tenor.com/view/cat-space-shocked-gif-11077933",
                                                                  "https://tenor.com/view/mr-bean-funny-hello-hi-wave-gif-3528683",
                                                                  "https://tenor.com/view/michaelscott-wink-yes-gif-5795910",
                                                                  "https://tenor.com/view/salttruck-gif-8448136",
                                                                  "https://tenor.com/view/cat-neutered-kitten-what-wtf-gif-10638247",
                                                                  "https://gph.is/2SGx6It",
                                                                  "https://cdn.discordapp.com/emojis/393622342581878785.gif?v=1",
                                                                  "https://cdn.discordapp.com/attachments/467724813465681921/533562203580923914/image0-1.gif",
                                                                  "https://tenor.com/view/dead-im-yoshi-gif-10650779",
                                                                  "https://media.giphy.com/media/l4FGpPki5v2Bcd6Ss/giphy.gif"]))
        message_content = message.content.split(' ')[1]
        print(message_content)

    if message.content.startswith("gg"):
        await client.send_message(message.channel, "👏👏👏")

    if message.content.startswith("blbl"):
        await client.send_message(message.channel, "🦑")

    if message.content.upper().startswith("/HELP"):
        help = discord.Embed(title='Commandes:', description='Voici la liste des commandes', colour=0x43d312)
        help.set_author(name="Family's Slave", icon_url="https://cdn.discordapp.com/attachments/546794122783096832/547126252205506570/green-letter-f-icon-png-3.png")
        help.add_field(name="Prefix:", value="/", inline=False)
        help.add_field(name="/help", value="Affiche les commandes", inline=True)
        help.add_field(name="/say (+texte)", value="Fait dire au bot le texte", inline=True)
        help.add_field(name="/ping", value="Affiche le ping", inline=True)
        help.add_field(name="/gif", value="Donne un GIF aleatoirement!", inline=True)
        help.add_field(name="/coucou <membre>", value="Passe le coucou à t'es amis !", inline=True)
        await client.send_message(message.channel, embed=help)

    if message.content.upper().startswith("/AIDE"):
        await client.send_message(message.channel, "Merci d'éxécuter la commande /help pour avoir la liste des commandes.")

    if message.content.upper().startswith("/COUCOU"):
        argscc = message.content.split(" ")
        await client.send_message(message.channel, "Coucou " + argscc[1] + " ! :D")



client.run(os.environ['TOKEN_BOT'])
