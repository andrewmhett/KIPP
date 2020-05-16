from datetime import datetime
from config import *
from random import SystemRandom
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
    def pick_playlist_song(self):
        i=self.playlistindex
        if len(self.search_server_configs("PLAYLIST:{0}".format(self.playlist))[0][1:])>1:
            while i == self.playlistindex:
                i=SystemRandom().randrange(0,len(self.search_server_configs("PLAYLIST:{0}".format(self.playlist))[0][1:]))
            self.playlistindex=i
        song=self.search_server_configs("PLAYLIST:{0}".format(self.playlist))[0][1:][i]
        return song
    def add_server_config(self,data):
        arr=READ_DATA_IN(KIPP_DIR+"/KIPPSTUFF/ServerConfigs/{0}".format(str(self.server.id)))
        if arr==None:
            arr=[]
        arr.append(data)
        with open(KIPP_DIR+'/KIPPSTUFF/ServerConfigs/{0}'.format(str(self.server.id)),'w') as f:
            writer=csv.writer(f)
            for row in arr:
                writer.writerow(row)
            f.close()
    def change_server_config(self,data,newdata):
        arr=READ_DATA_IN(KIPP_DIR+"/KIPPSTUFF/ServerConfigs/{0}".format(str(self.server.id)))
        if arr==None:
            arr=[]
        cntr=0
        for row in arr:
            if data in str(row):
                arr[cntr] = newdata
                break
            cntr=cntr+1
        with open(KIPP_DIR+'/KIPPSTUFF/ServerConfigs/{0}'.format(str(self.server.id)),'w') as f:
            writer=csv.writer(f)
            for row in arr:
                writer.writerow(row)
            f.close()
    def search_server_configs(self,query):
        data=READ_DATA_IN(KIPP_DIR+'/KIPPSTUFF/ServerConfigs/{0}'.format(str(self.server.id)),condition=lambda x: True if query in str(x) else False)
        return data
