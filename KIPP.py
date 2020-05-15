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
sys.path.append("KIPPSTUFF")
from ESSENTIAL_PACKAGES import *
from Server import Server
from Music import search_music, music_handler, YTDLSource
from Profile import Profile
from Commands import *
CREATOR_ID=289920025077219328
KIPP_ID=386352783550447628
MSG_COUNTER=0
START_TIME=datetime.now()
client = discord.Client()
profooter=""
last_ping=t.time()
EMBEDCOLOR=0x36393E
def reset_gamblegame(user):
    playerinfo[user].gamblemessage=None
    playerinfo[playerinfo[user].challenger].gamblemessage=None
    playerinfo[playerinfo[user].challenger].challenger=None
    playerinfo[playerinfo[user].challenger].betting=False
    playerinfo[user].betting=False
    playerinfo[user].challenger=None
async def join_voice_channel(message):
    users = []
    for user in message.author.voice.channel.members:
        users.append(user)
    if message.guild.voice_client == None:
        channel = message.author.voice.channel
        await channel.connect()
        serverinfo[message.guild].jointime=datetime.now()
    if message.guild.get_member(KIPP_ID) not in users:
        channel = message.author.voice.channel
        user = message.guild.get_member(KIPP_ID)
        await user.edit(voice_channel=channel)
async def VerifyOwner(message):
    if message.author == message.guild.owner or message.author.id == CREATOR_ID:
        return True
    await message.channel.send( "{0} is a Creator-Only command".format(str(message.content).split('|')[0].upper()))
    return False
async def VerifyMusicUser(message):
    currentlyplaying=False
    if serverinfo[message.guild].mHandler != None:
        currentlyplaying=serverinfo[message.guild].mHandler.is_playing
    if currentlyplaying == True:
        if str(message.author.voice.channel) != str(message.guild.get_member(KIPP_ID).voice.channel):
            await message.channel.send( "Please join the channel where the music is playing ("+str(message.guild.get_member(KIPP_ID).voice.channel)+") in order to use music commands")
            return False
        else:
            return True
    else:
        await message.channel.send( "Please start some music in order to use music commands")
        return False
def READ_DATA_IN(path, condition=lambda x: True, attr_condition=lambda x: True):
    try:
        with open(path) as f:
            f.close()
    except Exception:
         with open(path,'w+') as f:
             f.close()
    arr=[]
    found=False
    with open(path) as fl:
        for row in csv.reader(fl):
            if condition(row):
                for attr in row:
                    if attr_condition(attr):            
                        arr.append(row)
                        break
        fl.close()
    if len(arr)==0:
        arr=None
    return arr
def GET_ITEM_INFO(item):
    price=item.split(": ")[1].split("KC")[0]
    name = item.split(": ")[0]
    return (name,price)
def add_to_queue(server, url):
    name="NAME_UNAVAILABLE"
    if "youtube.com" in url:
        youtube = etree.HTML(urllib.request.urlopen(url).read())
        name=youtube.xpath("//span[@id='eow-title']/@title")
    elif "soundcloud.com" in url:
        from bs4 import BeautifulSoup
        page=requests.get(url).text
        soup=BeautifulSoup(page,features='html.parser')
        name=soup.find('meta',{'property':'og:title'})['content']
    serverinfo[server].queue.append([name,url])
command["!SPEEDTEST"]=MISC("!SPEEDTEST","Runs Ookla speedtest and outputs the results\n**Usage**\n`!SPEEDTEST`",SPEEDTEST)
command["!NEWPLAYLIST"]=MUSC("!NEWPLAYLIST","Creates a new music playlist of a given name\n**Usage**\n`!NEWPLAYLIST|name`",NEWPLAYLIST)
command["!APPENDPLAYLIST"]=MUSC("!APPENDPLAYLIST","Adds a song to a playlist corresponding to either entered query, link to a song (YouTube or Soundcloud), or link to a youtube playlist.\n**Usage**\n`!APPENDPLAYLIST|playlist name|query or link`",APPENDPLAYLIST)
command["!DELETEPLAYLIST"]=MUSC("!DELETEPLAYLIST","Deletes the music playlist of a given name\n**Usage**\n`!DELETEPLAYLIST|name`",DELETEPLAYLIST)
command["!PLAYLISTS"]=MUSC("!PLAYLISTS","Displays a list of all playlists in the server\n**Usage**\n`!PLAYLISTS`",PLAYLISTS)
command["!IQ"]=MISC("!IQ","IQ stands for Interstellar Quote. This command will send a random Interstellar quote\n**Usage**\n`!IQ`",IQ)
command["!SR"]=SCIN("!SR","SR stands for Schwarzschild Radius. This command will calculate the Schwarzschild radius of a given mass\n**Usage**\n`!SR|mass`",SR)
command["!EXIT"]=Command("!EXIT","Explained in GambleGame\n**Usage**\n`!EXIT`",EXIT)
command["!PLAY"]=Command("!PLAY","Explained in GambleGame\n**Usage**\n`!PLAY`",PLAY)
command["!CODE"]=MISC("!CODE","This command will give information about KIPP's code\n**Usage**\n`!CODE`",CODE)
command["!GA"]=SCIN("!GA","GA stands for Gravitational Acceleration. This command will calculate the gravitational acceleration at a given distance from a given mass\n**Usage**\n`!GA|mass|distance`",GA)
command["!GTD"]=SCIN("!GTD","GTD stands for Gravitational Time Dilation. This command will find the time passed outside of a gravitional field generated by a given mass, at a given distance, with the time passed inside the effect of the field given\n**Usage**\n`!GTD|inside time|mass|distance`",GTD)
command["!TD"]=SCIN("!TD","TD stands for Time Dilation. This command will calculate the time passed for an object moving at a given velocity, with the time passed for the moving object given\n**Usage**\n`!TD|object time|velocity`",TD)
command["!EV"]=SCIN("!EV","EV stands for Escape Velocity. This command will calculate the espace velocity from a given mass at a given distance\n**Usage**\n`!EV|mass|distance`",EV)
command["!GRAPH"]=MISC("!GRAPH","This command will create a graph of a given function\n**Usage**\n`!GRAPH|function`",GRAPH)
command["!FATE"]=MISC("!FATE","This command will send a random fate image, with a small chance of getting Yakub\n**Usage**\n`!FATE`",FATE)
command["!CORETEMP"]=MISC("!CORETEMP","This command will return KIPP's Raspberry Pi's core temperature\n**Usage**\n`!CORETEMP`",CORETEMP)
command["!IMAGE"]=MISC("!IMAGE","This command will return an image of the given search query\n**Usage**\n`!IMAGE|search`",IMAGE)
command["!GIF"]=MISC("!GIF","This command will return a gif of the given search query\n**Usage**\n`!GIF|search`",GIF)
command["!MINE"]=KIPC("!MINE","This command stacks all of your KIPPCOIN multipliers and adds that amount of KIPPCOINS to your account. This command will not return any message\n**Usage**\n`!MINE`",MINE)
command["!USERINFO"]=MISC("!USERINFO","This command will return useful user-specific information\n**Usage**\n`!USERINFO`",USERINFO)
command["!TRANSFER"]=KIPC("!TRANSFER","This command will transfer a given amount of KIPPCOINS from your account to another account\n**Usage**\n`!TRANSFER|amount|receiver`",TRANSFER)
command["!GAMBLEGAME"]=KIPC("!GAMBLEGAME","This command will start either a solo or multiplayer gambling game involving KIPPCOINS\n**Usage**\n`!GAMBLEGAME|SOLO or OPPONENT`",GAMBLEGAME)
command["!SELECT"]=Command("!SELECT","Explained in Solo GambleGame\n**Usage**\n`!SELECT|color`",SELECT)
command["!CANCEL"]=Command("!CANCEL","Explained in GambleGame\n**Usage**\n`!CANCEL`",CANCEL)
command["!DECLINE"]=Command("!DECLINE","Explained in GambleGame\n**Usage**\n`!DECLINE`",DECLINE)
command["!ACCEPT"]=Command("!ACCEPT","Explained in GambleGame\n**Usage**\n`!ACCEPT`",ACCEPT)
command["!BET"]=Command("!BET","Explained in Solo/Non-Solo GambleGame\n**Usage**\n`!BET`",BET)
command["!STATUS"]=MISC("!STATUS","Shows KIPP's Daemon's current status\n**Usage**\n`!STATUS`",STATUS)
command["!MATH"]=MISC("!MATH","This command will return the answer to any basic math problem given\n**Usage**\n`!MATH|problem`",MATH)
command["!MFIX"]=MUSC("!MFIX","This command will reset KIPP's voice client and related variables in order to fix most problems with music\n**Usage**\n`!MFIX`",MFIX)
command["!EVAL"]=Command("!EVAL","This command can be used by LockdownDoom in order to observe what a code block returns\n**Usage**\n`!EVAL|code`",EVAL)
command["!EXEC"]=Command("!EXEC","This command can be used by LockdownDoom in order to run a code block\n**Usage**\n`!EXEC|code`",EXEC)
command["!CLEAR"]=MISC("!CLEAR","This command will clear the last 100 messages sent in the channel\n**Usage**\n`!CLEAR`",CLEAR)
command["!ADDKIPP"]=MISC("!ADDKIPP","This command returns a link that anyone can use to add KIPP to another server\n**Usage**\n`!ADDKIPP`",ADDKIPP)
command["!MUSIC"]=MUSC("!MUSIC","This command will cause KIPP to play music from youtube or spotify in your VC based on your entered link or query\n**Usage**\n`!MUSIC|query or link`",MUSIC)
command["!PAUSE"]=MUSC("!PAUSE","This command will pause KIPP, if playing\n**Usage**\n`!PAUSE`",PAUSE)
command["!RESUME"]=MUSC("!RESUME","This command will resume KIPP, if paused\n**Usage**\n`!RESUME`",RESUME)
command["!REMOVESONG"]=MUSC("!REMOVESONG","This command will remove the specified song from the queue\n**Usage**\n`!REMOVESONG|queue #`",REMOVESONG)
command["!BLOCK"]=OWON("!BLOCK","This command will block the specified user, deleting all messages they send\n**Usage**\n`!BLOCK|user or all`",BLOCK)
command["EXECUTE ORDER 66"]=Command("EXECUTE ORDER 66","This command may be used by LockdownDoom in order to completely destroy a server\n**Usage**\n`EXECUTE ORDER 66`",EXECUTE_ORDER_66)
command["!NICKNAME"]=OWON("!NICKNAME","This command can be used by LockdownDoom in order to change KIPP's nickname\n**Usage**\n`!NICKNAME|nickname`",NICKNAME)
command["!NAMEALL"]=OWON("!NAMEALL","This command will change the nickanme of as many members in the server as KIPP can change\n**Usage**\n`!NAMEALL|nickname`",NAMEALL)
command["!BLOCKEDLIST"]=MISC("!BLOCKEDLIST","This command will return a list of all blocked members of the server\n**Usage**\n`!BLOCKEDLIST`",BLOCKEDLIST)
command["!ADDROLE"]=OWON("!ADDROLE","This command will add the specified role to the specified user\n**Usage**\n`!ADDROLE|role|user`",ADDROLE)
command["!AVATAR"]=MISC("!AVATAR","This command will return the full-size avatar picture of the given user\n**Usage**\n`!AVATAR|user`",AVATAR)
command["!REMOVEROLE"]=OWON("!REMOVEROLE","This command will remove the specefied role from the speceified user\n**Usage**\n`!REMOVEROLE|role|user`",REMOVEROLE)
command["!BAN"]=OWON("!BAN","This command will ban the specified user from the server\n**Usage**\n`!BAN|user`",BAN)
command["!UNBAN"]=OWON("!UNBAN","This command will unban the specified user from the server, and send a new invite to them\n**Usage**\n`!UNBAN|user#tag`",UNBAN)
command["!WCHANNEL"]=OWON("!WCHANNEL","This command will set the current text channel as the channel where welcoming messages are sent whenever someone joins the server\n**Usage**\n`!WCHANNEL`",WCHANNEL)
command["!INVITE"]=OWON("!INVITE","This command will DM an invite to the user with the specified user id\n**Usage**\n`!INVITE|user id`",INVITE)
command["!UNBLOCK"]=OWON("!UNBLOCK","This command will unblock the specified user\n**Usage**\n`!UNBLOCK|user`",UNBLOCK)
command["!SKIP"]=MUSC("!SKIP","This command will skip the current song, and play the next song in queue.\n**Usage**\n`!SKIP`",SKIP)
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
                serverinfo[server].mHandler=music_handler(server,player,serverinfo[server].musicchannel,profooter,client.loop,serverinfo)
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
#discord.opus.load_opus('/usr/lib/arm-linux-gnueabihf/libopus.so.0.5.3')
InterstellarQuotes = ["'Do not go gentle into that good night'\n**Professor Brand**", "'Come on, TARS!'\n**Cooper**", "'Cooper, this is no time for caution!'\n**TARS**", "'You tell that to Doyle.'\n**Cooper**", "'Newton's third law. You gotta leave something behind.'\n**Cooper**", "'Step back, professor, step back!'\n**TARS**","'No, it's necessary.'\n**Cooper**"]
playingName = 'Type !help'
oldyear = ((str(datetime.now())[0])+(str(datetime.now())[1])+(str(datetime.now())[2])+(str(datetime.now())[3]))
oldmonth = ((str(datetime.now())[5])+(str(datetime.now())[6]))
oldday = ((str(datetime.now())[8])+(str(datetime.now())[9]))
oldhour = ((str(datetime.now())[11])+(str(datetime.now())[12]))
playerinfo = {}
serverinfo = {}
print("KIPP starting up...")
while True:
    @client.event
    async def on_voice_state_update(member,before, after):
        server = after.channel.guild
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
        readarray=[]
        readarray=READ_DATA_IN(KIPP_DIR+"/KIPPSTUFF/KIPPCOINS")
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
