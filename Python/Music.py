from ESSENTIAL_PACKAGES import *
from Footer import get_footer
EMBEDCOLOR=0x36393E
ytdl_format_options = {
    'format': 'bestaudio/best',
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
def search_music(query, serverinfo, index):
    music=None
    try:
        query_string = urllib.parse.urlencode({"search_query" : query})
        req = "http://www.youtube.com/results?"+query_string
        searchresults=re.findall("watch\?v=(.{11})", requests.get(req).text)
        music="http://www.youtube.com/watch?v="+searchresults[index]
    except IndexError:
        print("Not found")
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
    async def from_url(cls, url, *, loop=None, stream=False):
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
        if data.get('duration')==0 or data.get('filesize')>20000000:
            stream=True
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        cls.url=url
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        cls.file=filename if not stream else ""
        b_options=""
        if stream:
            b_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options, before_options=b_options), data=data)
class music_handler:
    def __init__(self,server,player,channel):
        self.server=server
        self.resend_timer=0
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
            self.length = "Live"
        self.desc = ("`0:00 / "+self.length)
        self.em = discord.Embed(colour=EMBEDCOLOR)
        self.em.description="[{0}]({1})".format(self.title,self.link)
        self.em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
        self.em.add_field(name="",value=self.desc,inline=True)
        self.em.set_footer(text=self.footer)
        self.is_playing=True
        self.pausedatetime=None
        self.pausetime=None
    def skip(self):
        self.server.voice_client.stop()
        self.player.is_live=False
