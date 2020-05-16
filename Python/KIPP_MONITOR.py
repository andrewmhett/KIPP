import os
from subprocess import Popen, PIPE
import websockets.exceptions
import concurrent.futures._base
#from aiohttp import errors as aiohttp_errors
import aiohttp
import logging
import threading
print(os.environ)
KIPP_DIR=os.environ['KIPP_DIR']
def WebMonitor():
    os.system('sudo -E python3.6 "{0}/WebServer/Webserver.py"'.format(KIPP_DIR))
t1=threading.Thread(target=WebMonitor)
t1.start()
KIPP_RESET_ERRORS = [ConnectionResetError,
                     websockets.exceptions.ConnectionClosed,
                     concurrent.futures._base.TimeoutError,
                     aiohttp.ClientOSError,
                     websockets.exceptions.InvalidStatusCode]
try:
    logging.log(50,"Backing KIPP up to GitHub...")
    os.system('sudo -E {0}/Bash/BackupKIPP.sh'.format(KIPP_DIR))
except FileNotFoundError:
    logging.log(50,"KIPP backup file not found.")
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
