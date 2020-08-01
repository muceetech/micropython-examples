from machine import Pin
from time import sleep
sw = Pin(5,Pin.IN,Pin.PULL_UP)
led = Pin(16, Pin.OUT)
while True:
  if sw.value() == 0:
      led.value(not led.value())
      sleep(0.5)
