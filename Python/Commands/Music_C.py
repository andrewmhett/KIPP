import sys
import os
KIPP_DIR=os.environ["KIPP_DIR"]
sys.path.append(KIPP_DIR+"/Python")
from ESSENTIAL_PACKAGES import *
from .Command_utils import *
from Command import *

async def find_valid_song(query, serverinfo):
    index=0
    ytdl = youtube_dl.YoutubeDL()
    music4=""
    while index<=10:
        try:
            music4=search_music(query, serverinfo, index)
            if music4 != None:
                ytdl.extract_info(music4, download=False)
                break
            else:
                index+=1
        except youtube_dl.utils.DownloadError:
            index+=1
    return music4

async def NEWPLAYLIST(message,message2,serverinfo,playerinfo):
    name=message2.split("|")[1]
    if serverinfo[message.guild].search_server_configs("PLAYLIST:{0}".format(name)) == None:
        serverinfo[message.guild].add_server_config(["PLAYLIST:{0}".format(name)])
        await message.channel.send("Created a new playlist named `{0}`.".format(name))
    else:
        await message.channel.send( "There is already a playlist named `{0}`. If you would like to make a new playlist of that name, please delete the current playlist.".format(name))

async def DELETEPLAYLIST(message,message2,serverinfo,playerinfo):
    name=message2.split("|")[1]
    if serverinfo[message.guild].search_server_configs("PLAYLIST:{0}".format(name)) != None:
        serverinfo[message.guild].change_server_config("PLAYLIST:{0}".format(name),"")
        counter=0
        new_queue=[]
        for song in serverinfo[message.guild].queue:
            if song != "PLAYLIST: {0}".format(message2.split("|")[1]) or counter==0:
                new_queue.append(serverinfo[message.guild].queue[counter])
            elif song == "PLAYLIST: {0}".format(message2.split("|")[1]):
                serverinfo[message.guild].playlist=None
            counter+=1
        serverinfo[message.guild].queue=new_queue
        await message.channel.send("Deleted playlist `{0}`.".format(name))
    else:
        await message.channel.send( "There is no playlist named `{0}`. Please check spelling or refer to the list of playlists found at **!PLAYLISTS**.".format(name))

async def RENAMEPLAYLIST(message,message2,serverinfo,playerinfo):
    name=message2.split("|")[1]
    new_name=message2.split("|")[2]
    if serverinfo[message.guild].search_server_configs("PLAYLIST:{0}".format(name)) != None:
        line=["PLAYLIST:{0}".format(new_name)]
        for link in serverinfo[message.guild].search_server_configs("PLAYLIST:{0}".format(name))[0][1:]:
            line.append(link)
        serverinfo[message.guild].change_server_config("PLAYLIST:{0}".format(name),line)
        counter=0
        for song in serverinfo[message.guild].queue:
            if song == "PLAYLIST: {0}".format(name):
                serverinfo[message.guild].queue[counter]="PLAYLIST: {0}".format(new_name)
            counter+=1
        await message.channel.send("Renamed playlist `{0}` to `{1}`.".format(name,new_name))
    else:
        await message.channel.send( "There is no playlist named `{0}`. Please check spelling or refer to the list of playlists found at **!PLAYLISTS**.".format(name))

async def APPENDPLAYLIST(message,message2,serverinfo,playerinfo):
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
            if not music4.startswith("https://www.youtube.com") and not music4.startswith("https://www.soundcloud.com"):
                query=music4
                music4=await find_valid_song(query,serverinfo)
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
                tag=music4.split("list=")[1]
                from pyyoutube import Api
                api=Api(api_key=YOUTUBE_API_KEY)
                for song in api.get_playlist_items(playlist_id=tag,count=None).items:
                    arr.append("https://www.youtube.com/watch?v={0}".format(song.snippet.resourceId.videoId))
                    counter+=1
            else:
                single=True
                arr.append(music4)
            line=["PLAYLIST:{0}".format(name)]
            for item in arr:
                line.append(item)
            song=""
            url=music4
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

async def PLAYLISTS(message,message2,serverinfo,playerinfo):
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

async def MFIX(message,message2,serverinfo,playerinfo):
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

async def MUSIC(message,message2,serverinfo,playerinfo):
    server=message.guild
    notsearched = False
    serverinfo[message.guild].musictextchannel = message.channel
    currentlyplaying=False
    if serverinfo[message.guild].mHandler != None:
        currentlyplaying=serverinfo[message.guild].mHandler.is_playing
    if (currentlyplaying == False) or (currentlyplaying == True and message.author.voice.channel == message.guild.get_member(KIPP_ID).voice.channel):
        try:
            if message2.split("|")[1].startswith("PLAYLIST:")==False:
                if serverinfo[message.guild].search_server_configs("PLAYLIST:{0}".format(message2.split("|")[1])) != None:
                    await message.channel.send("Command usage note -- this syntax will find music matching the query `{0}` on YouTube. If you meant to play the playlist named `{0}`, use the command `!MUSIC|PLAYLIST:{0}`.".format(message2.split("|")[1]))
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
                        notsearched=False
                        if not music4.startswith("https://www.youtube.com") and "soundcloud.com" not in music4:
                            if str(message.author.voice.channel) != "None":
                                query=music4
                                music4=await find_valid_song(query,serverinfo[message.guild])
                                serverinfo[message.guild].loading = False
                                notsearched=False
                                if music4==None:
                                    notsearched=True
                                    await message.channel.send("Could not find music matching query `{0}`".format(query))
                        server = message.guild
                        if notsearched == False:
                            if ((music3[0]).upper() == "!MUSIC"):
                                if ("channel" not in music4 and "youtube.com" in music4) or ("soundcloud.com" in music4):
                                    serverinfo[message.guild].musiccolor=playerinfo[message.author].hrolecolor
                                    await join_voice_channel(message,serverinfo)
                                    if serverinfo[message.guild].playlist != None:
                                        serverinfo[message.guild].queue=serverinfo[message.guild].queue[:-1]
                                        add_to_queue(message.guild, music4, serverinfo)
                                        serverinfo[message.guild].queue.append("PLAYLIST: {0}".format(serverinfo[message.guild].playlist))
                                    else:
                                        add_to_queue(message.guild, music4, serverinfo)
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
                                elif "channel" in music4 and "youtube.com" in music4:
                                    await message.channel.send( "Please do not try to play an entire youtube channel. Get one specific song you would like to hear, and play that.")
                                    serverinfo[message.guild].loading = False
                        else:
                            serverinfo[message.guild].loading=False
                    else:
                        await message.delete()
                else:
                    await message.channel.send( "Please use the correct syntax. Use !music|youtubelink/soundcloudlink or !music|youtubesearch to use the music command.")
                    serverinfo[message.guild].loading = False
            else:
                if serverinfo[message.guild].playlist == None:
                    if serverinfo[message.guild].search_server_configs(message2.split("|")[1]) != None:
                        if len(serverinfo[message.guild].search_server_configs(message2.split("|")[1])[0][1:])>0:
                            await join_voice_channel(message,serverinfo)
                            serverinfo[message.guild].musicchannel=message.channel
                            serverinfo[message.guild].playlist=message2.split('PLAYLIST:')[1]
                            serverinfo[message.guild].queue.append("PLAYLIST: {0}".format(message2.split("PLAYLIST:")[1]))
                        else:
                            await message.channel.send("The playlist named `{0}` is empty. You may append songs to this playlist with **!APPENDPLAYLIST**.".format(message2.split("PLAYLIST:")[1]))
                    else:
                        await message.channel.send( "There is no playlist named `{0}`. Use **!PLAYLISTS** to see a list of all playlists in this server.".format(message2.split("PLAYLIST:")[1]))
                else:
                    await message.channel.send("There is already a playlist playing. In order to play another playlist, please remove the current playlist from the queue.")
        except Exception as err:
            serverinfo[message.guild].loading = False
            raise
    elif (currentlyplaying == True) and (message.author.voice.channel != message.guild.get_member(KIPP_ID).voice.channel):
        await message.channel.send( "There is a song currently playing in another voice channel ("+str(message.guild.get_member(KIPP_ID).voice.channel)+"). Join that voice channel in order to change the music, or you can wait for that music to end, and run this command again.")

async def PAUSE(message,message2,serverinfo,playerinfo):
    if await VerifyMusicUser(message,serverinfo):
        if serverinfo[message.guild].mHandler.paused == False:
            await message.channel.send( "Music paused.")
            serverinfo[message.guild].mHandler.pausedatetime=datetime.now()
            serverinfo[message.guild].mHandler.paused=True
            message.guild.voice_client.pause()
        else:
            await message.channel.send( "Music already is paused. To resume, use the **!resume** command.")

async def RESUME(message,message2,serverinfo,playerinfo):
    if await VerifyMusicUser(message,serverinfo):
        if serverinfo[message.guild].mHandler.paused:
            message.guild.voice_client.resume()
            serverinfo[message.guild].mHandler.paused=False
            await message.channel.send( "Music resumed.")
        else:
            await message.channel.send( "There is currently music playing. To pause the music, use the **!pause** command.")

async def REMOVESONG(message,message2,serverinfo,playerinfo):
    if await VerifyMusicUser(message,serverinfo):
        try:
            index = int(message2.split("|")[1])
        except Exception:
            await message.channel.send( "Song index must be an integer.")
        if len(serverinfo[message.guild].queue)>1:
            if index >0 and index <= len(serverinfo[message.guild].queue):
                if serverinfo[message.guild].playlist != None and len(serverinfo[message.guild].queue[index])>2:
                    serverinfo[message.guild].playlist = None
                serverinfo[message.guild].queue.pop(index)
                await message.channel.send( "Removed song #{0} from queue".format(index))
            else:
                await message.channel.send("Invalid song index")
        else:
            await message.channel.send("There are no songs in the queue.")

async def SKIP(message,message2,serverinfo,playerinfo):
    if await VerifyMusicUser(message,serverinfo):
        if serverinfo[message.guild].mHandler.paused == True:
            message.guild.voice_client.resume()
            serverinfo[message.guild].mHandler.paused = False
        serverinfo[message.guild].mHandler.skip()
        if len(serverinfo[message.guild].queue)==1:
            await message.channel.send( "There are no more songs in the queue. Current song ended.")

command["!NEWPLAYLIST"]=MUSC("!NEWPLAYLIST","Creates a new music playlist of a given name\n!NEWPLAYLIST|name",NEWPLAYLIST,[str])
command["!APPENDPLAYLIST"]=MUSC("!APPENDPLAYLIST","Adds a song to a playlist corresponding to either entered query, link to a song (YouTube or Soundcloud), or link to a youtube playlist.\n!APPENDPLAYLIST|playlist name|query or link",APPENDPLAYLIST,[str,str])
command["!DELETEPLAYLIST"]=MUSC("!DELETEPLAYLIST","Deletes the music playlist of a given name\n!DELETEPLAYLIST|name",DELETEPLAYLIST,[str])
command["!RENAMEPLAYLIST"]=MUSC("!RENAMEPLAYLIST","Renames a playlist\n!RENAMEPLAYLIST|original name|new name",RENAMEPLAYLIST,[str,str])
command["!PLAYLISTS"]=MUSC("!PLAYLISTS","Displays a list of all playlists in the server\n!PLAYLISTS",PLAYLISTS,[])
command["!MFIX"]=MUSC("!MFIX","This command will reset KIPP's voice client and related variables in order to fix most problems with music\n!MFIX",MFIX,[])
command["!MUSIC"]=MUSC("!MUSIC","This command will cause KIPP to play music from YouTube or Soundcloud in your voice channel based on your entered link or query\n!MUSIC|query or link",MUSIC,[str])
command["!PAUSE"]=MUSC("!PAUSE","This command will pause KIPP, if playing\n!PAUSE",PAUSE,[])
command["!RESUME"]=MUSC("!RESUME","This command will resume KIPP, if paused\n!RESUME",RESUME,[])
command["!REMOVESONG"]=MUSC("!REMOVESONG","This command will remove the specified song from the queue\n!REMOVESONG|queue position",REMOVESONG,[int])
command["!SKIP"]=MUSC("!SKIP","This command will skip the current song, and play the next song in queue.\n!SKIP",SKIP,[])
