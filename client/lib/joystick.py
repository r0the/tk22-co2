import machine

class Joystick:
    def __init__(self):
        self.center_pin = machine.Pin(32, machine.Pin.IN)
        self.down_pin = machine.Pin(39, machine.Pin.IN)
        self.left_pin = machine.Pin(34, machine.Pin.IN)
        self.right_pin = machine.Pin(36, machine.Pin.IN)
        self.up_pin = machine.Pin(33, machine.Pin.IN)
        self.center_current = False
        self.center_last = False
        self.down_current = False
        self.down_last = False
        self.left_current = False
        self.left_last = False
        self.right_current = False
        self.right_last = False
        self.up_current = False
        self.up_last = False
    
    def any(self):
        return self.center_current or self.down_current or self.left_current or self.right_current or self.up_current

    def any_pressed(self):
        return self.center_pressed() or self.down_pressed() or self.left_pressed() or self.right_pressed() or self.up_pressed()

    def center(self):
        return self.center_current

    def center_pressed(self):
        return self.center_current and not self.center_last

    def down(self):
        return self.down_current

    def down_pressed(self):
        return self.down_current and not self.down_last

    def left(self):
        return self.left_current

    def left_pressed(self):
        return self.left_current and not self.left_last

    def right(self):
        return self.right_current

    def right_pressed(self):
        return self.right_current and not self.right_last

    def up(self):
        return self.up_current

    def up_pressed(self):
        return self.up_current and not self.up_last

    def update(self):
        self.center_last = self.center_current
        self.down_last = self.down_current
        self.left_last = self.left_current
        self.right_last = self.right_current
        self.up_last = self.up_current

        self.center_current = not self.center_pin.value()
        self.down_current = not self.down_pin.value()
        self.left_current = not self.left_pin.value()
        self.right_current = not self.right_pin.value()
        self.up_current = not self.up_pin.value()
