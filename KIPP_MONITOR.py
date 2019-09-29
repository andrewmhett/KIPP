import os
from subprocess import Popen, PIPE
import discord.errors
import websockets.exceptions
import concurrent.futures._base
from aiohttp import errors as aiohttp_errors
import logging
import threading
def WebMonitor():
    os.system('python3.6 "/home/pi/Desktop/KIPPSTUFF/Web Server/Webserver.py"')
t1=threading.Thread(target=WebMonitor)
t1.start()
KIPP_RESET_ERRORS = [ConnectionResetError,
                     discord.errors.ConnectionClosed,
                     websockets.exceptions.ConnectionClosed,
                     concurrent.futures._base.TimeoutError,
                     aiohttp_errors.ClientOSError,
                     websockets.exceptions.InvalidStatusCode]
try:
    logging.log(50,"Backing KIPP up to GitHub...")
    p=Popen(os.system('sudo /home/pi/Desktop/KIPPSTUFF/BackupKIPP.sh'),stdout=PIPE,stderr=PIPE)
    #p.communicate()
    p.kill()
except FileNotFoundError:
    logging.log(50,"KIPP backup file not found.")
try:
    logging.log(50,"Checking for package updates")
    p=Popen(os.system('sudo /home/pi/Desktop/KIPPSTUFF/REQUIREMENTUPDATES.sh'),stdout=PIPE,stderr=PIPE)
    p.communicate()
    p.kill()
except FileNotFoundError:
    logging.log(50,"KIPP package updater not found.")
while True:
    logging.log(50,"KIPP starting...")
    try:
        p=Popen(os.system("sudo python3.6 /home/pi/Desktop/KIPP.py"),stdout=PIPE,stderr=PIPE)
        stdout=p.communicate()[0]
    except Exception as e:
        if type(e) in KIPP_RESET_ERRORS:
            pass
    p.kill()
    logging.log(50,"KIPP restarting...")
