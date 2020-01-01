import RPi.GPIO as gpio
import time

def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(20, gpio.OUT)
 gpio.setup(26, gpio.OUT)

def forward(tf):
 init()
 gpio.output(20, True)
 gpio.output(26, False)
 time.sleep(tf)
 gpio.cleanup()

def reverse(tf):
 init()
 gpio.output(20, False)
 gpio.output(26, True)
 time.sleep(tf)
 gpio.cleanup()

print "forward"
forward(7)
print "backward"
reverse(3)
