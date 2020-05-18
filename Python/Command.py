import sys
import os
KIPP_DIR=os.environ["KIPP_DIR"]
sys.path.append(KIPP_DIR+"/Python/Commands")
from ESSENTIAL_PACKAGES import *
from Command_utils import VerifyOwner
CREATOR_ID=289920025077219328
KIPP_ID=386352783550447628

command={}
commands=[]
serverinfo={}
playerinfo={}

class Command:
    def __init__(self,n,h,e):
        self.Help=h,
        self.exe=e,
        self.Name=n
        commands.append(self)
    async def Execute(self,message,message2,sinfo,pinfo):
        global serverinfo
        global playerinfo
        serverinfo=sinfo
        playerinfo=pinfo
        valid=True
        if isinstance(self,CRON) and message.author.id != CREATOR_ID:
            await message.channel.send("Sorry, but this is a CREATOR_ONLY command.")
            valid=False
        if isinstance(self,CRON) and not VerifyOwner(message):
            await message.channel.send("Sorry, but this is a OWNER_ONLY command.")
            valid=False
        if valid:
            await self.exe[0](message,message2,serverinfo,playerinfo)
        return serverinfo, playerinfo

class MISC(Command):
    pass
class OWON(Command):
    pass
class CRON(Command):
    pass
class KIPC(Command):
    pass
class MUSC(Command):
    pass
class SCIN(Command):
    pass
