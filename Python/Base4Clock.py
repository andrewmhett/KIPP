from datetime import datetime
import baseconvert

base_4_lookup={
        0:"◳",
        1:"◲",
        2:"◱",
        3:"◰"
        }

def std_length(base_4_number):
    out_arr=[0,0,0]
    for i in range(len(base_4_number)):
        out_arr[2-i]=base_4_number[len(base_4_number)-i-1]
    return out_arr

def get_clock():
    now = datetime.now()
    clock=[]
    now_arr=[int(now.strftime("%H")),int(now.strftime("%M"))]
    for i in range(2):
        base_4_arr=[*(i for i in baseconvert.base(now_arr[i],10,4))]
        clock.append(std_length(base_4_arr))
    base_4_clock=[]
    for i in range(len(clock[0])):
        base_4_clock.append(base_4_lookup[clock[0][i]])
    for i in range(len(clock[1])):
        base_4_clock.append(base_4_lookup[clock[1][i]])
    clock_str="%s%s%s %s%s%s" % (tuple(base_4_clock))
    return clock_str
