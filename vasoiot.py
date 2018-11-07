#! /usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(17, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(21, gpio.OUT)

waterPumpIsOn = False
while True:
	if(gpio.input(17) == 1):
		#Nivel de agua baixo, alertar usuário

	if(gpio.input(4) == 1):
		print("Nivel de humidade: OK")
		if(waterPumpIsOn == True):
			gpio.output(21, 0)
	else:
		print("Nivel de humidade: BAIXO")
		#Ativar bomba da água
		if(waterPumpIsOn == False):
			gpio.output(21, 1)
	time.sleep(1)

gpio.cleanup()
exit()
