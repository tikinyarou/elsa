from machine import Pin
from time import sleep_ms
sw = Pin(23,Pin.IN,Pin.PULL_UP)
led = Pin(2,Pin.OUT)
while True:
    if sw.value() == 1:
        led.value(1)
    else:
        led.value(0)
