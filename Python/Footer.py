from datetime import datetime
def get_footer():
    weekint = datetime.today().weekday()
    if weekint == 0:
        weekday = "Monday"
    if weekint == 1:
        weekday = "Tuesday"
    if weekint == 2:
        weekday = "Wednesday"
    if weekint == 3:
        weekday = "Thursday"
    if weekint == 4:
        weekday = "Friday"
    if weekint == 5:
        weekday = "Saturday"
    if weekint == 6:
        weekday = "Sunday"
    year = ((str(datetime.now())[0])+(str(datetime.now())[1])+(str(datetime.now())[2])+(str(datetime.now())[3]))
    month = ((str(datetime.now())[5])+(str(datetime.now())[6]))
    day = ((str(datetime.now())[8])+(str(datetime.now())[9]))
    minute = ((str(datetime.now())[14])+(str(datetime.now())[15]))
    if (int((str(datetime.now())[11])+(str(datetime.now())[12]))>12) or (int((str(datetime.now())[11])+(str(datetime.now())[12])) == 12):
        timeBinary = 1
        if int((str(datetime.now())[11])+(str(datetime.now())[12]))>12:
            hour = str(int((str(datetime.now())[11])+(str(datetime.now())[12]))-12)
        else:
            hour = str(int((str(datetime.now())[11])+(str(datetime.now())[12])))
    else:
        hour = ((str(datetime.now())[11])+(str(datetime.now())[12]))
        timeBinary = 0
    if str(hour) == "00":
        hour = "12"
    if str(month) == "01":
        strmonth = "January"
    if str(month) == "02":
        strmonth = "February"
    if str(month) == "03":
        strmonth = "March"
    if str(month) == "04":
        strmonth = "April"
    if str(month) == "05":
        strmonth = "May"
    if str(month) == "06":
        strmonth = "June"
    if str(month) == "07":
        strmonth = "July"
    if str(month) == "08":
        strmonth = "August"
    if str(month) == "09":
        strmonth = "September"
    if str(month) == "10":
        strmonth = "October"
    if str(month) == "11":
        strmonth = "November"
    if str(month) == "12":
        strmonth = "December"
    if day == "11" or day == "12" or str(day) == "13" or (str(day).endswith('1') == False and day != "11") or (str(day).endswith('2') == False and str(day) != "12") or (str(day).endswith('3') == False and day != "13"):
        ending = "th"
    if str(day).endswith("1") and str(day) != "11":
        ending = "st"
    if str(day).endswith("2") and str(day) != "12":
        ending = "nd"
    if str(day).endswith("3") and str(day) != "13":
        ending = "rd"
    if str(day).startswith('0'):
        day = str(day)
        day = day.split('0')[1]
    if timeBinary == 0:
        footer = ("KIPP | "+weekday+" "+strmonth+" "+str(day)+ending+", "+str(year)+" at "+hour+":"+minute+" AM")
    if timeBinary == 1:
        footer = ("KIPP | "+weekday+" "+strmonth+" "+str(day)+ending+", "+str(year)+" at "+hour+":"+minute+" PM")
    return footer
