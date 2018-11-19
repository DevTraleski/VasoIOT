import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.OUT)

gpio.output(4, 1)
time.sleep(5)
gpio.output(4, 0)
gpio.cleanup()
