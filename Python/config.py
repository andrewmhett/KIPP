commands=[]
serverinfo={}
playerinfo={}
CREATOR_ID=289920025077219328
KIPP_ID=386352783550447628
profooter=""
def READ_DATA_IN(path, condition=lambda x: True, attr_condition=lambda x: True):
    try:
        with open(path) as f:
            f.close()
    except Exception:
         with open(path,'w+') as f:
             f.close()
    arr=[]
    found=False
    with open(path) as fl:
        for row in csv.reader(fl):
            if condition(row):
                for attr in row:
                    if attr_condition(attr):            
                        arr.append(row)
                        break
        fl.close()
    if len(arr)==0:
        arr=None
    return arr
