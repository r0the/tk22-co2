import machine
import utime

_buzzer_pin = machine.Pin(26, machine.Pin.OUT)
_buzzer_pwm = None

melody_index = 7
melody = "melody/melody" + str(melody_index) + ".txt"
melody_file = None

melodies_text = ["Axel F", "Drunken Sailor", "Stayin' Alive", "Counting Stars", "Wahn-Sing", "Rasputin", "Coffin Dance", "Pieps"]

jetzt = utime.ticks_ms()
wecker_utime = jetzt

speed = 60

B = 2 ** (1 / 12)
A = 220
def tone_to_frequency(tone):
    return int(A * (B ** (int(tone[0]) + 3)))

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

def update_buzzer(element):
    play_tone(element)

def play_tone(tone):
    if int(tone[2]) == 0:
        buzzer_off()
    else:
        buzzer_play(tone_to_frequency())

def update_melody(state, activated, play, last_play, stupid_user, melody_index, melody_changed):
    global wecker_utime
    global speed
    global melody_file
    jetzt = utime.ticks_ms()
    melody="melody/melody" + str(melody_index) + ".txt"
    
    if melody_changed:
        melody_file = None
    if not last_play and play:
        buzzer_off()
    if not melody_file:
        melody_file = open(melody, "r")
    
    if state != 2 or not play or not activated and not stupid_user:
        buzzer_off()
    if utime.ticks_diff(wecker_utime, jetzt) <= 0 and play and state == 2 and activated:
        element = melody_file.readline()
        element = element.replace('\n', '')
        element = element.split(' ')
        if element == ['']:
            melody_file.close()
            melody_file = None
        else:
            if len(element) == 3:
                update_buzzer(element)    
                wecker = round(float(element[1]) * 1000 * 60) // speed
                wecker_utime = utime.ticks_add(jetzt, wecker)
            elif len(element) == 1:
                speed = int(element[0])
                wecker = 0
                wecker_utime = utime.ticks_add(jetzt, wecker)
