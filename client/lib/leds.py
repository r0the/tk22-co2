import machine
import utime

_green_pin = machine.Pin(27, machine.Pin.OUT)
_yellow_pin = machine.Pin(14, machine.Pin.OUT)
_red_pin = machine.Pin(13, machine.Pin.OUT)

def startup():
    for i in range(3):
        update(i)
        utime.sleep(1)

def update(state):
    _green_pin.value(state == 0)
    _yellow_pin.value(state == 1)
    _red_pin.value(state == 2)
