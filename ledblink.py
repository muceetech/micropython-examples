from machine import Pin
import time
 

p0 = Pin(16, Pin.OUT)    # create output pin on GPIO16
while True:
    p0.on()                 # set pin to "on" (high) level
    time.sleep(1)
    p0.off()                # set pin to "off" (low) level
    time.sleep(1)
