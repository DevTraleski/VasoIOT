import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(20, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(4, gpio.OUT)

gpio.cleanup()
