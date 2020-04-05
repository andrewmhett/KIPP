# KIPP
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4ff9da4213c241baa013284e6e6848bc)](https://www.codacy.com/app/LockdownDoom/KIPP?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LockdownDoom/KIPP&amp;utm_campaign=Badge_Grade)
### Information
KIPP is currently in development. KIPP's development started in December, 2018; I wanted to have a discord bot that I could fully customize, and thought that making one would be a good idea. Since the very early stages of development, KIPP has been developed on a Raspberry Pi, so running KIPP on any other OS than Linux may be difficult.

### Getting and Running KIPP
###### Python 3.x required
###### Raspberry Pi required
#### Step 1: Cloning KIPP
In order to run KIPP, KIPP's program and its dependencies must be on your computer. Cloning this repository onto a Raspberry Pi is very simple, and can be done through this command in a terminal. For this set of instructions, we're going to clone KIPP into the Raspberry Pi's home directory.
```
cd /home/pi
git clone https://github.com/LockdownDoom/KIPP
```
This will clone this repository into a directory named `KIPP` in `/home/pi`.
#### Step 2: Running KIPP
KIPP automatically checks for the status of his dependencies during start-up, so there is no need to install these manually. To run KIPP, simply open a terminal and use this command.
```
cd /home/pi/KIPP
python3 ./KIPP/KIPP_MONITOR.py
```
This will start up and run KIPP. This monitor program will restart KIPP if any unexpected network/server errors occur or if KIPP crashes.
#### OPTIONAL: Run KIPP as a Linux daemon
The previous steps are all that is necessary to get KIPP running, but this step is also useful. Setting KIPP up as a Linux daemon will make him start up and run in the background of the Raspberry Pi from when you turn it on to when you turn it off.
First, you must create the `KIPP.service` file in the `/lib/systemd/system` directory of your Raspberry Pi.
```
cd /lib/systemd/system/
sudo vim KIPP.service
```
This will open a vim window for a file named `KIPP.service`. Now, edit the contents of this file so that they match this:
```
[Unit]
Description=KIPP Daemon
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/pi/KIPP/KIPP_MONITOR.py
Restart=on-abort
RestartSec=0

[Install]
WantedBy=multi-user.target
```
After creating the `KIPP.service` file, you may choose to have KIPP's daemon run non-stop and start on bootup, or use the default behaviour of full-manual control over it. In order to activate the former, run this command:
```
sudo systemctl enable KIPP.service
```
If you want to stop KIPP's daemon, simply go to a terminal and type:
```
sudo systemctl stop KIPP.service
```
And if you want to start the service back up:
```
sudo systemctl start KIPP.service
```
And finally, if you want to check the status of the daemon:
```
sudo systemctl status KIPP.service
```
