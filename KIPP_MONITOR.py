import os
from subprocess import Popen, PIPE
import websockets.exceptions
import concurrent.futures._base
#from aiohttp import errors as aiohttp_errors
import aiohttp
import logging
import threading
def WebMonitor():
    os.system('python3.6 "/home/pi/Desktop/KIPPSTUFF/Web Server/Webserver.py"')
t1=threading.Thread(target=WebMonitor)
t1.start()
KIPP_RESET_ERRORS = [ConnectionResetError,
                     websockets.exceptions.ConnectionClosed,
                     concurrent.futures._base.TimeoutError,
                     aiohttp.ClientOSError,
                     websockets.exceptions.InvalidStatusCode]
try:
    logging.log(50,"Backing KIPP up to GitHub...")
    os.system('sudo /home/pi/Desktop/KIPPSTUFF/BackupKIPP.sh')
except FileNotFoundError:
    logging.log(50,"KIPP backup file not found.")
try:
    logging.log(50,"Checking for package updates")
    os.system('sudo /home/pi/Desktop/KIPPSTUFF/REQUIREMENTUPDATES.sh')
except FileNotFoundError:
    logging.log(50,"KIPP package updater not found.")
while True:
    logging.log(50,"KIPP starting...")
    try:
        os.system("sudo python3.6 /home/pi/Desktop/KIPP.py")
    except Exception as e:
        if type(e) in KIPP_RESET_ERRORS:
            pass
    logging.log(50,"KIPP restarting...")
