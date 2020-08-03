import network
import ntptime
from machine import RTC


rtc = RTC()
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('ssid', 'password') # connect to an AP with your ssid and password .change your ssid and password
    ntptime.settime() # set the rtc datetime from the remote server
    while not wlan.isconnected():
        pass
    print('network config:', wlan.ifconfig())

while True:
    a = rtc.datetime()    # get the date and time in UTC
    print(a)
    
