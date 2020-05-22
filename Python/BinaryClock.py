from datetime import datetime

bin_lookup={
        '1':"▮",
        '0':"▯"
        }

def std_length(bin_str):
    if len(bin_str)<4:
        bin_str="0"*(4-len(bin_str))+bin_str
    return bin_str

def get_clock():
    now = datetime.now()
    clock=[]
    for i in range(2):
        clock.append(std_length(bin(int(now.strftime("%H")[i]))[2:]))
    for i in range(2):
        clock.append(std_length(bin(int(now.strftime("%M")[i]))[2:]))
    clock_str=""
    for bin_str in clock:
        for char in bin_str:
            clock_str=clock_str+bin_lookup[char]
        clock_str=clock_str+" "
    return clock_str
