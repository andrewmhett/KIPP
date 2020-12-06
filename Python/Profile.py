from ESSENTIAL_PACKAGES import *
KIPP_DIR = os.environ['KIPP_DIR']


class Profile:
    def __init__(self, user):
        """Class used to keep track of user-specific data

        :param user: the discord.py member object to track data for
        :type user: <discord.member.Member>
        """
        self.gamblemessage = None
        self.bet = None
        self.solo = False
        self.color = None
        self.gamblerequest = False
        self.challenger = None
        self.betting = False
        self.user = user
        self.has_autominer = False
        self.shop_message = None
        self.chess_board = None
        self.chess_engine = None

    def GET_KIPPCOINS(self):
        return int(subprocess.Popen(["sudo", "-E", KIPP_DIR + "/C++/KIPPCOINS_IO", "r", str(self.user.id)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0])

    def GIVE_KIPPCOINS(self, KC):
        balance = int(subprocess.Popen(["sudo", "-E", KIPP_DIR + "/C++/KIPPCOINS_IO", "r", str(
            self.user.id)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]) + KC
        subprocess.Popen([KIPP_DIR + "/C++/KIPPCOINS_IO",
                          "w", str(self.user.id), str(balance)])

    def GIVE_ITEM(self, shop_index):
        bin_data = str(bin(int(subprocess.Popen(["sudo", "-E", KIPP_DIR + "/C++/ITEMS_IO", "r", str(
            self.user.id)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0])))
        print(bin_data)
        bin_data = bin_data.split("0b")[1][::-1]
        while shop_index > len(bin_data):
            bin_data = bin_data + '0'
        out_bin = ""
        for i in range(len(bin_data)):
            if i == shop_index - 1:
                out_bin += '1'
            else:
                out_bin += bin_data[i]
        out_bin = out_bin[::-1]
        print(out_bin)
        subprocess.Popen(["sudo", "-E", KIPP_DIR + "/C++/ITEMS_IO", "w", str(self.user.id),
                          str(int(out_bin, 2))], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def HAS_ITEM(self, shop_index):
        bin_data = str(bin(int(subprocess.Popen(["sudo", "-E", KIPP_DIR + "/C++/ITEMS_IO", "r", str(
            self.user.id)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0])))
        bin_data = bin_data.split("0b")[1]
        if (shop_index > len(bin_data)):
            return False
        bin_data = bin_data[::-1]
        return bool(int(bin_data[shop_index - 1]))
