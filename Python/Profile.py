from ESSENTIAL_PACKAGES import *
KIPP_DIR=os.environ['KIPP_DIR']
class Profile:
    def __init__(self,user):
        """
        Class used to keep track of user-specific data
        
        :param user: the discord.py member object to track data for
        :type user: <discord.member.Member>
        """
        self.gamblemessage=None
        self.bet=None
        self.solo=False
        self.color=None
        self.gamblerequest=False
        self.challenger=None
        self.betting=False
        self.numkippservers = 0
        self.game = ""
        self.highestrole = ""
        self.nickname = ""
        self.hrolecolor = None
        self.streaming = False
        self.user = user
        self.instore=False
        self.storepage=None
    def GET_KIPPCOINS(self):
        return int(subprocess.Popen([KIPP_DIR+"/C++/KIPPCOINS_IO","r",str(self.user.id)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0])
    def GIVE_KIPPCOINS(self, KC):
       balance=int(subprocess.Popen([KIPP_DIR+"/C++/KIPPCOINS_IO","r",str(self.user.id)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0])+KC
       subprocess.Popen([KIPP_DIR+"/C++/KIPPCOINS_IO","w",str(self.user.id),str(balance)])
