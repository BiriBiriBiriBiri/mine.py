import discord
import shelve
global auth
auth = {}
client = discord.Client()
with shelve.open("sauth.db") as sauth:
    try:
        auth["username"] = sauth["username"]
        auth["password"] = sauth["password"]
    except KeyError:
        print("Please input username")
        auth["username"] = input()
        print("Please input password")
        auth["password"] = input()
sauth.close()

@client.event
async def on_ready():
    global auth
    with shelve.open("sauth.db") as sauth:
        sauth["username"] = auth["username"]
        sauth["password"] = auth["password"]
    sauth.close()
    print("Logged in as")
    print(client.user.name)
    print('--------------')


@client.event
async def on_message(msg):
    if msg.content == "!mine" and msg.author.id == client.user.id:
        while (1==1):
            await client.send_message(msg.channel, "!mine")
client.run(auth['username'],auth['password'])
