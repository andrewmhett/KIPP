import sys
import os
KIPP_DIR=os.environ["KIPP_DIR"]
sys.path.append(KIPP_DIR+"/Python")
from ESSENTIAL_PACKAGES import *
from .Command_utils import *
from Command import *

async def BLOCK(message,message2,serverinfo,playerinfo):
    owner = message.guild.owner
    blockedP = str(message.content)
    blockedP2 = blockedP.split('|')
    if blockedP2[1].upper() != "ALL":
        blockedP2[1] = message.guild.get_member_named(str(blockedP2[1]))
    if str(blockedP2[1]) != "None":
        if str(blockedP2[1]).upper() == "ALL":
            for member in message.guild.members:
                if member.id not in serverinfo[message.guild].blocked:
                    if (member.id != CREATOR_ID) and (member.id != KIPP_ID) and (member != owner):
                        serverinfo[message.guild].blocked.append(member.id)
            await message.channel.send( "Blocked everyone in server")
        elif blockedP2[1].id != CREATOR_ID and blockedP2[1] != owner and blockedP2[1].id != KIPP_ID:
            if blockedP2[1].id in serverinfo[message.guild].blocked:
                await message.channel.send( "User already blocked.")
            elif blockedP2[1].id not in serverinfo[message.guild].blocked:
                serverinfo[message.guild].blocked.append(blockedP2[1].id)
                msg =("Blocked "+str(blockedP2[1])).format(message)
                await message.channel.send( msg)
        elif blockedP2[1].id == CREATOR_ID:
            msg = "Why would I block my own creator?"
            await message.channel.send( msg)
        elif blockedP2[1] == message.author:
            await message.channel.send( "Why would you want to block yourself?")
        elif blockedP2[1] == message.guild.get_member(KIPP_ID):
            await message.channel.send( "Why would I block myself?")
    else:
        await message.channel.send( "This user is not in this server. Make sure that you used the command like this: '!block|nickname OR !block|username'.")

async def WCHANNEL(message,message2,serverinfo,playerinfo):
    if serverinfo[message.guild].search_server_configs("WELCOME_CHANNEL") != None:
        if serverinfo[message.guild].search_server_configs("WELCOME_CHANNEL")[1] == str(message.channel.id):
            await message.channel.send("This channel already is the welcome channel.")
        else:
            serverinfo[message.guild].change_server_config("WELCOME_CHANNEL",["WELCOME_CHANNEL",str(message.channel.id)])
            await message.channel.send("Changed the welcome channel to this text channel.")
    else:
        serverinfo[message.guild].add_server_config(["WELCOME_CHANNEL",str(message.channel.id)])
        await message.channel.send("Set this text channel as the welcome channel. All joining users will be welcomed here.")

async def INVITE(message,message2,serverinfo,playerinfo):
    unbanuser = str(message.content).split('|')[1]
    unbanuser = await client.get_user_info(unbanuser)
    try:
        invite = await client.create_invite(message.channel, max_uses=1)
        await unbanuser.send("You have been invited to the server '"+str(message.guild)+"'. Here is the invite to the server.\n"+str(invite))
        await message.channel.send( "Successfully sent an invite to "+str(unbanuser))
    except discord.DiscordException:
        await message.channel.send("Failed to invite "+str(unbanuser)+" to the server.")

async def UNBLOCK(message,message2,serverinfo,playerinfo):
    unblocked1 = str(message.content).split('|')
    unblocked = unblocked1[1]
    if unblocked.upper() != "ALL":
        unblocked = message.guild.get_member_named(unblocked)
    if str(unblocked).upper() == "ALL":
        serverinfo[message.guild].blocked=[]
        await message.channel.send("Unblocked everyone in server")
    if (unblocked.id not in serverinfo[message.guild].blocked) and (str(unblocked).upper() != "ALL"):
        msg = "User not blocked."
        await message.channel.send(msg)
    elif unblocked.id in serverinfo[message.guild].blocked:
        msg = "Unblocked "+str(unblocked)
        serverinfo[message.guild].blocked.remove(unblocked.id)
        await message.channel.send(msg)

command["!BLOCK"]=OWON("!BLOCK","This command will block the specified user, deleting all messages they send\n!BLOCK|user or 'ALL'",BLOCK,[str])
command["!WCHANNEL"]=OWON("!WCHANNEL","This command will set the current text channel as the channel where welcoming messages are sent whenever someone joins the server\n!WCHANNEL",WCHANNEL,[])
command["!INVITE"]=OWON("!INVITE","This command will DM an invite to the user with the specified user id\n!INVITE|user id",INVITE,[int])
command["!UNBLOCK"]=OWON("!UNBLOCK","This command will unblock the specified user\n!UNBLOCK|user",UNBLOCK,[str])
