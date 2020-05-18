import sys
import os
KIPP_DIR=os.environ["KIPP_DIR"]
sys.path.append(KIPP_DIR+"/Python")
from ESSENTIAL_PACKAGES import *
from Command_utils import *
from Command import *

async def EVAL(message,message2,serverinfo,playerinfo):
    try:
        await message.channel.send(eval(str(message.content).split('|')[1]))
    except Exception as err:
        await message.channel.send(err)

async def EXEC(message,message2,serverinfo,playerinfo):
    try:
        if 'await' in str(message.content):
            await eval(str(message.content).split('|')[1].replace('await ',''))
        else:
            exec(str(message.content).split('|')[1])
        await message.channel.send('Passed without exception.')
    except Exception as err:
        await message.channel.send(err)

command["!EVAL"]=CRON("!EVAL","This command can be used by LockdownDoom in order to observe what a code block returns\n**Usage**\n`!EVAL|code`",EVAL)
command["!EXEC"]=CRON("!EXEC","This command can be used by LockdownDoom in order to run a code block\n**Usage**\n`!EXEC|code`",EXEC)
