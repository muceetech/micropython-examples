from machine import Pin, I2C
import ssd1306
import network
import urequests
import ntptime
import time

#ESP32-C3  Xiao Board Pin assignment for SSD 1306 OLED 3.3V
i2c = I2C(scl=Pin(7), sda=Pin(6))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Configuration
WIFI_SSID = 'ssid'
WIFI_PASS = 'password'

# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    time.sleep(0.5)

ntptime.host = 'time.nplindia.org'  # ntp server

ntptime.settime()

# Convert UTC to IST (+5:30)
def get_ist_time():
    return time.localtime(time.time() + 19800)

def format_time_str(t):
    return "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5])

while True:
    t = get_ist_time()
    oled.fill(0)
    oled.text("Time:", 0, 0)
    oled.text(format_time_str(t), 0, 15)
    oled.text("{:02d}/{:02d}/{}".format(t[2], t[1], t[0]), 0, 30)  # DD/MM/YYYY
    oled.show()
    time.sleep(1)



