import sys
import os
KIPP_DIR=os.environ["KIPP_DIR"]
sys.path.append(KIPP_DIR+"/Python")
from ESSENTIAL_PACKAGES import *
from .Command_utils import *
from Command import *
import threading

def mine_kippcoins(message,message2,serverinfo,playerinfo):
    amount_mined=1
    if playerinfo[message.author].HAS_ITEM(1):
        amount_mined*=2
    if playerinfo[message.author].HAS_ITEM(2):
        amount_mined*=4
    if playerinfo[message.author].HAS_ITEM(3):
        amount_mined*=8
    if playerinfo[message.author].HAS_ITEM(4):
        amount_mined*=16
    playerinfo[message.author].GIVE_KIPPCOINS(amount_mined) 

async def MINE(message,message2,serverinfo,playerinfo):
    threading.Thread(target=mine_kippcoins,args=[message,message2,serverinfo,playerinfo]).start()

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
        emb = discord.Embed(title="Transfer",description="Transferred `{0}` KIPPCOINS to **{1}**'s account.\n You now have `{2}` KIPPCOINS.".format(amount,str(receiver),int(playerinfo[patron].GET_KIPPCOINS())),colour=EMBEDCOLOR)
        emb.set_footer(text=get_footer())
        await message.channel.send(embed=emb)
    else:
        await message.channel.send("The amount entered was either higher than the amount of KIPPCOINS you have, or was negative.")

async def GAMBLEGAME(message,message2,serverinfo,playerinfo):
    if message2.split('|')[1] == "SOLO":
        playerinfo[message.author].solo = True
        emb = discord.Embed(title="Solo GambleGame",description="Use `!SELECT|color` to choose a color:\n`Red`\n`Blue`\n`Green`\n`Black`",colour=EMBEDCOLOR)
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

def to_roman_numeral(num):
    numeralMap = {
      1:"I",
      4:"IV",
      5:"V",
      9:"IX",
      10:"X",
      40:"XL",
      45:"XLV",
      50:"L",
      90:"XC",
      100:"C",
      400:"CD",
      500:"D",
      900:"CM",
      1000:"M"
    }
    keys=list(numeralMap.keys())
    index=13
    output=""
    while num != 0:
        while (num/keys[index])>=1:
          num-=keys[index];
          output+=numeralMap[keys[index]];
        index-=1;
    return output

async def INVENTORY(message,message2,serverinfo,playerinfo):
    items=subprocess.Popen(["sudo","cat",KIPP_DIR+"/C++/SHOP_ITEMS.txt"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
    item_index=0
    em=discord.Embed(title="Inventory",color=EMBEDCOLOR,description="")
    plaques=[]
    for item in items:
        if len(item)>0:
            item_index+=1
            if playerinfo[message.author].HAS_ITEM(item_index):
                if "PLAQUE" in item:
                    plaques.append(item.split("KIPP YEAR ")[1].split(" PLAQUE")[0])
                else:
                    em.description+="\n`{0}`".format(item.split(":")[0])
    if len(plaques)>0:
        plaque_str=""
        for plaque_num in plaques:
            roman_numeral_row="YEAR {0}".format(to_roman_numeral(int(plaque_num)))
            padding="="*int((20-len(roman_numeral_row))/2)
            roman_numeral_row=padding+roman_numeral_row+padding
            roman_numeral_row+="="*(20-len(roman_numeral_row))
            plaque_str+="\n```+--------------------+\n|========KIPP========|\n|{0}|\n|=December 1st, {1}=|\n+--------------------+```".format(roman_numeral_row,str(2017+int(plaque_num)))
        em.add_field(name="Plaques",value=plaque_str)
    if len(em.description)==0 and len(plaques)==0:
        em.description="You don't own any items."
    await message.channel.send(embed=em)

async def BUY(message,message2,serverinfo,playerinfo):
    item_dict={}
    items=subprocess.Popen(["sudo","cat",KIPP_DIR+"/C++/SHOP_ITEMS.txt"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
    for item in items:
        if len(item)>0:
            item_dict[item.split(":")[0]]=int(item.split(":")[1])
    item_index=0
    purchase_index=int(message2.split("|")[1])
    if purchase_index<0 or purchase_index>len(items) or items[purchase_index-1].split(":")[2]=='0':
        await message.channel.send("Invalid item index.")
        return
    if playerinfo[message.author].HAS_ITEM(purchase_index):
        await message.channel.send("You already own this item.")
        return
    playerinfo[message.author].shop_message=None
    for item in items:
        if len(item)>0:
            item_index+=1
            name=item.split(":")[0]
            if item_dict[name]<=playerinfo[message.author].GET_KIPPCOINS() and purchase_index==item_index:
                playerinfo[message.author].GIVE_ITEM(item_index)
                playerinfo[message.author].GIVE_KIPPCOINS(-1*item_dict[name])
                await message.channel.send("Successfully purchased `{0}`. Your new KC balance stands at `{1} KC`".format(name,playerinfo[message.author].GET_KIPPCOINS()))
                if playerinfo[message.author].shop_message != None:
                    await message.channel.delete(playerinfo[message.author].shop_message)
                return
    await message.channel.send("You cannot afford this item. Use `!MINE` in order to mine KC.")

async def SHOP(message,message2,serverinfo,playerinfo):
    item_dict={}
    items=subprocess.Popen(["sudo","cat",KIPP_DIR+"/C++/SHOP_ITEMS.txt"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
    in_budget=[]
    out_of_budget=[]
    for item in items:
        if len(item)>0:
            item_dict[item.split(":")[0]]=int(item.split(":")[1])
    em=discord.Embed(title="Shop",color=EMBEDCOLOR)
    em.description="Current balance: `{0} KC`\n```#  NAME                      PRICE\n".format(playerinfo[message.author].GET_KIPPCOINS())
    item_index=0
    for item in items:
        if len(item)>0:
            item_index+=1
            name=item.split(":")[0]
            if not playerinfo[message.author].HAS_ITEM(item_index) and items[item_index-1].split(":")[2]=='1':
                if item_dict[name]<=playerinfo[message.author].GET_KIPPCOINS():
                    in_budget.append([name,item_index])
                else:
                    out_of_budget.append([name,item_index])
    if len(in_budget)>0:
        em.description+="-------------IN BUDGET------------"
        for item in in_budget:
            em.description+="\n{0}".format(item[1])+"  "
            em.description+="{0}".format(item[0])+(" "*(26-len(item[0])))
            em.description+="{0}".format(item_dict[item[0]])
        em.description+="\n"
    if len(out_of_budget)>0:
        em.description+="-----------OUT OF BUDGET----------"
        for item in out_of_budget:
            em.description+="\n{0}".format(item[1])+"  "
            em.description+="{0}".format(item[0])+(" "*(26-len(item[0])))
            em.description+="{0}".format(item_dict[item[0]])
        em.description+="\n"
    em.description+="```In order to buy an item, use `!BUY|item number`\n(the item number is listed in the left column)"
    if len(in_budget)==0 and len(out_of_budget)==0:
        em.description="You have purchased every item in the shop."
    elif len(in_budget)==0:
        em.description+="\n__It looks like you can't afford any items in the shop.__\nUse `!MINE` to mine KC."
    playerinfo[message.author].shop_message = await message.channel.send(embed=em)

async def BALANCE(message,message2,serverinfo,playerinfo):
    em=discord.Embed(title="KIPPCOIN Balance",description="Balance: `{0} KC`".format(playerinfo[message.author].GET_KIPPCOINS()),color=EMBEDCOLOR)
    await message.channel.send(embed=em)

command["!MINE"]=KIPC("!MINE","This command stacks all of your KIPPCOIN multipliers and adds that amount of KIPPCOINS to your account. This command will not return any message\n!MINE",MINE,[])
command["!TRANSFER"]=KIPC("!TRANSFER","This command will transfer a given amount of KIPPCOINS from your account to another account\n!TRANSFER|amount|receiver",TRANSFER,[int,str])
command["!GAMBLEGAME"]=KIPC("!GAMBLEGAME","This command will start either a solo or multiplayer gambling game involving KIPPCOINS\n!GAMBLEGAME|'SOLO' or opponent user",GAMBLEGAME,[str])
command["!SHOP"]=KIPC("!SHOP","Opens the KIPPCOIN shop\n!SHOP",SHOP,[])
command["!BUY"]=KIPC("!BUY","Purchases an item from the shop\n!BUY|item number",BUY,[int])
command["!INVENTORY"]=KIPC("!INVENTORY","Displays your inventory\n!INVENTORY",INVENTORY,[])
command["!BALANCE"]=KIPC("!BALANCE","Displays your KIPPCOIN balance\n!BALANCE",BALANCE,[])
