import machine

green = machine.Pin(27, machine.Pin.OUT)
yellow = machine.Pin(14, machine.Pin.OUT)
red = machine.Pin(13, machine.Pin.OUT)

def update_led(state):
    green.value(state == 0)
    yellow.value(state == 1)
    red.value(state == 2)
    
def update_light(co2, state, grenzwert_rot, grenzwert_gelb, unterschwelle_rot, unterschwelle_gelb):
    if grenzwert_gelb<=co2 and state==0:
        state=1
    if grenzwert_rot<=co2 and state==1:
        state=2
    if unterschwelle_rot>co2 and state==2:
        state=1
    if unterschwelle_gelb>co2 and state==1:
        state=0
    return state
