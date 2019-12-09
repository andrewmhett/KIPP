from ESSENTIAL_PACKAGES import *
class music_handler():
    def __init__(self,server,player,channel,footer):
        self.server=server
        self.channel=channel
        server.voice_client.encoder_options(sample_rate=48000,channels=2)
        player.start()
        self.player=player
        self.paused=False
        self.message=None
	self.footer=footer
        self.starttime=datetime.datetime.now()
        self.duration=player.duration
        self.title=player.title
        self.link=player.url
        if self.player.is_live == False:
            mins=int(self.duration/60)
            seconds=int(self.duration-(mins*60))
            hours=int(mins/60)
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
        self.desc = ("["+self.title+"]("+self.link+")\n**Progress:**: `0:00 / "+self.length+"`\n**Volume:** "+str(int(self.player.volume*100)))
        self.em = discord.Embed(description=self.desc,colour=EMBEDCOLOR)
        self.em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
        #video_id = music4.split("watch?v=")[1]
        #thumbnail = "https://img.youtube.com/vi/"+video_id+"/0.jpg"
        #self.em.set_thumbnail(url=thumbnail)
        #self.thumbnail = thumbnail
        self.footer=self.footer
        self.em.set_footer(text=self.footer)
        self.is_playing=True
        self.pausedatetime=None
        self.pausetime=None
        #client.loop.create_task(self.update_loop())
    async def update_loop(self):
        self.is_playing=self.player.is_playing()
        queuelist="\nNo songs in queue"
        if len(serverinfo[self.server].queue)>1:
            queuelist=""
            i=0
            for song in serverinfo[self.server].queue[1:]:
                i=i+1
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
            percent=int(18*(((int(self.hours)*3600)+(int(self.minutedelta)*60)+int(self.seconddelta))/int(self.duration)))+1
            if self.player.is_live == False:
                self.bar=("▣"*percent)+"▢"*(18-percent)
            else:
                self.bar="▣"*18
        pauseStr=""
        if self.paused:
            pauseStr=" (paused)"
        if self.hours>0:
            self.minutedelta=int(self.minutedelta)-(hours*60)
            if len(str(self.minutedelta))==1:
                self.minutedelta="0"+str(self.minutedelta)
            else:
                self.minutedelta=str(self.minutedelta)
            self.em=discord.Embed(description = self.desc.split('**Progress:**')[0]+'**Volume:** '+str(int(self.player.volume*100))+'%'+'\n**Progress:** `'+str(self.hours)+":"+str(self.minutedelta)+':'+str(self.seconddelta)+' / '+self.length+pauseStr+'`\n'+self.bar+'\n**Queue:**'+queuelist,colour=EMBEDCOLOR)
        else:
            self.em=discord.Embed(description = self.desc.split('**Progress:**')[0]+'**Volume:** '+str(int(self.player.volume*100))+'%'+'\n**Progress:** `'+str(self.minutedelta)+':'+str(self.seconddelta)+' / '+self.length+pauseStr+'`\n'+self.bar+'\n**Queue:**'+queuelist,colour=EMBEDCOLOR)
        self.em.set_footer(text=self.footer)
        self.em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
        if self.is_playing==False or c.seconds >= self.duration and self.player.is_live == False:
            em=discord.Embed(description = "["+self.title+"]("+self.link+")\n**Song Ended**", colour=EMBEDCOLOR)
            em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
            await client.edit_message(self.message,embed=em)
            serverinfo[self.server].queue.remove(serverinfo[self.server].queue[0])
            self.is_playing=False
            serverinfo[self.server].mHandler=None
            serverinfo[self.server].end_time=datetime.datetime.now()
        else:
            if self.message != None:
                try:
                    await client.edit_message(self.message,embed=self.em)
                except:
                    self.message=None
            if self.message==None:
                self.message=await client.send_message(self.channel,embed=self.em)
            else:
                self.message=await client.edit_message(self.message,embed=self.em)