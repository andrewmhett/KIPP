import flask
import json
import time as t
app=flask.Flask(__name__)
#counter=0
#oldcount=0
from subprocess import Popen, PIPE
p=Popen('/home/pi/KIPP/KIPPSTUFF/DaemonStatus.sh',stdout=PIPE,stderr=PIPE)
stdout=p.communicate()[0].decode()
p.kill()
status=stdout.split('ago')[0]+"ago"
import datetime
def get_time():
    time=datetime.datetime.now().strftime("%H:%M")
    if int(time[0:2])>12:
        ti=str(int(time[0:2])-12)+time[2:]+" PM"
    else:
        ti=time+" AM"
    if ti[0:2]=="00":
        ti="12:"+ti.split(":")[1]
    return ti
tmp = open('/sys/class/thermal/thermal_zone0/temp')
oldcpu = tmp.read()
tmp.close()
oldcpu=str(int(oldcpu)/1000)
def eventStream():
    global time
    global status
    global ti
    while True:
        if datetime.datetime.now().strftime("%H:%M") != time:
            ti=get_time()
            yield "event:time_event\ndata:{}\n\n".format(ti)
        p=Popen('/home/pi/KIPP/KIPPSTUFF/DaemonStatus.sh',stdout=PIPE,stderr=PIPE)
        stdout=p.communicate()[0].decode()
        p.kill()
        if (stdout.split('ago')[0]+"ago" != status):
            status=stdout.split('ago')[0]+"ago"
            yield "event:status_event\ndata:{}\n\n".format(status.replace("\n","<br>"))
        tmp = open('/sys/class/thermal/thermal_zone0/temp')
        cpu = tmp.read()
        tmp.close()
        cpu=str(int(cpu)/1000)
        yield "event:cpu_event\ndata:{}\n\n".format(cpu)
        t.sleep(1)
@app.route('/')
def home():
    global status
    global ti
    global oldcpu
    return flask.render_template('index.html',time=ti,cpu=oldcpu)
@app.route('/CountUp')
def CountUp():
    global counter
    counter+=1
    return "done"
@app.route('/CountDown')
def CountDown():
    global counter
    counter-=1
    return "done"
@app.route('/stream')
def stream():
    return flask.Response(eventStream(),mimetype="text/event-stream")
app.run(host='0.0.0.0', port=80)
