import sys
import os
KIPP_DIR=os.environ["KIPP_DIR"]
from ESSENTIAL_PACKAGES import *
from Music import *
from Footer import get_footer
CREATOR_ID=289920025077219328
KIPP_ID=386352783550447628
command={}
commands=[]
serverinfo={}
playerinfo={}
InterstellarQuotes = ["'Do not go gentle into that good night'\n**Professor Brand**", "'Come on, TARS!'\n**Cooper**", "'Cooper, this is no time for caution!'\n**TARS**", "'You tell that to Doyle.'\n**Cooper**", "'Newton's third law. You gotta leave something behind.'\n**Cooper**", "'Step back, professor, step back!'\n**TARS**","'No, it's necessary.'\n**Cooper**"]
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
class Command:
    def __init__(self,n,h,e):
        self.Help=h,
        self.exe=e,
        self.Name=n
        commands.append(self)
    async def Execute(self,message,message2,sinfo,pinfo):
        global serverinfo
        global playerinfo
        serverinfo=sinfo
        playerinfo=pinfo
        await self.exe[0](message,message2)
        return serverinfo, playerinfo
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
async def HELP(message,message2):
    if "|" in message2:
        found=False
        for command in commands:
            search=message2.split("|")[1]
            if "!" not in search:
                search="!"+search
                if command.Name==search:
                    emb=discord.Embed(title="Help for {0}".format(command.Name),description=command.Help[0],colour=EMBEDCOLOR)
                    emb.set_footer(text=get_footer())
                    await message.channel.send( embed=emb)
                    found=True
        if found==False:
            await message.channel.send("Sorry, but I couldn't find a registered command with that name.")
    else:
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
        em.set_footer(text=get_footer())
        await message.channel.send(embed=em)
async def IQ(message,message2):
    arrlen = int(len(InterstellarQuotes))
    quoteNum = SystemRandom().randrange(0,arrlen)
    description = str(InterstellarQuotes[quoteNum])
    em = discord.Embed(title="Interstellar Quote",description=description,colour=EMBEDCOLOR)
    em.set_footer(text=get_footer())
    await message.channel.send( embed=em)
async def SR(message,message2):
    mass = str(message.content).split('|')[1].replace('^', '**')
    calc = (2*(eval('6.67*10**-11'))*(eval(mass)))/eval('299792458**2')
    await message.channel.send( "The Schwarzschild Radius of an object with a mass of "+str(mass).replace('**','^')+" kg is: "+str(calc)+" m")
async def EXIT(message,message2):
    if playerinfo[message.author].betting==True:
        playerinfo[message.author].gamblerequest=False
        emb=discord.Embed(title="GambleGame",description="GAME ENDED",colour=EMBEDCOLOR)
        emb.set_footer(text=get_footer())
        await playerinfo[message.author].gamblemessage.edit(embed=emb)
        reset_gamblegame(message.author)
async def PLAY(message,message2):
    if playerinfo[message.author].solo == True and playerinfo[message.author].bet != None:
        rand=SystemRandom().randrange(1,4)
        color=["Red","Blue","Green","Black"][rand]
        if color == playerinfo[message.author].color:
            emb = discord.Embed(title="Solo GambleGame",description="Selected Color: **{0}**\nActual Color: **{1}**\nYou gain `{2} KC`".format(playerinfo[message.author].color,color,playerinfo[message.author].bet),colour=EMBEDCOLOR)
            emb.set_footer(text=get_footer())
            playerinfo[message.author].GIVE_KIPPCOINS(int(playerinfo[message.author].bet))
        if color != playerinfo[message.author].color:
            emb = discord.Embed(title="Solo GambleGame",description="Selected Color: **{0}**\nActual Color: **{1}**\nYou lose `{2} KC`".format(playerinfo[message.author].color,color,playerinfo[message.author].bet),colour=EMBEDCOLOR)
            emb.set_footer(text=get_footer())
            playerinfo[message.author].GIVE_KIPPCOINS(-1*int(playerinfo[message.author].bet))
        await playerinfo[message.author].gamblemessage.edit(embed=emb)
        await message.delete()
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
            emb.set_footer(text=get_footer())
            await playerinfo[message.author].gamblemessage.edit(embed=emb)
            playerinfo[winner].GIVE_KIPPCOINS(int(playerinfo[message.author].bet))
            playerinfo[playerinfo[winner].challenger].GIVE_KIPPCOINS(-1*int(playerinfo[message.author].bet))
            reset_gamblegame(message.author)
async def CODE(message,message2):
    from subprocess import Popen, PIPE
    p=Popen(KIPP_DIR+'/Bash/NewestCommit.sh',stdout=PIPE,stderr=PIPE)
    stdout=p.communicate()[0]
    p.kill()
    try:
        await message.channel.send("{0} My code is backed up on GitHub here: https://github.com/LockdownDoom/KIPP/blob/master/KIPP.py\nAlso, my code has been reviewed by Codacy here: https://app.codacy.com/project/LockdownDoom/KIPP/dashboard?branchId=10423847".format('Newest commit:\n```\n'+stdout.decode()[64:]+'\n```\n'))
    except discord.DiscordException:
        await message.channel.send("{0} My code is backed up on GitHub here: https://github.com/LockdownDoom/KIPP/blob/master/KIPP.py\nAlso, my code has been reviewed by Codacy here: https://app.codacy.com/project/LockdownDoom/KIPP/dashboard?branchId=10423847".format('Newest commit:\nThe newest commit is too large to be displayed here.'))
async def GA(message,message2):
    mass = str(message.content).split('|')[1].replace('^', '**')
    dist = str(message.content).split('|')[2].replace('^', '**')
    calc = (eval('6.67*10**-11')*eval(mass))/(eval(dist)**2)
    await message.channel.send( "The gravitational acceleration towards an object with a mass of "+str(mass).replace('**','^')+" kg at a distance of "+str(dist)+"m is: "+str(calc)+' m/s^2')
async def GTD(message,message2):
    from math import sqrt
    oldtime = str(message.content).split('|')[1].replace('^', '**')
    mass = str(message.content).split('|')[2].replace('^', '**')
    distance = str(message.content).split('|')[3].replace('^', '**')
    calc=float(oldtime)/(sqrt(1-((2*(eval('6.67*10**-11'))*(eval(str(mass))))/((eval(str(distance)))*(eval('299792458**2'))))))
    await message.channel.send( "If the time passed for the observer inside of this gravity field was {0} seconds, and the mass of the object creating the gravity is {1} kg, and the observer's distance away from the center of the object creating the gravity is {2} m, the time passed outside the gravity field would be {3} seconds.".format(str(eval(str(oldtime))),str(mass),str(eval(str(distance))),str(eval(str(calc)))).replace('**','^'))
async def TD(message,message2):
    from math import sqrt
    oldtime = str(message.content).split('|')[1].replace('^', '**')
    velocity = str(message.content).split('|')[2].replace('^', '**')
    try:
        calc = float(oldtime)/(sqrt(1-eval(str((float(velocity)/299792458)**2))))
    except ZeroDivisionError:
        calc=0
    if calc != 0:
        await message.channel.send( 'If the local time is passed is '+str(oldtime)+' seconds, the non-local time passed for an object travelling '+str(velocity)+' m/s would be '+str(calc)+' seconds.')
    else:
        await message.channel.send( 'Ah hah. Hah hah hah. You tried to trick me! Surely you must know that when you travel the speed of light, zero local time passes while you travel an infinite distance!')
async def EV(message,message2):
    from math import sqrt
    mass = str(message.content).split('|')[1].replace('^', '**')
    dist = str(message.content).split('|')[2].replace('^', '**')
    calc = sqrt((2*eval('6.67*10**-11')*eval(mass))/eval(str(dist)))
    await message.channel.send( 'The escape velocity from an object with a mass of '+str(mass).replace('**','^')+' kg at a distance of '+str(dist)+' m is: '+str(calc)+' m/s')
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
        await client.send_message_file(message.channel, f)
async def CORETEMP(message,message2):
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    await message.channel.send( '{:.2f}'.format( float(cpu)/1000 ) + ' C')
async def send_image(message,url,ext):
    emb=discord.Embed(title=("{0} result for '{1}'".format(ext,str(message.content).split('|')[1])),colour=EMBEDCOLOR)
    emb.set_image(url=url)
    emb.set_footer(text=get_footer())
    await message.channel.send(embed=emb)
async def IMAGE(message,message2):
    await message.channel.send( "Processing image request...")
    url = "https://www.google.com/search?tbm=isch&source=hp&biw=2560&bih=1309&ei=eCYOW5bML6Oi0gK774NY&q={0}&oq={1}&gs_l=img.3..0l10.3693.4072.0.4294.7.6.0.1.1.0.59.152.3.3.0....0...1ac.1.64.img..3.4.156.0...0.OLvQBmMFRWY".format(message2.split('|')[1].replace(' ','+').replace("'","%27"),message2.split('|')[1].replace(' ','+').replace("'","%27"))
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    req = requests.get(url, headers=headers)
    req=req.content
    i=0
    cont=0
    while True:
        try:
            i=i+1
            if cont>300:
                await message.channel.send("No results for image search **{0}**".format(str(message.content).split('|')[1]))
                break
            if ".JPEG" in ("https://"+str(req).split('https://')[i].split('"')[0]).upper() or ".JPG" in ("https://"+str(req).split('https://')[i].split('"')[0]).upper():
                image = "https://"+str(req).split('https://')[i].split('"')[0]
                if requests.get(image).status_code==200:
                    await send_image(message,image,"Image")
                    break
        except Exception:
            cont=cont+1
async def GIF(message,message2):
    await message.channel.send( "Processing gif request...")
    url = "https://www.google.com/search?tbm=isch&source=hp&biw=2560&bih=1309&ei=eCYOW5bML6Oi0gK774NY&q={0}&oq={1}&gs_l=img.3..0l10.3693.4072.0.4294.7.6.0.1.1.0.59.152.3.3.0....0...1ac.1.64.img..3.4.156.0...0.OLvQBmMFRWY".format(message2.split('|')[1].replace(' ','+').replace("'","%27")+" gif",message2.split('|')[1].replace(' ','+').replace("'","%27")+"gif")
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    req = requests.get(url, headers=headers)
    req=req.content
    i=0
    cont=0
    while True:
        try:
            if cont>300:
                await message.channel.send("No results for gif search **{0}**".format(str(message.content).split('|')[1]))
                break
            i=i+1
            if ".GIF" in ("https://"+str(req).split('https://')[i].split('"')[0]).upper():
                image = "https://"+str(req).split('https://')[i].split('"')[0]
                if requests.get(image).status_code==200:
                    await send_image(message,image,"Gif")
                    break
        except Exception:
            cont=cont+1
async def MINE(message,message2):
    playerinfo[message.author].GIVE_KIPPCOINS(1)
async def USERINFO(message,message2):
    description = "**Mutual servers with KIPP:** "+str(playerinfo[message.author].numkippservers)+"\n**Currently Playing:** "+str(playerinfo[message.author].game)+"\n**Highest role in Server:** "+str(playerinfo[message.author].highestrole)+"\n**Nickname in Server:** "+playerinfo[message.author].nickname+"\n**KIPPCOINS:** "+str(playerinfo[message.author].GET_KIPPCOINS())
    em = discord.Embed(description=description,colour=EMBEDCOLOR)
    em.set_author(name=str(message.author), icon_url=message.author.avatar_url)
    em.set_footer(text=get_footer())
    await message.channel.send( embed=em)
async def TRANSFER(message,message2):
    try:
        patron=message.author
        amount=message2.split("|")[1]
        receiver=message.guild.get_member_named(str(message.content).split("|")[2])
    except Exception as err:
        if err == IndexError:
            await message.channel.send( "Make sure you specify both an amount and a receiver.")
        else:
            await message.channel.send( "The receiver could not be found.")
    if int(amount)<=int(playerinfo[patron].GET_KIPPCOINS()) and int(amount)>0:
        playerinfo[patron].GIVE_KIPPCOINS(-1*int(amount))
        playerinfo[receiver].GIVE_KIPPCOINS(int(amount))
        emb = discord.Embed(title="Transfer",description="Transferred **{0}** KIPPCOINS to **{1}**'s account.\n You now have **{2}** KIPPCOINS.".format(amount,str(receiver),int(playerinfo[patron].GET_KIPPCOINS())),colour=EMBEDCOLOR)
        emb.set_footer(text=get_footer())
        await message.channel.send(embed=emb)
    else:
        await message.channel.send("The amount entered was either higher than the amount of KIPPCOINS you have, or was negative.")
async def GAMBLEGAME(message,message2):
    if message2.split('|')[1] == "SOLO":
        playerinfo[message.author].solo = True
        emb = discord.Embed(title="Solo GambleGame",description="Use **!SELECT|color** to choose a color:\n**Red**\n**Blue**\n**Green**\n**Black**",colour=EMBEDCOLOR)
        emb.set_footer(text=get_footer())
        message1=await message.channel.send(embed=emb)
        playerinfo[message.author].gamblemessage=message1
    else:
        try:
            opponent=message.guild.get_member_named(str(message.content).split("|")[1])
        except Exception:
            await message.channel.send("This user does not exist.")
        if str(opponent.status).upper != "OFFLINE" and str(opponent.status).upper != "IDLE":
            playerinfo[opponent].gamblerequest=True
            playerinfo[opponent].challenger=message.author
            playerinfo[message.author].challenger=opponent
            desc = "{0}, you have been challenged to a GambleGame by {1}.\n**!ACCEPT** or **!DECLINE**\n{2} may **!CANCEL**".format(opponent.mention,message.author.mention,message.author.mention)
            emb=discord.Embed(title="GambleGame Request",description = desc,colour=EMBEDCOLOR)
            emb.set_footer(text=get_footer())
            message1 = await message.channel.send(embed=emb)
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
            await message.delete()
            emb = discord.Embed(title="Solo GambleGame",description="Color selected: **{0}**\nUse **!BET|KC** to bet KIPPCOINS\nAvailable KC: `{1}`".format(message1,str(playerinfo[message.author].GET_KIPPCOINS())),colour=EMBEDCOLOR)
            emb.set_footer(text=get_footer())
            await playerinfo[message.author].gamblemessage.edit(embed=emb)
async def CANCEL(message,message2):
    if playerinfo[playerinfo[message.author].challenger].gamblerequest == True:
        emb=discord.Embed(title="GambleGame Request",description="CANCELLED",colour=EMBEDCOLOR)
        emb.set_footer(text=get_footer())
        playerinfo[playerinfo[message.author].challenger].gamblerequest=False
        playerinfo[playerinfo[message.author].challenger].challenger=None
        playerinfo[message.author].challenger=None
        await playerinfo[message.author].gamblemessage.edit(embed=emb)
        playerinfo[playerinfo[message.author].challenger].gamblemessage=None
        playerinfo[message.author].gamblemessage=None
        await message.delete()
async def DECLINE(message,message2):
    if playerinfo[message.author].gamblerequest == True:
        emb=discord.Embed(title="GambleGame Request",description="DECLINED",colour=EMBEDCOLOR)
        emb.set_footer(text=get_footer())
        playerinfo[message.author].gamblerequest=False
        playerinfo[message.author].gamblemessage=None
        playerinfo[playerinfo[message.author].challenger].gamblemessage=None
        playerinfo[message.author].challenger=Noneplayerinfo[playerinfo[message.author].challenger].gambplayerinfo[playerinfo[message.author].challenger].gamblemessage=None
        playerinfo[message.author].gamblemessage=None
        playerinfo[message.author].gamblemessage=None
        await playerinfo[message.author].gamblemessage.edit(embed=emb)
        await message.delete()
async def ACCEPT(message,message2):
    if playerinfo[message.author].gamblerequest == True:
        playerinfo[message.author].gamblerequest=False
        playerinfo[message.author].betting=True
        playerinfo[message.author].bet = 0
        playerinfo[playerinfo[message.author].challenger].bet = 0
        playerinfo[playerinfo[message.author].challenger].betting=True
        emb=discord.Embed(title="GambleGame",description="Game started.\nEach player must bet the same amount. Once this is done, the winner will be decided.\n\n**{0}**:\nKC Available `{1}`\nBet: **0**\n\n**{2}**:\nKC Available `{3}`\nBet: **0**\n\nUse **!BET|VALUE** to bet\nUse **!EXIT** to leave the game".format(message.author,str(playerinfo[message.author].GET_KIPPCOINS()),playerinfo[message.author].challenger,str(playerinfo[playerinfo[message.author].challenger].GET_KIPPCOINS())),colour=EMBEDCOLOR)
        emb.set_footer(text=get_footer())
        await playerinfo[message.author].gamblemessage.edit(embed=emb)
        await message.delete()
async def BET(message,message2):
    if playerinfo[message.author].solo == True and playerinfo[message.author].color != None:
        amount= int(str(message.content).split("|")[1])
        if amount<=int(playerinfo[message.author].GET_KIPPCOINS()) and amount >0:
            playerinfo[message.author].bet = amount
            emb = discord.Embed(title="Solo GambleGame",description="Color: **{0}**\nBet: `{1} KC`\n**!PLAY**".format(playerinfo[message.author].color,str(playerinfo[message.author].bet)),colour=EMBEDCOLOR)
            emb.set_footer(text=get_footer())
            await playerinfo[message.author].gamblemessage.edit(embed=emb)
        await message.delete()
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
                emb.set_footer(text=get_footer())
                await playerinfo[message.author].gamblemessage.edit(embed=emb)
            await message.delete()
async def STATUS(message,message2):
    from subprocess import Popen, PIPE
    p=Popen(KIPP_DIR+'/BASH/DaemonStatus.sh',stdout=PIPE,stderr=PIPE)
    stdout=p.communicate()[0].decode()
    p.kill()
    await message.channel.send("```"+stdout.split('ago')[0]+"ago```")
async def MATH(message,message2):
    mathP = str(message.content)
    mathP2 = mathP.split('|')
    math = str(mathP2[1])
    try:
        mathT = eval(math)
    except SyntaxError:
        await message.channel.send( "Sorry, KIPP failed to process this request.")
    msg = str(math)+" = "+str(mathT)
    await message.channel.send( msg)
async def MFIX(message,message2):
    await message.channel.send("Resetting variables...")
    serverinfo[message.guild].count=0
    try:
        serverinfo[message.guild].mHandler.is_playing=False
        serverinfo[message.guild].mHandler.player.stop()
    except Exception as err:
        print(err)
    serverinfo[message.guild].playlist=None
    serverinfo[message.guild].mHandler=None
    await message.channel.send("Clearing queue...")
    serverinfo[message.guild].queue = []
    await message.channel.send("Resetting voice client...")
    try:
        await message.guild.voice_client.disconnect()
    except Exception as err:
        print(err)
    await message.channel.send( "Done.")
async def EVAL(message,message2):
    if message.author.id == CREATOR_ID:
        try:
            await message.channel.send(eval(str(message.content).split('|')[1]))
        except Exception as err:
            await message.channel.send(err)
async def EXEC(message,message2):
    if message.author.id == CREATOR_ID:
        try:
            if 'await' in str(message.content):
                await eval(str(message.content).split('|')[1].replace('await ',''))
            else:
                exec(str(message.content).split('|')[1])
            await message.channel.send('Passed without exception.')
        except Exception as err:
            if type(err) in KIPP_RESET_ERRORS:
                raise
            else:
                await message.channel.send(err)
async def CLEAR(message,message2):
    mgs = []
    await message.channel.purge(limit=100)
async def ADDKIPP(message,message2):
    msg = 'https://discordapp.com/oauth2/authorize?client_id=386352783550447628&permissions=2146958583&scope=bot'
    await message.channel.send( msg)
async def MUSIC(message,message2):
    server=message.guild
    notsearched = False
    serverinfo[message.guild].musictextchannel = message.channel
    currentlyplaying=False
    if serverinfo[message.guild].mHandler != None:
        currentlyplaying=serverinfo[message.guild].mHandler.is_playing
    if (currentlyplaying == False) or (currentlyplaying == True and message.author.voice.channel == message.guild.get_member(KIPP_ID).voice.channel):
        try:
            if message2.split("|")[1].startswith("PLAYLIST:")==False:
                if (message2.split('!MUSIC')[1]).startswith('|') == True:
                    if serverinfo[message.guild].loading == False:
                        serverinfo[message.guild].loading = True
                        music2 = str(message.content)
                        music3 = music2.split('|')
                        music4= music3[1]
                        serverinfo[server].musictextchannel = message.channel
                        serverinfo[message.guild].paused = False
                        if "&index" in music4:
                            music4 = music4.split('&index')
                            music4 = music4[0]
                        if music4.startswith("https://youtu.be"):
                            music4 = music4.split('youtu.be/')[1]
                            music4 = "https://www.youtube.com/watch?v="+music4
                        if str(message.author.voice.channel) != "None":
                            query=music4
                            music4=search_music(music4)
                            serverinfo[message.guild].loading = False
                            notsearched=False
                            if music4==None:
                                notsearched=True
                                await message.channel.send("Could not find music matching query `{0}`".format(query))
                            server = message.guild
                            if notsearched == False:
                                if ((music3[0]).upper() == "!MUSIC"):
                                    if ("user" not in music4 and "youtube.com" in music4) or ("soundcloud.com" in music4):
                                        serverinfo[message.guild].musiccolor=playerinfo[message.author].hrolecolor
                                        await join_voice_channel(message)
                                        if serverinfo[message.guild].playlist != None:
                                            serverinfo[message.guild].queue=serverinfo[message.guild].queue[:-1]
                                            add_to_queue(message.guild, music4)
                                            serverinfo[message.guild].queue.append("PLAYLIST: {0}".format(serverinfo[message.guild].playlist))
                                        else:
                                            add_to_queue(message.guild, music4)
                                        if serverinfo[message.guild].mHandler != None:
                                            if len(serverinfo[message.guild].queue)>1:
                                                if serverinfo[message.guild].playlist != None:
                                                    await message.channel.send( "Song added to queue. #"+str(len(serverinfo[message.guild].queue)-2))
                                                else:
                                                    await message.channel.send( "Song added to queue. #"+str(len(serverinfo[message.guild].queue)-1))
                                                serverinfo[message.guild].loading=False
                                        if len(serverinfo[message.guild].queue) == 1:
                                            serverinfo[message.guild].musicchannel=message.channel
                                            serverinfo[message.guild].loading = False
                                    else:
                                        await message.channel.send( "Please do not try to play an entire youtube channel. Get one specific song you would like to hear, and play that.")
                                        serverinfo[message.guild].loading = False
                        else:
                            await message.channel.send( "You are not in a voice channel. Get in one for KIPP to play music.")
                            serverinfo[message.guild].loading = False
                    else:
                        await message.delete()
                else:
                    await message.channel.send( "Please use the correct syntax. Use !music|youtubelink or !music|youtubesearch to use the music command.")
                    serverinfo[message.guild].loading = False
            else:
                if serverinfo[message.guild].search_server_configs(message2.split("|")[1]) != None:
                    if len(serverinfo[message.guild].search_server_configs(message2.split("|")[1])[0][1:])>0:
                        await join_voice_channel(message)
                        serverinfo[message.guild].musicchannel=message.channel
                        serverinfo[message.guild].queue.append("PLAYLIST: {0}".format(message2.split("PLAYLIST:")[1]))
                    else:
                        await message.channel.send( "There are no songs in the playlist named `{0}`. You may append songs to this playlist with **!APPENDPLAYLIST**.".format(message2.split("PLAYLIST:")[1]))
                else:
                    await message.channel.send( "There is no playlist named `{0}`. Use **!PLAYLISTS** to see a list of all playlists in this server.".format(message2.split("PLAYLIST:")[1]))
        except Exception as err:
            serverinfo[message.guild].loading = False
            await message.channel.send( err)
            raise
    elif (currentlyplaying == True) and (message.author.voice.channel != message.guild.get_member(KIPP_ID).voice.channel):
        await message.channel.send( "There is a song currently playing in another voice channel ("+str(message.guild.get_member(KIPP_ID).voice.channel)+"). Join that voice channel in order to change the music, or you can wait for that music to end, and run this command again.")
async def SKIP(message,message2):
    if await VerifyMusicUser(message):
        import datetime as d
        if serverinfo[message.guild].mHandler.paused == True:
            message.guild.voice_client.resume()
            serverinfo[message.guild].mHandler.paused = False
        serverinfo[message.guild].mHandler.skip()
        if len(serverinfo[message.guild].queue)==1:
            await message.channel.send( "There are no more songs in the queue. Current song ended.")
async def REMOVESONG(message,message2):
    if await VerifyMusicUser(message):
        try:
            index = int(message2.split("|")[1])
        except Exception:
            await message.channel.send( "Song index must be an integer.")
        if len(serverinfo[message.guild].queue)>1:
            if index >0 and index <= len(serverinfo[message.guild].queue):
                serverinfo[message.guild].queue.remove(serverinfo[message.guild].queue[index])
                await message.channel.send( "Removed song #{0} from queue".format(index))
                if serverinfo[message.guild].playlist != None:
                    serverinfo[message.guild].playlist = None
            else:
                await message.channel.send("Invalid song index")
        else:
            await message.channel.send("There are no songs in the queue.")
async def PAUSE(message,message2):
    if await VerifyMusicUser(message):
        player = serverinfo[message.guild].mHandler.player
        if serverinfo[message.guild].mHandler.paused == False:
            await message.channel.send( "Music paused.")
            serverinfo[message.guild].mHandler.pausedatetime=datetime.now()
            serverinfo[message.guild].mHandler.paused=True
            message.guild.voice_client.pause()
        else:
            await message.channel.send( "Music already is paused. To resume, use the **!resume** command.")
async def RESUME(message,message2):
    if await VerifyMusicUser(message):
        player = serverinfo[message.guild].mHandler.player
        if serverinfo[message.guild].mHandler.paused:
            message.guild.voice_client.resume()
            serverinfo[message.guild].mHandler.paused=False
            await message.channel.send( "Music resumed.")
        else:
            await message.channel.send( "There is currently music playing. To pause the music, use the **!pause** command.")
async def BLOCK(message,message2):
    if await VerifyOwner(message):
        owner = message.guild.owner
        blockedP = str(message.content)
        blockedP2 = blockedP.split('|')
        if blockedP2[1].upper() != "ALL":
            blockedP2[1] = message.guild.get_member_named(str(blockedP2[1]))
        if str(blockedP2[1]) != "None":
            if str(blockedP2[1]).upper() == "ALL":
                for member in message.guild.members:
                    if str(member) not in serverinfo[message.guild].blocked:
                        if (member.id != CREATOR_ID) and (str(member) != "KIPP#4780") and (member != owner):
                            serverinfo[message.guild].blocked.append(str(member.id))
                await message.channel.send( "Blocked everyone in server")
            elif blockedP2[1].id != CREATOR_ID and blockedP2[1] != owner and blockedP2[1].id != KIPP_ID:
                if blockedP2[1].id in serverinfo[message.guild].blocked:
                    await message.channel.send( "User already blocked.")
                elif blockedP2[1].id not in serverinfo[message.guild].blocked:
                    serverinfo[message.guild].blocked.append(blockedP2[1].id)
                    msg =("Blocked "+str(blockedP2[1])).format(message)
                    await message.channel.send( msg)
            elif blockedP2[1].id == CREATOR_ID:
                msg = "Why would I block my own creator?"
                await message.channel.send( msg)
            elif blockedP2[1] == message.author:
                await message.channel.send( "Why would you want to block yourself?")
            elif blockedP2[1] == message.guild.get_member(KIPP_ID):
                await message.channel.send( "Why would I block myself?")
        else:
            await message.channel.send( "This user is not in this server. Make sure that you used the command like this: '!block|nickname OR !block|username'.")
async def EXECUTE_ORDER_66(message,message2):
    if message.author.id == CREATOR_ID:
        server = message.guild
        channels = []
        members = []
        roles = []
        for channel in server.channels:
            channels.append(channel)
        for channel in channels:
            await channel.delete()
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
                    await role.delete()
                except discord.DiscordException:
                    pass
            except TypeError:
                pass
async def NICKNAME(message,message2):
    if message.author.id == CREATOR_ID:
        nickname = str(message.content).split('|')[1]
        for member in message.guild.members:
            if str(member) == "KIPP#4780":
                try:
                    await client.change_nickname(member, nickname)
                    await message.channel.send( "Successfully changed nickname to "+str(nickname)+".")
                except discord.DiscordException:
                    await message.channel.send( "KIPP does not have permission to change his nickname.")
async def NAMEALL(message,message2):
    if await VerifyOwner(message):
        try:
            uchanged = 0
            for member in message.guild.members:
                if str(member) != "KIPP#4780" and member.id != CREATOR_ID:
                    try:
                        await client.change_nickname(member, str(message.content.split("|")[1]))
                        uchanged = uchanged+1
                    except discord.DiscordException:
                        pass
        except discord.DiscordException:
            await message.channel.send( "Could not change some nicknames")
        if uchanged == 1:
            await message.channel.send( "Changed "+str(uchanged)+" nickname")
        if uchanged != 1:
            await message.channel.send( "Changed "+str(uchanged)+" nicknames")
async def BLOCKEDLIST(message,message2):
    if len(serverinfo[message.guild].blocked)>0:
        names=[]
        for i in serverinfo[message.guild].blocked:
            try:
                names.append("**"+str(message.guild.get_member(i))+"**")
            except discord.DiscordException:
                try:
                    names.append("**"+str(await client.get_user_info(i)+"**"))
                except Exception:
                    print("Couldn't find user.")
        blocked=", ".join(names)
        await message.channel.send( "The users currently blocked in this server are: "+blocked)
    else:
        await message.channel.send( "There are no users currently blocked in this server. To block a user, use the **!block** command.")
async def ADDROLE(message,message2):
    if await VerifyOwner(message):
        user = str(message.content).split('|')[2]
        rolechange = str(message.content).split('|')[1]
        user = message.guild.get_member_named(user)
        role = discord.utils.get(user.server.roles, name=str(rolechange))
        if str(role) != "None":
            try:
                await client.add_roles(user, role)
                await message.channel.send( "Successfully added the role '"+str(rolechange)+"' to "+str(user)+"'s roles")
            except discord.DiscordException:
                await message.channel.send( "Either this role is above KIPP's role, or KIPP doesn't have enough permissions to do this.")
        else:
            await message.channel.send( "This role doesn't exist. Check the capital letters in the role, and make sure they are the same as what you enter.")
async def AVATAR(message,message2):
    member = str(message.content).split('|')[1]
    member = message.guild.get_member_named(member)
    await message.channel.send( str(member)+"'s icon URL is: "+str(member.avatar_url))
async def REMOVEROLE(message,message2):
    if await VerifyOwner(message):
        user1 = str(message.content).split('|')[2]
        rolechange = str(message.content).split('|')[1]
        user = message.guild.get_member_named(user1)
        role = discord.utils.get(user.server.roles, name=str(rolechange))
        if str(role) != "None":
            try:
                await client.remove_roles(user, role)
                await message.channel.send( "Successfully removed the role '"+str(rolechange)+"' from "+str(user)+"'s roles.")
            except discord.DiscordException:
                await message.channel.send( "Either this role is above KIPP's role, or KIPP doesn't have enough permissions to do this.")
        else:
            await message.channel.send( "This role doesn't exist. Check the capital letters in the role, and make sure they are the same as what you enter.")
async def BAN(message,message2):
    if await VerifyOwner(message):
        banuser = str(message.content).split('|')[1]
        banuser = message.guild.get_member_named(banuser)
        try:
            try:
                await client.ban(banuser)
                await message.channel.send( "Successfully banned "+str(banuser)+" from "+str(message.guild)+".")
            except discord.DiscordException:
                await message.channel.send( "KIPP does not have permission to ban "+str(banuser)+", or this user is already banned")
        except AttributeError:
            await message.channel.send( "This user is already banned, or this user is not in the server. Make sure that you used the command like this: '!ban|nickname OR !ban|username'.")
async def UNBAN(message,message2):
    if await VerifyOwner(message):
        if '#' in message2:
            unbanuser = str(message.content).split('|')[1]
            banned = await client.get_bans(message.guild)
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
                    await client.unban(message.guild, unbanuser)
                    await message.channel.send( "Successfully unbanned "+str(unbanuser)+" from "+str(message.guild)+".")
                    try:
                        invite = await client.create_invite(message.channel, max_uses=1)
                        await unbanuser.send("You have been unbanned from the server '"+str(message.guild)+"'. Here is an invite to the server.\n"+str(invite))
                        await message.channel.send( "Successfully sent an invite to "+str(unbanuser))
                    except discord.DiscordException:
                        await message.channel.send( "Failed to re-invite "+str(unbanuser)+" to the server.")
                except discord.DiscordException:
                    await message.channel.send( "KIPP does not have permission to unban "+str(unbanuser)+", or this user is not banned.")
            except AttributeError:
                await message.channel.send( "This user is not banned.")
        else:
            await message.channel.send( "Make sure you use '!unban|username#tag'.")
async def WCHANNEL(message,message2):
    if await VerifyOwner(message):
        if serverinfo[message.guild].search_server_configs("WELCOME_CHANNEL") != None:
            if serverinfo[message.guild].search_server_configs("WELCOME_CHANNEL")[1] == str(message.channel.id):
                await message.channel.send("This channel already is the welcome channel.")
            else:
                serverinfo[message.guild].change_server_config("WELCOME_CHANNEL",["WELCOME_CHANNEL",str(message.channel.id)])
                await message.channel.send("Changed the welcome channel to this text channel.")
        else:
            serverinfo[message.guild].add_server_config(["WELCOME_CHANNEL",str(message.channel.id)])
            await message.channel.send("Set this text channel as the welcome channel. All joining users will be welcomed here.")
async def NEWPLAYLIST(message,message2):
    name=message2.split("|")[1]
    if serverinfo[message.guild].search_server_configs("PLAYLIST:{0}".format(name)) == None:
        serverinfo[message.guild].add_server_config(["PLAYLIST:{0}".format(name)])
        await message.channel.send("Created a new playlist named `{0}`.".format(name))
    else:
        await message.channel.send( "There is already a playlist named `{0}`. If you would like to make a new playlist of that name, please delete the current playlist.".format(name))
async def DELETEPLAYLIST(message,message2):
    name=message2.split("|")[1]
    if serverinfo[message.guild].search_server_configs("PLAYLIST:{0}".format(name)) != None:
        serverinfo[message.guild].change_server_config("PLAYLIST:{0}".format(name),"")
        await message.channel.send("Deleted playlist `{0}`.".format(name))
    else:
        await message.channel.send( "There is no playlist named `{0}`. Please check spelling or refer to the list of playlists found at **!PLAYLISTS**.".format(name))
async def APPENDPLAYLIST(message,message2):
    name=message2.split("|")[1]
    if serverinfo[message.guild].search_server_configs("PLAYLIST:{0}".format(name)) != None:
        if serverinfo[message.guild].loading == False:
            await message.channel.send("Processing...")
            serverinfo[message.guild].loading = True
            music4=str(message.content).split("|")[2]
            if "list" in music4 and "watch" in music4:
                await message.channel.send("Invalid link.")
                return
            if "&index" in music4:
                music4 = music4.split('&index')
                music4 = music4[0]
            if music4.startswith("https://youtu.be"):
                music4 = music4.split('youtu.be/')[1]
                music4 = "https://www.youtube.com/watch?v="+music4   
            query=music4
            music4=search_music(music4)
            if music4 == None:
                await message.channel.send("Could not find song with query `{0}`".format(query))
                return
            serverinfo[message.guild].loading = False
            if len(serverinfo[message.guild].search_server_configs("PLAYLIST:{0}".format(name))[0])>1:
                arr=serverinfo[message.guild].search_server_configs("PLAYLIST:{0}".format(name))[0][1:]
            else:
                arr=[]
            if "user" in music4:
                return
            single=False
            counter=0
            if "list" in music4:
                from bs4 import BeautifulSoup
                page=requests.get(music4).text
                soup=BeautifulSoup(page,features='html.parser')
                for link in soup.find_all("a", {"dir":"ltr"}):
                    if "watch" in link['href']:
                        arr.append("https://www.youtube.com"+link['href'].split("&list")[0])
                        counter+=1
            else:
                single=True
                arr.append(music4)
            line=["PLAYLIST:{0}".format(name)]
            for item in arr:
                line.append(item)
            song=""
            url=music4
            if "youtube.com" in url:
                youtube = etree.HTML(urllib.request.urlopen(url).read())
                song=youtube.xpath("//span[@id='eow-title']/@title")
            elif "soundcloud.com" in url:
                from bs4 import BeautifulSoup
                page=requests.get(url).text
                soup=BeautifulSoup(page,features='html.parser')
                song=soup.find('meta',{'property':'og:title'})['content']
            serverinfo[message.guild].change_server_config("PLAYLIST:{0}".format(name),line)
            if single:
                await message.channel.send("Successfully added **{0}** to playlist `{1}`. `#{2}`.".format(song,name,len(arr)))
            else:
                await message.channel.send("Successfully added `{0}` songs to playlist `{1}`.".format(counter,name))
    else:
        await message.channel.send("There is no playlist named `{0}`. Please check **!PLAYLISTS** for a list of all playlists in this server.".format(name))
async def PLAYLISTS(message,message2):
    playlist_dict={}
    if serverinfo[message.guild].search_server_configs("PLAYLIST") != None:
        for playlist in serverinfo[message.guild].search_server_configs("PLAYLIST"):
            playlist_dict[playlist[0].split(":")[1]]=len(playlist[1:])
        embed=discord.Embed(title="Playlists",color=EMBEDCOLOR)
        val=""
        for key in list(playlist_dict.keys()):
            val=val+"`"+str(key)+"`\n"
        embed.add_field(name="Name",value=val)
        val=""
        for value in list(playlist_dict.values()):
            val=val+"`"+str(value)+"`\n"
        embed.add_field(name="# Songs",value=val,inline=True)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(title="Playlists",color=EMBEDCOLOR,description="There are no playlists in this server")
        await message.channel.send(embed=embed)
async def INVITE(message,message2):
    if await VerifyOwner(message):
        unbanuser = str(message.content).split('|')[1]
        unbanuser = await client.get_user_info(unbanuser)
        try:
            invite = await client.create_invite(message.channel, max_uses=1)
            await unbanuser.send("You have been invited to the server '"+str(message.guild)+"'. Here is the invite to the server.\n"+str(invite))
            await message.channel.send( "Successfully sent an invite to "+str(unbanuser))
        except discord.DiscordException:
            await message.channel.send( "Failed to invite "+str(unbanuser)+" to the server.")
async def UNBLOCK(message,message2):
    if await VerifyOwner(message):
        unblocked1 = str(message.content).split('|')
        unblocked = unblocked1[1]
        if unblocked.upper() != "ALL":
            unblocked = message.guild.get_member_named(unblocked)
        if str(unblocked).upper() == "ALL":
            serverinfo[message.guild].blocked=[]
            await message.channel.send( "Unblocked everyone in server")
        if (unblocked.id not in serverinfo[message.guild].blocked) and (str(unblocked).upper() != "ALL"):
            msg = "User not blocked."
            await message.channel.send( msg)
        elif unblocked.id in serverinfo[message.guild].blocked:
            msg = "Unblocked "+str(unblocked)
            serverinfo[message.guild].blocked.remove(unblocked.id)
            await message.channel.send( msg)
command["!HELP"]=Command("!HELP","Displays either a list of commands or command-specific help\n**Usage**\n`!HELP or !HELP|command`",HELP)
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
