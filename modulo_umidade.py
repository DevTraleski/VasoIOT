#! /usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.IN, pull_up_down = gpio.PUD_DOWN)

while True:
	if(gpio.input(4) == 1):
		print("Sinal recebido")
	else:
		print("Sem sinal")
	time.sleep(1)

gpio.cleanup()
exit()
