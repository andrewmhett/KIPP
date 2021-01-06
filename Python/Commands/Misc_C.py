from ESSENTIAL_PACKAGES import *
from .Command_utils import *
from Command import *
import multiprocessing

async def FACEDETECT(message, message2, serverinfo, playerinfo):
    import subprocess
    os.system("sudo rm out_0.bmp; sudo rm img.jpg")
    os.system(
        "sudo curl \"{0}\" -o img.jpg".format(str(message.content).split("|")[1]))
    if os.path.exists("img.jpg"):
        stdout = subprocess.Popen("sudo /home/pi/openvino/deployment_tools/inference_engine/samples/build/armv7l/Release/object_detection_sample_ssd -m /home/pi/openvino/deployment_tools/inference_engine/samples/build/face-detection-adas-0001.xml -d MYRIAD -i img.jpg",
                                  shell=True, stdout=subprocess.PIPE).communicate()[0].decode()
        faces = stdout.count("PRINTED")
        if faces > 0:
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


async def CODE(message, message2, serverinfo, playerinfo):
    from subprocess import Popen, PIPE
    p = Popen(KIPP_DIR + '/Bash/NewestCommit.sh', stdout=PIPE, stderr=PIPE)
    emb = discord.Embed(title="Source Code")
    stdout = p.communicate()[0]
    p.kill()
    try:
        commit_msg = 'Newest commit:\n```diff\n' + \
            stdout.decode()[61:] + '\n```\n'
        if len(commit_msg) > 1800:
            raise discord.DiscordException
    except discord.DiscordException:
        commit_msg = 'The newest commit was too large to be displayed here.\n'
    emb.color = EMBEDCOLOR
    emb.description = "{0} My code is backed up on GitHub [here](https://github.com/andrewmhett/KIPP)\nAlso, my code has been reviewed by Codacy [here](https://app.codacy.com/gh/andrewmhett/KIPP/dashboard?branch=master)".format(commit_msg)
    await message.channel.send(embed=emb)


def locate_image(message2, queue):
    extensions=["jpeg","jpg"]
    url = "https://www.google.com/search?tbm=isch&source=hp&biw=2560&bih=1309&ei=eCYOW5bML6Oi0gK774NY&q={0}&oq={0}&gs_l=img.3..0l10.3693.4072.0.4294.7.6.0.1.1.0.59.152.3.3.0....0...1ac.1.64.img..3.4.156.0...0.OLvQBmMFRWY".format(
        message2.split('|')[1].replace(' ', '+').replace("'", "%27"))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    req = requests.get(url, headers=headers)
    html = str(req.content).split('["')
    for slice in html:
        if slice.startswith('https') and slice.split('"')[0].split('.')[-1] in extensions:
            image=slice.split('"')[0]
            if requests.get(image).status_code == 200:
                queue.put(image)
                break


async def IMAGE(message, message2, serverinfo, playerinfo):
    await message.channel.send("Processing image request...")
    queue = multiprocessing.Queue()
    proc = multiprocessing.Process(target=locate_image, args=(message2, queue))
    proc.start()
    try:
        image = queue.get(timeout=10)
    except Exception:
        image=""
    if image == "":
        await message.channel.send("No results for image search **{0}**".format(str(message.content).split('|')[1]))
    else:
        try:
            await send_image(message, image, "Image")
        except discord.errors.Forbidden:
            await message.channel.send("Missing permissions to send an image in this channel")

def locate_gif(message2, queue):
    extensions=["gif"]
    url = "https://www.google.com/search?tbm=isch&source=hp&biw=2560&bih=1309&ei=eCYOW5bML6Oi0gK774NY&q={0}&oq={0}&gs_l=img.3..0l10.3693.4072.0.4294.7.6.0.1.1.0.59.152.3.3.0....0...1ac.1.64.img..3.4.156.0...0.OLvQBmMFRWY".format(
        message2.split('|')[1].replace(' ', '+').replace("'", "%27"))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    req = requests.get(url, headers=headers)
    html = str(req.content).split('["')
    for slice in html:
        if slice.startswith('https') and slice.split('"')[0].split('.')[-1] in extensions:
            image=slice.split('"')[0]
            if requests.get(image).status_code == 200:
                queue.put(image)
                break


async def GIF(message, message2, serverinfo, playerinfo):
    await message.channel.send("Processing GIF request...")
    queue = multiprocessing.Queue()
    proc = multiprocessing.Process(target=locate_gif, args=(message2, queue))
    proc.start()
    try:
        image = queue.get(timeout=10)
    except Exception:
        image=""
    if image == "":
        await message.channel.send("No results for GIF search **{0}**".format(str(message.content).split('|')[1]))
    else:
        try:
            await send_image(message, image, "GIF")
        except discord.errors.Forbidden:
            await message.channel.send("Missing permissions to send an image in this channel")

async def STATUS(message, message2, serverinfo, playerinfo):
    from subprocess import Popen, PIPE
    p = Popen(KIPP_DIR + '/Bash/DaemonStatus.sh', stdout=PIPE, stderr=PIPE)
    stdout = p.communicate()[0].decode()
    p.kill()
    await message.channel.send("```" + stdout.split('ago')[0] + "ago```")


async def MATH(message, message2, serverinfo, playerinfo):
    infix = str(message.content.split("|")[1])
    value_dict = {"(": 1, ")": -1}
    valid_parens = True
    counter = 0
    for char in infix:
        if char == "(" or char == ")":
            counter += value_dict[char]
            if counter < 0:
                valid_parens = False
    if counter != 0:
        valid_parens = False
    if valid_parens:
        output = subprocess.Popen([KIPP_DIR + "/C++/evaluate", infix],
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0].decode()
        arr = output.split(": ")
        desc = arr[0] + ": `" + arr[1].split(" \n")[0] + "`\n" + arr[1].split(" \n")[
            1] + ": `" + arr[2].split(" \n")[0] + "`\n" + "RESULT: `" + arr[2].split(" \n")[1] + "`"
        if arr[2].split(" \n")[1] != "":
            em = discord.Embed(title="Math Evaluator",
                               description=desc, color=EMBEDCOLOR)
            await message.channel.send(embed=em)
        else:
            await message.channel.send("Unable to evaluate this expression.")
    else:
        await message.channel.send("Invalid parentheses")


async def CLEAR(message, message2, serverinfo, playerinfo):
    await message.channel.purge(limit=100)


async def ADDKIPP(message, message2, serverinfo, playerinfo):
    msg = 'https://discordapp.com/oauth2/authorize?client_id=386352783550447628&permissions=2146958583&scope=bot'
    await message.channel.send(msg)


async def BLOCKEDLIST(message, message2, serverinfo, playerinfo):
    if len(serverinfo[message.guild].blocked) > 0:
        names = []
        for i in serverinfo[message.guild].blocked:
            try:
                names.append("**" + str(message.guild.get_member(i)) + "**")
            except discord.DiscordException:
                try:
                    names.append("**" + str(await client.get_user_info(i) + "**"))
                except Exception:
                    print("Couldn't find user.")
        blocked = ", ".join(names)
        await message.channel.send("The users currently blocked in this server are: " + blocked)
    else:
        await message.channel.send("There are no users currently blocked in this server. To block a user, use the **!block** command.")


async def AVATAR(message, message2, serverinfo, playerinfo):
    member = str(message.content).split('|')[1]
    member = message.guild.get_member_named(member)
    await message.channel.send(str(member) + "'s icon URL is: " + str(member.avatar_url))


async def IQ(message, message2, serverinfo, playerinfo):
    arrlen = int(len(InterstellarQuotes))
    quoteNum = SystemRandom().randrange(0, arrlen)
    description = str(InterstellarQuotes[quoteNum])
    em = discord.Embed(title="Interstellar Quote",
                       description=description, colour=EMBEDCOLOR)
    em.set_footer(text=get_footer())
    await message.channel.send(embed=em)


async def COINFLIP(message, message2, serverinfo, playerinfo):
    rand = SystemRandom().randrange(0, 2)
    if rand == 0:
        await message.channel.send("Heads")
    else:
        await message.channel.send("Tails")


async def FATE(message, message2, serverinfo, playerinfo):
    imgs = os.listdir(KIPP_DIR + "/FATE")
    arrlen = int(len(imgs))
    picNum = SystemRandom().randrange(0, arrlen)
    yakub = False
    if "YAKUB" in imgs[picNum].upper():
        yakub = True
    if message.author.id == 289985985243119616:
        await message.channel.send(file=discord.File(KIPP_DIR + "/FATE/yakub.png"))
    else:
        await message.channel.send(file=discord.File(KIPP_DIR + "/FATE/" + imgs[picNum]))
    if yakub == True or message.author.id == 289985985243119616:
        msg = "You will see Yakub. You will live."
        await message.channel.send(msg)
    else:
        msg = "You will die."
        await message.channel.send(msg)

MISC("!IQ", "IQ stands for Interstellar Quote. This command will send a random Interstellar quote\n!IQ", IQ, [])
MISC("!CODE", "This command will give information about KIPP's code\n!CODE", CODE, [])
MISC("!IMAGE", "This command will return an image of the given search query\n!IMAGE|search",
     IMAGE, [str])
MISC("!GIF", "This command will return gif of the given search query\n!GIF|search",
     GIF, [str])
MISC("!STATUS", "Shows KIPP's Daemon's current status\n!STATUS", STATUS, [])
MISC("!MATH", "This command will return the answer to any basic math problem given\n!MATH|problem",
     MATH, [str])
MISC("!CLEAR", "This command will clear the last 100 messages sent in the channel\n!CLEAR", CLEAR, [])
MISC("!ADDKIPP", "This command returns a link that anyone can use to add KIPP to another server\n!ADDKIPP", ADDKIPP, [])
MISC("!BLOCKEDLIST", "This command will return a list of all blocked members of the server\n!BLOCKEDLIST", BLOCKEDLIST, [])
MISC("!AVATAR", "This command will return the full-size avatar picture of the given user\n!AVATAR|user",
     AVATAR, [str])
MISC("!FACEDETECT", "This command utilizes an Intel Neural Compute Stick 2 in order to process an image to detect a face\n!FACEDETECT|link to image",
     FACEDETECT, [str])
MISC("!COINFLIP", "Flip a coin and return either Heads or Tails\n!COINFLIP", COINFLIP, [])
MISC("!FATE", "Shows your fate. A very low chance of getting Yakub.\n!FATE", FATE, [])
