from ESSENTIAL_PACKAGES import *
from Footer import get_footer
from config import *
EMBEDCOLOR=0x36393E
ytdl_format_options = {
    'format': 'bestaudio/best',
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
def search_music(query):
    music=None
    if ((query.startswith("https://www.youtube.com") == False) and (query.startswith("https://youtu.be") == False) and (query.startswith("http://www.youtube.com") == False) and "//soundcloud.com" not in query):
        try:
            query_string = urllib.parse.urlencode({"search_query" : query})
            req = urllib.request.Request("http://www.youtube.com/results?" + query_string)
            with urllib.request.urlopen(req) as html:
                searchresults = re.findall(r'href=\"\/watch\?v=(.{11})', html.read().decode())
            music="http://www.youtube.com/watch?v="+searchresults[0]
        except IndexError:
            logging.log(50,"Not found")
    return music
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=1.0):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.duration = data.get('duration')
        self.is_live=False
        if self.duration == 0:
            self.is_live = True
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=True):
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        cls.url=url
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
class music_handler:
    def __init__(self,server,player,channel,loop):
        self.server=server
        self.resend_timer=0
        self.loop=loop
        self.channel=channel
        server.voice_client.play(player)
        self.player=player
        self.paused=False
        self.message=None
        self.starttime=datetime.now()
        self.duration=player.duration
        self.title=player.title
        self.link=player.url
        self.footer=get_footer()
        self.hours=0
        if self.player.is_live == False:
            mins=int(self.duration/60)
            seconds=int(self.duration-(mins*60))
            hours=int(mins/60)
            self.hours=hours
            if hours > 0:
                mins=mins-(hours*60)
                if len(str(mins))==1:
                    mins="0"+str(mins)
                if len(str(seconds)) == 1:
                    self.length=str(hours)+":"+str(mins)+":"+"0"+str(seconds)
                else:
                    self.length=str(hours)+":"+str(mins)+":"+str(seconds)
            else:
                if len(str(seconds)) == 1:
                    self.length=str(mins)+":"+"0"+str(seconds)
                else:
                    self.length=str(mins)+":"+str(seconds)
        else:
            self.length = "Currently Streaming"
        self.desc = ("["+self.title+"]("+self.link+")\n`0:00 / "+self.length)
        self.em = discord.Embed(description=self.desc,colour=EMBEDCOLOR)
        self.em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
        self.em.set_footer(text=self.footer)
        self.is_playing=True
        self.pausedatetime=None
        self.pausetime=None
        self.task = self.loop.create_task(self.update_loop())
    def skip(self):
        self.server.voice_client.stop()
        self.player.is_live=False
    async def update_loop(self):
        while self.is_playing:
            self.resend_timer+=1
            if self.server.voice_client.is_playing():
                self.is_playing=True
            elif self.paused:
                self.is_playing=True
            else:
                self.is_playing=False
            import datetime
            queuelist="\nNo songs in queue"
            if len(serverinfo[self.server].queue)>1:
                queuelist=""
                i=0
                for song in serverinfo[self.server].queue[1:]:
                    i=i+1
                    if len(song)>2:
                        queuelist=queuelist+"\n`#{0}` {1}".format(i,song)
                    else:
                        queuelist=queuelist+"\n`#{0}` {1}".format(i,"["+(''.join(song[0]))+"]("+song[1]+")")
            if self.paused:
                self.pausetime=datetime.datetime.now()-self.pausedatetime
            if self.pausetime==None:
                c = datetime.datetime.now()-self.starttime
            else:
                c = datetime.datetime.now()-(self.starttime+datetime.timedelta(seconds=self.pausetime.seconds))
            if self.paused == False:
                progress = divmod(c.days * 86400 + c.seconds, 60)
                self.minutedelta=str(progress).split('(')[1].split(')')[0].split(',')[0]
                self.seconddelta=str(progress).split('(')[1].split(')')[0].split(', ')[1]
                if len(str(self.seconddelta)) == 1:
                    self.seconddelta='0'+str(self.seconddelta)
                self.hours=int(int(self.minutedelta)/60)
                if self.player.is_live == False:
                    percent=int(18*(((int(self.hours)*3600)+(int(self.minutedelta)*60)+int(self.seconddelta))/int(self.duration)))+1
                    self.bar=("▣"*percent)+"▢"*(18-percent)
                else:
                    self.bar="▣"*18
            pauseStr=""
            if self.paused:
                pauseStr=" (paused)"
            if self.hours>0:
                self.minutedelta=int(self.minutedelta)-(self.hours*60)
                if len(str(self.minutedelta))==1:
                    self.minutedelta="0"+str(self.minutedelta)
                else:
                    self.minutedelta=str(self.minutedelta)
                self.em=discord.Embed(description = self.desc.split('`')[0]+"`"+str(self.hours)+":"+str(self.minutedelta)+':'+str(self.seconddelta)+' / '+self.length+'`'+pauseStr+'\n'+self.bar+'\n**Queue:**'+queuelist,colour=EMBEDCOLOR)
            else:
                self.em=discord.Embed(description = self.desc.split('`')[0]+"`"+str(self.minutedelta)+':'+str(self.seconddelta)+' / '+self.length+'`'+pauseStr+'\n'+self.bar+'\n**Queue:**'+queuelist,colour=EMBEDCOLOR)
            self.em.set_footer(text=self.footer)
            self.em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
            if self.resend_timer/30 >= 5:
                await self.message.delete()
            if (self.is_playing == False or c.seconds >= self.duration) and self.player.is_live == False:
                self.server.voice_client.stop()
                em=discord.Embed(description = "["+self.title+"]("+self.link+")\n**Song Ended**", colour=EMBEDCOLOR)
                em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
                await self.message.edit(embed=em)
                serverinfo[self.server].queue.remove(serverinfo[self.server].queue[0])
                self.is_playing=False
                serverinfo[self.server].mHandler=None
                serverinfo[self.server].end_time=datetime.datetime.now()
                self.task.cancel()
            elif self.paused and self.server.voice_client == None:
                self.is_playing=False
                self.pausetimeout=True
            else:
                if self.message != None:
                    try:
                        await self.message.edit(embed=self.em)
                    except Exception as e:
                        self.message=await self.channel.send(embed=self.em)
                else:
                    self.message = await self.channel.send(embed=self.em)
            await asyncio.sleep(2)
