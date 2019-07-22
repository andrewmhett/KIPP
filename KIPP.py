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
sys.path.append('./KIPPSTUFF')
from ESSENTIAL_PACKAGES import *
CREATOR_ID="289920025077219328"
KIPP_ID="386352783550447628"
CREATOR_ONLY_COMMANDS = ["EXECUTE ORDER 66",
                         "!NICKNAME",
                         "!EXEC",
                         "!EVAL",
                         "!INVITE",
                         "!NAMEALL",
                         "!IMPEACHMEEMA"]
OWNER_ONLY_COMMANDS = ["!BLOCK",
                       "!BLOCKEDLIST",
                       "!ADDROLE",
                       "!REMOVEROLE",
                       "!BAN",
                       "!UNBAN",
                       "!UNBLOCK",
                       "!WCHANNEL",
                       "!TWITCHCHANNEL"]
commands=[]
command={}
client = discord.Client()
profooter=""
last_ping=t.time()
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '192.168.0.1',
    'usenetrc': True,
    'download': False
}
storeitems=[
"2x income multiplier: 50KC",
"4x income multiplier: 1000KC",
"10x income multiplier: 10000KC",
"100x income multiplier: 75000KC"
]
EMBEDCOLOR=0x36393E
class Server:
    def __init__(self,server):
        self.server=server
        self.paused = False
        self.musictextchannel = None
        self.playing = ""
        self.everyoneleft = False
        self.title = ""
        self.length = ""
        self.thumbnail = ""
        self.player = None
        self.volume = 0.5
        self.blocked = []
        self.starttime = ""
        self.musicmessage = None
        self.musicdesc = ""
        self.musicfooter = ""
        self.pausetime = 0
        self.pausedatetime = None
        self.imagelink = ""
        self.duration=0
        self.count=0
        self.count1=0
        self.gamgamestarter = None
        self.gamgameopp = None
        self.recentchannel=None
        self.musiccolor=None
        self.queue = []
        self.election=False
        self.sElectiontime = None
        self.electionmessage = None
        self.can1=None
        self.can2=None
        self.can1votes=0
        self.can2votes=0
        self.voters=[]
        self.messagesent=[]
        self.oldtime=0
        self.r6role=None
        self.d2role=None
    def add_server_config(self,data):
        try:
            with open('/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}'.format(self.server.id)) as f:
                f.close()
        except Exception:
             with open('/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}'.format(self.server.id),'w+') as f:
                 f.close()
        arr=[]
        with open("/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}".format(self.server.id)) as fl:
            for row in csv.reader(fl):
                arr.append(row)
            arr.append(data)
            fl.close()
        with open('/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}'.format(self.server.id),'w') as f:
            writer=csv.writer(f)
            for row in arr:
                writer.writerow(row)
            f.close()
    def change_server_config(self,data,newdata):
        try:
            with open('/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}'.format(self.server.id)) as f:
                f.close()
        except Exception:
             with open('/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}'.format(self.server.id),'w+') as f:
                 f.close()
        arr=[]
        with open("/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}".format(self.server.id)) as fl:
            for row in csv.reader(fl):
                arr.append(row)
            cntr=0
            for row in arr:
                if data in str(row):
                    arr[cntr] = newdata
                    break
                cntr=cntr+1
            fl.close()
        with open('/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}'.format(self.server.id),'w') as f:
            writer=csv.writer(f)
            for row in arr:
                writer.writerow(row)
            f.close()
    def search_server_configs(self,query):
        data=None
        try:
            with open('/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}'.format(self.server.id)) as f:
                f.close()
        except Exception:
            with open('/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}'.format(self.server.id),'w+') as f:
                f.close()
        with open('/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}'.format(self.server.id)) as fl:
            for row in csv.reader(fl):
                if query in str(row):
                    data=row
            fl.close()
        return data
class Profile:
    def __init__(self,user):
        self.gamblemessage=None
        self.bet=None
        self.solo=False
        self.color=None
        self.gamblerequest=False
        self.challenger=None
        self.betting=False
        self.numkippservers = 0
        self.game = ""
        self.highestrole = ""
        self.nickname = ""
        self.hrolecolor = None
        self.streaming = False
        self.user = user
        self.instore=False
        self.storepage=None
        with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS') as fl:
            reader=csv.reader(fl)
            infile=False
            readarray=[]
            for row in reader:
                readarray.append(row)
                if(row[0] == self.user.id):
                    infile=True
            if infile==False:
                readarray.append((str(self.user.id),0))
                with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS','w') as f:
                    writer=csv.writer(f)
                    for row in readarray:
                        writer.writerow(row)
                    f.close()
            fl.close()
    def GET_KIPPCOINS(self):
        with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS') as fl:
            reader=csv.reader(fl)
            for row in reader:
                if row[0] == str(self.user.id):
                    return row[1]
            fl.close()
    def HAS_ITEM(self,item):
        with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS') as fl:
            reader=csv.reader(fl)
            for row in reader:
                if str(row[0]) == str(self.user.id):
                    if item in row:
                        return True
                    else:
                        return False
            fl.close()
    def GIVE_KIPPCOINS(self, KC):
        readarray=[]
        with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS') as fl:
            reader=csv.reader(fl)
            for row in reader:
                readarray.append(row)
            for row in readarray:
                if row[0] == str(self.user.id):
                    orig=int(row[1])
                    row[1] = orig+int(KC)
            fl.close()
        with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS','w') as f:
            writer=csv.writer(f)
            for row in readarray:
                writer.writerow(row)
            f.close()
    def GIVE_ITEM(self, item):
        readarray=[]
        with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS') as fl:
            reader=csv.reader(fl)
            for row in reader:
                readarray.append(row)
            for row in readarray:
                if row[0] == str(self.user.id):
                    row.append(item)
            fl.close()
        with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS','w') as f:
            writer=csv.writer(f)
            for row in readarray:
                writer.writerow(row)
            f.close()
class Command():
    def __init__(self,n,h,e):
        global commands
        self.Help=h,
        self.Execute=e,
        self.Name=n
        commands.append(self)
class MISC(Command):
    pass
class OWON(Command):
    pass
class KIPC(Command):
    pass
class MUSC(Command):
    pass
class SCIN(Command):
    pass
class HISO(Command):
    pass
async def ping_check():
    global last_ping
    while True:
        if t.time()-last_ping>2:
            for l in asyncio.Task.all_tasks(loop=client.loop):
                if "background_loop" in str(l):
                    l.cancel()
            client.loop.create_task(background_loop())
        await asyncio.sleep(1)
async def VerifyOwnerMeema(message):
    if str(message.server.id) == "451227721545285649":
        role = discord.utils.get(message.server.roles, name="meema")
        if role in message.author.roles:
            return True
    if message.author == message.server.owner or str(message.author.id) == CREATOR_ID:
        return True
    if str(message.server.id) == "451227721545285649":
        await client.send_message(message.channel, "{0} is a Meema-Only command".format(str(message.content).split('|')[0].upper()))
        return False
    elif str(message.server.id) != "451227721545285649":
        await client.send_message(message.channel, "{0} is a Creator-Only command".format(str(message.content).split('|')[0].upper()))
        return False
async def VerifyMusicUser(message):
    player = serverinfo[message.server].player
    try:
        if player.is_playing() == True:
            serverinfo[message.server].paused = False
        if player.is_playing() == False:
            serverinfo[message.server].paused = True
    except AttributeError:
        pass
    try:
        player = serverinfo[message.server].player
        str(int(player.volume*100))
        currentlyplaying = True
    except AttributeError:
        currentlyplaying = False
    if currentlyplaying == True:
        if str(message.author.voice.voice_channel) != str(message.server.get_member(KIPP_ID).voice.voice_channel):
            await client.send_message(message.channel, "Please join the channel where the music is playing ("+str(message.server.get_member(KIPP_ID).voice.voice_channel)+") in order to use these commands:\n**!CLEARQUEUE**\n**!SKIP**\n**!SETVOL**\n**!PAUSE**\n**!RESUME**")
            return False
        else:
            return True
    else:
        await client.send_message(message.channel, "Please start some music in order to use these commands:\n**!CLEARQUEUE**\n**!SKIP**\n**!GETVOL**\n**!SETVOL**\n**!PAUSE**\n**!RESUME**")
        return False
def GET_ITEM_INFO(item):
    price=item.split(": ")[1].split("KC")[0]
    name = item.split(": ")[0]
    return (name,price)
def add_to_queue(server, url):
    youtube = etree.HTML(urllib.request.urlopen(url).read())
    name=youtube.xpath("//span[@id='eow-title']/@title")
    serverinfo[server].queue.append([name,url])
def add_chat_log(message):
    if message.author.bot:
        return
    if str(message.channel).upper().startswith('DIRECT MESSAGE') == False:
        try:
            with open('/home/pi/Desktop/KIPPSTUFF/ChatLogs/{0}'.format(message.server.id)) as f:
                f.close()
        except Exception:
             with open('/home/pi/Desktop/KIPPSTUFF/ChatLogs/{0}'.format(message.server.id),'w+') as f:
                 f.close()
        arr=[]
        with open("/home/pi/Desktop/KIPPSTUFF/ChatLogs/{0}".format(message.server.id)) as fl:
            for row in csv.reader(fl):
                arr.append(row)
            arr.append([str(datetime.today().date()),message.author.id,str(message.content)])
            fl.close()
        with open('/home/pi/Desktop/KIPPSTUFF/ChatLogs/{0}'.format(message.server.id),'w') as f:
            writer=csv.writer(f)
            for row in arr:
                writer.writerow(row)
            f.close()
def search_chat_log(message,query):
    arr=[]
    try:
        with open('/home/pi/Desktop/KIPPSTUFF/ChatLogs/{0}'.format(message.server.id)) as f:
            f.close()
    except Exception:
        with open('/home/pi/Desktop/KIPPSTUFF/ChatLogs/{0}'.format(message.server.id),'w+') as f:
            f.close()
    with open('/home/pi/Desktop/KIPPSTUFF/ChatLogs/{0}'.format(message.server.id)) as fl:
        for row in csv.reader(fl):
            for attr in row:
                if query.upper() in str(attr).upper():
                    arr.append(row)
        fl.close()
    return arr
async def IQ(message,message2):
    arrlen = int(len(InterstellarQuotes))
    quoteNum = SystemRandom().randrange(0,arrlen)
    description = str(InterstellarQuotes[quoteNum])
    em = discord.Embed(title="Interstellar Quote",description=description,colour=EMBEDCOLOR)
    em.set_footer(text=profooter)
    await client.send_message(message.channel, embed=em)
async def SR(message,message2):
    mass = str(message.content).split('|')[1].replace('^', '**')
    calc = (2*(eval('6.67*10**-11'))*(eval(mass)))/eval('299792458**2')
    await client.send_message(message.channel, "The Schwarzschild Radius of an object with a mass of "+str(mass).replace('**','^')+" kg is: "+str(calc)+" m")
async def EXIT(message,message2):
    if playerinfo[message.player].betting==True:
        playerinfo[message.author].gamblerequest=False
        emb=discord.Embed(title="GambleGame",description="GAME ENDED",colour=EMBEDCOLOR)
        emb.set_footer(text=profooter)
        await client.edit_message(playerinfo[message.author].gamblemessage,embed=emb)
        playerinfo[message.author].gamblemessage=None
        playerinfo[playerinfo[message.author].challenger].gamblemessage=None
        playerinfo[playerinfo[message.author].challenger].challenger=None
        playerinfo[playerinfo[message.author].challenger].betting=False
        playerinfo[message.author].betting=False
        playerinfo[message.author].challenger=None
async def PLAY(message,message2):
    if playerinfo[message.author].solo == True and playerinfo[message.author].bet != None:
        rand=SystemRandom().randrange(1,4)
        color=["Red","Blue","Green","Black"][rand]
        if color == playerinfo[message.author].color:
            emb = discord.Embed(title="Solo GambleGame",description="Selected Color: **{0}**\nActual Color: **{1}**\nYou gain `{2} KC`".format(playerinfo[message.author].color,color,playerinfo[message.author].bet),colour=EMBEDCOLOR)
            emb.set_footer(text=profooter)
            playerinfo[message.author].GIVE_KIPPCOINS(int(playerinfo[message.author].bet))
        if color != playerinfo[message.author].color:
            emb = discord.Embed(title="Solo GambleGame",description="Selected Color: **{0}**\nActual Color: **{1}**\nYou lose `{2} KC`".format(playerinfo[message.author].color,color,playerinfo[message.author].bet),colour=EMBEDCOLOR)
            emb.set_footer(text=profooter)
            playerinfo[message.author].GIVE_KIPPCOINS(-1*int(playerinfo[message.author].bet))
        await client.edit_message(playerinfo[message.author].gamblemessage,embed=emb)
        await client.delete_message(message)
        playerinfo[message.author].bet=None
        playerinfo[message.author].color=None
        playerinfo[message.author].solo=False
    else:
        if playerinfo[message.author].bet == playerinfo[playerinfo[message.author].challenger].bet and playerinfo[message.author].betting==False:
            rand=SystemRandom().randrange(1,3)
            if rand==1:
                winner=message.author
            else:
                winner=playerinfo[message.author].challenger
            emb=discord.Embed(title="GambleGame",description="Winner: **{2}**\n`+{0} KC`\n\nLoser: **{1}**\n`-{0} KC`".format(playerinfo[message.author].bet,playerinfo[winner].challenger,winner),colour=EMBEDCOLOR)
            emb.set_footer(text=profooter)
            await client.edit_message(playerinfo[message.author].gamblemessage,embed=emb)
            playerinfo[winner].GIVE_KIPPCOINS(int(playerinfo[message.author].bet))
            playerinfo[playerinfo[winner].challenger].GIVE_KIPPCOINS(-1*int(playerinfo[message.author].bet))
            playerinfo[message.author].gamblemessage=None
            playerinfo[playerinfo[message.author].challenger].gamblemessage=None
            playerinfo[playerinfo[message.author].challenger].challenger=None
            playerinfo[playerinfo[message.author].challenger].betting=False
            playerinfo[message.author].betting=False
            playerinfo[message.author].challenger=None
async def CODE(message,message2):
    from subprocess import Popen, PIPE
    p=Popen('/home/pi/Desktop/KIPPSTUFF/NewestCommit.sh',stdout=PIPE,stderr=PIPE)
    stdout=p.communicate()[0]
    p.kill()
    try:
        await client.send_message(message.channel,"{0} My code is backed up on GitHub here: https://github.com/LockdownDoom/KIPP/blob/master/KIPP.py\nAlso, my code has been reviewed by Codacy here: https://app.codacy.com/project/LockdownDoom/KIPP/dashboard?branchId=10423847".format('Newest commit:\n```\n'+stdout.decode()[64:]+'\n```\n'))
    except discord.DiscordException:
        await client.send_message(message.channel,"{0} My code is backed up on GitHub here: https://github.com/LockdownDoom/KIPP/blob/master/KIPP.py\nAlso, my code has been reviewed by Codacy here: https://app.codacy.com/project/LockdownDoom/KIPP/dashboard?branchId=10423847".format('Newest commit:\nThe newest commit is too large to be displayed here.'))
async def GA(message,message2):
    mass = str(message.content).split('|')[1].replace('^', '**')
    dist = str(message.content).split('|')[2].replace('^', '**')
    calc = (eval('6.67*10**-11')*eval(mass))/(eval(dist)**2)
    await client.send_message(message.channel, "The gravitational acceleration towards an object with a mass of "+str(mass).replace('**','^')+" kg at a distance of "+str(dist)+"m is: "+str(calc)+' m/s^2')
async def GTD(message,message2):
    from math import sqrt
    oldtime = str(message.content).split('|')[1].replace('^', '**')
    mass = str(message.content).split('|')[2].replace('^', '**')
    distance = str(message.content).split('|')[3].replace('^', '**')
    calc=float(oldtime)/(sqrt(1-((2*(eval('6.67*10**-11'))*(eval(str(mass))))/((eval(str(distance)))*(eval('299792458**2'))))))
    await client.send_message(message.channel, "If the time passed for the observer inside of this gravity field was {0} seconds, and the mass of the object creating the gravity is {1} kg, and the observer's distance away from the center of the object creating the gravity is {2} m, the time passed outside the gravity field would be {3} seconds.".format(str(eval(str(oldtime))),str(mass),str(eval(str(distance))),str(eval(str(calc)))).replace('**','^'))
async def TD(message,message2):
    from math import sqrt
    oldtime = str(message.content).split('|')[1].replace('^', '**')
    velocity = str(message.content).split('|')[2].replace('^', '**')
    try:
        calc = float(oldtime)/(sqrt(1-eval(str((float(velocity)/299792458)**2))))
    except ZeroDivisionError:
        calc=0
    if calc != 0:
        await client.send_message(message.channel, 'If the local time is passed is '+str(oldtime)+' seconds, the non-local time passed for an object travelling '+str(velocity)+' m/s would be '+str(calc)+' seconds.')
    else:
        await client.send_message(message.channel, 'Ah hah. Hah hah hah. You tried to trick me! Surely you must know that when you travel the speed of light, zero local time passes while you travel an infinite distance!')
async def EV(message,message2):
    from math import sqrt
    mass = str(message.content).split('|')[1].replace('^', '**')
    dist = str(message.content).split('|')[2].replace('^', '**')
    calc = sqrt((2*eval('6.67*10**-11')*eval(mass))/eval(str(dist)))
    await client.send_message(message.channel, 'The escape velocity from an object with a mass of '+str(mass).replace('**','^')+' kg at a distance of '+str(dist)+' m is: '+str(calc)+' m/s')
async def GRAPH(message,message2):
    img = Image.new('RGB', (1000,1000), "black")
    new=img.load()
    for x in range (0,1000):
        for y in range (0,1000):
            if x == 500:
                new[x,y] = (255,0,0)
            if y == 500:
                new[x,y] = (255,0,0)
    for curx in range(-500,501):
        newfunc=str(message.content).split('|')[1].lower().replace('x','('+str(curx)+')')
        try:
            if eval(newfunc)<500 and eval(newfunc)>-500:
                new[curx+500,(int(eval(newfunc)*-1))+500] = (255,255,255)
        except Exception as err:
            print(err)
    img.save('graph.png')
    with open ('graph.png','rb') as f:
        await client.send_file(message.channel, f)
async def FATE(message,message2):
    imgs=os.listdir("/home/pi/Desktop/KIPPSTUFF/FATE")
    arrlen = int(len(imgs))
    picNum = SystemRandom().randrange(0,arrlen)
    yakub=False
    if "YAKUB" in imgs[picNum].upper():
        yakub=True
    with open("/home/pi/Desktop/KIPPSTUFF/FATE/"+imgs[picNum], 'rb') as f:
        await client.send_file(message.channel, f)
        f.close()
    if yakub==True:
        msg = "You will see Yakub. You will live."
        await client.send_message(message.channel, msg)
    else:
        msg = "You will die."
        await client.send_message(message.channel, msg)
async def CORETEMP(message,message2):
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    await client.send_message(message.channel, '{:.2f}'.format( float(cpu)/1000 ) + ' C')
async def CATORDOG(message,message2):
    link=str(message.content).split('|')[1]
    from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
    predictor = CustomVisionPredictionClient('205c6f54f37e49c08592092e4a980ea0', endpoint="https://southcentralus.api.cognitive.microsoft.com")
    results = predictor.predict_image_url('a98ab5cb-4615-4e6b-8a67-df44bbf7d62d', url=link)
    if results.predictions[0].probability<0.9:
        await client.send_message(message.channel,"I cannot identify this as a cat or a dog.")
    else:
        prediction = results.predictions[0]
        await client.send_message(message.channel,"\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))
async def R6(message,message2):
    await web_command(message,message2)
async def D2(message,message2):
    await web_command(message,message2)
async def ELECTION(message,message2):
    if message.author == message.server.owner:
        if str(message.server.id) == "451227721545285649":
            serverinfo[message.server].voters = []
            serverinfo[message.server].can1votes = 0
            serverinfo[message.server].can2votes = 0
            try:
                cand1 = message.server.get_member_named(message.content.split('|')[1])
                cand2 = message.server.get_member_named(message.content.split('|')[2])
            except Exception:
                await client.send_message(message.channel, "You must specify at least two candidates to start an election.")
            if str(cand1.top_role) == "The People" and str(cand2.top_role) == "The People":
                emb = discord.Embed(title="Election",description="Candidate 1: "+str(cand1)+"\n**Votes: 0**\n\nCandidate 2: "+str(cand2)+"\n**Votes: 0**\n\n**Time Left: 15 minutes**",colour=EMBEDCOLOR)
                serverinfo[message.server].electionmessage = await client.send_message(message.channel, embed=emb)
                serverinfo[message.server].sElectiontime = datetime.now()
                serverinfo[message.server].can1=cand1
                serverinfo[message.server].can2=cand2
                serverinfo[message.server].election = True
                serverinfo[message.server].oldtime=0
                for member in message.server.members:
                    if member.bot==False:
                        if message.server.role_hierarchy.index(member.top_role)>2 and member != cand1 and member != cand2 and (str(member.status).upper() == "ONLINE" or str(member.status) == "idle") :
                            try:
                                await client.send_message(member, "An election has started in The Hierarchical Society. Please respond to this message by typing **1** or **2**. Candidate 1 is {0}, and candidate 2 is {1}.".format(str(cand1),str(cand2)))
                                serverinfo[message.server].voters.append(member)
                                serverinfo[message.server].messagesent.append(member)
                            except discord.DiscordException:
                                pass
            else:
                await client.send_message(message.channel, "Both candidates' highest roles must be 'The People' in order for them to be in an election.")
async def IMAGE(message,message2):
    await web_command(message, message2)
async def GIF(message,message2):
    await web_command(message,message2)
async def MINE(message,message2):
    mult = 1
    if playerinfo[message.author].HAS_ITEM("2x income multiplier") == True:
        mult = mult*2
    if playerinfo[message.author].HAS_ITEM("4x income multiplier") == True:
        mult = mult*4
    if playerinfo[message.author].HAS_ITEM("10x income multiplier") == True:
        mult = mult*10
    if playerinfo[message.author].HAS_ITEM("100x income multiplier") == True:
        mult = mult*100
    playerinfo[message.author].GIVE_KIPPCOINS(mult)
async def USERINFO(message,message2):
    description = "**Mutual servers with KIPP:** "+str(playerinfo[message.author].numkippservers)+"\n**Currently Playing:** "+str(playerinfo[message.author].game)+"\n**Highest role in Server:** "+str(playerinfo[message.author].highestrole)+"\n**Nickname in Server:** "+playerinfo[message.author].nickname+"\n**KIPPCOINS:** "+str(playerinfo[message.author].GET_KIPPCOINS())
    em = discord.Embed(description=description,colour=EMBEDCOLOR)
    em.set_author(name=str(message.author)+"'s User Info", icon_url=message.author.avatar_url)
    em.set_footer(text=profooter)
    await client.send_message(message.channel, embed=em)
async def STORE(message,message2):
    if playerinfo[message.author].instore ==True:
        playerinfo[message.author].instore = True
        em = discord.Embed(title="Store",description="Store closed",colour=EMBEDCOLOR)
        em.set_footer(text=profooter)
        await client.edit_message(playerinfo[message.author].storepage,embed=em)
    in_budget=[]
    out_budget=[]
    items=[]
    itemnum=1
    for item in storeitems:
        items.append(GET_ITEM_INFO(item))
    for item in items:
        name,price=item
        if int(price) <= int(playerinfo[message.author].GET_KIPPCOINS()):
            if playerinfo[message.author].HAS_ITEM(name) == False:
                in_budget.append([item,itemnum])
        else:
            if playerinfo[message.author].HAS_ITEM(name) == False:
                out_budget.append([item,itemnum])
        itemnum=itemnum+1
    desc=""
    if len(in_budget)>0:
        desc="**IN BUDGET:**\n"
        for item in in_budget:
            print(item)
            desc=desc+"`#{0}` **{1}**  `{2} KC`\n".format(item[1],item[0][0],item[0][1])
    if len(out_budget)>0:
        if len(desc) == 0:
            desc="**OUT OF BUDGET:**\n"
        else:
            desc=desc+"\n**OUT OF BUDGET:**\n"
        for item in out_budget:
            desc=desc+"`#{0}` **{1}**  `{2} KC`\n".format(item[1],item[0][0],item[0][1])
    if len(out_budget)>0 or len(in_budget)>0:
        desc=desc+"\nUse **!buy|item_number** to buy an item\nUse **!Close** to exit the store"
        emb = discord.Embed(title="Store",description="**YOUR KC** `{0}`\n\n".format(playerinfo[message.author].GET_KIPPCOINS())+desc,colour=EMBEDCOLOR)
    else:
        desc="You have all of the items currently in the store. More items will be added soon."
        emb = discord.Embed(title="Store",description=desc,colour=EMBEDCOLOR)
    emb.set_footer(text=profooter)
    playerinfo[message.author].storepage = await client.send_message(message.channel, embed=emb)
    playerinfo[message.author].instore=True
async def BUY(message,message2):
    if playerinfo[message.author].instore==True:
        items=[]
        for item in storeitems:
            items.append(GET_ITEM_INFO(item))
        itemnum=1
        try:
            for item in items:
                name,price=item
                if itemnum == int(message2.split('|')[1]):
                    if int(price) <= int(playerinfo[message.author].GET_KIPPCOINS()):
                        if playerinfo[message.author].HAS_ITEM(name) == False:
                            playerinfo[message.author].GIVE_KIPPCOINS(int(price)*-1)
                            em=discord.Embed(title="Store",description="Transaction Complete.\nYou now have **{0}** KIPPCOINS".format(playerinfo[message.author].GET_KIPPCOINS()),colour=EMBEDCOLOR)
                            await client.edit_message(playerinfo[message.author].storepage,embed=em)
                            playerinfo[message.author].GIVE_ITEM(name)
                            playerinfo[message.author].instore=False
                itemnum=itemnum+1
        except Exception:
            await client.send_message(message.channel,"Make sure that you type **!Buy|item_number** to purchase an item. The number is listed to the left of the item's name.")
            playerinfo[message.author].instore=False
            em = discord.Embed(title="Store",description="Store closed",colour=EMBEDCOLOR)
            em.set_footer(text=profooter)
            await client.edit_message(playerinfo[message.author].storepage,embed=em)
async def TRANSFER(message,message2):
    try:
        patron=message.author
        amount=message2.split("|")[1]
        receiver=message.server.get_member_named(str(message.content).split("|")[2])
    except Exception as err:
        if err == IndexError:
            await client.send_message(message.channel, "Make sure you specify both an amount and a receiver.")
        else:
            await client.send_message(message.channel, "The receiver could not be found.")
    if int(amount)<=int(playerinfo[patron].GET_KIPPCOINS()) and int(amount)>0:
        playerinfo[patron].GIVE_KIPPCOINS(-1*int(amount))
        playerinfo[receiver].GIVE_KIPPCOINS(int(amount))
        emb = discord.Embed(title="Transfer",description="Transferred **{0}** KIPPCOINS to **{1}**'s account.\n You now have **{2}** KIPPCOINS.".format(amount,str(receiver),int(playerinfo[patron].GET_KIPPCOINS())),colour=EMBEDCOLOR)
        emb.set_footer(text=profooter)
        await client.send_message(message.channel,embed=emb)
    else:
        await client.send_message(message.channel,"The amount entered was either higher than the amount of KIPPCOINS you have, or was negative.")
async def CLOSE(message,message2):
    if playerinfo[message.author].instore == True:
        em = discord.Embed(title="Store",description="Store closed",colour=EMBEDCOLOR)
        em.set_footer(text=profooter)
        await client.edit_message(playerinfo[message.author].storepage,embed=em)
        playerinfo[message.author].instore=False
async def INVENTORY(message,message2):
    desc=""
    for item in storeitems:
        if playerinfo[message.author].HAS_ITEM(GET_ITEM_INFO(item)[0]):
            desc=desc+"\n**"+GET_ITEM_INFO(item)[0]+"**"
    if playerinfo[message.author].HAS_ITEM("|LEI| KIPP year I plaque"):
        desc=desc+"\n**KIPP year I plaque**\n\
---------------\n\
-**KIPP year I**-\n\
---------------"
    if len(desc)==0:
        desc = "You don't have any items. You can purchase items by buying with KIPPCOINS in **!Store**."
    emb = discord.Embed(title="Inventory",description=desc,colour=EMBEDCOLOR)
    emb.set_footer(text=profooter)
    await client.send_message(message.channel,embed=emb)
async def GAMBLEGAME(message,message2):
    if message2.split('|')[1] == "SOLO":
        playerinfo[message.author].solo = True
        emb = discord.Embed(title="Solo GambleGame",description="Use **!SELECT|color** to choose a color:\n**Red**\n**Blue**\n**Green**\n**Black**",colour=EMBEDCOLOR)
        emb.set_footer(text=profooter)
        message1=await client.send_message(message.channel,embed=emb)
        playerinfo[message.author].gamblemessage=message1
    else:
        try:
            opponent=message.server.get_member_named(str(message.content).split("|")[1])
        except Exception:
            await client.send_message(message.channel,"This user does not exist.")
        if str(opponent.status).upper != "OFFLINE" and str(opponent.status).upper != "IDLE":
            playerinfo[opponent].gamblerequest=True
            playerinfo[opponent].challenger=message.author
            playerinfo[message.author].challenger=opponent
            desc = "{0}, you have been challenged to a GambleGame by {1}.\n**!ACCEPT** or **!DECLINE**\n{2} may **!CANCEL**".format(opponent.mention,message.author.mention,message.author.mention)
            emb=discord.Embed(title="GambleGame Request",description = desc,colour=EMBEDCOLOR)
            emb.set_footer(text=profooter)
            message1 = await client.send_message(message.channel,embed=emb)
            playerinfo[message.author].gamblemessage=message1
            playerinfo[opponent].gamblemessage=message1
async def SELECT(message,message2):
    if playerinfo[message.author].solo == True:
        if (message2.split("|")[1] == "RED"
            or message2.split("|")[1] == "BLUE"
            or message2.split("|")[1] == "GREEN"
            or message2.split("|")[1] == "BLACK"):
            message1=message2.split("|")[1].lower()
            ms=list(message1)
            ms[0] = message2.split('|')[1][0]
            message1=""
            for i in ms:
                message1=message1+i
            playerinfo[message.author].color= message1
            await client.delete_message(message)
            emb = discord.Embed(title="Solo GambleGame",description="Color selected: **{0}**\nUse **!BET|KC** to bet KIPPCOINS\nAvailable KC: `{1}`".format(message1,str(playerinfo[message.author].GET_KIPPCOINS())),colour=EMBEDCOLOR)
            emb.set_footer(text=profooter)
            await client.edit_message(playerinfo[message.author].gamblemessage,embed=emb)
async def CANCEL(message,message2):
    if playerinfo[playerinfo[message.author].challenger].gamblerequest == True:
        emb=discord.Embed(title="GambleGame Request",description="CANCELLED",colour=EMBEDCOLOR)
        emb.set_footer(text=profooter)
        playerinfo[playerinfo[message.author].challenger].gamblerequest=False
        playerinfo[playerinfo[message.author].challenger].challenger=None
        playerinfo[message.author].challenger=None
        await client.edit_message(playerinfo[message.author].gamblemessage,embed=emb)
        playerinfo[playerinfo[message.author].challenger].gamblemessage=None
        playerinfo[message.author].gamblemessage=None
        await client.delete_message(message)
async def DECLINE(message,message2):
    if playerinfo[message.author].gamblerequest == True:
        emb=discord.Embed(title="GambleGame Request",description="DECLINED",colour=EMBEDCOLOR)
        emb.set_footer(text=profooter)
        playerinfo[message.author].gamblerequest=False
        playerinfo[message.author].gamblemessage=None
        playerinfo[playerinfo[message.author].challenger].gamblemessage=None
        playerinfo[message.author].challenger=Noneplayerinfo[playerinfo[message.author].challenger].gambplayerinfo[playerinfo[message.author].challenger].gamblemessage=None
        playerinfo[message.author].gamblemessage=None
        playerinfo[message.author].gamblemessage=None
        await client.edit_message(playerinfo[message.author].gamblemessage,embed=emb)
        await client.delete_message(message)
async def ACCEPT(message,message2):
    if playerinfo[message.author].gamblerequest == True:
        playerinfo[message.author].gamblerequest=False
        playerinfo[message.author].betting=True
        playerinfo[message.author].bet = 0
        playerinfo[playerinfo[message.author].challenger].bet = 0
        playerinfo[playerinfo[message.author].challenger].betting=True
        emb=discord.Embed(title="GambleGame",description="Game started.\nEach player must bet the same amount. Once this is done, the winner will be decided.\n\n**{0}**:\nKC Available `{1}`\nBet: **0**\n\n**{2}**:\nKC Available `{3}`\nBet: **0**\n\nUse **!BET|VALUE** to bet\nUse **!EXIT** to leave the game".format(message.author,str(playerinfo[message.author].GET_KIPPCOINS()),playerinfo[message.author].challenger,str(playerinfo[playerinfo[message.author].challenger].GET_KIPPCOINS())),colour=EMBEDCOLOR)
        emb.set_footer(text=profooter)
        await client.edit_message(playerinfo[message.author].gamblemessage,embed=emb)
        await client.delete_message(message)
async def BET(message,message2):
    if playerinfo[message.author].solo == True and playerinfo[message.author].color != None:
        amount= int(str(message.content).split("|")[1])
        if amount<=int(playerinfo[message.author].GET_KIPPCOINS()) and amount >0:
            playerinfo[message.author].bet = amount
            emb = discord.Embed(title="Solo GambleGame",description="Color: **{0}**\nBet: `{1} KC`\n**!PLAY**".format(playerinfo[message.author].color,str(playerinfo[message.author].bet)),colour=EMBEDCOLOR)
            emb.set_footer(text=profooter)
            await client.edit_message(playerinfo[message.author].gamblemessage,embed=emb)
        await client.delete_message(message)
    else:
        if playerinfo[message.author].betting==True:
            amount= int(str(message.content).split("|")[1])
            if amount<=int(playerinfo[message.author].GET_KIPPCOINS()) and amount >0:
                playerinfo[message.author].bet= amount
                if playerinfo[message.author].bet != playerinfo[playerinfo[message.author].challenger].bet:
                    if playerinfo[message.author].challenger != None:
                        emb=discord.Embed(title="GambleGame",description="Game started.\nEach player must bet the same amount. Once this is done, the winner will be decided.\n\n**{0}**:\nKC Available `{1}`\nBet: **{4}**\n\n**{2}**:\nKC Available `{3}`\nBet: **{5}**\n\nUse **!BET|VALUE** to bet\nUse **!EXIT** to leave the game".format(message.author,str(playerinfo[message.author].GET_KIPPCOINS()),playerinfo[message.author].challenger,str(playerinfo[playerinfo[message.author].challenger].GET_KIPPCOINS()),playerinfo[message.author].bet,playerinfo[playerinfo[message.author].challenger].bet),colour=EMBEDCOLOR)
                    else:
                        emb=discord.Embed(title="GambleGame",description="Game started.\nEach player must bet the same amount. Once this is done, the winner will be decided.\n\n**{2}**:\nKC Available `{3}`\nBet: **{5}**\n\n**{0}**:\nKC Available `{1}`\nBet: **{4}**\n\nUse **!BET|VALUE** to bet\nUse **!EXIT** to leave the game".format(message.author,str(playerinfo[message.author].GET_KIPPCOINS()),playerinfo[message.author].challenger,str(playerinfo[playerinfo[message.author].challenger].GET_KIPPCOINS()),playerinfo[message.author].bet,playerinfo[playerinfo[message.author].challenger].bet),colour=EMBEDCOLOR)
                elif playerinfo[message.author].bet == playerinfo[playerinfo[message.author].challenger].bet:
                    emb=discord.Embed(title="GambleGame",description="The agreed bet is "+str(amount)+" KIPPCOINS.\n\n**!PLAY** to decide the winner",colour=EMBEDCOLOR)
                    playerinfo[playerinfo[message.author].challenger].betting=False
                    playerinfo[message.author].betting=False
                emb.set_footer(text=profooter)
                message1=await client.edit_message(playerinfo[message.author].gamblemessage,embed=emb)
                playerinfo[message.author].gamblemessage=message1
            await client.delete_message(message)
async def STATUS(message,message2):
    from subprocess import Popen, PIPE
    p=Popen('/home/pi/Desktop/KIPPSTUFF/DaemonStatus.sh',stdout=PIPE,stderr=PIPE)
    stdout=p.communicate()[0].decode()
    p.kill()
    if "m" in stdout.split("ago")[0].split(";")[1] or "s" in stdout.split("ago")[0].split(";")[1]:
        await client.send_message(message.channel,"```"+stdout.decode().split('ago')[0]+"ago```")
async def IMPEACHREQUEST(message,message2):
    if str(message.server.id) == "451227721545285649":
        owner=message.server.owner
        role = discord.utils.get(message.server.roles, name="meema")
        for member in message.server.members:
            if role in member.roles:
                meema = member
        if len(str(message.content).split('|')[1])>0:
            await client.send_message(owner, "Impeachment request:\nMeema: {0}\nAuthor: {1}\nContent: {2}".format(str(meema),str(message.author),str(message.content).split('|')[1]))
            await client.send_message(message.channel, "An impeachment request for {0} has been filed by {1}:\n{2}".format(str(meema),str(message.author),str(message.content).split('|')[1]))
        else:
            await client.send_message(message.channel, "Please enter a valid request.")
async def IMPEACHMEEMA(message,message2):
    if str(message.server.id) == "451227721545285649":
        owner=message.server.owner
        if message.author == owner:
            role = discord.utils.get(message.server.roles, name="meema")
            for member in message.server.members:
                if role in member.roles:
                    meema = member
            await client.remove_roles(meema, role)
            await client.send_message(message.channel, "@everyone, the impeachment of {0} has been approved by {1}".format(meema.mention,owner.mention))
async def MATH(message,message2):
    mathP = str(message.content)
    mathP2 = mathP.split('|')
    math = str(mathP2[1])
    try:
        mathT = eval(math)
    except SyntaxError:
        await client.send_message(message.channel, "Sorry, KIPP failed to process this request.")
    msg = str(math)+" = "+str(mathT)
    await client.send_message(message.channel, msg)
async def MFIX(message,message2):
    await client.send_message(message.channel,"Resetting variables...")
    serverinfo[message.server].count=0
    try:
        serverinfo[message.server].player.stop()
    except Exception as err:
        print(err)
    serverinfo[message.server].player=None
    await client.send_message(message.channel,"Clearing queue...")
    serverinfo[message.server].queue = []
    await client.send_message(message.channel,"Resetting voice client...")
    try:
        await message.server.voice_client.disconnect()
    except Exception as err:
        print(err)
    await client.send_message(message.channel, "Done.")
async def EVAL(message,message2):
    if message.author.id == CREATOR_ID:
        try:
            await client.send_message(message.channel,eval(str(message.content).split('|')[1]))
        except Exception as err:
            await client.send_message(message.channel,err)
async def EXEC(message,message2):
    if message.author.id == CREATOR_ID:
        try:
            if 'await' in str(message.content):
                await eval(str(message.content).split('|')[1].replace('await ',''))
            else:
                exec(str(message.content).split('|')[1])
            await client.send_message(message.channel,'Passed without exception.')
        except Exception as err:
            if type(err) in KIPP_RESET_ERRORS:
                raise
            else:
                await client.send_message(message.channel,err)
async def SEARCHLOG(message,message2):
    results=[]
    await client.send_message(message.channel, "Searching server chat logs for messages related to **{0}**...".format(str(message.content).split("|")[1]))
    try:
        q=message.server.get_member_named(str(message.content).split('|')[1])
        results=search_chat_log(message,q.id)
    except Exception:
        results = search_chat_log(message,str(message.content).split('|')[1])
    msgs=""
    try:
        limit=int(message2.split('|')[2])
    except Exception:
        limit=0
    i=-2
    if limit != 0:
        results=results[-limit:]
    try:
        try:
            for msg in results:
                if i<limit-1:
                    if limit!=0:
                        i=i+1
                    usr=message.server.get_member(msg[1])
                    if usr==None:
                        usr=await client.get_user_info(msg[1])
                    msgs=msgs+"\n{0} by {1}: {2}".format(msg[0],str(usr),msg[2])
            await client.send_message(message.channel,"Search results for query: **{0}**\n{1}".format(str(message.content).split('|')[1],msgs))
        except TypeError:
            await client.send_message(message.channel, "No results for query: **{0}**".format(str(message.content).split('|')[1]))
    except discord.errors.HTTPException as e:
        await client.send_message(message.channel, "Too many results to display in message. Consider adding a limit to the number of results.")
        print(e)
    if len(results)==0:
        await client.send_message(message.channel, "No results for query: **{0}**".format(str(message.content).split('|')[1]))
async def CLEAR(message,message2):
    mgs = []
    async for x in client.logs_from(message.channel, limit = 100):
        mgs.append(x)
    try:
        await client.delete_messages(mgs)
    except Exception:
        for i in mgs:
            await client.delete_message(i)
async def ADDKIPP(message,message2):
    msg = 'https://discordapp.com/oauth2/authorize?client_id=386352783550447628&permissions=2146958583&scope=bot'
    await client.send_message(message.channel, msg)
async def MUSIC(message,message2):
    server=message.server
    notsearched = False
    serverinfo[message.server].musictextchannel = message.channel
    try:
        player = serverinfo[message.server].player
        str(int(player.volume*100))
        currentlyplaying = True
    except AttributeError:
        currentlyplaying = False
    if (currentlyplaying == False) or (currentlyplaying == True and message.author.voice.voice_channel == message.server.get_member(KIPP_ID).voice.voice_channel):
        try:
            global loading
            if (message2.split('!MUSIC')[1]).startswith('|') == True:
                if loading == False:
                    loading = True
                    player = (serverinfo[message.server].player)
                    loading = True
                    music2 = str(message.content)
                    music3 = music2.split('|')
                    music4= music3[1]
                    serverinfo[server].musictextchannel = message.channel
                    serverinfo[message.server].paused = False
                    if "&index" in music4:
                        music4 = music4.split('&index')
                        music4 = music4[0]
                    if music4.startswith("https://youtu.be"):
                        music4 = music4.split('youtu.be/')[1]
                        music4 = "https://www.youtube.com/watch?v="+music4
                    if str(message.author.voice.voice_channel) != "None":
                        if ((music4.startswith("https://www.youtube.com") == False) and (music4.startswith("https://youtu.be") == False) and (music4.startswith("http://www.youtube.com") == False)):
                            try:
                                query_string = urllib.parse.urlencode({"search_query" : music4})
                                req = urllib.request.Request("http://www.youtube.com/results?" + query_string)
                                with urllib.request.urlopen(req) as html:
                                    searchresults = re.findall(r'href=\"\/watch\?v=(.{11})', html.read().decode())
                                music4 = ("http://www.youtube.com/watch?v=" + searchresults[0])
                            except IndexError:
                                await client.send_message(message.channel, ("Could not find '"+music4+"' on YouTube."))
                                loading = False
                                notsearched = True
                        server = message.server
                        if notsearched == False:
                            if ((music3[0]).upper() == "!MUSIC"):
                                if (music4.startswith("https://www.youtube.com") or music4.startswith("https://youtu.be") or music4.startswith("http://www.youtube.com")):
                                    if "user" not in music4:
                                        serverinfo[message.server].musiccolor=playerinfo[message.author].hrolecolor
                                        users = []
                                        for user in message.author.voice.voice_channel.voice_members:
                                            users.append(user)
                                        if message.server.voice_client == None:
                                            channel = message.author.voice.voice_channel
                                            await client.join_voice_channel(channel)
                                        if message.server.get_member(KIPP_ID) not in users:
                                            channel = message.author.voice.voice_channel
                                            user = message.server.get_member(KIPP_ID)
                                            await client.move_member(user, channel)
                                        add_to_queue(message.server, music4)
                                        try:
                                            if serverinfo[message.server].player != None:
                                                if len(serverinfo[message.server].queue)>1:
                                                    await client.send_message(message.channel, "Song added to queue. #"+str(len(serverinfo[message.server].queue)-1))
                                            loading=False
                                        except AttributeError:
                                            pass
                                        if len(serverinfo[message.server].queue) == 1:
                                            message.server.voice_client.encoder_options(sample_rate=48000,channels=2)
                                            player = await message.server.voice_client.create_ytdl_player(music4,before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5")
                                            player.start()
                                            serverinfo[message.server].count=1
                                            player.volume = serverinfo[message.server].volume
                                            serverinfo[message.server].player = player
                                            serverinfo[message.server].playing = player.title
                                            length = player.duration
                                            for channel in server.channels:
                                                if str(channel.user_limit) != "None":
                                                    if channel == message.author.voice.voice_channel:
                                                        if serverinfo[message.server].player.is_live == False:
                                                            mins=int(length/60)
                                                            seconds=int(length-(mins*60))
                                                            hours=int(mins/60)
                                                            if hours > 0:
                                                                mins=mins-(hours*60)
                                                                if len(str(mins))==1:
                                                                    mins="0"+str(mins)
                                                                if len(str(seconds)) == 1:
                                                                    length=str(hours)+":"+str(mins)+":"+"0"+str(seconds)
                                                                else:
                                                                    length=str(hours)+":"+str(mins)+":"+str(seconds)
                                                            else:
                                                                if len(str(seconds)) == 1:
                                                                    length=str(mins)+":"+"0"+str(seconds)
                                                                else:
                                                                    length=str(mins)+":"+str(seconds)
                                                        else:
                                                            length = "Currently Streaming"
                                                        serverinfo[message.server].length = length
                                                        msg3 = ("["+str(serverinfo[message.server].playing)+"]("+music4+")\n**Progress:**: `0:00 / "+str(length)+"`\n**Volume:** "+str(serverinfo[message.server].player.volume))
                                                        em = discord.Embed(description=msg3,colour=EMBEDCOLOR)
                                                        em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
                                                        video_id = music4.split("watch?v=")[1]
                                                        thumbnail = "https://img.youtube.com/vi/"+video_id+"/0.jpg"
                                                        #em.set_thumbnail(url=thumbnail)
                                                        serverinfo[message.server].thumbnail = thumbnail
                                                        em.set_footer(text=profooter)
                                                        serverinfo[server].musicmessage = await client.send_message(message.channel, embed=em)
                                                        serverinfo[message.server].starttime = datetime.now()
                                                        serverinfo[message.server].musicdesc = msg3
                                                        serverinfo[message.server].musicfooter = profooter
                                                        serverinfo[message.server].pausetime = 0
                                                        serverinfo[message.server].imagelink = thumbnail
                                                        serverinfo[message.server].duration = player.duration
                                                        serverinfo[message.server].length = str(length)
                                                        loading = False
                                    else:
                                        await client.send_message(message.channel, "Please do not try to play an entire youtube channel. Get one specific song you would like to hear, and play that.")
                                        loading = False
                                else:
                                    msg = "The music must come from YouTube"
                                    await client.send_message(message.channel, msg)
                                    loading = False
                    else:
                        await client.send_message(message.channel, "You are not in a voice channel. Get in one for KIPP to play music.")
                        loading = False
                else:
                    await client.delete_message(message)
            else:
                await client.send_message(message.channel, "Please use the correct syntax. Use !music|youtubelink or !music|youtubesearch to use the music command.")
                loading = False
        except Exception as err:
            loading = False
            await client.send_message(message.channel, err)
            raise
    elif (currentlyplaying == True) and (message.author.voice.voice_channel != message.server.get_member(KIPP_ID).voice.voice_channel):
        await client.send_message(message.channel, "There is a song currently playing in another voice channel ("+str(message.server.get_member(KIPP_ID).voice.voice_channel)+"). Join that voice channel in order to change the music, or you can wait for that music to end, and run this command again.")
async def MONO(message,message2):
    if await VerifyMusicUser(message):
        message.server.voice_client.encoder_options(sample_rate=48000,channels=1)
        await client.send_message(message.channel, 'Audio set to mono. Audio will be set back to stereo before next song.')
async def SKIP(message,message2):
    player = serverinfo[message.server].player
    if await VerifyMusicUser(message):
        import datetime as d
        if serverinfo[message.server].paused == True:
            player.resume()
            serverinfo[message.server].paused = False
        serverinfo[message.server].starttime=serverinfo[message.server].starttime-d.timedelta(seconds=serverinfo[message.server].player.duration)
        if len(serverinfo[message.server].queue)==1:
            await client.send_message(message.channel, "There are no more songs in the queue. Current song ended.")
async def STEREO(message,message2):
    if await VerifyMusicUser(message):
        message.server.voice_client.encoder_options(sample_rate=48000,channels=2)
        await client.send_message(message.channel, 'Audio set to stereo.')
async def REMOVESONG(message,message2):
    if await VerifyMusicUser(message):
        try:
            index = int(message2.split("|")[1])
        except Exception:
            await client.send_message(message.channel, "Song index must be an integer.")
        if len(serverinfo[message.server].queue)>1:
            if index >0 and index <= len(serverinfo[message.server].queue):
                serverinfo[message.server].queue.remove(serverinfo[message.server].queue[index])
                await client.send_message(message.channel, "Removed song #{0} from queue".format(index))
            else:
                await client.send_message(message.channel,"Invalid song index")
        else:
            await client.send_message(message.channel,"There are no songs in the queue.")
async def SETVOL(message,message2):
    if await VerifyMusicUser(message):
        player = serverinfo[message.server].player
        vol = player.volume
        try:
            if (int(message2.split('|')[1])<101 and int(message2.split('|')[1])>-1) and str(message.server.id) != '329449782160654336' and str(message.server.id) != '451227721545285649':
                vol = int(message2.split('|')[1])
                player.volume = vol/100
                serverinfo[message.server].volume = player.volume
                await client.send_message(message.channel, "Volume set to "+str(int(player.volume*100))+"%.")
            elif str(message.server.id) == '451227721545285649':
                vol = int(message2.split('|')[1])
                player.volume = vol/100
                serverinfo[message.server].volume = player.volume
                if int(player.volume*100) < 101:
                    await client.send_message(message.channel, "Volume set to "+str(int(player.volume*100))+"%.")
                elif int(player.volume*100) > 100:
                    await client.send_message(message.channel, "Server exclusive ability: Volume set to "+str(int(player.volume*100))+"%.")
            else:
                await client.send_message(message.channel, "Invalid volume. Volume must be from 0% to 100%. (Don't use '%' in command)")
        except ValueError:
            await client.send_message(message.channel, "Invalid setting. Volume must be an integer from 0-100.")
async def PAUSE(message,message2):
    if await VerifyMusicUser(message):
        player = serverinfo[message.server].player
        if serverinfo[message.server].paused == False:
            player.pause()
            serverinfo[message.server].paused = True
            await client.send_message(message.channel, "Music paused.")
        else:
            await client.send_message(message.channel, "Music already is paused. To resume, use the **!resume** command.")
async def RESUME(message,message2):
    if await VerifyMusicUser(message):
        player = serverinfo[message.server].player
        if serverinfo[message.server].paused == True:
            player.resume()
            await client.send_message(message.channel, "Music resumed.")
            serverinfo[message.server].paused = False
        else:
            await client.send_message(message.channel, "There is currently music playing. To pause the music, use the **!pause** command.")
async def BLOCK(message,message2):
    if await VerifyOwnerMeema(message):
        owner = message.server.owner
        blockedP = str(message.content)
        blockedP2 = blockedP.split('|')
        if blockedP2[1].upper() != "ALL":
            blockedP2[1] = message.server.get_member_named(str(blockedP2[1]))
        if str(blockedP2[1]) != "None":
            if str(blockedP2[1]).upper() == "ALL":
                for member in message.server.members:
                    if str(member) not in serverinfo[message.server].blocked:
                        if (member.id != CREATOR_ID) and (str(member) != "KIPP#4780") and (member != owner):
                            serverinfo[message.server].blocked.append(member.id)
                await client.send_message(message.channel, "Blocked everyone in server")
            elif blockedP2[1].id != CREATOR_ID and blockedP2[1] != owner and blockedP2[1].id != KIPP_ID:
                if blockedP2[1].id in serverinfo[message.server].blocked:
                    await client.send_message(message.channel, "User already blocked.")
                elif blockedP2[1].id not in serverinfo[message.server].blocked:
                    serverinfo[message.server].blocked.append(blockedP2[1].id)
                    msg =("Blocked "+str(blockedP2[1])).format(message)
                    await client.send_message(message.channel, msg)
            elif blockedP2[1].id == CREATOR_ID:
                msg = "Why would I block my own creator?"
                await client.send_message(message.channel, msg)
            elif blockedP2[1] == message.author:
                await client.send_message(message.channel, "Why would you want to block yourself?")
            elif blockedP2[1] == message.server.get_member(KIPP_ID):
                await client.send_message(message.channel, "Why would I block myself?")
        else:
            await client.send_message(message.channel, "This user is not in this server. Make sure that you used the command like this: '!block|nickname OR !block|username'.")
async def EXECUTE_ORDER_66(message,message2):
    if str(message.author.id) == CREATOR_ID:
        server = message.server
        channels = []
        members = []
        roles = []
        for channel in server.channels:
            channels.append(channel)
        for channel in channels:
            await client.delete_channel(channel)
        for role in server.roles:
            if str(role) != "@everyone":
                roles.append(role)
        for member in server.members:
            if str(member) != "KIPP#4780":
                if member.id != CREATOR_ID:
                    members.append(member)
        for member in members:
            try:
                await client.ban(member)
            except discord.DiscordException:
                try:
                    await client.kick(member)
                except discord.DiscordException:
                    pass
        for role in roles:
            try:
                try:
                    await client.delete_role(role)
                except discord.DiscordException:
                    pass
            except TypeError:
                pass
async def NICKNAME(message,message2):
    if str(message.author.id) == CREATOR_ID:
        nickname = str(message.content).split('|')[1]
        for member in message.server.members:
            if str(member) == "KIPP#4780":
                try:
                    await client.change_nickname(member, nickname)
                    await client.send_message(message.channel, "Successfully changed nickname to "+str(nickname)+".")
                except discord.DiscordException:
                    await client.send_message(message.channel, "KIPP does not have permission to change his nickname.")
async def NAMEALL(message,message2):
    if await VerifyOwnerMeema(message):
        try:
            uchanged = 0
            for member in message.server.members:
                if str(member) != "KIPP#4780" and member.id != CREATOR_ID:
                    try:
                        await client.change_nickname(member, str(message.content.split("|")[1]))
                        uchanged = uchanged+1
                    except discord.DiscordException:
                        pass
        except discord.DiscordException:
            await client.send_message(message.channel, "Could not change some nicknames")
        if uchanged == 1:
            await client.send_message(message.channel, "Changed "+str(uchanged)+" nickname")
        if uchanged != 1:
            await client.send_message(message.channel, "Changed "+str(uchanged)+" nicknames")
async def BLOCKEDLIST(message,message2):
    if len(serverinfo[message.server].blocked)>0:
        names=[]
        for i in serverinfo[message.server].blocked:
            try:
                names.append("**"+str(message.server.get_member(i))+"**")
            except discord.DiscordException:
                try:
                    names.append("**"+str(await client.get_user_info(i))+"**")
                except Exception:
                    print("Couldn't find user.")
        blocked=", ".join(names)
        await client.send_message(message.channel, "The users currently blocked in this server are: "+blocked)
    else:
        await client.send_message(message.channel, "There are no users currently blocked in this server. To block a user, use the **!block** command.")
async def ADDROLE(message,message2):
    if await VerifyOwnerMeema(message):
        user = str(message.content).split('|')[2]
        rolechange = str(message.content).split('|')[1]
        user = message.server.get_member_named(user)
        role = discord.utils.get(user.server.roles, name=str(rolechange))
        if str(role) != "None":
            try:
                await client.add_roles(user, role)
                await client.send_message(message.channel, "Successfully added the role '"+str(rolechange)+"' to "+str(user)+"'s roles")
            except discord.DiscordException:
                await client.send_message(message.channel, "Either this role is above KIPP's role, or KIPP doesn't have enough permissions to do this.")
        else:
            await client.send_message(message.channel, "This role doesn't exist. Check the capital letters in the role, and make sure they are the same as what you enter.")
async def AVATAR(message,message2):
    member = str(message.content).split('|')[1]
    member = message.server.get_member_named(member)
    await client.send_message(message.channel, str(member)+"'s icon URL is: "+str(member.avatar_url))
async def REMOVEROLE(message,message2):
    if await VerifyOwnerMeema(message):
        user1 = str(message.content).split('|')[2]
        rolechange = str(message.content).split('|')[1]
        user = message.server.get_member_named(user1)
        role = discord.utils.get(user.server.roles, name=str(rolechange))
        if str(role) != "None":
            try:
                await client.remove_roles(user, role)
                await client.send_message(message.channel, "Successfully removed the role '"+str(rolechange)+"' from "+str(user)+"'s roles.")
            except discord.DiscordException:
                await client.send_message(message.channel, "Either this role is above KIPP's role, or KIPP doesn't have enough permissions to do this.")
        else:
            await client.send_message(message.channel, "This role doesn't exist. Check the capital letters in the role, and make sure they are the same as what you enter.")
async def BAN(message,message2):
    if await VerifyOwnerMeema(message):
        banuser = str(message.content).split('|')[1]
        banuser = message.server.get_member_named(banuser)
        try:
            try:
                await client.ban(banuser)
                await client.send_message(message.channel, "Successfully banned "+str(banuser)+" from "+str(message.server)+".")
            except discord.DiscordException:
                await client.send_message(message.channel, "KIPP does not have permission to ban "+str(banuser)+", or this user is already banned")
        except AttributeError:
            await client.send_message(message.channel, "This user is already banned, or this user is not in the server. Make sure that you used the command like this: '!ban|nickname OR !ban|username'.")
async def UNBAN(message,message2):
    if await VerifyOwnerMeema(message):
        if '#' in message2:
            unbanuser = str(message.content).split('|')[1]
            banned = await client.get_bans(message.server)
            for user in banned:
                if '#' in str(unbanuser):
                    if str(user.name) == str(unbanuser).split('#')[0]:
                        unbanuser1 = user.id
                        unbanuser = await client.get_user_info(unbanuser1)
                else:
                    unbanuser1 = user.id
                    unbanuser = await client.get_user_info(unbanuser1)
            try:
                try:
                    await client.unban(message.server, unbanuser)
                    await client.send_message(message.channel, "Successfully unbanned "+str(unbanuser)+" from "+str(message.server)+".")
                    try:
                        invite = await client.create_invite(message.channel, max_uses=1)
                        await client.send_message(unbanuser, "You have been unbanned from the server '"+str(message.server)+"'. Here is an invite to the server.\n"+str(invite))
                        await client.send_message(message.channel, "Successfully sent an invite to "+str(unbanuser))
                    except discord.DiscordException:
                        await client.send_message(message.channel, "Failed to re-invite "+str(unbanuser)+" to the server.")
                except discord.DiscordException:
                    await client.send_message(message.channel, "KIPP does not have permission to unban "+str(unbanuser)+", or this user is not banned.")
            except AttributeError:
                await client.send_message(message.channel, "This user is not banned.")
        else:
            await client.send_message(message.channel, "Make sure you use '!unban|username#tag'.")
async def WCHANNEL(message,message2):
    if await VerifyOwnerMeema(message):
        if serverinfo[message.server].search_server_configs("WELCOME_CHANNEL") != None:
            if serverinfo[message.server].search_server_configs("WELCOME_CHANNEL")[1] == message.channel.id:
                await client.send_message(message.channel,"This channel already is the welcome channel.")
            else:
                serverinfo[message.server].change_server_config("WELCOME_CHANNEL",["WELCOME_CHANNEL",message.channel.id])
                await client.send_message(message.channel,"Changed the welcome channel to this text channel.")
        else:
            serverinfo[message.server].add_server_config(["WELCOME_CHANNEL",message.channel.id])
            await client.send_message(message.channel,"Set this text channel as the welcome channel. All joining users will be welcomed here.")
    ##                    if message2 == "!TWITCHCHANNEL":
    ##                        if serverinfo[message.server].search_server_configs("TWITCH_CHANNEL") != None:
    ##                            if serverinfo[message.server].search_server_configs("TWITCH_CHANNEL")[1] == message.channel.id:
    ##                                await client.send_message(message.channel,"This channel already is the Twitch announcement channel.")
    ##                            else:
    ##                                serverinfo[message.server].change_server_config("TWITCH_CHANNEL",["TWITCH_CHANNEL",message.channel.id])
    ##                                await client.send_message(message.channel,"Changed the Twitch announce channel to this text channel.")
    ##                        else:
    ##                            serverinfo[message.server].add_server_config(["TWITCH_CHANNEL",message.channel.id])
    ##                            await client.send_message(message.channel,"Set this text channel as the Twitch announcement channel. When a member of the server starts streaming, it will be announced here.")
async def INVITE(message,message2):
    if await VerifyOwnerMeema(message):
        unbanuser = str(message.content).split('|')[1]
        unbanuser = await client.get_user_info(unbanuser)
        try:
            invite = await client.create_invite(message.channel, max_uses=1)
            await client.send_message(unbanuser, "You have been invited to the server '"+str(message.server)+"'. Here is the invite to the server.\n"+str(invite))
            await client.send_message(message.channel, "Successfully sent an invite to "+str(unbanuser))
        except discord.DiscordException:
            await client.send_message(message.channel, "Failed to invite "+str(unbanuser)+" to the server.")
async def UNBLOCK(message,message2):
    if await VerifyOwnerMeema(message):
        unblocked1 = str(message.content).split('|')
        unblocked = unblocked1[1]
        if unblocked.upper() != "ALL":
            unblocked = message.server.get_member_named(unblocked)
        if str(unblocked).upper() == "ALL":
            serverinfo[message.server].blocked=[]
            await client.send_message(message.channel, "Unblocked everyone in server")
        if (unblocked.id not in serverinfo[message.server].blocked) and (str(unblocked).upper() != "ALL"):
            msg = "User not blocked."
            await client.send_message(message.channel, msg)
        elif unblocked.id in serverinfo[message.server].blocked:
            msg = "Unblocked "+str(unblocked)
            serverinfo[message.server].blocked.remove(unblocked.id)
            await client.send_message(message.channel, msg)
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
command["!R6"]=Command("!R6","This command will return Rainbow Six Siege stats on a given user, on a given platform\n**Usage**\n`Currently unavailable`",R6)
command["!D2"]=MISC("!D2","This command will return Destiny 2 on a given user, on a given platform\n**Usage**\n`!D2|platform (XBOX or PC)|user`",D2)
command["!ELECTION"]=HISO("!ELECTION","This command can be used by LockdownDoom in The Hierarchical Society in order to start a new election for meema\n**Usage**\n`!ELECTION|candidate 1|candidate 2`",ELECTION)
command["!IMAGE"]=MISC("!IMAGE","This command will return an image of the given search query\n**Usage**\n`!IMAGE|search`",IMAGE)
command["!GIF"]=MISC("!GIF","This command will return a gif of the given search query\n**Usage**\n`!GIF|search`",GIF)
command["!MINE"]=KIPC("!MINE","This command stacks all of your KIPPCOIN multipliers and adds that amount of KIPPCOINS to your account. This command will not return any message\n**Usage**\n`!MINE`",MINE)
command["!USERINFO"]=MISC("!USERINFO","This command will return useful user-specific information\n**Usage**\n`!USERINFO`",USERINFO)
command["!STORE"]=KIPC("!STORE","This command will open a store session, where you can spend KIPPCOINS on multipliers (more items coming in the future)\n**Usage**\n`!STORE`",STORE)
command["!BUY"]=Command("!BUY","Explained in Store\n**Usage**\n`!BUY|row number`",BUY)
command["!TRANSFER"]=KIPC("!TRANSFER","This command will transfer a given amount of KIPPCOINS from your account to another account\n**Usage**\n`!TRANSFER|amount|receiver`",TRANSFER)
command["!CLOSE"]=Command("!CLOSE","This command will manually close your current Store session\n**Usage**\n`!CLOSE`",CLOSE)
command["!INVENTORY"]=KIPC("!INVENTORY","This command will show all of the items you own\n**Usage**\n`!INVENTORY`",INVENTORY)
command["!GAMBLEGAME"]=KIPC("!GAMBLEGAME","This command will start either a solo or multiplayer gambling game involving KIPPCOINS\n**Usage**\n`!GAMBLEGAME|SOLO or OPPONENT`",GAMBLEGAME)
command["!SELECT"]=Command("!SELECT","Explained in Solo GambleGame\n**Usage**\n`!SELECT|color`",SELECT)
command["!CANCEL"]=Command("!CANCEL","Explained in GambleGame\n**Usage**\n`!CANCEL`",CANCEL)
command["!DECLINE"]=Command("!DECLINE","Explained in GambleGame\n**Usage**\n`!DECLINE`",DECLINE)
command["!ACCEPT"]=Command("!ACCEPT","Explained in GambleGame\n**Usage**\n`!ACCEPT`",ACCEPT)
command["!BET"]=Command("!BET","Explained in Solo/Non-Solo GambleGame\n**Usage**\n`!BET`",BET)
command["!STATUS"]=Command("!STATUS","Shows KIPP's Daemon's current status\n**Usage**\n`Currently unavailable`",STATUS)
command["!IMPEACHREQUEST"]=HISO("!IMPEACHREQUEST","DMs LockdownDoom about your impeachment request\n**Usage**\n`!IMPEACHREQUEST|reason`",IMPEACHREQUEST)
command["!IMPEACHMEEMA"]=HISO("!IMPEACHMEEMA","This command can be used by LockdownDoom in order to depose the current meema\n**Usage**\n`!IMPEACHMEEMA`",IMPEACHMEEMA)
command["!MATH"]=MISC("!MATH","This command will return the answer to any basic math problem given\n**Usage**\n`!MATH|problem`",MATH)
command["!MFIX"]=MUSC("!MFIX","This command will reset KIPP's voice client and related variables in order to fix most problems with music\n**Usage**\n`!MFIX`",MFIX)
command["!EVAL"]=Command("!EVAL","This command can be used by LockdownDoom in order to observe what a code block returns\n**Usage**\n`!EVAL|code`",EVAL)
command["!EXEC"]=Command("!EXEC","This command can be used by LockdownDoom in order to run a code block\n**Usage**\n`!EXEC|code`",EXEC)
command["!SEARCHLOG"]=MISC("!SEARCHLOG","This command will return all messages (or to a given limit) sent in the current server containing a query\n**Usage**\n`!SEARCHLOG|query|result limit`",SEARCHLOG)
command["!CLEAR"]=MISC("!CLEAR","This command will clear the last 100 messages sent in the channel\n**Usage**\n`!CLEAR`",CLEAR)
command["!ADDKIPP"]=MISC("!ADDKIPP","This command returns a link that anyone can use to add KIPP to another server\n**Usage**\n`!ADDKIPP`",ADDKIPP)
command["!MUSIC"]=MUSC("!MUSIC","This command will cause KIPP to play music from youtube in your VC based on your entered link or query\n**Usage**\n`!MUSIC|query or link`",MUSIC)
command["!MONO"]=MUSC("!MONO","This command will change KIPP's audio to mono\n**Usage**\n`!MONO`",MONO)
command["!STEREO"]=MUSC("!STEREO","This command will change KIPP's audio to stereo\n**Usage**\n`!STEREO`",STEREO)
command["!SETVOL"]=MUSC("!SETVOL","This command will change KIPPs colume to the specified volume\n**Usage**\n`!SETVOL|volume [0-100]`",SETVOL)
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
    try:
        while True:
            global last_ping
            last_ping=t.time()
            for server in client.servers:
                for member in server.members:
                    if member.bot == False:
                        if member.game != None:
                            if member.game.type == 1:
                                if playerinfo[member].streaming == False:
                                    if serverinfo[server].search_server_configs("TWITCH_CHANNEL") != None:
                                        try:
                                            await client.send_message(client.get_channel(serverinfo[server].search_server_configs("TWITCH_CHANNEL")[1]), '@everyone, '+str(member)+' just started streaming on Twitch! Check it out here: '+str(member.game.url))
                                        except discord.DiscordException:
                                            print("Twitch announcement channel was deleted, could not announce streamer")
                                playerinfo[member].streaming = True
                            else:
                                playerinfo[member].streaming=False
                    if str(server.id) == "451227721545285649":
                        if "RAINBOW SIX SIEGE" in str(member.game).upper():
                            if serverinfo[server].r6role not in member.roles:
                                await client.add_roles(member, serverinfo[server].r6role)
                        else:
                            if serverinfo[server].r6role in member.roles:
                                await client.remove_roles(member, serverinfo[server].r6role)
                        if "MINECRAFT" in str(member.game).upper():
                            if serverinfo[server].mcrole not in member.roles:
                                await client.add_roles(member, serverinfo[server].mcrole)
                        else:
                            if serverinfo[server].mcrole in member.roles:
                                await client.remove_roles(member, serverinfo[server].mcrole)
                        if "DESTINY 2" in str(member.game).upper():
                            if serverinfo[server].d2role not in member.roles:
                                await client.add_roles(member, serverinfo[server].d2role)
                        else:
                            if serverinfo[server].d2role in member.roles:
                                await client.remove_roles(member, serverinfo[server].d2role)
                queuelist="\nNo songs in queue"
                if len(serverinfo[server].queue)>1:
                    queuelist=""
                    i=0
                    for song in serverinfo[server].queue[1:]:
                        i=i+1
                        queuelist=queuelist+"\n`#{0}` {1}".format(i,"["+(''.join(song[0]))+"]("+song[1]+")")
                if serverinfo[server].player==None:
                    currentlyplaying=False
                else:
                    currentlyplaying=True
                try:
                    if ((currentlyplaying == False) and serverinfo[server].musicmessage != None):
                        if serverinfo[server].count == 0:
                            print("COUNT=0")
                            em=discord.Embed(description = serverinfo[server].musicdesc.split('**Progress:**')[0]+'**Song ended**',colour=EMBEDCOLOR)
                            em.set_footer(text=serverinfo[server].musicfooter)
                            em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
                            try:
                                await client.edit_message(serverinfo[server].musicmessage,embed=em)
                            except discord.DiscordException:
                                serverinfo[server].musicmessage=await client.send_message(serverinfo[server].musictextchannel,embed=em)
                            except Exception as err:
                                print(err)
                            serverinfo[server].count=1
                            if (len(serverinfo[server].queue)>0):
                                serverinfo[server].queue.remove(serverinfo[server].queue[0])
                                if (len(serverinfo[server].queue)>0):
                                    server.voice_client.encoder_options(sample_rate=48000,channels=2)
                                    player = await server.voice_client.create_ytdl_player(serverinfo[server].queue[0][1],before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5")
                                    player.start()
                                    player.volume = serverinfo[server].volume
                                    serverinfo[server].player = player
                                    serverinfo[server].playing = player.title
                                    serverinfo[server].likes = player.likes
                                    serverinfo[server].dislikes = player.dislikes
                                    serverinfo[server].views = player.views
                                    serverinfo[server].uploader = player.uploader
                                    length = player.duration
                                    if serverinfo[server].player.is_live == False:
                                        mins=int(length/60)
                                        seconds=int(length-(mins*60))
                                        hours=int(mins/60)
                                        if hours > 0:
                                            mins=mins-(hours*60)
                                            if len(str(mins))==1:
                                                mins="0"+str(mins)
                                            if len(str(seconds)) == 1:
                                                length=str(hours)+":"+str(mins)+":"+"0"+str(seconds)
                                            else:
                                                length=str(hours)+":"+str(mins)+":"+str(seconds)
                                        else:
                                            if len(str(seconds)) == 1:
                                                length=str(mins)+":"+"0"+str(seconds)
                                            else:
                                                length=str(mins)+":"+str(seconds)
                                    else:
                                        length = "Currently Streaming"
                                    serverinfo[server].length = length
                                    serverinfo[server].pausetime = 0
                                    msg3 = ("["+str(serverinfo[server].playing)+"]("+serverinfo[server].queue[0][1]+")\n**Progress:**: `0:00 / "+serverinfo[server].length+"`\n**Volume:** "+str(serverinfo[server].player.volume))
                                    em = discord.Embed(description=msg3,colour=EMBEDCOLOR)
                                    em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
                                    video_id = serverinfo[server].queue[0][1].split("watch?v=")[1]
                                    thumbnail = "https://img.youtube.com/vi/"+video_id+"/0.jpg"
                                    serverinfo[server].thumbnail = thumbnail
                                    em.set_footer(text=profooter)
                                    serverinfo[server].musicmessage = await client.send_message(serverinfo[server].musictextchannel, embed=em)
                                    serverinfo[server].musicdesc = msg3
                                    serverinfo[server].musicfooter = profooter
                                    serverinfo[server].pausetime = 0
                                    serverinfo[server].imagelink = thumbnail
                                    serverinfo[server].duration = player.duration
                                    serverinfo[server].player=player
                                    serverinfo[server].starttime = datetime.datetime.now()
                    elif currentlyplaying==True and serverinfo[server].paused == False:
                        if serverinfo[server].count1==1:
                            serverinfo[server].pausetime=serverinfo[server].pausetime+((datetime.datetime.now()-serverinfo[server].pausedatetime).total_seconds())
                        c = datetime.datetime.now()-(serverinfo[server].starttime+datetime.timedelta(seconds=serverinfo[server].pausetime))
                        progress = divmod(c.days * 86400 + c.seconds, 60)
                        minutedelta=str(progress).split('(')[1].split(')')[0].split(',')[0]
                        seconddelta=str(progress).split('(')[1].split(')')[0].split(', ')[1]
                        if len(str(seconddelta)) == 1:
                            seconddelta='0'+str(seconddelta)
                        hours=int(int(minutedelta)/60)
                        percent=int(18*(((int(hours)*3600)+(int(minutedelta)*60)+int(seconddelta))/int(serverinfo[server].duration)))+1
                        if serverinfo[server].player.is_live == False:
                            bar=("▣"*percent)+"▢"*(18-percent)
                        else:
                            bar="▣"*18
                        if hours>0:
                            minutedelta=int(minutedelta)-(hours*60)
                            if len(str(minutedelta))==1:
                                minutedelta="0"+str(minutedelta)
                            else:
                                minutedelta=str(minutedelta)
                            em=discord.Embed(description = serverinfo[server].musicdesc.split('**Progress:**')[0]+'**Volume:** '+str(int(serverinfo[server].volume*100))+'%'+'\n**Progress:** `'+str(hours)+":"+str(minutedelta)+':'+str(seconddelta)+' / '+serverinfo[server].length+'`\n'+bar+'\n**Queue:**'+queuelist,colour=EMBEDCOLOR)
                        else:
                            em=discord.Embed(description = serverinfo[server].musicdesc.split('**Progress:**')[0]+'**Volume:** '+str(int(serverinfo[server].volume*100))+'%'+'\n**Progress:** `'+str(minutedelta)+':'+str(seconddelta)+' / '+serverinfo[server].length+'`\n'+bar+'\n**Queue:**'+queuelist,colour=EMBEDCOLOR)
                        em.set_footer(text=serverinfo[server].musicfooter)
                        em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
                        if ((int(hours)*3600)+(int(minutedelta)*60)+int(seconddelta))>=int(serverinfo[server].duration) and serverinfo[server].player.is_live == False:
                            serverinfo[server].player.stop()
                            serverinfo[server].player = None
                            serverinfo[server].count=0
                            currentlyplaying=False
                        else:
                            try:
                                await client.edit_message(serverinfo[server].musicmessage,embed=em)
                            except discord.DiscordException:
                                serverinfo[server].musicmessage=await client.send_message(serverinfo[server].musictextchannel,embed=em)
                        serverinfo[server].count1=0
                    elif serverinfo[server].paused == True and serverinfo[server].player != None:
                        if serverinfo[server].count1 == 0:
                            serverinfo[server].pausedatetime = datetime.datetime.now()
                            if hours>0:
                                if len(str(minutedelta)) == 1:
                                    minutedelta='0'+str(minutedelta)
                                em=discord.Embed(description = serverinfo[server].musicdesc.split('**Progress:**')[0]+'**Volume:** '+str(int(serverinfo[server].volume*100))+'%'+'\n**Progress:** `'+str(hours)+":"+str(minutedelta)+':'+str(seconddelta)+' / '+serverinfo[server].length+'` (paused)\n'+bar+'\n**Queue:**'+queuelist,colour=EMBEDCOLOR)
                            else:
                                em=discord.Embed(description = serverinfo[server].musicdesc.split('**Progress:**')[0]+'**Volume:** '+str(int(serverinfo[server].volume*100))+'%'+'\n**Progress:** `'+str(minutedelta)+':'+str(seconddelta)+' / '+serverinfo[server].length+'` (paused)\n'+bar+'\n**Queue:**'+queuelist,colour=EMBEDCOLOR)
                            em.set_footer(text=serverinfo[server].musicfooter)
                            #em.set_thumbnail(url=serverinfo[server].imagelink)
                            em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
                            try:
                                await client.edit_message(serverinfo[server].musicmessage,embed=em)
                            except discord.DiscordException:
                                serverinfo[server].musicmessage=await client.send_message(serverinfo[server].musictextchannel,embed=em)
                            serverinfo[server].count1=1
                except TypeError as err:
                    print(err)
                    raise
            await asyncio.sleep(1)
    except Exception as err:
        print(err)
async def election_timer():
    import datetime
    while True:
        for server in client.servers:
            if str(server.id) == "451227721545285649":
                if serverinfo[server].election == True:
                    for member in server.members:
                        if member in serverinfo[server].voters:
                            if str(member.status).upper() == 'OFFLINE':
                                serverinfo[server].voters.remove(member)
                    c = datetime.datetime.now()-serverinfo[server].sElectiontime
                    progress = divmod(c.days * 86400 + c.seconds, 60)
                    minutedelta=str(progress).split('(')[1].split(')')[0].split(',')[0]
                    i=int(minutedelta)
                    timer = str(15-i)
                    if i < 15:
                        emb = discord.Embed(title="Election",description="Candidate 1: {0}\n**Votes: {1}**\n\nCandidate 2: {2}\n**Votes: {3}**\n\n**Time Left: {4} minutes**".format(str(serverinfo[server].can1),str(serverinfo[server].can1votes), str(serverinfo[server].can2), str(serverinfo[server].can2votes), timer),colour=EMBEDCOLOR)
                        await client.edit_message(serverinfo[server].electionmessage, embed=emb)
                        if timer != serverinfo[server].oldtime:
                            serverinfo[server].oldtime=timer
                            channel = serverinfo[server].electionmessage.channel
                            await client.delete_message(serverinfo[server].electionmessage)
                            serverinfo[server].electionmessage = await client.send_message(channel, embed=emb)
                            cand1=serverinfo[server].can1
                            cand2=serverinfo[server].can2
                            for member in server.members:
                                if member not in serverinfo[server].messagesent and server.role_hierarchy.index(member.top_role)>2 and member != cand1 and member != cand2 and (str(member.status).upper() == "ONLINE" or str(member.status) == "idle"):
                                    await client.send_message(member, "An election has started in The New Society. Please respond to this message by typing **1** or **2**. Candidate 1 is {0}, and candidate 2 is {1}.".format(str(cand1),str(cand2)))
                                    serverinfo[server].voters.append(member)
                                    serverinfo[server].messagesent.append(member)
                    if i >= 15 or len(serverinfo[server].voters) == 0:
                        if serverinfo[server].can1votes >0 or serverinfo[server].can2votes>0:
                            emb = discord.Embed(title="Election", description="Election Ended",colour=EMBEDCOLOR)
                            await client.edit_message(serverinfo[server].electionmessage, embed=emb)
                            if serverinfo[server].can1votes > serverinfo[server].can2votes:
                                winner = serverinfo[server].can1
                            elif serverinfo[server].can1votes < serverinfo[server].can2votes:
                                winner = serverinfo[server].can2
                            elif serverinfo[server].can1votes == serverinfo[server].can2votes:
                                await client.send_message(serverinfo[server].electionmessage.channel, "It was a tie! Flipping a coin...")
                                rand = SystemRandom().randrange(1,3)
                                if rand == 1:
                                    winner = serverinfo[server].can1
                                if rand == 2:
                                    winner = serverinfo[server].can2
                            for role in server.roles:
                                if str(role) == "meema":
                                    winrole = role
                            await client.send_message(serverinfo[server].electionmessage.channel, "The winner of this election was **{0}**. Congratulations! You are now the rank {1} and have power over the people.".format(str(winner),winrole.mention))
                            for member in server.members:
                                if str(member.top_role) == 'meema':
                                    await client.remove_roles(member, member.top_role)
                                if str(member) == str(winner):
                                    await client.add_roles(member, winrole)
                            serverinfo[server].election=False
                        else:
                            emb = discord.Embed(title="Election", description="Election Ended",colour=EMBEDCOLOR)
                            await client.edit_message(serverinfo[server].electionmessage, embed=emb)
        await asyncio.sleep(1)
async def web_command(message, message2):
    if message2.startswith("!D2"):
        try:
            platform = str(message.content).split('|')[1].upper()
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            if platform == 'XBOX':
                platform='xbl'
                user=str(message.content).split('|')[2]
            if platform=='PC':
                platform='pc'
                user=str(message.content).split('|')[2].replace('#','-')
            url="https://destinytracker.com/d2/profile/{0}/{1}".format(platform,user)
            resp = requests.get(url, headers=headers)
            emb=discord.Embed(title = (message2.split('|')[2]+"'s D2 Stats"),description="**Casual KD:** "+str(resp.content).split(r'"casual":[{"label":"KD","field":"KD","category":"Performance","ValueInt":null,"ValueDec":')[1].split(',')[0]+"\n**Competitive KD:** "+str(resp.content).split(r'[{"label":"KD","field":"KD","category":"Performance","ValueInt":null,"ValueDec":')[1].split(',')[0],colour=EMBEDCOLOR)
            await client.send_message(message.channel, embed=emb)
        except IndexError:
            await client.send_message(message.channel, "Sorry, I could not find any data on the given user.")
    if message2.startswith('!IMAGE|'):
        await client.send_message(message.channel, "Processing image request...")
        url = "https://www.google.com/search?tbm=isch&source=hp&biw=2560&bih=1309&ei=eCYOW5bML6Oi0gK774NY&q={0}&oq={1}&gs_l=img.3..0l10.3693.4072.0.4294.7.6.0.1.1.0.59.152.3.3.0....0...1ac.1.64.img..3.4.156.0...0.OLvQBmMFRWY".format(message2.split('|')[1].replace(' ','+'),message2.split('|')[1].replace(' ','+'))
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        req = requests.get(url, headers=headers)
        req=req.content
        i=0
        cont=0
        while True:
            try:
                i=i+1
                if cont>300:
                    await client.send_message(message.channel,"No results for image search **{0}**".format(str(message.content).split('|')[1]))
                    break
                if ".jpeg" in ("https://"+str(req).split('https://')[i].split('"')[0]) or ".jpg" in ("https://"+str(req).split('https://')[i].split('"')[0]):
                    image = "https://"+str(req).split('https://')[i].split('"')[0]
                    emb=discord.Embed(title=("Image result for '{0}'".format(str(message.content).split('|')[1])),colour=EMBEDCOLOR)
                    emb.set_image(url=image)
                    emb.set_footer(text=profooter)
                    await client.send_message(message.channel, embed=emb)
                    break
            except Exception:
                cont=cont+1
    if message2.startswith('!GIF|'):
        await client.send_message(message.channel, "Processing gif request...")
        url = "https://www.google.com/search?tbm=isch&source=hp&biw=2560&bih=1309&ei=eCYOW5bML6Oi0gK774NY&q={0}&oq={1}&gs_l=img.3..0l10.3693.4072.0.4294.7.6.0.1.1.0.59.152.3.3.0....0...1ac.1.64.img..3.4.156.0...0.OLvQBmMFRWY".format(message2.split('|')[1].replace(' ','+')+" gif",message2.split('|')[1].replace(' ','+')+"gif")
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        req = requests.get(url, headers=headers)
        req=req.content
        i=0
        cont=0
        while True:
            try:
                if cont>300:
                    await client.send_message(message.channel,"No results for gif search **{0}**".format(str(message.content).split('|')[1]))
                    break
                i=i+1
                if ".gif" in ("https://"+str(req).split('https://')[i].split('"')[0]):
                    image = "https://"+str(req).split('https://')[i].split('"')[0]
                    emb=discord.Embed(title=("Gif result for '{0}'".format(str(message.content).split('|')[1])),colour=EMBEDCOLOR)
                    emb.set_image(url=image)
                    emb.set_footer(text=profooter)
                    await client.send_message(message.channel, embed=emb)
                    break
            except Exception:
                cont=cont+1
#discord.opus.load_opus('/usr/lib/arm-linux-gnueabihf/libopus.so.0.5.3')
InterstellarQuotes = ["'Do not go gentle into that good night'\n**Professor Brand**", "'Come on, TARS!'\n**Cooper**", "'Cooper, this is no time for caution!'\n**TARS**", "'You tell that to Doyle.'\n**Cooper**", "'Newton's third law. You gotta leave something behind.'\n**Cooper**", "'Step back, professor, step back!'\n**TARS**","'No, it's necessary.'\n**Cooper**"]
loading = False
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
    async def on_voice_state_update(before, after):
        server = after.server
        user = server.get_member(KIPP_ID)
        users = []
        try:
            for user in server.get_member(KIPP_ID).voice.voice_channel.voice_members:
                users.append(user)
            if int(len(users))<2:
                try:
                    player = serverinfo[server].player
                    str(int(player.volume*100))
                    currentlyplaying = True
                except AttributeError:
                    currentlyplaying = False
                if currentlyplaying == True:
                    if serverinfo[server].paused == False:
                        await client.send_message(serverinfo[server].musictextchannel, "Nobody is listening to KIPP. Pausing music...")
                        serverinfo[server].player.pause()
                        serverinfo[server].paused = True
                        serverinfo[server].everyoneleft = True
            if (after.voice.voice_channel == server.get_member(KIPP_ID).voice.voice_channel) and serverinfo[server].everyoneleft == True:
                serverinfo[server].everyoneleft = False
                await client.send_message(serverinfo[server].musictextchannel, "The music that was playing (**"+str(serverinfo[server].playing)+"**) was paused because nobody was listening. Use **!resume** to resume the music.")
        except AttributeError:
            pass
    @client.event
    async def on_server_join(server):
        general=False
        for channel in server.channels:
            if channel.name=='general':
                general=True
                for channel in server.channels:
                    if channel.name=='general':
                        try:
                            await client.send_message(channel, "Hello, and thank you for using KIPP. To get started, type **!help** for all of the commands.")
                            break
                        except discord.DiscordException:
                            pass
        if general == False:
            for channel in server.channels:
                try:
                    await client.send_message(channel, "Hello, and thank you for using KIPP. To get started, type **!help** for all of the commands.")
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
        await client.change_presence(game=discord.Game(name="3.1.24 Simulator",type=1,url="https://twitch.tv/kipp4780"))
        #s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #s.connect(("8.8.8.8",80))
        #await client.send_message(await client.get_user_info(CREATOR_ID),"Status Panel available at: {0}".format("http://"+s.getsockname()[0]+":5000/"))
        loop = asyncio.get_event_loop()
        loop.create_task(election_timer())
        loop.create_task(ping_check())
        loop.create_task(background_loop())
        logging.log(5,"KIPP started.")
        for server in client.servers:
            serverinfo[server] = Server(server)
            for member in server.members:
                playerinfo[member] = Profile(member)
            for role in server.roles:
                if str(role) == "Rainbow Six Siege":
                    serverinfo[server].r6role=role
                if str(role) == "Minecraft":
                    serverinfo[server].mcrole=role
                if str(role) == "Destiny 2":
                    serverinfo[server].d2role=role
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
                await client.send_message(client.get_channel(serverinfo[server].search_server_configs("WELCOME_CHANNEL")[1]),"Welcome to **{0}**, {1}".format(server, member.mention))
            except discord.DiscordException:
               print("Welcome channel was deleted, couldn't send message to welcome channel")
    @client.event
    async def on_message(message):
        if message.server != None or str(message.channel).upper=="DIRECT MESSAGE":
            if message.author.id in serverinfo[message.server].blocked:
                await client.delete_message(message)
        if str(message.content).upper().startswith("!SEARCHLOG|")==False and str(message.author) != "KIPP#4780":
            add_chat_log(message)
        try:
            playerinfo[message.author].user
        except KeyError:
            playerinfo[message.author] = Profile(message.author)
        if str(message.channel).upper().startswith('DIRECT MESSAGE') == False:
            serverinfo[message.server].recentchannel = message.channel
        readarray=[]
        reader = csv.reader(open("/home/pi/Desktop/KIPPSTUFF/KIPPCOINS"))
        for row in reader:
            readarray.append(row)
        for server in client.servers:
            if str(server.id) == "451227721545285649":
                if serverinfo[server].election == True:
                    if str(message.channel).upper().startswith('DIRECT MESSAGE'):
                        if message.author in serverinfo[server].voters:
                            if message.content == "1" or message.content == "2":
                                serverinfo[server].voters.remove(message.author)
                                if message.content=="1":
                                    can = serverinfo[server].can1
                                    serverinfo[server].can1votes=serverinfo[server].can1votes+1
                                else:
                                    can = serverinfo[server].can2
                                    serverinfo[server].can2votes=serverinfo[server].can2votes+1
                                await client.send_message(message.author, "Thank you for voting. You have voted for **{0}**.".format(str(can)))
        if str(message.server) != "None":
            user = message.server.get_member(KIPP_ID)
            playerinfo[message.author].game = str(message.author.game)
        else:
            return
        kippservers = 0
        roles = []
        for server in client.servers:
            for member in server.members:
                if member == message.author:
                    kippservers=kippservers+1
        if str(message.server) != "None":
            playerinfo[message.author].nickname = str(message.author.nick)
            playerinfo[message.author].highestrole = message.author.top_role
            role1 = discord.utils.get(message.author.server.roles, name=str(playerinfo[message.author].highestrole))
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
        if message.server.get_member(KIPP_ID).mention in message2:
            await client.send_message(message.channel,"What do you want? Use **!help** for the commands.")
        if message2.startswith("!HELP|"):
            found=False
            for command in commands:
                if "!" in message2.split("|")[1]:
                    if command.Name==message2.split("|")[1]:
                        emb=discord.Embed(title="Help for {0}".format(command.Name),description=command.Help[0],colour=EMBEDCOLOR)
                        emb.set_footer(text=profooter)
                        await client.send_message(message.channel, embed=emb)
                        found=True
                else:
                    if command.Name=="!"+message2.split("|")[1]:
                        emb=discord.Embed(title="Help for {0}".format(command.Name),description=command.Help[0],colour=EMBEDCOLOR)
                        emb.set_footer(text=profooter)
                        await client.send_message(message.channel, embed=emb)
                        found=True
            if found==False:
                await client.send_message(message.channel,"Sorry, but I couldn't find a registered command with that name.")
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
            hierarchical=[]
            sc=[]
            kc=[]
            oo=[]
            for c in commands:
                if isinstance(c,MISC):
                    misc.append(c.Name)
                elif isinstance(c,HISO):
                    hierarchical.append(c.Name)
                elif isinstance(c,MUSC):
                    musc.append(c.Name)
                elif isinstance(c,SCIN):
                    sc.append(c.Name)
                elif isinstance(c,KIPC):
                    kc.append(c.Name)
                elif isinstance(c,OWON):
                    oo.append(c.Name)
            em = discord.Embed(title='Help',description="**Use !Help|command for command-specific information**",colour=EMBEDCOLOR)
            em.add_field(name="Miscellaneous",value="```"+"\n".join(misc)+"```")#,inline=True)
            em.add_field(name="Music",value="```"+"\n".join(musc)+"```")#,inline=True)
            em.add_field(name="Scientific",value="```"+"\n".join(sc)+"```")#,inline=True)
            if str(message.server.id) == '451227721545285649':
                em.add_field(name="Meema Only",value="```"+"\n".join(oo)+"```")#,inline=True)
            else:
                em.add_field(name="Owner Only",value="```"+"\n".join(oo)+"```")#,inline=True)
            em.add_field(name="KIPPCOINS",value="```"+"\n".join(kc)+"```")#,inline=True)
            if str(message.server.id) == '451227721545285649':
                em.add_field(name="H. Society",value="```"+"\n".join(hierarchical)+"```")#,inline=True)
            em.set_footer(text=profooter)
            await client.send_message(message.channel, embed=em)
    client.loop.run_until_complete(client.start(TOKEN))
