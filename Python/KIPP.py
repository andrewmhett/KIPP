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
        global MSG_COUNTER
        MSG_COUNTER=MSG_COUNTER+1
        if message.guild != None or str(message.channel).upper=="DIRECT MESSAGE":
            if message.author.id in serverinfo[message.guild].blocked:
                await client.delete_message(message)
                return
        if str(message.channel).upper().startswith('DIRECT MESSAGE') == False:
            serverinfo[message.guild].recentchannel = message.channel
        if str(message.guild) != "None":
            user = message.guild.get_member(KIPP_ID)
            playerinfo[message.author].game = str(message.author.activity)
        else:
            return
        kippservers = 0
        roles = []
        for server in client.guilds:
            for member in server.members:
                if member == message.author:
                    kippservers=kippservers+1
        if str(message.guild) != "None":
            playerinfo[message.author].nickname = str(message.author.nick)
            playerinfo[message.author].highestrole = message.author.top_role
            role1 = discord.utils.get(message.author.guild.roles, name=str(playerinfo[message.author].highestrole))
            playerinfo[message.author].hrolecolor = role1.colour
            playerinfo[message.author].numkippservers = kippservers
        weekint = datetime.today().weekday()
        if weekint == 0:
            weekday = "Monday"
        if weekint == 1:
            weekday = "Tuesday"
        if weekint == 2:
            weekday = "Wednesday"
        if weekint == 3:
            weekday = "Thursday"
        if weekint == 4:
            weekday = "Friday"
        if weekint == 5:
            weekday = "Saturday"
        if weekint == 6:
            weekday = "Sunday"
        year = ((str(datetime.now())[0])+(str(datetime.now())[1])+(str(datetime.now())[2])+(str(datetime.now())[3]))
        month = ((str(datetime.now())[5])+(str(datetime.now())[6]))
        day = ((str(datetime.now())[8])+(str(datetime.now())[9]))
        minute = ((str(datetime.now())[14])+(str(datetime.now())[15]))
        if (int((str(datetime.now())[11])+(str(datetime.now())[12]))>12) or (int((str(datetime.now())[11])+(str(datetime.now())[12])) == 12):
            timeBinary = 1
            if int((str(datetime.now())[11])+(str(datetime.now())[12]))>12:
                hour = str(int((str(datetime.now())[11])+(str(datetime.now())[12]))-12)
            else:
                hour = str(int((str(datetime.now())[11])+(str(datetime.now())[12])))
        else:
            hour = ((str(datetime.now())[11])+(str(datetime.now())[12]))
            timeBinary = 0
        if str(hour) == "00":
            hour = "12"
        if str(month) == "01":
            strmonth = "January"
        if str(month) == "02":
            strmonth = "February"
        if str(month) == "03":
            strmonth = "March"
        if str(month) == "04":
            strmonth = "April"
        if str(month) == "05":
            strmonth = "May"
        if str(month) == "06":
            strmonth = "June"
        if str(month) == "07":
            strmonth = "July"
        if str(month) == "08":
            strmonth = "August"
        if str(month) == "09":
            strmonth = "September"
        if str(month) == "10":
            strmonth = "October"
        if str(month) == "11":
            strmonth = "November"
        if str(month) == "12":
            strmonth = "December"
        if day == "11" or day == "12" or str(day) == "13" or (str(day).endswith('1') == False and day != "11") or (str(day).endswith('2') == False and str(day) != "12") or (str(day).endswith('3') == False and day != "13"):
            ending = "th"
        if str(day).endswith("1") and str(day) != "11":
            ending = "st"
        if str(day).endswith("2") and str(day) != "12":
            ending = "nd"
        if str(day).endswith("3") and str(day) != "13":
            ending = "rd"
        if str(day).startswith('0'):
            day = str(day)
            day = day.split('0')[1]
        global profooter
        if timeBinary == 0:
            profooter = ("KIPP | "+weekday+" "+strmonth+" "+str(day)+ending+", "+str(year)+" at "+hour+":"+minute+" AM")
        if timeBinary == 1:
            profooter = ("KIPP | "+weekday+" "+strmonth+" "+str(day)+ending+", "+str(year)+" at "+hour+":"+minute+" PM")
        message2 = str(message.content).upper()
        if message.author == client.user:
            return
        if message.guild.get_member(KIPP_ID).mention in message2:
            await message.channel.send("What do you want? Use **!help** for the commands.")
        if message2.startswith("!HELP|"):
            found=False
            for command in commands:
                search=message2.split("|")[1]
                if "!" not in search:
                    search="!"+search
                    if command.Name==search:
                        emb=discord.Embed(title="Help for {0}".format(command.Name),description=command.Help[0],colour=EMBEDCOLOR)
                        emb.set_footer(text=profooter)
                        await message.channel.send( embed=emb)
                        found=True
            if found==False:
                await message.channel.send("Sorry, but I couldn't find a registered command with that name.")
        else:
            if "|" in message2:
                c=message2.split("|")[0]
            else:
                c=message2
            for command in commands:
                if command.Name == c:
                    await command.Execute[0](message,message2)
        if message2 == ('!HELP'):
            misc=[]
            musc=[]
            sc=[]
            kc=[]
            oo=[]
            for c in commands:
                if isinstance(c,MISC):
                    misc.append(c.Name)
                elif isinstance(c,MUSC):
                    musc.append(c.Name)
                elif isinstance(c,SCIN):
                    sc.append(c.Name)
                elif isinstance(c,KIPC):
                    kc.append(c.Name)
                elif isinstance(c,OWON):
                    oo.append(c.Name)
            em = discord.Embed(title='Help',description="**Use !Help|command for command-specific information**",colour=EMBEDCOLOR)
            em.add_field(name="Miscellaneous",value="```"+"\n".join(misc)+"```")
            em.add_field(name="Music",value="```"+"\n".join(musc)+"```")
            em.add_field(name="Scientific",value="```"+"\n".join(sc)+"```")
            if str(message.guild.id) == '451227721545285649':
                em.add_field(name="Meema Only",value="```"+"\n".join(oo)+"```")
            else:
                em.add_field(name="Owner Only",value="```"+"\n".join(oo)+"```")
            em.add_field(name="KIPPCOINS",value="```"+"\n".join(kc)+"```")
            em.set_footer(text=profooter)
            await message.channel.send(embed=em)
    client.loop.run_until_complete(client.start(TOKEN))
