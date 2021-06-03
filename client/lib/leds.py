import machine
import lib.joystick as joystick
import utime

grenzwert_rot = 1200
unterschwelle_rot = grenzwert_rot * 0.9
grenzwert_gelb = 850
unterschwelle_gelb = grenzwert_gelb * 0.9

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

def update_color(co2, state):
    if grenzwert_gelb <= co2 and state == 0:
        color = 1
        return color
    if grenzwert_rot <= co2 and state == 1:
        color = 2
        return color
    if unterschwelle_rot > co2 and state == 2:
        color = 1
        return color
    if unterschwelle_gelb > co2 and state == 1:
        color = 0
        return color
    return state

def update_grenzwerte():
    global grenzwert_rot, grenzwert_gelb
    if joystick.up():
        grenzwert_rot += 1
    if joystick.down():
        grenzwert_rot -= 1
        if grenzwert_gelb >= 0.8 * grenzwert_rot:
            grenzwert_gelb = int(0.8 * grenzwert_rot)
    if grenzwert_rot < 500:
        grenzwert_rot = 500
    if grenzwert_rot > 2000:
        grenzwert_rot = 2000
    if joystick.right():
        grenzwert_gelb += 1
        if grenzwert_gelb >= 0.8*grenzwert_rot:
            grenzwert_rot = int(grenzwert_gelb / 0.8)
    if joystick.left():
        grenzwert_gelb -= 1
    if grenzwert_gelb < 400:
        grenzwert_gelb = 400
    if grenzwert_gelb > 1600:
        grenzwert_gelb = 1600
        
def update_unterschwellen():
    global unterschwelle_rot, unterschwelle_gelb
    unterschwelle_gelb = grenzwert_gelb * 0.9
    unterschwelle_rot = grenzwert_rot * 0.9

