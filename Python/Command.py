import sys
import os
KIPP_DIR=os.environ["KIPP_DIR"]
sys.path.append(KIPP_DIR+"/Python/Commands")
from ESSENTIAL_PACKAGES import *
from Commands.Command_utils import VerifyOwner
CREATOR_ID=289920025077219328
KIPP_ID=386352783550447628
if len(sys.argv)>1:
    if sys.argv[1] == "dev":
        KIPP_ID=726545013064073277
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
        try:
            if isinstance(self,CRON) and message.author.id != CREATOR_ID:
                await message.channel.send("Sorry, but this is a CREATOR_ONLY command.")
                valid=False
            if isinstance(self,OWON) and not await VerifyOwner(message):
                await message.channel.send("Sorry, but this is a OWNER_ONLY command.")
                valid=False
            if valid:
                await self.exe[0](message,message2,serverinfo,playerinfo)
        except IndexError:
            await message.channel.send("Invalid number of arguments. Use `!HELP|{0}` to find the correct command syntax.".format(self.Name[1:]))
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
