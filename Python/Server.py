from ESSENTIAL_PACKAGES import *
def READ_DATA_IN(path, condition=lambda x: True, attr_condition=lambda x: True):
    try:
        with open(path) as f:
            f.close()
    except Exception:
         with open(path,'w+') as f:
             f.close()
    arr=[]
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
        self.task=None
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
                if self.server.voice_client.is_playing():
                    self.mHandler.is_playing=True
                elif self.mHandler.paused:
                    self.mHandler.is_playing=True
                else:
                    self.mHandler.is_playing=False
                self.mHandler.resend_timer+=1
                import datetime
                queuelist="\nNo songs in queue"
                if len(self.queue)>1:
                    queuelist=""
                    i=0
                    for song in self.queue[1:3]:
                        i=i+1
                        if len(song)>2:
                            queuelist=queuelist+"\n`#{0}` {1}".format(i,song)
                        else:
                            queuelist=queuelist+"\n`#{0}` {1}".format(i,"["+(''.join(song[0]))+"]("+song[1]+")")
                    if len(self.queue)-3>0:
                        queuelist+=("\n`...and {0} more songs`".format(len(self.queue)-3) if len(self.queue)-3>1 else "\n`...and 1 more song`")
                if self.mHandler.paused:
                    self.mHandler.pausetime=datetime.datetime.now()-self.mHandler.pausedatetime
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
                    self.mHandler.minutedelta=int(self.mHandler.minutedelta)%60
                    blocks=[" "," "," ","╸","╸","╸","╸","╍"]
                    if self.mHandler.player.is_live == False and self.mHandler.player.duration != 0:
                        percent=int(21*(((int(self.mHandler.hours)*3600)+(int(self.mHandler.minutedelta)*60)+int(self.mHandler.seconddelta))/int(self.mHandler.duration)))
                        perc=((int(self.mHandler.hours)*3600)+(int(self.mHandler.minutedelta)*60)+int(self.mHandler.seconddelta))/self.mHandler.duration
                        rem=perc%(1/21)
                        rem=rem*21
                        if rem==0:
                            self.mHandler.bar="7"*percent+" "*(21-percent)
                        else:
                            self.mHandler.bar="7"*percent+str(int(rem*7))+" "*(20-percent)
                        perc_str=str(int(perc*100))+"%"
                        if int(perc*100)<10:
                            perc_str="0"+perc_str
                        out_str=""
                        for i in range(9):
                            if self.mHandler.bar[i] != " ":
                                out_str+=blocks[int(self.mHandler.bar[i])]
                            else:
                                out_str+=" "
                        out_str+=perc_str
                        for i in range(12,21):
                            if self.mHandler.bar[i] != " ":
                                out_str+=blocks[int(self.mHandler.bar[i])]
                            else:
                                out_str+=" "
                        self.mHandler.bar="`"+out_str+"`"
                    else:
                        self.mHandler.bar="`"+(" "*5)+"Live Stream"+(" "*5)+"`"
                pauseStr=""
                volume_blocks=['▁','▂','▃','▅','▆','▇']
                if not self.mHandler.paused:
                    volume=0
                    for sample in self.mHandler.volume_data:
                        volume+=audioop.rms(sample,2)
                    volume/=50
                    self.mHandler.volume_array.append(volume)
                    if len(self.mHandler.volume_array)>17:
                        self.mHandler.volume_array.pop(0)
                max_volume=max(self.mHandler.volume_array)
                vol_increment=max_volume/6
                volume_graph=""
                for volume in self.mHandler.volume_array:
                    if vol_increment>0:
                        volume_graph+=volume_blocks[int(volume/vol_increment)]
                    else:
                        volume_graph+=' '
                volume_graph="`"+((17-len(volume_graph))*'▁')+volume_graph+"`"
                volume_graph="`▁"+volume_graph[2:]
                if self.mHandler.paused:
                    pauseStr=" (paused)"
                self.mHandler.desc=self.mHandler.bar+"\n{0}".format(volume_graph)
                if self.mHandler.hours>0:
                    if len(str(self.mHandler.minutedelta))==1:
                        self.mHandler.minutedelta="0"+str(self.mHandler.minutedelta)
                    else:
                        self.mHandler.minutedelta=str(self.mHandler.minutedelta)
                    self.mHandler.desc = self.mHandler.desc+"`"+str(self.mHandler.hours)+":"+str(self.mHandler.minutedelta)+':'+str(self.mHandler.seconddelta)+' / '+self.mHandler.length+'`'+pauseStr
                else:
                    self.mHandler.desc= self.mHandler.desc+"\n`"+str(self.mHandler.minutedelta)+':'+str(self.mHandler.seconddelta)+' / '+self.mHandler.length+'`'+pauseStr
                self.mHandler.em.clear_fields()
                self.mHandler.em.add_field(name="Progress",value=self.mHandler.desc,inline=True)
                self.mHandler.em.add_field(name="Queue",value=queuelist,inline=True)
                self.mHandler.em.set_footer(text=self.mHandler.footer)
                if self.mHandler.resend_timer/30 >= 5:
                    self.mHandler.resend_timer=0
                    try:
                        await self.mHandler.message.delete()
                        self.mHandler.message=None
                    except discord.DiscordException:
                        pass
                if (self.mHandler.is_playing == False or c.seconds >= self.mHandler.duration) and self.mHandler.player.is_live == False:
                    self.server.voice_client.stop()
                    try:
                        await self.mHandler.message.delete()
                    except discord.DiscordException:
                        pass
                    self.queue.remove(self.queue[0])
                    self.mHandler.is_playing=False
                    self.mHandler=None
                    self.end_time=datetime.datetime.now()
                else:
                    if self.mHandler.message != None:
                        try:
                            await self.mHandler.message.edit(embed=self.mHandler.em)
                        except discord.errors.NotFound:
                            self.mHandler.message = await self.mHandler.channel.send(embed=self.mHandler.em)
                    else:
                        self.mHandler.message = await self.mHandler.channel.send(embed=self.mHandler.em)
            await asyncio.sleep(1)
