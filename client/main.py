import machine
import utime
import lib.scd30 as scd30
import lib.joystick as joystick
import lib.display as display
import lib.leds as leds
import lib.music as music

#machine.reset()

#Variablen

breite = 128
hoehe = 64

locked = False
standalone = True

version_text = open('lib/version_text.txt')

version = version_text.readline().replace('\n', '')
product = version_text.readline().replace('\n', '')
production_number = version_text.readline().replace('\n', '')
version_text.close()

i = 0
m = 0
position = 0
index = 0
d = False
setting = 4
s = 0
start = 0
done = False
place = 0

state = 0

jetzt = utime.ticks_ms()
last = utime.ticks_add(jetzt, display.sleeptime)
last_pressed = utime.ticks_add(jetzt, music.alarm_wait)

last_co2 = 0
last_humidity = 0
last_temperatrue = 0

melody_changed = False
highest_index = len(music.melodies_text) - 1
shown = False

#Pin-Belegung

#Sensor
scl = machine.Pin(22)
sda = machine.Pin(21)
i2c = machine.SoftI2C(scl, sda)

#Display
draw_menuline = display.draw_menuline
draw_segment = display.draw_segment
draw_segments = display.draw_segments

#Ziffern
segment_length = 15
segment_width = 2

#Geräte
sensor = scd30.EasySCD30(i2c)
#buzzer_pwm.freq(int(frequency))
#buzzer_pwm.duty(0)

#Ausführung

display.startup(version, product)
# LEDs testen
leds.startup()
display.clear()
display.show()

def read_sensor():
    sensor.read()

def update_state():
    global state
    state = leds.update_color(sensor.co2, state)
    leds.update(state)

"""def check_password(check):
    if not locked:
        return True
    else:
        check = hashing.hash(check)
        if password == check:
            return True
        else:
            return False
    return True"""

def save_config():
    config = open("config.txt", "w")
    parameters = [str(leds.grenzwert_rot), str(leds.grenzwert_gelb), str(music.activated), str(music.melody_index), str(music.alarm_wait), str(display.sleeptime)]
    for p in parameters:
        config.write(p + "\n")
    config.close()

def load_config():
    try:
        config = open("config.txt","r")
        leds.grenzwert_rot = int(config.readline())
        leds.grenzwert_gelb = int(config.readline())
        music.activated = bool(config.readline())
        music.melody_index = int(config.readline())
        music.alarm_wait = int(config.readline())
        display.sleeptime = int(config.readline())
        config.close()
    except OSError:
        pass

while True:
    jetzt = utime.ticks_ms()
    joystick.update()
    read_sensor()
    leds.update_unterschwellen()
    update_state()
    music.update_melody(state, melody_changed)
    melody_changed = False
    
    if joystick.any():
        shown = False

    if i == 0:
        if m > 2:
            m = 0
        if m < 0:
            m = 2
        if joystick.down_pressed():
            m = m + 1
        if joystick.up_pressed():
            m = m - 1
        if joystick.center_pressed() and m == 1:
            i = 2
        if joystick.center_pressed() and m == 2:
            i = 1
        if joystick.center_pressed() and m == 0:
            i = 3
        if joystick.left_pressed() or joystick.right_pressed():
            i = 4
        if not shown:
            display.clear()
            display.text_rightbound('-' + product, hoehe - 12)
            draw_menuline("Luftqualitaet", 0, m == 0, 4)
            draw_menuline("div. Messw.", 1, m == 1, 4)
            draw_menuline("Einstellungen", 2, m == 2, 4)
            shown = True

    elif i == 1:
        if setting == 4:
            if not shown:
                display.clear()
                if not standalone:
                    draw_menuline("Zimmer", 3, s == 3, 4)
                draw_menuline("Grenzwerte", 0, s == 0, 4 - standalone)
                draw_menuline("Alarm", 1, s == 1, 4 - standalone)
                draw_menuline("Zeiten", 2, s == 2, 4 - standalone)
                shown = True
            if s > (3 - standalone):
                s = 0
            if s < 0:
                s = 3 - standalone
            if joystick.down_pressed():
                s += 1
            if joystick.up_pressed():
                s -= 1
            if joystick.center_pressed():
                setting = s
            if joystick.right_pressed() or joystick.left_pressed():
                i = 0
                
        elif setting == 0:
            if not shown:
                display.clear()
                display.text( "Rot: " + str(leds.grenzwert_rot) + " ppm", breite // 2 - 55, 18)
                display.text( "Gelb: " + str(leds.grenzwert_gelb) + " ppm", breite // 2 - 55, 38)
                shown = True
            leds.update_grenzwerte()
            if joystick.center_pressed():
                setting=4
                save_config()
                
        elif setting==1:
            if not shown:
                display.clear()
                draw_menuline("None", 0, position == 0, 3)
                draw_menuline(music.melodies_text[index - 1], 1, position == 1, 3)
                draw_menuline(music.melodies_text[index], 2, position == 2, 3)
                shown = True
            if position > 2:
                position = 2
            if position < 0:
                position = 2
            if joystick.down_pressed():
                position += 1
                if position > 2:
                    index += 1
            if joystick.up_pressed():
                position -= 1
            if index < 0:
                index = highest_index
            if index > highest_index:
                index = 0
            if joystick.center_pressed():
                if position == 0:
                    music.activated = False
                else:
                    music.melody_index = (index + position - 2) % 7
                    music.play = True
                    music.activated = True
                    melody_changed = True
                setting = 4
                i = 0
                save_config()
            if joystick.left_pressed() or joystick.right_pressed():
                setting = 4
                alarm = False
                index = 1
                position = 0
        elif setting == 2:
            display.update_sleeptime()
            music.update_snooze()
            if joystick.center_pressed():
                setting = 4
                save_config()
            y = hoehe // 2 - 9
            if not shown:
                display.clear()
                display.text_center("Sleeptime: " + str(display.sleeptime // 1000) + "s", y)
                display.text_center("Snooze: " + str(music.alarm_wait // 1000) + "s", y + 10)
                shown = True

    elif i == 2:
        humidity = sensor.humidity
        temperature = sensor.temperature
        if last_humidity != int(humidity) or last_temperature != int(temperature) or not shown:
            display.clear()
            display.text("%", 116, 50)
            display.text("C", 2 * segment_length + 6 * segment_width - 4, 50)
            display.text(".", 2 * segment_length + 6 * segment_width - 9, 45)
            draw_segments(round(sensor.humidity), 124 - segment_length - 2 * segment_width)
            draw_segments(round(sensor.temperature), 4 + segment_length + 4 * segment_width)
            shown = True
        last_humidity = int(humidity)
        last_temperature = int(temperature)
        if joystick.any_pressed():
            i = 0
            
    elif i == 3:
        co2 = sensor.co2
        if last_co2 != int(co2) or not shown:
            display.clear()
            draw_segments(round(sensor.co2), 124 - segment_length - 2 * segment_width)
            display.text("ppm CO2", 68, 50)
            shown = True
        last_co2 = int(co2)
        if joystick.any_pressed():
            i = 0
            
    elif i == 4:
        y = hoehe // 2 - 29
        if not shown:
            display.about(standalone, product, production_number, version, y)
            shown = True
        if joystick.any_pressed():
            i = 0
                
    elif i < 0 or i > 4:
        display.clear()
        if not d:
            Zeit=utime.ticks_add(jetzt, 5000)
            d = True
        display.text("ERROR", breite // 2 - 20, hoehe // 2 - 4)
        if utime.ticks_diff(jetzt, Zeit) >= 0:
            i = 0
            d = False
    
    if joystick.any():
        if utime.ticks_diff(jetzt, last) > 0 and i == 3:
            i = 0
        last = utime.ticks_add(jetzt, display.sleeptime)
        if state == 2 and music.play:
            last_pressed = utime.ticks_add(jetzt, music.alarm_wait)
            music.play = False
    if joystick.center_pressed():
        start = utime.ticks_add(jetzt, 50_000)
    if joystick.center() and utime.ticks_diff(jetzt, start) > 0:
        machine.reset()
    if utime.ticks_diff(jetzt, last_pressed) > 0 and not music.play:
        music.play = True
    if utime.ticks_diff(jetzt, last) > 0 and i != 3:
        shown = False
        i = 3
        setting = 4

    if not done:
        load_config()
        done = True

    display.show()
