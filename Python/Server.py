from ESSENTIAL_PACKAGES import *
import hashlib
import time

def READ_DATA_IN(path, condition=lambda x: True, attr_condition=lambda x: True):
    try:
        with open(path) as f:
            f.close()
    except Exception:
        with open(path, 'w+') as f:
            f.close()
    arr = []
    with open(path) as fl:
        for row in csv.reader(fl):
            if condition(row):
                for attr in row:
                    if attr_condition(attr):
                        arr.append(row)
                        break
        fl.close()
    if len(arr) == 0:
        arr = None
    return arr

KIPP_DIR = os.environ["KIPP_DIR"]

class Server:
    def __init__(self, server):
        self.id_hash=hashlib.sha1(str(server.id).encode("utf-8")).hexdigest()
        self.action_queue=[]
        self.task = None
        self.old_queue=[]
        self.server = server
        self.mHandler = None
        self.everyoneleft = False
        self.blocked = []
        self.gamgamestarter = None
        self.gamgameopp = None
        self.recentchannel = None
        self.queue = []
        self.oldtime = 0
        self.end_time = datetime.now()
        self.loading = False
        self.jointime = datetime.now()
        self.playlist = None
        self.playlistindex = 0
        self.music_task = None
        self.current_timestamp = ""
        self.action_lookup={
            "REMOVE_SONG":self.remove_song,
            "SHUFFLE_QUEUE":self.shuffle_queue,
            "CLEAR_QUEUE":self.clear_queue,
            "MOVE_SONG":self.move_song,
            "INITIALIZE":self.initialize_dashboard,
            "TOGGLE_PAUSE":self.toggle_pause,
            "SKIP":self.skip
        }
        threading.Thread(target=self.update_web_dashboard).start()
        threading.Thread(target=self.track_time).start()
        self.post_data("song_queue","")
        self.post_data("current_song","")

    def toggle_pause(self):
        if self.mHandler.paused:
            self.server.voice_client.resume()
            self.mHandler.paused = False
        else:
            self.mHandler.pausedatetime = datetime.now()
            self.mHandler.paused = True
            self.server.voice_client.pause()

    def skip(self):
        if self.mHandler.paused == True:
            self.server.voice_client.resume()
            self.mHandler.paused = False
        self.mHandler.skip()

    def initialize_dashboard(self):
        queue_str=""
        for song_pair in self.queue[1:]:
            queue_str+=song_pair[0]+",->"+song_pair[1]+",\n"
        self.post_data("song_queue",queue_str)
        c = datetime.datetime.now() - self.mHandler.starttime
        current_song_json="{"+'"{0}":"{1}","{2}":"{3}","{4}":{5},"{6}":{7},"{8}":"{9}","{10}":"{11}"'.format(
        "current_name",self.mHandler.title,"current_link",self.mHandler.link,
        "total_length",self.mHandler.duration,"seconds_elapsed",c.seconds,
        "current_timestamp",self.current_timestamp, "total_timestamp",self.mHandler.length)+"}"
        self.post_data("current_song",current_song_json)

    def remove_song(self, index):
        index=int(index)+1
        if index<len(self.queue):
            self.queue.pop(index)

    def shuffle_queue(self):
        import random
        end = None
        new_queue = self.queue[1:]
        if self.queue[len(self.queue) - 1][0].startswith("PLAYLIST: "):
            end = self.queue[len(
                self.queue) - 1]
            new_queue = self.queue[1:-1]
        random.shuffle(new_queue)
        i = 1
        for song in new_queue:
            self.queue[i] = song
            i += 1
        if end != None:
            self.queue[i] = end

    def clear_queue(self):
        self.queue=[]

    def move_song(self,index1,index2):
        index1=int(index1)+1
        index2=int(index2)+1
        if index2>0 and index2<len(self.queue):
            prev=self.queue[index1]
            self.queue[index1]=self.queue[index2]
            self.queue[index2]=prev

    def pick_playlist_song(self):
        i = self.playlistindex
        if len(self.search_server_configs("PLAYLIST:{0}".format(self.playlist))[0][1:]) > 1:
            while i == self.playlistindex:
                i = SystemRandom().randrange(0, len(self.search_server_configs(
                    "PLAYLIST:{0}".format(self.playlist))[0][1:]))
            self.playlistindex = i
        song = self.search_server_configs(
            "PLAYLIST:{0}".format(self.playlist))[0][1:][i]
        return song

    def add_server_config(self, data):
        arr = READ_DATA_IN(
            KIPP_DIR + "/ServerConfigs/{0}".format(str(self.server.id)))
        if arr == None:
            arr = []
        arr.append(data)
        with open(KIPP_DIR + '/ServerConfigs/{0}'.format(str(self.server.id)), 'w') as f:
            writer = csv.writer(f)
            for row in arr:
                writer.writerow(row)
            f.close()

    def change_server_config(self, data, newdata):
        arr = READ_DATA_IN(
            KIPP_DIR + "/ServerConfigs/{0}".format(str(self.server.id)))
        if arr == None:
            arr = []
        cntr = 0
        for row in arr:
            if data in str(row):
                arr[cntr] = newdata
                break
            cntr = cntr + 1
        with open(KIPP_DIR + '/ServerConfigs/{0}'.format(str(self.server.id)), 'w') as f:
            writer = csv.writer(f)
            for row in arr:
                writer.writerow(row)
            f.close()

    def search_server_configs(self, query):
        data = READ_DATA_IN(KIPP_DIR + '/ServerConfigs/{0}'.format(
            str(self.server.id)), condition=lambda x: True if query in str(x) else False)
        return data

    def post_data(self,endpoint,data):
        from private_key import n, d
        hash=int.from_bytes(hashlib.sha512((datetime.strftime(datetime.utcnow(),"%H:%M")+data).encode('latin1')).digest(),byteorder='big')
        signature=pow(hash,d,n)
        try:
            requests.post(HEROKU_URL+"/{0}?id_hash={1}&signature={2}".format(endpoint,self.id_hash,signature),data)
        except Exception:
            pass

    def update_web_dashboard(self):
        old_queue=[]
        old_song_json=""
        import datetime
        while True:
            if self.mHandler != None:
                try:
                    if old_queue != self.queue[1:]:
                        #update the queue on the web dashboard
                        old_queue=self.queue[1:]
                        queue_str=""
                        for song_pair in self.queue[1:]:
                            queue_str+=song_pair[0]+",->"+song_pair[1]+",\n"
                        self.post_data("song_queue",queue_str)
                    c = datetime.datetime.now() - self.mHandler.starttime
                    current_song_json="{"+'"{0}":"{1}","{2}":"{3}","{4}":{5},"{6}":{7},"{8}":"{9}","{10}":"{11}"'.format(
                    "current_name",self.mHandler.title,"current_link",self.mHandler.link,
                    "total_length",self.mHandler.duration,"seconds_elapsed",c.seconds,
                    "current_timestamp",self.current_timestamp, "total_timestamp",self.mHandler.length)+"}"
                    if current_song_json != old_song_json:
                        old_song_json=current_song_json
                        self.post_data("current_song",current_song_json)
                    actions_str = requests.get(HEROKU_URL+"/action_queue?id_hash="+self.id_hash).content.decode()
                    counter=0
                    for action in actions_str.split("<br>"):
                        if len(action)>0:
                            counter+=1
                            self.action_queue.append(action)
                    if counter>0:
                        self.post_data("action_queue","")
                    for i in range(len(self.action_queue)-1):
                        o=1
                        while self.action_queue[i]==self.action_queue[i+o]:
                            self.action_queue.pop(i+o)
                            if o<len(self.action_queue)-1:
                                o+=1
                            else:
                                break
                    for action_set in self.action_queue:
                        action=action_set.split(",->")[0]
                        args=[]
                        if ",->" in action_set:
                            args=action_set.split(",->")[1:]
                        self.action_lookup[action](*args)
                        self.action_queue.pop(0)
                except Exception:
                    pass
                time.sleep(0.2)
            else:
                if old_song_json != {}:
                    old_song_json={}
                time.sleep(1)

    def track_time(self):
        import datetime
        previous_time=datetime.datetime.now()
        while True:
            if self.mHandler != None:
                c = datetime.datetime.now() - self.mHandler.starttime
                if self.server.voice_client.is_playing():
                    self.mHandler.is_playing = True
                elif self.mHandler.paused:
                    self.mHandler.is_playing = True
                else:
                    self.mHandler.is_playing = False
                self.mHandler.resend_timer += (datetime.datetime.now()-previous_time).microseconds/1000000
                if self.mHandler.paused:
                    pausetime = datetime.datetime.now() - previous_time
                    self.mHandler.starttime+=datetime.timedelta(microseconds=pausetime.microseconds)
                else:
                    if (self.mHandler.is_playing == False or c.seconds >= self.mHandler.duration) and self.mHandler.player.is_live == False:
                        self.server.voice_client.stop()
                        self.queue.remove(self.queue[0])
                        self.mHandler.is_playing = False
                        self.mHandler = None
                        self.post_data("current_song","")
                        self.end_time = datetime.datetime.now()
                previous_time=datetime.datetime.now()
                time.sleep(0.25)
            else:
                time.sleep(1)

    async def update_loop(self):
        while True:
            try:
                if self.mHandler != None:
                    import datetime
                    queuelist = "\nNo songs in queue"
                    if len(self.queue) > 1:
                        queuelist = ""
                        i = 0
                        for song in self.queue[1:3]:
                            i = i + 1
                            if len(song) > 2:
                                queuelist = queuelist + \
                                    "\n`#{0}` {1}".format(i, song)
                            else:
                                queuelist = queuelist + \
                                    "\n`#{0}` {1}".format(
                                        i, "[" + (''.join(song[0])) + "](" + song[1] + ")")
                        if len(self.queue) - 3 > 0:
                            queuelist += ("\n`...and {0} more songs`".format(len(self.queue) - 3) if len(
                                self.queue) - 3 > 1 else "\n`...and 1 more song`")

                    c = datetime.datetime.now() - self.mHandler.starttime
                    if self.mHandler.paused == False:
                        progress = divmod(c.days * 86400 + c.seconds, 60)
                        self.mHandler.minutedelta = progress[0]
                        self.mHandler.seconddelta = progress[1]
                        if len(str(self.mHandler.seconddelta)) == 1:
                            self.mHandler.seconddelta = '0' + \
                                str(self.mHandler.seconddelta)
                        self.mHandler.hours = int(
                            int(self.mHandler.minutedelta) / 60)
                        self.mHandler.minutedelta = int(
                            self.mHandler.minutedelta) % 60
                        blocks = [" ", " ", " ", "╸", "╸", "╸", "╸", "╍"]
                        if self.mHandler.player.is_live == False and self.mHandler.player.duration != 0:
                            percent = int(21 * (((int(self.mHandler.hours) * 3600) + (int(self.mHandler.minutedelta)
                                                                                      * 60) + int(self.mHandler.seconddelta)) / int(self.mHandler.duration)))
                            perc = ((int(self.mHandler.hours) * 3600) + (int(self.mHandler.minutedelta)
                                                                         * 60) + int(self.mHandler.seconddelta)) / self.mHandler.duration
                            rem = perc % (1 / 21)
                            rem = rem * 21
                            if rem == 0:
                                self.mHandler.bar = "7" * \
                                    percent + " " * (21 - percent)
                            else:
                                self.mHandler.bar = "7" * percent + \
                                    str(int(rem * 7)) + " " * (20 - percent)
                            perc_str = str(int(perc * 100)) + "%"
                            if int(perc * 100) < 10:
                                perc_str = "0" + perc_str
                            out_str = ""
                            for i in range(9):
                                if self.mHandler.bar[i] != " ":
                                    out_str += blocks[int(self.mHandler.bar[i])]
                                else:
                                    out_str += " "
                            out_str += perc_str
                            for i in range(12, 21):
                                if self.mHandler.bar[i] != " ":
                                    out_str += blocks[int(self.mHandler.bar[i])]
                                else:
                                    out_str += " "
                            self.mHandler.bar = "`" + out_str + "`"
                        else:
                            self.mHandler.bar = "`" + \
                                (" " * 5) + "Live Stream" + (" " * 5) + "`"
                    pauseStr = ""
                    volume_blocks = ['▁', '▂', '▃', '▅', '▆', '▇']
                    if not self.mHandler.paused:
                        volume = 0
                        for sample in self.mHandler.volume_data:
                            volume += audioop.rms(sample, 2)
                        volume /= 50
                        self.mHandler.volume_array.append(volume)
                        if len(self.mHandler.volume_array) > 17:
                            self.mHandler.volume_array.pop(0)
                    max_volume = max(self.mHandler.volume_array)
                    vol_increment = max_volume / 5
                    volume_graph = ""
                    for volume in self.mHandler.volume_array:
                        if vol_increment > 0:
                            volume_graph += volume_blocks[int(
                                volume / vol_increment)]
                        else:
                            volume_graph += '▁'
                    volume_graph = "`" + \
                        ((17 - len(volume_graph)) * '▁') + volume_graph + "`"
                    volume_graph = "`▁" + volume_graph[2:]
                    if self.mHandler.paused:
                        pauseStr = " (paused)"
                    self.mHandler.desc = self.mHandler.bar + \
                        "\n{0}".format(volume_graph)
                    if self.mHandler.hours > 0:
                        if len(str(self.mHandler.minutedelta)) == 1:
                            self.mHandler.minutedelta = "0" + \
                                str(self.mHandler.minutedelta)
                        else:
                            self.mHandler.minutedelta = str(
                                self.mHandler.minutedelta)
                        self.current_timestamp= + str(self.mHandler.hours) + ":" + str(
                            self.mHandler.minutedelta) + ':' + str(self.mHandler.seconddelta)
                        self.mHandler.desc =  self.mHandler.desc+"\n`" +self.current_timestamp + ' / ' + self.mHandler.length + '`' + pauseStr
                    else:
                        self.current_timestamp= str(self.mHandler.minutedelta) + ':' + str(
                            self.mHandler.seconddelta)
                        self.mHandler.desc =  self.mHandler.desc + "\n`" +self.current_timestamp + ' / ' + self.mHandler.length + '`' + pauseStr
                    self.mHandler.em.clear_fields()
                    self.mHandler.em.add_field(
                        name="Progress", value=self.mHandler.desc, inline=True)
                    self.mHandler.em.add_field(
                        name="Queue", value=queuelist, inline=True)
                    self.mHandler.em.set_footer(text=self.mHandler.footer)
                    if self.mHandler.resend_timer / 30 >= 5:
                        self.mHandler.resend_timer = 0
                        try:
                            await self.mHandler.message.delete()
                            self.mHandler.message = None
                        except discord.DiscordException:
                            pass
                    if (self.mHandler.is_playing == False or c.seconds >= self.mHandler.duration) and self.mHandler.player.is_live == False:
                        self.server.voice_client.stop()
                        try:
                            await self.mHandler.message.delete()
                        except discord.DiscordException:
                            pass
                    else:
                        if self.mHandler.message != None:
                            try:
                                await self.mHandler.message.edit(embed=self.mHandler.em)
                            except discord.errors.NotFound:
                                if self.mHandler != None:
                                    self.mHandler.message = await self.mHandler.channel.send(embed=self.mHandler.em)
                        else:
                            self.mHandler.message = await self.mHandler.channel.send(embed=self.mHandler.em)
            except Exception as e:
                os.system('sudo echo "{0} {1}" >> $KIPP_DIR/log.txt'.format(
                datetime.datetime.strftime(datetime.datetime.now(),
                                           "[%m/%d/%Y %H:%M:%S]"), e))
            await asyncio.sleep(1)
