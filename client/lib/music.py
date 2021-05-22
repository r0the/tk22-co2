import machine
import utime

_buzzer_pin = machine.Pin(26, machine.Pin.OUT)
_buzzer_pwm = None

_last_play = True
_melody_file = None

melody_index = 7
melodies_text = ["Axel F", "Drunken Sailor", "Stayin' Alive", "Counting Stars", "Wahn-Sing", "Rasputin", "Coffin Dance", "Pieps"]
play = True

_tempo = 60
_timer = 0

B = 2 ** (1 / 12)
A = 220
def tone_to_frequency(tone):
    return int(A * (B ** (int(tone) + 3)))

def buzzer_off():
    global _buzzer_pwm
    if _buzzer_pwm:
        _buzzer_pwm.deinit()
        _buzzer_pwm = None

def buzzer_play(freq):
    global _buzzer_pwm
    if not _buzzer_pwm:
        _buzzer_pwm = machine.PWM(_buzzer_pin)
    _buzzer_pwm.freq(freq)
    _buzzer_pwm.duty(1)

def play_tone(tone):
    if int(tone[2]) == 0:
        buzzer_off()
    else:
        buzzer_play(tone_to_frequency(tone[0]))

def update_melody(state, activated, stupid_user, melody_index, melody_changed):
    global _last_play
    global _melody_file
    global _tempo
    global _timer

    now = utime.ticks_ms()

    if melody_changed:
        _melody_file = None
    if not _last_play and play:
        buzzer_off()
    _last_play = play
    if not _melody_file:
        file_name = "melody/melody" + str(melody_index) + ".txt"
        _melody_file = open(file_name, "r")
    if state != 2 or not play or not activated and not stupid_user:
        buzzer_off()
    if utime.ticks_diff(_timer, now) <= 0 and play and state == 2 and activated:
        element = _melody_file.readline()
        element = element.replace('\n', '')
        element = element.split(' ')
        if element == ['']:
            _melody_file.close()
            _melody_file = None
        else:
            if len(element) == 3:
                play_tone(element)    
                duration = round(float(element[1]) * 1000 * 60) // _tempo
                _timer = utime.ticks_add(now, duration)
            elif len(element) == 1:
                _tempo = int(element[0])
                _timer = now
