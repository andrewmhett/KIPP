from ESSENTIAL_PACKAGES import *
class Profile:
    def __init__(self,user):
        self.gamblemessage=None
        self.bet=None
        self.solo=False
        self.color=None
        self.gamblerequest=False
        self.challenger=None
        self.betting=False
        self.numkippservers = 0
        self.game = ""
        self.highestrole = ""
        self.nickname = ""
        self.hrolecolor = None
        self.streaming = False
        self.user = user
        self.instore=False
        self.storepage=None
        with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS') as fl:
            reader=csv.reader(fl)
            infile=False
            readarray=[]
            for row in reader:
                readarray.append(row)
                if(row[0] == self.user.id):
                    infile=True
            if infile==False:
                readarray.append((str(self.user.id),0))
                with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS','w') as f:
                    writer=csv.writer(f)
                    for row in readarray:
                        writer.writerow(row)
                    f.close()
            fl.close()
    def GET_KIPPCOINS(self):
        with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS') as fl:
            reader=csv.reader(fl)
            for row in reader:
                if row[0] == str(self.user.id):
                    return row[1]
            fl.close()
    def HAS_ITEM(self,item):
        with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS') as fl:
            reader=csv.reader(fl)
            for row in reader:
                if str(row[0]) == str(self.user.id):
                    if item in row:
                        return True
                    else:
                        return False
            fl.close()
    def GIVE_KIPPCOINS(self, KC):
        readarray=READ_DATA_IN('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS')
        for row in readarray:
             if row[0] == str(self.user.id):
                orig=int(row[1])
                row[1] = orig+int(KC)
        with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS','w') as f:
            writer=csv.writer(f)
            for row in readarray:
                writer.writerow(row)
            f.close()
    def GIVE_ITEM(self, item):
        readarray=READ_DATA_IN('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS',condition=lambda x: True if x[0] == str(self.user.id) else False)
        with open('/home/pi/Desktop/KIPPSTUFF/KIPPCOINS','w') as f:
            writer=csv.writer(f)
            for row in readarray:
                writer.writerow(row)
            f.close()