import sys
import os
KIPP_DIR=os.environ["KIPP_DIR"]
sys.path.append(KIPP_DIR+"/Python")
from ESSENTIAL_PACKAGES import *
from .Command_utils import *
from Command import *

async def MINE(message,message2,serverinfo,playerinfo):
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

async def STOCKS(message,message2,serverinfo,playerinfo):
    em=discord.Embed(title="KIPPCOIN Stocks",color=EMBEDCOLOR)
    markets=subprocess.Popen(["sudo","-E",KIPP_DIR+"/C++/STOCKS_IO","r","a"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode()
    markets=markets.split("\n")
    markets_string="```NAME  CHANGE         KC/SHARE NUM"
    markets_string+="\n"+"-"*(len(markets_string)-2)
    stock_deltas=subprocess.Popen(["sudo","cat",KIPP_DIR+"/STOCKS.txt"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
    market_change_map={}
    for stock in stock_deltas:
        if len(stock)>0 and not stock.startswith("LAST UPDATED"):
            market_change_map[stock.split(":")[0]]=int(stock.split(":")[1])
    for market in markets:
        if len(market)>0:
            market_row="\n"+market.split(":")[0]+"  "
            per_share_price=market.split(":")[1].split(" ")[2]
            kc_change=market_change_map[market.split(":")[0]]
            if int(kc_change)>=0:
                kc_change="+"+str(kc_change)
            try:
                percent_change=round(100*(int(kc_change)/(int(per_share_price)-int(kc_change))),1)
            except ZeroDivisionError:
                percent_change=0
            change_string=str(kc_change)+(" "*(6-len(str(kc_change))))+"("+('+' if percent_change>=0 else '')+str(percent_change)+"%)"
            market_row+=change_string+(" "*(15-len(change_string)))
            market_row+=per_share_price+(" "*(9-len(per_share_price)))
            market_row+=market.split(" ")[1]
            markets_string+=market_row
    markets_string+="```"
    em.add_field(name="Markets",value=markets_string)
    shares=subprocess.Popen(["sudo","-E",KIPP_DIR+"/C++/SHARES_IO","r",str(message.author.id),"a"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
    shares_string=""
    has_shares=False
    for share in shares:
        if len(share)>0:
            if int(share.split(": ")[1])>0:
                has_shares=True
    if not has_shares:
        shares_string="__You don't own any shares.__\nSee `!HELP|BUYSHARES` and `!SHARES`"
    else:
        shares_string="Use `!SHARES` for information about your shares."
    em.add_field(name="Your Shares",value=shares_string,inline=False)
    await message.channel.send(embed=em)

async def BUYSHARES(message,message2,serverinfo,playerinfo):
    markets=subprocess.Popen(["sudo","-E",KIPP_DIR+"/C++/STOCKS_IO","r","a"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode()
    markets=markets.split("\n")
    market_found=False
    for market in markets:
        if len(market)>0:
            if market.split(":")[0] == message2.split("|")[1] or market.split(":")[0].replace("_","") == message2.split("|")[1]:
                market_found=True
                price_per_share=int(market.split(":")[1].split(" ")[2])
                num_purchasing=int(message2.split("|")[2])
                if num_purchasing<=0:
                    await message.channel.send("Please specify a valid amount of shares to purchase.")
                    return
                if num_purchasing<=int(market.split(":")[1].split(" ")[1]):
                    if price_per_share*num_purchasing<=playerinfo[message.author].GET_KIPPCOINS():
                        num_shares_held=int(subprocess.Popen(["sudo","-E",KIPP_DIR+"/C++/SHARES_IO","r",str(message.author.id),market.split(":")[0]],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode())
                        os.system("sudo -E {0}/C++/SHARES_IO wn {1} {2} {3}".format(KIPP_DIR,message.author.id,market.split(":")[0],num_purchasing+num_shares_held))
                        os.system("sudo -E {0}/C++/STOCKS_IO wn {1} {2}".format(KIPP_DIR,market.split(":")[0],int(market.split(":")[1].split(" ")[1])-num_purchasing))
                        playerinfo[message.author].GIVE_KIPPCOINS(-1*num_purchasing*(int(market.split(":")[1].split(" ")[2])))
                        await message.channel.send("Successfully purchased `{0}` share{1} of `{2}`.".format(num_purchasing,("s" if num_purchasing != 1 else ""),message2.split("|")[1]))
                    else:
                        await message.channel.send("You cannot afford this many shares of `{0}`".format(message2.split("|")[1]))
                        break
                else:
                    await message.channel.send("There are not this many shares of `{0}` available.".format(message2.split("|")[1]))
                    break
    if not market_found:
        await message.channel.send("The market named `{0}` doesn't exist.".format(message2.split("|")[1]))

async def SELLSHARES(message,message2,serverinfo,playerinfo):
    shares=subprocess.Popen(["sudo","-E",KIPP_DIR+"/C++/SHARES_IO","r",str(message.author.id),"a"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
    markets=subprocess.Popen(["sudo","-E",KIPP_DIR+"/C++/STOCKS_IO","r","a"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
    market_value_map={}
    for market in markets:
        if len(market)>0:
            market_value_map[market.split(":")[0]]=[int(market.split(":")[1].split(" ")[2]),int(market.split(":")[1].split(" ")[1])]
    market_found=False
    for share in shares:
        if len(share)>0:
            if share.split(":")[0]==message2.split("|")[1] or share.split(":")[0].replace("_","")==message2.split("|")[1]:
                market_found=True
                num_shares_held=int(share.split(": ")[1])
                num_selling=int(message2.split("|")[2])
                if num_selling<=0:
                    await message.channel.send("Please specify a valid amount of shares to sell.")
                    return
                if num_selling<=num_shares_held:
                    market=share.split(":")[0]
                    os.system("sudo -E {0}/C++/SHARES_IO wn {1} {2} {3}".format(KIPP_DIR,message.author.id,market.split(":")[0],num_shares_held-num_selling))
                    os.system("sudo -E {0}/C++/STOCKS_IO wn {1} {2}".format(KIPP_DIR,market,market_value_map[market][1]+num_selling))
                    playerinfo[message.author].GIVE_KIPPCOINS(num_selling*market_value_map[market][0])
                    await message.channel.send("Successfully sold `{0}` share{1} of `{2}`.".format(num_selling,("s" if num_selling != 1 else ""),message2.split("|")[1]))
                else:
                    await message.channel.send("You don't own this many shares from `{0}`".format(message2.split("|")[1]))
                break
    if not market_found:
        await message.channel.send("You don't own any shares from `{0}`.".format(message2.split("|")[1]))

async def SHARES(message,message2,serverinfo,playerinfo):
    markets=subprocess.Popen(["sudo","-E",KIPP_DIR+"/C++/STOCKS_IO","r","a"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
    shares=subprocess.Popen(["sudo","-E",KIPP_DIR+"/C++/SHARES_IO","r",str(message.author.id),"a"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
    em=discord.Embed(title="Shares",color=EMBEDCOLOR)
    market_value_map={}
    shares_string=""
    for market in markets:
        if len(market)>0:
            market_value_map[market.split(":")[0]]=int(market.split(":")[1].split(" ")[2])
    has_shares=False
    for share in shares:
        if len(share)>0:
            if int(share.split(": ")[1])>0 and has_shares==False:
                has_shares=True
    if has_shares:
        shares_string="```NAME  SHARES   KC VALUE\n-----------------------"
        for share in shares:
            if len(share)>0:
                if int(share.split(": ")[1])>0:
                    value_string="{0}  {1}".format(share.split(":")[0],share.split(": ")[1])
                    shares_string+="\n"+value_string
                    shares_string+=" "*(15-len(value_string))
                    shares_string+=str(market_value_map[share.split(":")[0]]*int(share.split(": ")[1]))
        shares_string+="```\nSee `!HELP|SELLSHARES`"
    else:
        shares_string="You don't own any shares."
    em.add_field(name="Your Shares",value=shares_string)
    afford_string=""
    can_afford=False
    for market in markets:
        if len(market)>0:
            price_per_share=int(market.split(":")[1].split(" ")[2])
            within_budget=int(playerinfo[message.author].GET_KIPPCOINS()/price_per_share)
            if within_budget>0:
                can_afford=True
                afford_string+="\n`{0} share{1} of {2}`".format(within_budget,("s" if within_budget != 1 else ""),market.split(":")[0])
    if not can_afford:
        afford_string="You cannot afford any shares."
    em.add_field(name="Shares You can Afford",value=afford_string,inline=False)
    await message.channel.send(embed=em)

async def STONKS(message,message2,serverinfo,playerinfo):
    await STOCKS(message,message2,serverinfo,playerinfo)

async def LEADERBOARD(message,message2,serverinfo,playerinfo):
    net_worth_dict={}
    market_value_map={}
    markets=subprocess.Popen(["sudo","-E",KIPP_DIR+"/C++/STOCKS_IO","r","a"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
    for market in markets:
        if len(market)>0:
            market_value_map[market.split(":")[0]]=int(market.split(":")[1].split(" ")[2])
    await message.channel.send("Calculating values...")
    for member in message.guild.members:
        if not member.bot:
            shares=subprocess.Popen(["sudo","-E",KIPP_DIR+"/C++/SHARES_IO","r",str(member.id),"a"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode().split("\n")
            net_worth=0
            net_worth+=playerinfo[member].GET_KIPPCOINS()
            for share in shares:
                if len(share)>0:
                    net_worth+=market_value_map[share.split(":")[0]]*int(share.split(": ")[1])
            net_worth_dict[member.id]=[str(member),net_worth]
    await message.channel.send("Sorting...")
    net_worth_pairs=sorted(net_worth_dict.values(), key=lambda item: item[1])[::-1]
    position=0
    leaderboard_string="```#  USERNAME            KC NET WTH\n---------------------------------"
    for pair in net_worth_pairs:
        if position<10:
            position+=1
            leaderboard_string+="\n{0}".format(position)+(" "*(3-len(str(position))))
            display_name=pair[0]
            if len(display_name)>17:
                name_sections=["#".join(display_name.split("#")[0:-1]),display_name.split("#")[-1]]
                name_sections[0]=name_sections[0][0:9]+"...#"
                display_name="".join(name_sections)
            leaderboard_string+=display_name
            leaderboard_string+=" "*(20-len(display_name))
            leaderboard_string+=str(pair[1])
        else:
            break
    if len(net_worth_dict)<10:
        num=len(net_worth_dict)
        for i in range(10-num):
            leaderboard_string+="\n{0}".format(num+i+1)+(" "*(3-len(str(num+i+1))))+"_____               _____"
    leaderboard_string+="```"
    em=discord.Embed(title="KIPPCOIN Leaderboard",color=EMBEDCOLOR)
    em.description=leaderboard_string
    await message.channel.send(embed=em)

command["!MINE"]=KIPC("!MINE","This command stacks all of your KIPPCOIN multipliers and adds that amount of KIPPCOINS to your account. This command will not return any message\n!MINE",MINE,[])
command["!TRANSFER"]=KIPC("!TRANSFER","This command will transfer a given amount of KIPPCOINS from your account to another account\n!TRANSFER|amount|receiver",TRANSFER,[int,str])
command["!GAMBLEGAME"]=KIPC("!GAMBLEGAME","This command will start either a solo or multiplayer gambling game involving KIPPCOINS\n!GAMBLEGAME|'SOLO' or opponent user",GAMBLEGAME,[str])
command["!SHOP"]=KIPC("!SHOP","Opens the KIPPCOIN shop\n!SHOP",SHOP,[])
command["!BUY"]=KIPC("!BUY","Purchases an item from the shop\n!BUY|item number",BUY,[int])
command["!INVENTORY"]=KIPC("!INVENTORY","Displays your inventory\n!INVENTORY",INVENTORY,[])
command["!BALANCE"]=KIPC("!BALANCE","Displays your KIPPCOIN balance\n!BALANCE",BALANCE,[])
command["!STOCKS"]=KIPC("!STOCKS","Displays relevant stock market information\n!STOCKS",STOCKS,[])
command["!STONKS"]=KIPC("!STONKS","An alias for `!STOCKS`\n!STONKS",STONKS,[])
command["!SHARES"]=KIPC("!SHARES","Displays information about the stock shares you own\n!SHARES",SHARES,[])
command["!BUYSHARES"]=KIPC("!BUYSHARES","Buys a specified number of shares from a specified market\n!BUYSHARES|market name|number of shares",BUYSHARES,[str,int])
command["!SELLSHARES"]=KIPC("!SELLSHARES","Sells a specified number of shares from a specified market\n!SELLSHARES|market name|number of shares",SELLSHARES,[str,int])
command["!LEADERBOARD"]=KIPC("!LEADERBOARD","Displays a KIPPCOIN net worth leaderboard\n!LEADERBOARD",LEADERBOARD,[])
