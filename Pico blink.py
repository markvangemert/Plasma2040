"""MicroPython Pico"""
import machine
import time

led = machine.Pin("LED", machine.Pin.OUT)
seconds = 1

while True:
    led.on()
    time.sleep(seconds)
    led.off()
    time.sleep(seconds)
