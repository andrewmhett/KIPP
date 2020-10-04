from ESSENTIAL_PACKAGES import *
from Footer import get_footer
from subprocess import check_output
EMBEDCOLOR=0x36393E

ytdl_format_options={
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'opus',
    }],
    'postprocessor_args':[
        '-ar', '48000'
    ],
    'keepvideo': False
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

def search_music(query, serverinfo):
    music=None
    from pyyoutube import Api
    api=Api(api_key=YOUTUBE_API_KEY)
    for song in api.search_by_keywords(q=query,search_type=["video"],count=10).items:
        try:
            api.get_video_by_id(video_id=song.id.videoId)
            music="https://www.youtube.com/watch?v={0}".format(song.id.videoId)
            break
        except RuntimeWarning:
            pass
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
        #data["url"]="https://www.youtube.com/watch?v={0}".format(data["id"])
        cls.url=url
        if 'entries' in data:
            data = data['entries'][0]
        b_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
        return cls(discord.FFmpegPCMAudio(data["url"], **ffmpeg_options, before_options=b_options), data=data)

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
