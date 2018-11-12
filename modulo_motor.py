#! /usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.OUT)

while True:
	gpio.output(4, 0)
	print("GPIO 4 set to 0")
	time.sleep(1)
	gpio.output(4, 1)
	print("GPIO 4 set to 1")
	time.sleep(1)

gpio.cleanup()
exit()
