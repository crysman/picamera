# pypicamera
a python script for a timelapse video - capturing JPEG stills every N sec
(using Raspberry Pi camera module) https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

to start automatically every (re)boot, ssh into RPi and

1. make a symlink into /etc/systemd:

       sudo ln -s ~/pypicamera/pypicamera.service /etc/systemd/system/pypicamera.service. 

2. test it:

       sudo systemctl restart pypicamera.service

3. if working properly, make it autostart:

       sudo systemctl enable pypicamera

crysman (copyleft) 2018-2019
