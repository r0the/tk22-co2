import machine

CENTER = 0
DOWN = 1
LEFT = 2
RIGHT = 3
UP = 4

PINS = [32, 39, 34, 36, 33]
COUNT = len(PINS)


class Joystick:
    def __init__(self):
        self.pin = []
        self.current = [False] * 5
        self.last = [False] * 5
        for pin in PINS:
            self.pin.append(machine.Pin(pin, machine.Pin.IN))
    
    def pressed(self, button):
        return self.current[button] and not self.last[button]

    def any(self):
        for i in range(COUNT):
            if self.current[i]:
                return True
        return False

    def any_pressed(self):
        for i in range(COUNT):
            if self.pressed(i):
                return True
        return False

    def center(self):
        return self.current[CENTER]

    def center_pressed(self):
        return self.pressed(CENTER)

    def down(self):
        return self.current[DOWN]

    def down_pressed(self):
        return self.pressed(DOWN)

    def left(self):
        return self.current[LEFT]

    def left_pressed(self):
        return self.pressed(LEFT)

    def right(self):
        return self.current[RIGHT]

    def right_pressed(self):
        return self.pressed(RIGHT)

    def up(self):
        return self.current[UP]

    def up_pressed(self):
        return self.pressed(UP)

    def update(self):
        for i in range(COUNT):
            self.last[i] = self.current[i]
            self.current[i] = not self.pin[i].value()
