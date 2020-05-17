from ESSENTIAL_PACKAGES import *
def READ_DATA_IN(path, condition=lambda x: True, attr_condition=lambda x: True):
    try:
        with open(path) as f:
            f.close()
    except Exception:
         with open(path,'w+') as f:
             f.close()
    arr=[]
    found=False
    with open(path) as fl:
        for row in csv.reader(fl):
            if condition(row):
                for attr in row:
                    if attr_condition(attr):            
                        arr.append(row)
                        break
        fl.close()
    if len(arr)==0:
        arr=None
    return arr
KIPP_DIR=os.environ["KIPP_DIR"]
class Server:
    def __init__(self,server):
        self.server=server
        self.mHandler=None
        self.everyoneleft = False
        self.blocked = []
        self.gamgamestarter = None
        self.gamgameopp = None
        self.recentchannel=None
        self.queue = []
        self.oldtime=0
        self.end_time=datetime.now()
        self.loading=False
        self.jointime=datetime.now()
        self.playlist=None
        self.playlistindex=0
        self.music_task=None
    def pick_playlist_song(self):
        i=self.playlistindex
        if len(self.search_server_configs("PLAYLIST:{0}".format(self.playlist))[0][1:])>1:
            while i == self.playlistindex:
                i=SystemRandom().randrange(0,len(self.search_server_configs("PLAYLIST:{0}".format(self.playlist))[0][1:]))
            self.playlistindex=i
        song=self.search_server_configs("PLAYLIST:{0}".format(self.playlist))[0][1:][i]
        return song
    def add_server_config(self,data):
        arr=READ_DATA_IN(KIPP_DIR+"/ServerConfigs/{0}".format(str(self.server.id)))
        if arr==None:
            arr=[]
        arr.append(data)
        with open(KIPP_DIR+'/ServerConfigs/{0}'.format(str(self.server.id)),'w') as f:
            writer=csv.writer(f)
            for row in arr:
                writer.writerow(row)
            f.close()
    def change_server_config(self,data,newdata):
        arr=READ_DATA_IN(KIPP_DIR+"/ServerConfigs/{0}".format(str(self.server.id)))
        if arr==None:
            arr=[]
        cntr=0
        for row in arr:
            if data in str(row):
                arr[cntr] = newdata
                break
            cntr=cntr+1
        with open(KIPP_DIR+'/ServerConfigs/{0}'.format(str(self.server.id)),'w') as f:
            writer=csv.writer(f)
            for row in arr:
                writer.writerow(row)
            f.close()
    def search_server_configs(self,query):
        data=READ_DATA_IN(KIPP_DIR+'/ServerConfigs/{0}'.format(str(self.server.id)),condition=lambda x: True if query in str(x) else False)
        return data
    async def update_loop(self):
        while True:
            if self.mHandler != None:
                if self.mHandler.is_playing:
                    self.mHandler.resend_timer+=1
                    if self.server.voice_client.is_playing():
                        self.mHandler.is_playing=True
                    elif self.paused:
                        self.mHandler.is_playing=True
                    else:
                        self.mHandler.is_playing=False
                    import datetime
                    queuelist="\nNo songs in queue"
                    if len(self.queue)>1:
                        queuelist=""
                        i=0
                        for song in self.queue[1:]:
                            i=i+1
                            if len(song)>2:
                                queuelist=queuelist+"\n`#{0}` {1}".format(i,song)
                            else:
                                queuelist=queuelist+"\n`#{0}` {1}".format(i,"["+(''.join(song[0]))+"]("+song[1]+")")
                    if self.mHandler.paused:
                        self.mHandler.pausetime=datetime.datetime.now()-self.pausedatetime
                    if self.mHandler.pausetime==None:
                        c = datetime.datetime.now()-self.mHandler.starttime
                    else:
                        c = datetime.datetime.now()-(self.mHandler.starttime+datetime.timedelta(seconds=self.mHandler.pausetime.seconds))
                    if self.mHandler.paused == False:
                        progress = divmod(c.days * 86400 + c.seconds, 60)
                        self.mHandler.minutedelta=str(progress).split('(')[1].split(')')[0].split(',')[0]
                        self.mHandler.seconddelta=str(progress).split('(')[1].split(')')[0].split(', ')[1]
                        if len(str(self.mHandler.seconddelta)) == 1:
                            self.mHandler.seconddelta='0'+str(self.mHandler.seconddelta)
                        self.mHandler.hours=int(int(self.mHandler.minutedelta)/60)
                        if self.mHandler.player.is_live == False:
                            percent=int(18*(((int(self.mHandler.hours)*3600)+(int(self.mHandler.minutedelta)*60)+int(self.mHandler.seconddelta))/int(self.mHandler.duration)))+1
                            self.mHandler.bar=("▣"*percent)+"▢"*(18-percent)
                        else:
                            self.mHandler.bar="▣"*18
                    pauseStr=""
                    if self.mHandler.paused:
                        pauseStr=" (paused)"
                    if self.mHandler.hours>0:
                        self.mHandler.minutedelta=int(self.mHandler.minutedelta)-(self.mHandler.hours*60)
                        if len(str(self.mHandler.minutedelta))==1:
                            self.mHandler.minutedelta="0"+str(self.mHandler.minutedelta)
                        else:
                            self.mHandler.minutedelta=str(self.mHandler.minutedelta)
                        self.mHandler.em=discord.Embed(description = self.mHandler.desc.split('`')[0]+"`"+str(self.mHandler.hours)+":"+str(self.mHandler.minutedelta)+':'+str(self.mHandler.seconddelta)+' / '+self.mHandler.length+'`'+pauseStr+'\n'+self.mHandler.bar+'\n**Queue:**'+queuelist,colour=EMBEDCOLOR)
                    else:
                        self.mHandler.em=discord.Embed(description = self.mHandler.desc.split('`')[0]+"`"+str(self.mHandler.minutedelta)+':'+str(self.mHandler.seconddelta)+' / '+self.mHandler.length+'`'+pauseStr+'\n'+self.mHandler.bar+'\n**Queue:**'+queuelist,colour=EMBEDCOLOR)
                    self.mHandler.em.set_footer(text=self.mHandler.footer)
                    self.mHandler.em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
                    if self.mHandler.resend_timer/30 >= 5:
                        await self.mHandler.message.delete()
                    if (self.mHandler.is_playing == False or c.seconds >= self.mHandler.duration) and self.mHandler.player.is_live == False:
                        self.server.voice_client.stop()
                        em=discord.Embed(description = "["+self.mHandler.title+"]("+self.mHandler.link+")\n**Song Ended**", colour=EMBEDCOLOR)
                        em.set_author(name = "Music", icon_url="http://www.charbase.com/images/glyph/9835")
                        await self.mHandler.message.edit(embed=em)
                        self.queue.remove(self.queue[0])
                        self.mHandler.is_playing=False
                        self.mHandler=None
                        self.end_time=datetime.datetime.now()
                    elif self.mHandler.paused and self.server.voice_client == None:
                        self.mHandler.is_playing=False
                        self.mHandler.pausetimeout=True
                    else:
                        if self.mHandler.message != None:
                            try:
                                await self.mHandler.message.edit(embed=self.mHandler.em)
                            except Exception as e:
                                self.mHandler.message=await self.mHandler.channel.send(embed=self.mHandler.em)
                        else:
                            self.mHandler.message = await self.mHandler.channel.send(embed=self.mHandler.em)
            await asyncio.sleep(2)
