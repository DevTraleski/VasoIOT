#! /usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.IN, pull_up_down = gpio.PUD_DOWN)

while True:
	print("GPIO 4: {}".format(gpio.input(4)))
	time.sleep(1.5)

gpio.cleanup()
exit()
