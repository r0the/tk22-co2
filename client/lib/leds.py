import machine

class Leds:
    def __init__(self):
        self.green = machine.Pin(27, machine.Pin.OUT)
        self.yellow = machine.Pin(14, machine.Pin.OUT)
        self.red = machine.Pin(13, machine.Pin.OUT)

    def update(self, state):
        self.green.value(state == 0)
        self.yellow.value(state == 1)
        self.red.value(state == 2)
