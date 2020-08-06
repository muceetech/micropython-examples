import tm1637
from machine import Pin
import time
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(0))

# dim
tm.brightness(5)

# 1234
tm.number(1234)
time.sleep(5)

# help
tm.show('help')
