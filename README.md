# picamera
a python script for a timelapse video - capturing JPEG stills every N sec
(using Raspberry Pi camera module) https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

to start automatically every (re)boot, make a symlink into /etc/systemd:

    sudo ln -s ~/camera.service /etc/systemd/system/camera.service

crysman (copyleft) 2018-10
