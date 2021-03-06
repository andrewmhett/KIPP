from ESSENTIAL_PACKAGES import *
from Music import search_music
from Footer import get_footer
import sys
import os
KIPP_DIR = os.environ["KIPP_DIR"]
sys.path.append(KIPP_DIR + "/Python")
CREATOR_ID = 289920025077219328
KIPP_ID = 386352783550447628
if len(sys.argv) > 1:
    if sys.argv[1] == "dev":
        KIPP_ID = 726545013064073277
InterstellarQuotes = ["'Do not go gentle into that good night'\n**Professor Brand**", "'Come on, TARS!'\n**Cooper**", "'Cooper, this is no time for caution!'\n**TARS**",
                      "'You tell that to Doyle.'\n**Cooper**", "'Newton's third law. You gotta leave something behind.'\n**Cooper**", "'Step back, professor, step back!'\n**TARS**", "'No, it's necessary.'\n**Cooper**"]

safe_domains = [
    "www.youtube.com",
    "youtu.be",
    "soundcloud.com"
]


def sanitize_url(url):
    invalid_link = False
    url_domain = ""
    try:
        request = requests.get(url)
        if request.url.split("https://")[1].split("/")[0] not in safe_domains:
            invalid_link = True
        else:
            for domain in safe_domains:
                if url.split("https://")[1].split("/")[0] == domain:
                    url_domain = domain
        for redirect in request.history:
            if redirect.url.split("https://")[1].split("/")[0] not in safe_domains:
                invalid_link = True
    except requests.exceptions.ConnectionError:
        invalid_link = True
    if invalid_link:
        return -1
    return url_domain


async def send_image(message, url, ext):
    emb = discord.Embed(title=("{0} result for '{1}'".format(
        ext, str(message.content).split('|')[1])), colour=EMBEDCOLOR)
    emb.set_image(url=url)
    emb.set_footer(text=get_footer())
    await message.channel.send(embed=emb)


def reset_gamblegame(user, playerinfo):
    playerinfo[user].gamblemessage = None
    playerinfo[playerinfo[user].challenger].gamblemessage = None
    playerinfo[playerinfo[user].challenger].challenger = None
    playerinfo[playerinfo[user].challenger].betting = False
    playerinfo[user].betting = False
    playerinfo[user].challenger = None


async def join_voice_channel(message, serverinfo):
    if message.author.voice != None:
        users = []
        for user in message.author.voice.channel.members:
            users.append(user)
        if message.guild.voice_client == None:
            channel = message.author.voice.channel
            await channel.connect()
            serverinfo[message.guild].jointime = datetime.now()
        if message.guild.get_member(KIPP_ID) not in users:
            channel = message.author.voice.channel
            user = message.guild.get_member(KIPP_ID)
            await user.edit(voice_channel=channel)
    else:
        await message.channel.send("You are not in a voice channel. Join one in order to play music.")


async def VerifyOwner(message):
    if message.author == message.guild.owner or message.author.id == CREATOR_ID:
        return True
    return False


async def VerifyMusicUser(message, serverinfo):
    currentlyplaying = False
    if serverinfo[message.guild].mHandler != None:
        currentlyplaying = serverinfo[message.guild].mHandler.is_playing
    if currentlyplaying == True:
        if str(message.author.voice.channel) != str(message.guild.get_member(KIPP_ID).voice.channel):
            await message.channel.send("Please join the channel where the music is playing (" + str(message.guild.get_member(KIPP_ID).voice.channel) + ") in order to use music commands")
            return False
        else:
            return True
    else:
        await message.channel.send("Please start some music in order to use music commands")
        return False


def add_to_queue(server, url, serverinfo):
    name = "NAME_UNAVAILABLE"
    # this parser code works for both youtube and soundcloud HTML
    from bs4 import BeautifulSoup
    page = requests.get(url).text
    soup = BeautifulSoup(page, features='html.parser')
    name = soup.find('meta', {'property': 'og:title'})['content']
    serverinfo[server].queue.append([name, url])
