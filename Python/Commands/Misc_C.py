from ESSENTIAL_PACKAGES import *
from .Command_utils import *
from Command import *
import multiprocessing

async def FACEDETECT(message,message2,serverinfo,playerinfo):
    import subprocess
    os.system("sudo rm out_0.bmp; sudo rm img.jpg")
    os.system("sudo curl \"{0}\" -o img.jpg".format(str(message.content).split("|")[1]))
    if os.path.exists("img.jpg"):
        stdout=subprocess.Popen("sudo /home/pi/openvino/deployment_tools/inference_engine/samples/build/armv7l/Release/object_detection_sample_ssd -m /home/pi/openvino/deployment_tools/inference_engine/samples/build/face-detection-adas-0001.xml -d MYRIAD -i img.jpg", shell=True,stdout=subprocess.PIPE).communicate()[0].decode()
        faces=stdout.count("PRINTED")
        if faces>0:
            if faces != 1:
                await message.channel.send("{0} faces were detected.".format(faces))
            else:
                await message.channel.send("1 face was detected.")
            file = discord.File("out_0.bmp", filename="out.png")
            await message.channel.send(file=file) 
        else:
            await message.channel.send("No faces were detected.")
    else:
        await message.channel.send("An error occurred while downloading the image.")

async def CODE(message,message2,serverinfo,playerinfo):
    from subprocess import Popen, PIPE
    p=Popen(KIPP_DIR+'/Bash/NewestCommit.sh',stdout=PIPE,stderr=PIPE)
    emb=discord.Embed(title="Source Code")
    stdout=p.communicate()[0]
    p.kill()
    try:
        commit_msg='Newest commit:\n```diff\n'+stdout.decode()[61:]+'\n```\n'
        if len(commit_msg)>1800:
            raise discord.DiscordException
    except discord.DiscordException:
        commit_msg = 'The newest commit was too large to be displayed here.\n'
    emb.color=EMBEDCOLOR
    emb.description="{0} My code is backed up on GitHub [here](https://github.com/andrewmhett/KIPP)\nAlso, my code has been reviewed by Codacy [here](https://app.codacy.com/project/LockdownDoom/KIPP/dashboard?branchId=10423847)".format(commit_msg)
    await message.channel.send(embed=emb)
    
def locate_image(message2,queue):
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
                queue.put("")
                break
            if ".JPEG" in ("https://"+str(req).split('https://')[i].split('"')[0]).upper() or ".JPG" in ("https://"+str(req).split('https://')[i].split('"')[0]).upper() and "File:" not in "https://"+str(req).split('https://')[i].split('"')[0]:
                image="https://"+str(req).split('https://')[i].split('"')[0]
                if requests.get(image).status_code==200:
                    queue.put(image)
                    break
        except Exception:
            cont+=1

async def IMAGE(message,message2,serverinfo,playerinfo):
    await message.channel.send("Processing image request...")
    queue=multiprocessing.Queue()
    proc=multiprocessing.Process(target=locate_image,args=(message2,queue))
    proc.start()
    proc.join()
    image=queue.get()
    if image == "":
        await message.channel.send("No results for image search **{0}**".format(str(message.content).split('|')[1]))
    else:
        await send_image(message,image,"Image")

async def USERINFO(message,message2,serverinfo,playerinfo):
    description = "**Currently Playing:** "+str(message.author.activity)+"\n**KIPPCOINS:** "+str(playerinfo[message.author].GET_KIPPCOINS())
    em = discord.Embed(description=description,colour=EMBEDCOLOR)
    em.set_author(name=str(message.author), icon_url=message.author.avatar_url)
    em.set_footer(text=get_footer())
    await message.channel.send( embed=em)

async def STATUS(message,message2,serverinfo,playerinfo):
    from subprocess import Popen, PIPE
    p=Popen(KIPP_DIR+'/Bash/DaemonStatus.sh',stdout=PIPE,stderr=PIPE)
    stdout=p.communicate()[0].decode()
    p.kill()
    await message.channel.send("```"+stdout.split('ago')[0]+"ago```")

async def MATH(message,message2,serverinfo,playerinfo):
    mathP = str(message.content)
    mathP2 = mathP.split('|')
    math = str(mathP2[1])
    try:
        mathT = eval(math)
    except SyntaxError:
        await message.channel.send( "Sorry, KIPP failed to process this request.")
    msg = str(math)+" = "+str(mathT)
    await message.channel.send( msg)

async def CLEAR(message,message2,serverinfo,playerinfo):
    await message.channel.purge(limit=100)

async def ADDKIPP(message,message2,serverinfo,playerinfo):
    msg = 'https://discordapp.com/oauth2/authorize?client_id=386352783550447628&permissions=2146958583&scope=bot'
    await message.channel.send( msg)

async def BLOCKEDLIST(message,message2,serverinfo,playerinfo):
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

async def AVATAR(message,message2,serverinfo,playerinfo):
    member = str(message.content).split('|')[1]
    member = message.guild.get_member_named(member)
    await message.channel.send( str(member)+"'s icon URL is: "+str(member.avatar_url))

async def IQ(message,message2,serverinfo,playerinfo):
    arrlen = int(len(InterstellarQuotes))
    quoteNum = SystemRandom().randrange(0,arrlen)
    description = str(InterstellarQuotes[quoteNum])
    em = discord.Embed(title="Interstellar Quote",description=description,colour=EMBEDCOLOR)
    em.set_footer(text=get_footer())
    await message.channel.send(embed=em)
    
async def COINFLIP(message,message2,serverinfo,playerinfo):
    rand=SystemRandom().randrange(0,2)
    if rand==0:
        await message.channel.send("Heads")
    else:
        await message.channel.send("Tails")

command["!IQ"]=MISC("!IQ","IQ stands for Interstellar Quote. This command will send a random Interstellar quote\n!IQ",IQ,[])
command["!CODE"]=MISC("!CODE","This command will give information about KIPP's code\n!CODE",CODE,[])
command["!IMAGE"]=MISC("!IMAGE","This command will return an image of the given search query\n!IMAGE|search",IMAGE,[str])
command["!USERINFO"]=MISC("!USERINFO","This command will return useful user-specific information\n!USERINFO",USERINFO,[])
command["!STATUS"]=MISC("!STATUS","Shows KIPP's Daemon's current status\n!STATUS",STATUS,[])
command["!MATH"]=MISC("!MATH","This command will return the answer to any basic math problem given\n!MATH|problem",MATH,[str])
command["!CLEAR"]=MISC("!CLEAR","This command will clear the last 100 messages sent in the channel\n!CLEAR",CLEAR,[])
command["!ADDKIPP"]=MISC("!ADDKIPP","This command returns a link that anyone can use to add KIPP to another server\n!ADDKIPP",ADDKIPP,[])
command["!BLOCKEDLIST"]=MISC("!BLOCKEDLIST","This command will return a list of all blocked members of the server\n!BLOCKEDLIST",BLOCKEDLIST,[])
command["!AVATAR"]=MISC("!AVATAR","This command will return the full-size avatar picture of the given user\n!AVATAR|user",AVATAR,[str])
command["!FACEDETECT"]=MISC("!FACEDETECT","This command utilizes an Intel Neural Compute Stick 2 in order to process an image to detect a face\n!FACEDETECT|link to image",FACEDETECT,[str])
command["!COINFLIP"]=MISC("!COINFLIP","Flip a coin and return either Heads or Tails\n!COINFLIP",COINFLIP,[])
