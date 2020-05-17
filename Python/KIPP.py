###########################
#                         #
#  #  #  ###  ####  ####  #
#  # #    #   #  #  #  #  #
#  ##     #   ####  ####  #
#  # #    #   #     #     #
#  #  #  ###  #     #     #
#                         #
###########################
import sys
import logging
import os
import threading
import subprocess
KIPP_DIR=os.environ['KIPP_DIR']
from ESSENTIAL_PACKAGES import *
from Server import Server
from Music import search_music, music_handler, YTDLSource
from Profile import Profile
from Commands import *
from config import *
MSG_COUNTER=0
client=discord.Client()
START_TIME=datetime.now()
last_ping=t.time()
async def background_loop():
    import datetime
    while True:
        for server in client.guilds:
            if serverinfo[server].mHandler == None and len(serverinfo[server].queue)>=1:
                music=serverinfo[server].queue[0][1]
                if len(serverinfo[server].queue[0])>2:
                    serverinfo[server].playlist=serverinfo[server].queue[0].split("PLAYLIST:")[1][1:]
                    music=serverinfo[server].pick_playlist_song()
                    if serverinfo[server].playlist != None:
                        serverinfo[server].queue.append(serverinfo[server].queue[0])
                player = await YTDLSource.from_url(music, loop=asyncio.get_event_loop()) 
                serverinfo[server].mHandler=music_handler(server,player,serverinfo[server].musicchannel,client.loop)
            if serverinfo[server].mHandler == None and len(serverinfo[server].queue)==0:
                c=datetime.datetime.now()-serverinfo[server].end_time
                b=datetime.datetime.now()-serverinfo[server].jointime
                if c.seconds/60 >= 5 and b.seconds/60 >= 5:
                    if server.voice_client != None:
                        try:
                            await server.voice_client.disconnect()
                        except Exception as e:
                            print ("Voice client timeout, can't disconnect")
        await asyncio.sleep(1)
oldyear = ((str(datetime.now())[0])+(str(datetime.now())[1])+(str(datetime.now())[2])+(str(datetime.now())[3]))
oldmonth = ((str(datetime.now())[5])+(str(datetime.now())[6]))
oldday = ((str(datetime.now())[8])+(str(datetime.now())[9]))
oldhour = ((str(datetime.now())[11])+(str(datetime.now())[12]))
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
        try:
            for user in server.get_member(KIPP_ID).voice.voice.channel.members:
                if user.bot == False:
                    users.append(user)
            if len(users)==0:
                currentlyplaying=False
                if serverinfo[server].mHandler != None:
                    currentlyplaying=serverinfo[server].mHandler.is_playing
                if currentlyplaying:
                    if serverinfo[server].mHandler.paused == False:
                        await serverinfo[server].musictextchannel.send("Nobody is listening to KIPP. Pausing music...")
                        serverinfo[server].mHandler.player.pause()
                        serverinfo[server].mHandler.paused = True
                        serverinfo[server].mHandler.pausedatetime=datetime.now()
                        serverinfo[server].everyoneleft = True
            if (after.voice.voice.channel == server.get_member(KIPP_ID).voice.voice.channel) and serverinfo[server].everyoneleft:
                serverinfo[server].everyoneleft = False
                await serverinfo[server].musictextchannel.send("The music that was playing (**"+str(serverinfo[server].mHandler.title)+"**) was paused because nobody was listening. Use **!resume** to resume the music.")
        except AttributeError:
            pass
    @client.event
    async def on_server_join(server):
        general=False
        for channel in server.channels:
            if channel.name=='general':
                general=True
                try:
                    await channel.send("Hello, and thank you for using KIPP. To get started, type **!help** for all of the commands.")
                    break
                except discord.DiscordException:
                    pass
        if general == False:
            for channel in server.channels:
                try:
                    await channel.send("Hello, and thank you for using KIPP. To get started, type **!help** for all of the commands.")
                    break
                except discord.DiscordException:
                    pass
        for member in server.members:
            try:
                playerinfo[member].game
            except KeyError:
                playerinfo[member] = Profile(member)
        try:
            serverinfo[server].musicmessage
        except KeyError:
            serverinfo[server] = Server(server)
    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Streaming(platform="Twitch",name="3.1.24 Simulator",twitch_name="KIPP4780",url="https://twitch.tv/kipp4780"))
        loop = asyncio.get_event_loop()
        loop.create_task(background_loop())
        logging.log(5,"KIPP started.")
        for server in client.guilds:
            serverinfo[server] = Server(server)
            for member in server.members:
                playerinfo[member] = Profile(member)
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
        if message.author == client.user or message.guild==None:
            return
        if message.author.id in serverinfo[message.guild].blocked:
            await client.delete_message(message)
            return
        serverinfo[message.guild].recentchannel = message.channel
        kippservers = 0
        roles = []
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
                await command.Execute[0](message,message2)
    client.loop.run_until_complete(client.start(TOKEN))
