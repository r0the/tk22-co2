import machine

CENTER = 0
DOWN = 1
LEFT = 2
RIGHT = 3
UP = 4

# Platine
_PINS = [39, 32, 33, 34, 36]

# Kabel
# _PINS = [32, 39, 34, 36, 33]
_COUNT = len(_PINS)

_pins = []
_current = [False] * 5
_last = [False] * 5
for pin in _PINS:
    _pins.append(machine.Pin(pin, machine.Pin.IN))

def _pressed(button):
    return _current[button] and not _last[button]

def any():
    for i in range(_COUNT):
        if _current[i]:
            return True
    return False

def any_pressed():
    for i in range(_COUNT):
        if _pressed(i):
            return True
    return False

def center():
    return _current[CENTER]

def center_pressed():
    return _pressed(CENTER)

def down():
    return _current[DOWN]

def down_pressed():
    return _pressed(DOWN)

def left():
    return _current[LEFT]

def left_pressed():
    return _pressed(LEFT)

def right():
    return _current[RIGHT]

def right_pressed():
    return _pressed(RIGHT)

def up():
    return _current[UP]

def up_pressed():
    return _pressed(UP)

def update():
    for i in range(_COUNT):
        _last[i] = _current[i]
        _current[i] = not _pins[i].value()
