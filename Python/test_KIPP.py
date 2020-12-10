from ESSENTIAL_PACKAGES import *
import Commands
from Command import commands

async def test_kipp():
  for command in commands:
    await command.Exec(discord.Message,command.Name,{},{})
