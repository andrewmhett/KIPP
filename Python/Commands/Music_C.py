import sys
import os
KIPP_DIR=os.environ["KIPP_DIR"]
sys.path.append(KIPP_DIR+"/Python")
from ESSENTIAL_PACKAGES import *
from .Command_utils import *
from Command import *

async def NEWPLAYLIST(message,message2,serverinfo,playerinfo):
    name=message2.split("|")[1]
    if serverinfo[message.guild].search_server_configs("PLAYLIST:{0}".format(name)) == None:
        serverinfo[message.guild].add_server_config(["PLAYLIST:{0}".format(name)])
        await message.channel.send("Created a new playlist named `{0}`. Before playing the playlist, you must use the `!APPENDPLAYLIST` command to add at least one song to the playlist. After this, you can play it with the `!MUSIC|PLAYLIST:{0}` command.".format(name))
    else:
        await message.channel.send( "There is already a playlist named `{0}`. If you would like to make a new playlist of that name, please delete or rename the existing playlist.".format(name))

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
        await message.channel.send("Processing...")
        music4=str(message.content).split("|")[2]
        if not music4.startswith("https://"):
            query=music4
            music4=search_music(query,serverinfo)
        if music4 == None:
            await message.channel.send("Could not find song with query `{0}`".format(query))
            return
        domain=sanitize_url(music4)
        if domain == -1:
            await message.channel.send("Unsafe or unsupported URL domain. Aborting...")
        if "list" in music4 and "watch" in music4:
            await message.channel.send("Invalid link.")
            return
        if "&index" in music4:
            music4 = music4.split('&list')
            music4 = music4[0]
        if domain == "youtu.be":
            music4 = music4.split('youtu.be/')[1]
            music4 = "https://www.youtube.com/watch?v="+music4
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
        message.guild.voice_client.stop()
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
    serverinfo[message.guild].musictextchannel = message.channel
    currentlyplaying=False
    if serverinfo[message.guild].mHandler != None:
        currentlyplaying=serverinfo[message.guild].mHandler.is_playing
    if (currentlyplaying == False) or (currentlyplaying == True and message.author.voice.channel == message.guild.get_member(KIPP_ID).voice.channel):
        try:
            if message2.split("|")[1].startswith("PLAYLIST:")==False:
                if serverinfo[message.guild].search_server_configs("PLAYLIST:{0}".format(message2.split("|")[1])) != None:
                    await message.channel.send("Command usage note -- this syntax will find music matching the query `{0}` on YouTube. If you meant to play the playlist named `{0}`, use the command `!MUSIC|PLAYLIST:{0}`.".format(message2.split("|")[1]))
                music2 = str(message.content)
                music3 = music2.split('|')
                music4= music3[1]
                serverinfo[server].musictextchannel = message.channel
                serverinfo[message.guild].paused = False
                if not music4.startswith("https://"):
                    if str(message.author.voice.channel) != "None":
                        query=music4
                        music4=search_music(query,serverinfo[message.guild])
                        if music4==None:
                            await message.channel.send("Could not find music matching query `{0}`".format(query))
                            return
                domain = sanitize_url(music4)
                if domain == -1:
                    await message.channel.send("Unsafe or unsupported URL domain. Aborting...")
                    return
                if domain == "soundcloud.com":
                    if "/sets/" in music4:
                        if "?in=" in music4:
                            music4=music4.split("?in")[0]
                        else:
                            await message.channel.send("Sorry, but Soundcloud playlists are not yet supported")
                            return
                if domain == "youtu.be":
                    music4 = music4.split('youtu.be/')[1]
                    music4 = "https://www.youtube.com/watch?v="+music4
                    domain="www.youtube.com"
                if "&index" in music4:
                    music4 = music4.split('&list')
                    music4 = music4[0]
                if "playlist" not in music4:
                    if domain == "www.youtube.com":
                        music4=music4.split("watch?v=")[1]
                        music4 = "https://www.youtube.com/watch?v="+music4
                    server = message.guild
                    if "channel" not in music4:
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
                                    await message.channel.send( "Song added to queue. `#"+str(len(serverinfo[message.guild].queue)-2)+"`")
                                else:
                                    await message.channel.send( "Song added to queue. `#"+str(len(serverinfo[message.guild].queue)-1)+"`")
                        if len(serverinfo[message.guild].queue) == 1:
                            serverinfo[message.guild].musicchannel=message.channel
                    else:
                        await message.channel.send( "Please do not try to play an entire YouTube channel. Get one specific song you would like to hear, and play that.")
                else:
                    await join_voice_channel(message,serverinfo)
                    if len(serverinfo[message.guild].queue) == 0:
                        serverinfo[message.guild].musicchannel=message.channel
                    from pyyoutube import Api
                    api=Api(api_key=YOUTUBE_API_KEY)
                    counter=0
                    for song in api.get_playlist_items(playlist_id=music4.split("playlist?list=")[1],count=None).items:
                        serverinfo[message.guild].queue.append([song.snippet.title,"https://www.youtube.com/watch?v={0}".format(song.snippet.resourceId.videoId)])
                        counter+=1
                    await message.channel.send("Added `{0}` songs to queue.".format(counter))
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
        except Exception:
            raise
    elif (currentlyplaying == True) and (message.author.voice.channel != message.guild.get_member(KIPP_ID).voice.channel):
        await message.channel.send( "There is a song currently playing in another voice channel ("+str(message.guild.get_member(KIPP_ID).voice.channel)+"). Join that voice channel in order to change the music, or you can wait for that music to end, and run this command again.")

async def QUEUE(message,message2,serverinfo,playerinfo):
    queuelist="\nNo songs in queue"
    if len(serverinfo[message.guild].queue)>1:
        queuelist=""
        i=0
        for song in serverinfo[message.guild].queue[1:]:
            i=i+1
            if len(song)>2:
                if len(queuelist)+len("\n`#{0}` {1}".format(i,song))<=1000:
                    queuelist=queuelist+"\n`#{0}` {1}".format(i,song)
                else:
                    break
            else:
                if len(queuelist)+len("\n`#{0}` {1}".format(i,song[0]))<=1000:
                    queuelist=queuelist+"\n`#{0}` {1}".format(i,"["+(''.join(song[0]))+"]("+song[1]+")")
                else:
                    break
        if len(serverinfo[message.guild].queue)-i>1:
            queuelist+=("\n`...and {0} more songs`".format(len(serverinfo[message.guild].queue)-i) if len(serverinfo[message.guild].queue)-i>2 else "\n`...and 1 more song`")
    em=discord.Embed(title="Queue",description=queuelist)
    em.color=EMBEDCOLOR
    await message.channel.send(embed=em)

async def CLEARQUEUE(message,message2,serverinfo,playerinfo):
    serverinfo[message.guild].queue=[serverinfo[message.guild].queue[0]]
    serverinfo[message.guild].playlist=None
    await message.channel.send("Removed all songs from the queue.")

async def SHUFFLE(message,message2,serverinfo,playerinfo):
    if len(serverinfo[message.guild].queue)>1:
        import random
        end=None
        new_queue=serverinfo[message.guild].queue[1:]
        if serverinfo[message.guild].queue[len(serverinfo[message.guild].queue)-1][0].startswith("PLAYLIST: "):
            end=serverinfo[message.guild].queue[len(serverinfo[message.guild].queue)-1]
            new_queue=serverinfo[message.guild].queue[1:-1]
        random.shuffle(new_queue)
        i=1
        for song in new_queue:
            serverinfo[message.guild].queue[i]=song
            i+=1
        if end != None:
            serverinfo[message.guild].queue[i]=end
        await message.channel.send("Shuffled the queue.")
    else:
        await message.channel.send("There are no songs in the queue to shuffle.")

async def PAUSE(message,message2,serverinfo,playerinfo):
    if await VerifyMusicUser(message,serverinfo):
        if serverinfo[message.guild].mHandler.paused == False:
            await message.channel.send( "Music paused.")
            serverinfo[message.guild].mHandler.pausedatetime=datetime.now()
            serverinfo[message.guild].mHandler.paused=True
            message.guild.voice_client.pause()
        else:
            await message.channel.send( "Music already is paused. To resume, use the `!RESUME` command.")

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
        index = int(message2.split("|")[1])
        if len(serverinfo[message.guild].queue)>1:
            if index >0 and index < len(serverinfo[message.guild].queue):
                if serverinfo[message.guild].playlist != None and len(serverinfo[message.guild].queue[index])>2:
                    serverinfo[message.guild].playlist = None
                serverinfo[message.guild].queue.pop(index)
                await message.channel.send( "Removed song at queue position `{0}`".format(index))
            else:
                await message.channel.send("Invalid song index")
        else:
            await message.channel.send("There are no songs in the queue.")

async def MOVESONG(message,message2,serverinfo,playerinfo):
    if await VerifyMusicUser(message,serverinfo):
        index1=int(message2.split("|")[1])
        index2=int(message2.split("|")[2])
        if index1>0 and index1<len(serverinfo[message.guild].queue):
            if index2>0 and index2<len(serverinfo[message.guild].queue):
                if not serverinfo[message.guild].queue[index1][0].startswith("PLAYLIST: "):
                    serverinfo[message.guild].queue.insert(index2,serverinfo[message.guild].queue.pop(index1))
                    await message.channel.send("Moved song at position `{0}` to position `{1}`".format(index1,index2))
                else:
                    await message.channel.send("Cannot move playlists in the queue.")
            else:
                await message.channel.send("Invalid argument: index to move to is out of bounds")
        else:
            await message.channel.send("Invalid argument: index to move from out of bounds")

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
command["!MOVESONG"]=MUSC("!MOVESONG","This command will move the song at the 'from index' to the 'to index'\n!MOVESONG|from position|to position",MOVESONG,[int,int])
command["!CLEARQUEUE"]=MUSC("!CLEARQUEUE","This command will clear all songs from the queue.\n!CLEARQUEUE",CLEARQUEUE,[])
command["!SKIP"]=MUSC("!SKIP","This command will skip the current song, and play the next song in queue.\n!SKIP",SKIP,[])
command["!QUEUE"]=MUSC("!QUEUE","Displays a larger version of the queue list displayed in KIPP's music message.\n!QUEUE",QUEUE,[])
command["!SHUFFLE"]=MUSC("!SHUFFLE","Shuffles the queue.\n!SHUFFLE",SHUFFLE,[])
