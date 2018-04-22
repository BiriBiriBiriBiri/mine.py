import discord
import datetime
import shelve
import time
global auth
global running
running = False
auth = {} # Create authentication dictionary
global mode
client = discord.Client()
with shelve.open("sauth.db") as sauth:
    try:
        auth["username"] = sauth["username"]
        auth["password"] = sauth["password"]  # Check if saved username + password exists, and if so save them to auth
    except KeyError:
        auth["username"] = input("Please input email: ")
        auth["password"] = input("Please input password: ") # If saved username + password does not exist, create them.
mode = input("Do you want to use non-stop mode? This will get you slightly more slime, but your discord messages will be lagged. (Input Y/N) ")
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
    print("Don't close this until you're done mining.")


@client.event
async def on_message(msg):
    global running
    global mode
    if msg.content == "!mine" and msg.author.id == client.user.id and running != True: # Check for inciting message
        if mode == "Y" or mode == "y" or mode == "Yes" or mode == "yes":
            sTime = 0
        else:
            sTime = 1
        running = True
        i = 0
        while (1==1):
            await client.send_message(msg.channel, "!mine") # Post "!mine" over and over again once begun.
            time.sleep(sTime)
            i +=1
            print(i)
            print(datetime.datetime.now().time())
client.run(auth['username'], auth['password']) # Log in in as credentials in auth.
