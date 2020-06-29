###########################
#                         #
#  #  #  ###  ####  ####  #
#  # #    #   #  #  #  #  #
#  ##     #   ####  ####  #
#  # #    #   #     #     #
#  #  #  ###  #     #     #
#                         #
###########################
#test
import sys
import logging
import os
import threading
import subprocess
KIPP_DIR=os.environ['KIPP_DIR']
sys.path.append(KIPP_DIR+"/Python/Commands")
from ESSENTIAL_PACKAGES import *
from Server import Server
from Music import search_music, music_handler, YTDLSource
from Profile import Profile
import Commands
from Command import commands
from BinaryClock import get_clock
CREATOR_ID=289920025077219328
KIPP_ID=386352783550447628
if len(sys.argv)>1:
    if sys.argv[1]=="dev":
        KIPP_ID=726545013064073277
serverinfo={}
playerinfo={}
client=discord.Client()
current_time=""
async def background_loop():
    import datetime
    global current_time
    while True:
        if get_clock() != current_time:
            try:
                await client.change_presence(activity=discord.Game(name=get_clock()))
                current_time=get_clock()
            except discord.DiscordException:
                print("Binary clock rate limited...")
        for server in client.guilds:
            if serverinfo[server].mHandler == None and len(serverinfo[server].queue)>=1:
                music=serverinfo[server].queue[0][1]
                if len(serverinfo[server].queue[0])>2:
                    serverinfo[server].playlist=serverinfo[server].queue[0].split("PLAYLIST:")[1][1:]
                    music=serverinfo[server].pick_playlist_song()
                    if serverinfo[server].playlist != None:
                        serverinfo[server].queue.append(serverinfo[server].queue[0])
                player = await YTDLSource.from_url(music, loop=client.loop)
                serverinfo[server].mHandler=music_handler(server,player,serverinfo[server].musicchannel)
            if serverinfo[server].mHandler == None and len(serverinfo[server].queue)==0:
                c=datetime.datetime.now()-serverinfo[server].end_time
                b=datetime.datetime.now()-serverinfo[server].jointime
                if c.seconds/60 >= 5 and b.seconds/60 >= 5:
                    if server.voice_client != None:
                        try:
                            await server.voice_client.disconnect()
                        except Exception:
                            print ("Voice client timeout, can't disconnect")
        await asyncio.sleep(1)
async def git_update_loop():
    while True:
        stdout=subprocess.check_output("sudo git pull --dry-run",shell=True).decode()
        if "up to date" not in stdout:
            print("New commit on master branch, updating and restarting...")
            os.system("sudo git pull")
            quit()
        await asyncio.sleep(120)
print("KIPP starting up...")
while True:
    @client.event
    async def on_voice_state_update(member,before, after):
        try:
            server = after.channel.guild
        except AttributeError:
            server = before.channel.guild
        user = server.get_member(KIPP_ID)
        users = []
        if before != None:
            if before.channel != server.get_member(KIPP_ID).voice.channel:
                return
        try:
            for user in server.get_member(KIPP_ID).voice.channel.members:
                if user.bot == False:
                    users.append(user)
            if len(users)==0:
                currentlyplaying=False
                if serverinfo[server].mHandler != None:
                    currentlyplaying=serverinfo[server].mHandler.is_playing
                if currentlyplaying:
                    if serverinfo[server].mHandler.paused == False:
                        await serverinfo[server].musictextchannel.send("Nobody is listening to KIPP. Pausing music...")
                        server.voice_client.pause()
                        serverinfo[server].mHandler.paused = True
                        serverinfo[server].mHandler.pausedatetime=datetime.now()
        except AttributeError:
            print(e)
    @client.event
    async def on_guild_join(server):
        for member in server.members:
            try:
                playerinfo[member]
            except KeyError:
                playerinfo[member] = Profile(member)
        try:
            serverinfo[server]
        except KeyError:
            serverinfo[server] = Server(server)
        serverinfo[server].task = client.loop.create_task(serverinfo[server].update_loop())
    @client.event
    async def on_guild_remove(server):
        serverinfo[server].task.cancel()
    @client.event
    async def on_ready():
        client.loop.create_task(background_loop())
        dev=False
        if len(sys.argv)>1:
            if sys.argv[1]=="dev":
                dev=True
        if not dev:
            client.loop.create_task(git_update_loop())
        logging.log(5,"KIPP started.")
        for server in client.guilds:
            serverinfo[server] = Server(server)
            for member in server.members:
                playerinfo[member] = Profile(member)
            client.loop.create_task(serverinfo[server].update_loop())
    @client.event
    async def on_join(member):
        server = member.server
        try:
            playerinfo[member].game
        except KeyError:
            playerinfo[member] = Profile(member)
            playerinfo[member].user = member
        if serverinfo[server].search_server_configs("WELCOME_CHANNEL") != None:
            try:
                await client.get_channel(serverinfo[server].search_server_configs("WELCOME_CHANNEL")[1]).send("Welcome to **{0}**, {1}".format(server, member.mention))
            except discord.DiscordException:
               print("Welcome channel was deleted, couldn't send message to welcome channel")
    @client.event
    async def on_message(message):
        global serverinfo
        global playerinfo
        if message.author == client.user or message.guild==None:
            return
        if message.author.id in serverinfo[message.guild].blocked:
            await client.delete_message(message)
            return
        serverinfo[message.guild].recentchannel = message.channel
        kippservers = 0
        for server in client.guilds:
            for member in server.members:
                if member == message.author:
                    kippservers=kippservers+1
        playerinfo[message.author].nickname = str(message.author.nick)
        playerinfo[message.author].highestrole = message.author.top_role
        role1 = discord.utils.get(message.author.guild.roles, name=str(playerinfo[message.author].highestrole))
        playerinfo[message.author].hrolecolor = role1.colour
        playerinfo[message.author].numkippservers = kippservers
        playerinfo[message.author].game = message.author.activity
        message2 = str(message.content).upper()
        if "|" in message2:
            c=message2.split("|")[0]
        else:
            c=message2
        for command in commands:
            if command.Name == c:
                serverinfo, playerinfo = await command.Execute(message,message2,serverinfo,playerinfo)
    client.loop.run_until_complete(client.start(TOKEN))
