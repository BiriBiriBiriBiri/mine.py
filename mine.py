import discord
import shelve
global auth
auth = {} # Create authentication dictionary
client = discord.Client()
with shelve.open("sauth.db") as sauth:
    try:
        auth["username"] = sauth["username"]
        auth["password"] = sauth["password"]  # Check if saved username + password exists, and if so save them to auth
    except KeyError:
        print("Please input username")
        auth["username"] = input()
        print("Please input password")
        auth["password"] = input() # If saved username + password does not exist, create them.
sauth.close()

@client.event
async def on_ready():
    global auth
    with shelve.open("sauth.db") as sauth:
        sauth["username"] = auth["username"]
        sauth["password"] = auth["password"] # Save username + password info to file
    sauth.close()
    print("Logged in as")
    print(client.user.name)
    print('--------------') # Notify user that they are logged in


@client.event
async def on_message(msg):
    if msg.content == "!mine" and msg.author.id == client.user.id: # Check for inciting message
        while (1==1):
            await client.send_message(msg.channel, "!mine") # Post "!mine" over and over again once begun.
client.run(auth['username'], auth['password']) # Log in in as credentials in auth.
