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
    def __init__(self,n,h,e,a_types):
        self.Help=h,
        self.exe=e,
        self.Name=n
        self.arg_types=a_types
        self.args=[]
        commands.append(self)
    def help(self):
        syntax_str="{0}\n**Syntax**\n`{1}".format(self.Help[0].split("\n")[0],self.Name.split("|")[0])
        counter=0
        for arg in self.Help[0].split("\n")[1].split("|")[1:]:
            syntax_str+="|<{0}> {1}".format(self.arg_types[counter].__name__,arg)
            counter+=1
        syntax_str+="`"
        if self.Name=="!HELP":
            syntax_str="`!HELP|(optional)<str> command_name`"
        return syntax_str
    async def validate_arguments(self,message,message2):
        self.args=message2.split("|")[1:]
        for arg in self.args:
            if len(arg)==0:
                return (-3,0)
        if self.Name=="!HELP":
            return (0,0) if len(self.args)==0 or len(self.args)==1 else (-2,0)
        if len(self.args)==len(self.arg_types):
            counter=0
            for arg in self.args:
                try:
                    self.arg_types[counter](arg)
                except ValueError:
                    return (-1,counter)
                counter+=1
        else:
            return (-2,0)
        return 0,counter
    async def Execute(self,message,message2,sinfo,pinfo):
        global serverinfo
        global playerinfo
        serverinfo=sinfo
        playerinfo=pinfo
        valid=True
        arg_valid_out,arg_num=await self.validate_arguments(message,message2)
        if arg_valid_out==0:
            if isinstance(self,CRON) and message.author.id != CREATOR_ID:
                await message.channel.send("Sorry, but this is a CREATOR_ONLY command.")
                valid=False
            if isinstance(self,OWON) and not await VerifyOwner(message):
                await message.channel.send("Sorry, but this is a OWNER_ONLY command.")
                valid=False
            if valid:
                await self.exe[0](message,message2,serverinfo,playerinfo)
        elif arg_valid_out==-1:
            await message.channel.send("Invalid syntax: (invalid type). Argument `{0}`. Expected `<{1}>`.".format(arg_num,self.arg_types[arg_num].__name__))
        elif arg_valid_out==-2:
            await message.channel.send("Invalid syntax: (invalid number of arguments). Expected `{0}`, got `{1}`.".format(str(len(self.arg_types))+(" or 1" if self.Name=="!HELP" else ""),len(self.args)))
        elif arg_valid_out==-3:
            await message.channel.send("Invalid syntax: (empty argument).")
        self.args=[]
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
