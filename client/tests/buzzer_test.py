import machine
import utime

_buzzer_pin = machine.Pin(26, machine.Pin.OUT)
_buzzer_pwm = machine.PWM(_buzzer_pin)
_buzzer_pwm.freq(440)
_buzzer_pwm.duty(1)
utime.sleep(1)
_buzzer_pwm.deinit()
