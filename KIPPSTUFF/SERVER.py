from ESSENTIAL_PACKAGES import *
class Server:
    def __init__(self,server):
        self.server=server
        self.mHandler=None
        self.everyoneleft = False
        self.blocked = []
        self.gamgamestarter = None
        self.gamgameopp = None
        self.recentchannel=None
        self.musiccolor=None
        self.queue = []
        self.election=False
        self.sElectiontime = None
        self.electionmessage = None
        self.can1=None
        self.can2=None
        self.can1votes=0
        self.can2votes=0
        self.voters=[]
        self.messagesent=[]
        self.oldtime=0
        self.r6role=None
        self.d2role=None
        self.events=[]
        self.end_time=datetime.datetime.now()
        self.loading=False
        self.jointime=datetime.datetime.now()
    def add_server_config(self,data):
        arr=READ_DATA_IN("/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}".format(self.server.id))
        with open('/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}'.format(self.server.id),'w') as f:
            writer=csv.writer(f)
            for row in arr:
                writer.writerow(row)
            f.close()
    def change_server_config(self,data,newdata):
        arr=READ_DATA_IN("/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}".format(self.server.id))
        cntr=0
        for row in arr:
            if data in str(row):
                arr[cntr] = newdata
                break
            cntr=cntr+1
        with open('/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}'.format(self.server.id),'w') as f:
            writer=csv.writer(f)
            for row in arr:
                writer.writerow(row)
            f.close()
    def search_server_configs(self,query):
        data=READ_DATA_IN('/home/pi/Desktop/KIPPSTUFF/ServerConfigs/{0}'.format(self.server.id),condition=lambda x: True if query in str(x) else False)
        return data