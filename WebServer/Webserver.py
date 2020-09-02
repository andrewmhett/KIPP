import flask
import os
import psutil
KIPP_DIR=os.environ['KIPP_DIR']
app=flask.Flask(__name__)
temp_dir = '/sys/class/thermal/thermal_zone0/temp'

def get_cpu_temp():
    temp=0
    with open(temp_dir,'r') as f:
        temp=int(f.read())/1000
        f.close()
    return temp

def get_system_usage():
    cpu=psutil.cpu_percent()
    mem=(psutil.virtual_memory().total-psutil.virtual_memory().available)*10**-9
    return (cpu, mem)

@app.route('/')
def home():
    cpu_usage,mem_usage=get_system_usage()
    return flask.render_template('index.html',temp=get_cpu_temp(),cpu=cpu_usage,total_mem=psutil.virtual_memory().total*10**-9,mem_in_use=mem_usage)

@app.route('/api/temperature')
def temperature():
    return str(get_cpu_temp())

@app.route('/api/cpu')
def CPU():
    return str(psutil.cpu_percent())

@app.route('/api/memory')
def MEM():
    return str((psutil.virtual_memory().total-psutil.virtual_memory().available)*10**-9)

app.run(host="0.0.0.0", port=80)
