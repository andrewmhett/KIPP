import os
from subprocess import Popen, PIPE
import websockets.exceptions
import concurrent.futures._base
#from aiohttp import errors as aiohttp_errors
import aiohttp
import logging
import threading
import time
import sys
KIPP_DIR=os.environ['KIPP_DIR']
def WebMonitor():
    os.system('sudo -E python3.6 "{0}/WebServer/Webserver.py"'.format(KIPP_DIR))
def GitUpdate():
    while True:
        stdout = Popen(KIPP_DIR+"/Bash/GitUpdater.sh",stdout=PIPE).communicate()[0].decode()
        if "Already up to date" not in stdout:
            print("New commit on master branch, restarting...")
            os.system("sudo systemctl restart KIPP")
        time.sleep(60)
t1=threading.Thread(target=WebMonitor)
t1.start()
dev=False
if len(sys.argv)>1:
    if sys.argv[1]=="dev":
        dev=True
if not dev:
    t2=threading.Thread(target=GitUpdate)
    t2.start()
KIPP_RESET_ERRORS = [ConnectionResetError,
                     websockets.exceptions.ConnectionClosed,
                     concurrent.futures._base.TimeoutError,
                     aiohttp.ClientOSError,
                     websockets.exceptions.InvalidStatusCode]
try:
    logging.log(50,"Checking for package updates")
    os.system('sudo -E {0}/Bash/REQUIREMENTUPDATES.sh'.format(KIPP_DIR))
except FileNotFoundError:
    logging.log(50,"KIPP package updater not found.")
while True:
    logging.log(50,"KIPP starting...")
    try:
        os.system("sudo -E python3.6 {0}/Python/KIPP.py".format(KIPP_DIR))
    except Exception as e:
        #if type(e) in KIPP_RESET_ERRORS:
            #pass
        logging.log(50, "ERROR: {0}".format(e))
    logging.log(50,"KIPP restarting...")
