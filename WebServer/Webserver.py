import flask
import json
import time as t
import os
KIPP_DIR=os.environ['KIPP_DIR']
app=flask.Flask(__name__)
import datetime
time=datetime.datetime.now().strftime("%H:%M")
def get_time():
    ampm="AM"
    if int(time[0:2])>=12:
        ampm="PM"
    if int(time[0:2])>12:
        ti=str(int(time[0:2])-12)+time[2:]+" "+ampm
    else:
        ti=time+" "+ampm
    if ti[0:2]=="00":
        ti="12:"+ti.split(":")[1]
    return ti
tmp = open('/sys/class/thermal/thermal_zone0/temp')
oldcpu = tmp.read()
tmp.close()
oldcpu=str(int(oldcpu)/1000)
def eventStream():
    while True:
        global time
        if datetime.datetime.now().strftime("%H:%M") != time:
            ti=get_time()
            time=datetime.datetime.now().strftime("%H:%M")
            yield "event:time_event\ndata:{}\n\n".format(ti)
        tmp = open('/sys/class/thermal/thermal_zone0/temp')
        cpu = tmp.read()
        tmp.close()
        cpu=str(int(cpu)/1000)
        yield "event:cpu_event\ndata:{}\n\n".format(cpu)
        t.sleep(1)
@app.route('/')
def home():
    global oldcpu
    ti=get_time()
    return flask.render_template('index.html',time=ti,cpu=oldcpu)
@app.route('/stream')
def stream():
    return flask.Response(eventStream(),mimetype="text/event-stream")
import socket
ip = socket.gethostbyname(socket.gethostname())
app.run(host=ip, port=80)
