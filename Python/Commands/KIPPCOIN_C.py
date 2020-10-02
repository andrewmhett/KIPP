import sys
import os
KIPP_DIR=os.environ["KIPP_DIR"]
sys.path.append(KIPP_DIR+"/Python")
from ESSENTIAL_PACKAGES import *
from .Command_utils import *
from Command import *

async def MINE(message,message2,serverinfo,playerinfo):
    playerinfo[message.author].GIVE_KIPPCOINS(1)

async def TRANSFER(message,message2,serverinfo,playerinfo):
    try:
        patron=message.author
        amount=message2.split("|")[1]
        receiver=message.guild.get_member_named(str(message.content).split("|")[2])
    except Exception as err:
        if err == IndexError:
            await message.channel.send( "Make sure you specify both an amount and a receiver.")
        else:
            await message.channel.send( "The receiver could not be found.")
    if int(amount)<=int(playerinfo[patron].GET_KIPPCOINS()) and int(amount)>0:
        playerinfo[patron].GIVE_KIPPCOINS(-1*int(amount))
        playerinfo[receiver].GIVE_KIPPCOINS(int(amount))
        emb = discord.Embed(title="Transfer",description="Transferred **{0}** KIPPCOINS to **{1}**'s account.\n You now have **{2}** KIPPCOINS.".format(amount,str(receiver),int(playerinfo[patron].GET_KIPPCOINS())),colour=EMBEDCOLOR)
        emb.set_footer(text=get_footer())
        await message.channel.send(embed=emb)
    else:
        await message.channel.send("The amount entered was either higher than the amount of KIPPCOINS you have, or was negative.")

async def GAMBLEGAME(message,message2,serverinfo,playerinfo):
    if message2.split('|')[1] == "SOLO":
        playerinfo[message.author].solo = True
        emb = discord.Embed(title="Solo GambleGame",description="Use **!SELECT|color** to choose a color:\n**Red**\n**Blue**\n**Green**\n**Black**",colour=EMBEDCOLOR)
        emb.set_footer(text=get_footer())
        message1=await message.channel.send(embed=emb)
        playerinfo[message.author].gamblemessage=message1
    else:
        try:
            opponent=message.guild.get_member_named(str(message.content).split("|")[1])
        except Exception:
            await message.channel.send("This user does not exist.")
        if str(opponent.status).upper != "OFFLINE" and str(opponent.status).upper != "IDLE":
            playerinfo[opponent].gamblerequest=True
            playerinfo[opponent].challenger=message.author
            playerinfo[message.author].challenger=opponent
            desc = "{0}, you have been challenged to a GambleGame by {1}.\n**!ACCEPT** or **!DECLINE**\n{2} may **!CANCEL**".format(opponent.mention,message.author.mention,message.author.mention)
            emb=discord.Embed(title="GambleGame Request",description = desc,colour=EMBEDCOLOR)
            emb.set_footer(text=get_footer())
            message1 = await message.channel.send(embed=emb)
            playerinfo[message.author].gamblemessage=message1
            playerinfo[opponent].gamblemessage=message1

command["!MINE"]=KIPC("!MINE","This command stacks all of your KIPPCOIN multipliers and adds that amount of KIPPCOINS to your account. This command will not return any message\n!MINE",MINE,[])
command["!TRANSFER"]=KIPC("!TRANSFER","This command will transfer a given amount of KIPPCOINS from your account to another account\n!TRANSFER|amount|receiver",TRANSFER,[int,str])
command["!GAMBLEGAME"]=KIPC("!GAMBLEGAME","This command will start either a solo or multiplayer gambling game involving KIPPCOINS\n!GAMBLEGAME|'SOLO' or opponent user",GAMBLEGAME,[str])
