# a python script for a timelapse video - capturing JPEG stills every N sec
# (using Raspberry Pi camera module) https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
# to start automatically every (re)boot, make a symlink into /etc/systemd:
#   sudo ln -s ~/camera.service /etc/systemd/system/camera.service
# crysman (copyleft) 2018-10

import picamera
import time
import os

delay = 10
quality = 21


if not os.path.exists("camimages"):
    os.makedirs("camimages")

with picamera.PiCamera() as camera:

    #https://picamera.readthedocs.io/en/release-1.9/recipes1.html#capturing-consistent-images
    # Wait for analog gain to settle on a higher value than 1
    if False:
        while camera.analog_gain <= 1:
            time.sleep(0.1)
        # Now fix the values
        camera.shutter_speed = camera.exposure_speed
        camera.exposure_mode = 'off'
        g = camera.awb_gains
        camera.awb_mode = 'off'
        camera.awb_gains = g

    #custom parameters:
    camera.rotation = 180
    camera.sharpness = 100
    camera.resolution = (2592, 1944) #higher res not available :/
    #camera.resolution = (3280, 2464) #(cam v2 ONLY!)

    #let's capture continuously:
    camera.start_preview()
    time.sleep(2)
    for filename in camera.capture_continuous('camimages/{timestamp:%Y%m%d%H%M%S}.jpg',format='jpeg',quality=quality):
        print("%s captured, sleeping %i sec.." % (filename,delay))
        time.sleep(delay)
