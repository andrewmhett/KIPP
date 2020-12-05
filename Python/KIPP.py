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
import difflib
KIPP_DIR=os.environ['KIPP_DIR']
sys.path.append(KIPP_DIR+"/Python/Commands")
from ESSENTIAL_PACKAGES import *
from Server import Server
from Music import search_music, music_handler, YTDLSource
from Profile import Profile
import Commands
from Command import commands
from Base4Clock import get_clock
import random
CREATOR_ID=289920025077219328
KIPP_ID=386352783550447628
if len(sys.argv)>1:
    if sys.argv[1]=="dev":
        KIPP_ID=726545013064073277
serverinfo={}
playerinfo={}
intents = discord.Intents.default()
intents.members = True
client=discord.Client(intents=intents)
current_time=""

def fluctuate(prev_delta):
    fluctuation=SystemRandom().choices([.1,.05,.03,.01,0,-.01,-.03,-.05,-.1],weights=(15,25,30,35,20,35,30,25,15),k=1)[0] if prev_delta > 0.01 or prev_delta < 0.01 else SystemRandom().randrange(-5,5)/1000
    return fluctuation+prev_delta

def update_stocks():
    if datetime.strftime(datetime.now(),format("%m/%d/%Y")) not in subprocess.Popen(["sudo","cat",KIPP_DIR+"/STOCKS.txt"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode():
        if int(datetime.strftime(datetime.now(),format("%H")))>=10:
            stocks=subprocess.Popen(["sudo","-E",KIPP_DIR+"/C++/STOCKS_IO","r","a"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
            prev_data=subprocess.Popen(["sudo","cat",KIPP_DIR+"/STOCKS.txt"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
            delta_dict={}
            for datum in prev_data:
                if len(datum)>0:
                    if not datum.startswith("LAST UPDATED"):
                        delta_dict[datum.split(":")[0]]=int(datum.split(":")[1])
            os.system("sudo truncate -s 0 {0}/STOCKS.txt".format(KIPP_DIR))
            prev_trends=subprocess.Popen(["sudo","cat",KIPP_DIR+"/TRENDS.txt"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
            os.system("sudo truncate -s 0 {0}/TRENDS.txt".format(KIPP_DIR))
            trend_dict={}
            for trend in prev_trends:
                if len(trend)>0:
                    trend_dict[trend.split(":")[0]]=[]
                    for prev in trend.split(":")[1].split(" "):
                        trend_dict[trend.split(":")[0]].append(prev)
            for stock in stocks:
                if len(stock)>0:
                    last_percent=delta_dict[stock.split(":")[0]]/int(stock.split(" ")[2])
                    new_percent=fluctuate(last_percent)
                    random_perc=random.SystemRandom().randint(0,50)/1000
                    if new_percent>0:
                        new_percent=max(random_perc/10,min(new_percent,random_perc))
                    else:
                        new_percent=max(-random_perc,min(new_percent,-random_perc/10))
                    delta=int(int(stock.split(" ")[2])*new_percent)
                    if int(stock.split(" ")[2])<20000:
                        delta+=500
                    if int(stock.split(" ")[2])>150000:
                        delta-=int(int(stock.split(" ")[2])*.08)
                    for i in range(9):
                        trend_dict[stock.split(":")[0]][i]=trend_dict[stock.split(":")[0]][i+1]
                    trend_dict[stock.split(":")[0]][9]=str(int(stock.split(" ")[2])+delta)
                    os.system('sudo echo "{0}:{1}" >> {2}/STOCKS.txt'.format(stock.split(":")[0],str(delta),KIPP_DIR))
                    os.system('sudo echo "{0}:{1}" >> {2}/TRENDS.txt'.format(stock.split(":")[0]," ".join(trend_dict[stock.split(":")[0]]),KIPP_DIR))
                    os.system('sudo -E {0}/C++/STOCKS_IO wp {1} {2}'.format(KIPP_DIR,stock.split(":")[0],str(delta+int(stock.split(" ")[2]))))
            os.system('sudo echo "LAST UPDATED:{0}" >> {1}/STOCKS.txt'.format(datetime.strftime(datetime.now(),format("%m/%d/%Y")),KIPP_DIR))

def automine_kippcoins():
    for server in client.guilds:
        for member in server.members:
            amount_mined=0
            if playerinfo[member].HAS_ITEM(6):
                amount_mined+=40
            if playerinfo[member].HAS_ITEM(7):
                amount_mined*=10
            if playerinfo[member].HAS_ITEM(8):
                amount_mined*=100
            if playerinfo[member].HAS_ITEM(9):
                amount_mined+=40000
            playerinfo[member].GIVE_KIPPCOINS(amount_mined)

async def background_loop():
    import datetime
    global current_time
    while True:
        try:
            if get_clock() != current_time:
                update_stocks()
                automine_kippcoins()
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
                    while len(serverinfo[server].queue)>0:
                        try:
                            player = await YTDLSource.from_url(music, loop=client.loop)
                            serverinfo[server].mHandler=music_handler(server,player,serverinfo[server].musicchannel)
                            break
                        except youtube_dl.utils.DownloadError:
                            serverinfo[server].queue=serverinfo[server].queue[1:]
                            if serverinfo[server].playlist != None:
                                music=serverinfo[server].pick_playlist_song()
                            else:
                                music=serverinfo[server].queue[0][1]
                if serverinfo[server].mHandler == None and len(serverinfo[server].queue)==0:
                    end_time_delta=datetime.datetime.now()-serverinfo[server].end_time
                    join_time_delta=datetime.datetime.now()-serverinfo[server].jointime
                    if join_time_delta.seconds/60 >= 5 and end_time_delta.seconds/60 >= 5:
                        if server.voice_client != None:
                            try:
                                await server.voice_client.disconnect()
                            except Exception:
                                print ("Voice client timeout, can't disconnect")
                else:
                    if serverinfo[server].mHandler.paused:
                        time_delta=datetime.datetime.now()-serverinfo[server].mHandler.pausedatetime
                        if time_delta.seconds>=60:
                            await serverinfo[server].musictextchannel.send("Song paused for more than an hour. Ending current song and clearing queue...")
                            await serverinfo[server].mHandler.message.delete()
                            serverinfo[server].mHandler=None
                            serverinfo[server].queue=[]
                            server.voice_client.stop()
                            await server.voice_client.disconnect()
        except Exception as e:
            os.system('sudo echo "{0} {1}" >> $KIPP_DIR/log.txt'.format(datetime.datetime.strftime(datetime.datetime.now(),"[%m/%d/%Y %H:%M:%S]"), e))
        await asyncio.sleep(1)

print("KIPP starting up...")
@client.event
async def on_voice_state_update(member,before, after):
    try:
        server = after.channel.guild
    except AttributeError:
        server = before.channel.guild
    user = server.get_member(KIPP_ID)
    users = []
    if before != None and server.get_member(KIPP_ID).voice != None:
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
    logging.log(5,"KIPP started.")
    for server in client.guilds:
        serverinfo[server] = Server(server)
        for member in server.members:
            playerinfo[member] = Profile(member)
        client.loop.create_task(serverinfo[server].update_loop())
@client.event
async def on_join(member):
    server = member.server
    if member not in playerinfo.keys():
        playerinfo[member] = Profile(member)
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
        return
    serverinfo[message.guild].recentchannel = message.channel
    if message.author not in playerinfo.keys():
        playerinfo[message.author] = Profile(message.author)
    message2 = str(message.content).upper()
    if message2[0]=='!' and len(message2)>1:
        if "|" in message2:
            c=message2.split("|")[0]
        else:
            c=message2
        for command in commands:
            if command.Name == c:
                client.loop.create_task(command.Execute(message,message2,serverinfo,playerinfo))
                return
        recommendations=difflib.get_close_matches(c[1:],(c.Name[1:] for c in commands))
        rec_msg="Unable to find and execute `{0}`.".format(c)
        rec=False
        if len(recommendations)==1:
            rec=True
            rec_msg+=" Did you mean `!{0}`?".format(recommendations[0])
        elif len(recommendations)>1:
            rec=True
            rec_msg+=" Did you mean to use one of these commands?\n`!{0}`".format('\n!'.join(recommendations))
        if rec:
            await message.channel.send(rec_msg)

client.run(TOKEN)
