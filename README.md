# KIPP
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4ff9da4213c241baa013284e6e6848bc)](https://www.codacy.com/app/LockdownDoom/KIPP?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LockdownDoom/KIPP&amp;utm_campaign=Badge_Grade)
### Information
KIPP is currently in development. KIPP's development started in December, 2018; I wanted to have a discord bot that I could fully customize, and thought that making one would be a good idea. Since the very early stages of development, KIPP has been developed on a Raspberry Pi, so running KIPP on anything besides a UNIX-based OS may be difficult; these steps will not work on Windows.

### Getting and Running KIPP
###### Python 3.x required
###### UNIX-based OS required
###### Raspberry Pi optional
#### Step 1: Cloning KIPP
In order to run KIPP, KIPP's program and its dependencies must be on your computer. Cloning this repository onto a Linux distribution is very simple, and can be done through this command in a terminal. For this set of instructions, we're going to clone KIPP into the home (~) directory.
```
cd ~
git clone https://github.com/LockdownDoom/KIPP
```
This will clone this repository into a directory named `KIPP` in `~`.
#### Step 2: Setting the `KIPP_DIR` environment variable
KIPP depends upon an environment variable named `KIPP_DIR` in order to know where his repository is stored on your machine. You can set this variable temporarily with this command:
```
export KIPP_DIR=/path/to/KIPP
```
In order to set this variable permanently, add this line to the file `/etc/environment`.
```
KIPP_DIR=/path/to/KIPP
```
#### Step 3: Running KIPP
KIPP automatically checks for the status of his dependencies during start-up, so there is no need to install these manually. To run KIPP, simply open a terminal and use this command.
```
cd ~/KIPP
python3 ./Python/KIPP_MONITOR.py
```
This will start up and run KIPP. This monitor program will restart KIPP if any unexpected network/server errors occur or if KIPP crashes. If it is necessary to run KIPP with `sudo`, make sure to spacify sudo's `-E` flag in order to pass the `KIPP_DIR` variable to KIPP.
#### OPTIONAL: Run KIPP as a Linux daemon
The previous steps are all that is necessary to get KIPP running, but this step is also useful. Setting KIPP up as a Linux daemon will make him start up and run in the background of the machine he is installed on. This is obviously a good idea when running KIPP from a Raspberry Pi since KIPP will run from when it starts up to when it shuts down.

First, you must create the `KIPP.service` file in the `/lib/systemd/system` directory.
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
Environment="KIPP_DIR=/path/to/KIPP"
Type=simple
ExecStart=sudo -E /bin/bash -c 'exec $KIPP_DIR/Python/KIPP_MONITOR.py'
Restart=always
RestartSec=0

[Install]
WantedBy=multi-user.target
```
After creating the `KIPP.service` file, you may choose to have KIPP's daemon run non-stop and start on bootup, or use full manual control over it. In order to activate the former, run this command:
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
