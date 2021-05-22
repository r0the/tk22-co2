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

version = "0.1.0_off"
product = "proto"
production_number = "000"
locked = False
standalone = True

i = 0
m = 0
position = 0
index = 0
d = False
setting = 4
s = 0
start = 0
done = False
sleeptime = 30_000
alarm_wait = 180_000
activated = True
password = "CA91ACE6F5DC0CC0323B88AA38EA72FA84A874A6"
rooms = ["Zi049", "Zi034", "Zi156"]
entered = ""
look = 0
place = 0
counter = 0
room = rooms[counter]
room_number = room.replace('Zi', '')

grenzwert_rot = 1200
unterschwelle_rot = grenzwert_rot * 0.9
grenzwert_gelb = 850
unterschwelle_gelb = grenzwert_gelb * 0.9

state = 0

jetzt = utime.ticks_ms()
last = utime.ticks_add(jetzt, sleeptime)
last_pressed = utime.ticks_add(jetzt, alarm_wait)

melody_changed=False

stupid_user = False
make_exception = False
expire = jetzt

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
joystick = joystick.Joystick()
krispplay = display.krispplay
sensor = scd30.EasySCD30(i2c)
#buzzer_pwm.freq(int(frequency))
#buzzer_pwm.duty(0)

#Ausführung

display.startup(version, product)
# LEDs testen
leds.startup()
krispplay.fill(0)
krispplay.show()


def StupidUserException():
    global stupid_user
    if make_exception:
        display.run_stupid_user(jetzt, expire, stupid_user)
    if utime.ticks_diff(jetzt, expire) >= 0:
        stupid_user = False

def read_sensor():
    sensor.read()

def update_state():
    global state
    co2 = sensor.co2
    if grenzwert_gelb <= co2 and state == 0:
        state = 1
    if grenzwert_rot <= co2 and state == 1:
        state = 2
    if unterschwelle_rot > co2 and state == 2:
        state = 1
    if unterschwelle_gelb > co2 and state == 1:
        state = 0
    leds.update(state)

def check_password(check):
    if not locked:
        return True
    else:
        check=hashing.hash(check)
        if password==check:
            return True
        else:
            return False
    return True

def save_config():
    config = open("config.txt", "w")
    parameters = [str(grenzwert_rot), str(grenzwert_gelb), str(activated), str(music.melody_index), str(alarm_wait), str(sleeptime)]
    for p in parameters:
        config.write(p + "\n")
    config.close()

def load_config():
    global grenzwert_rot
    global grenzwert_gelb
    global activated
    global alarm_wait
    global sleeptime
    try:
        config = open("config.txt","r")
        lines = []
        for i in config.readlines():
            try:
                lines.append(int(i))
            except ValueError:
                lines.append(bool(i))
        config.close()
        if len(lines) == 6:
            grenzwert_rot = lines[0]
            grenzwert_gelb = lines[1]
            activated = lines[2]
            music.melody_index = lines[3]
            alarm_wait = lines[4]
            sleeptime = lines[5]
    except OSError:
        pass

#buzzer_play(440)
#time.sleep(2)

#print(scd30.SCD30.get_temperature_offset(scd30.SCD30))

while True:
    jetzt = utime.ticks_ms()
    joystick.update()
    read_sensor()
    StupidUserException()
    unterschwelle_gelb = grenzwert_gelb * 0.9
    unterschwelle_rot = grenzwert_rot * 0.9
    update_state()
    music.update_melody(state, activated, stupid_user, melody_changed)
    melody_changed = False

    if i == 0 and not stupid_user:
        krispplay.fill(0)
        krispplay.text(product, 4, 52)
        draw_menuline("Luftqualitaet", 0, m == 0, 3)
        draw_menuline("div. Messw.", 1, m == 1, 3)
        draw_menuline("Einstellungen", 2, m == 2, 3)
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
    elif i == 1 and not stupid_user:
        if setting==4:
            krispplay.fill(0)
            draw_menuline("Grenzwerte", 0, s == 0, 4)
            draw_menuline("Alarm", 1, s == 1, 4)
            draw_menuline("Zeiten", 2, s == 2, 4)
            if not standalone:
                draw_menuline("Zimmer", 3, s == 3, 4)
            else:
                draw_menuline("About", 3, s == 3, 4)
            if s > 3:
                s = 0
            if s < 0:
                s = 2
            if joystick.down_pressed():
                s+=1
            if joystick.up_pressed():
                s-=1
            if joystick.center_pressed():
                setting=s
            if joystick.right_pressed() or joystick.left_pressed():
                i=0
        elif setting==0:
            krispplay.fill(0)
            krispplay.text( "Rot: " + str(grenzwert_rot) + " ppm", breite//2 - 55, 18)
            krispplay.text( "Gelb: " + str(grenzwert_gelb) + " ppm", breite//2 - 55, 38)
            if joystick.up():
                grenzwert_rot = int(grenzwert_rot + 1)
            if joystick.down():
                grenzwert_rot = int(grenzwert_rot - 1)
                if grenzwert_gelb >= 0.8*grenzwert_rot:
                    grenzwert_gelb=int(0.8*grenzwert_rot)
            if grenzwert_rot < 500:
                grenzwert_rot = 500
            if grenzwert_rot > 2000:
                grenzwert_rot = 2000
            if joystick.right():
                grenzwert_gelb = int(grenzwert_gelb + 1)
                if grenzwert_gelb >= 0.8*grenzwert_rot:
                    grenzwert_rot=int(grenzwert_gelb/0.8)
            if joystick.left():
                grenzwert_gelb = int(grenzwert_gelb - 1)
            if grenzwert_gelb < 400:
                grenzwert_gelb = 400
            if grenzwert_gelb > 1600:
                grenzwert_gelb = 1600
            if joystick.center_pressed():
                setting=4
                save_config()
        elif setting==1:
            krispplay.fill(0)
            highest_index = len(music.melodies_text) - 1
            draw_menuline("None", 0, position == 0, 3)
            draw_menuline(music.melodies_text[index - 1], 1, position == 1, 3)
            draw_menuline(music.melodies_text[index], 2, position == 2, 3)
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
                    if make_exception:
                        stupid_user = True
                        activated = True
                        music.play = True
                        expire = utime.ticks_add(jetzt, 50_000)
                    else:
                        activated = False
                else:
                    music.melody_index = (index + position - 2) % 7
                    music.play = True
                    activated = True
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
            krispplay.fill(0)
            text = "Sleeptime: " + str(sleeptime // 1000) + " s"
            y=hoehe // 2 - 9
            krispplay.text(text, (breite - len(text) * 8) // 2, y)
            text = "Snooze: " + str(alarm_wait // 1000) + " s"
            krispplay.text(text, (breite - len(text) * 8) // 2, y + 10)
            if joystick.up():
                sleeptime += 1000
            if joystick.down():
                sleeptime -= 1000
            if sleeptime < 10000:
                sleeptime = 10000
            if sleeptime > 120000:
                sleeptime = 120000
            if joystick.right():
                alarm_wait += 1000
            if joystick.left():
                alarm_wait -= 1000
            if alarm_wait < 10000:
                alarm_wait = 10000
            if alarm_wait > 3600000:
                alarm_wait = 3600000
            if joystick.center_pressed():
                setting = 4
                save_config()
        elif setting == 3:
            if not standalone:
                """if look==0 and locked:
                    krispplay.fill(0)
                    text="password:"
                    coordinate=(breite-8*(len(text)+len(entered)))//2
                    krispplay.text(text, coordinate, hoehe//2 - 4)
                    if joystick.up_pressed():
                        entered+="0"
                    if joystick.right_pressed():
                        entered+="1"
                    if joystick.down_pressed():
                        entered+="2"
                    if joystick.left_pressed():
                        entered+="3"
                    for g in range(len(entered)):
                        krispplay.text("*", coordinate+8*(len(text)+g), hoehe//2 - 4)
                    if joystick.center_pressed():
                        if check_password(entered):
                            look=1
                        else:
                            entered=""
                            setting=4

                else:
                    krispplay.fill(0)
                    if joystick.down_pressed():
                        place+=1
                        if place==2:
                            counter+=1
                    elif joystick.down() and place==2 and len(rooms)>25 and not joystick.down_pressed():
                        counter+=1
                    if joystick.up_pressed():
                        place-=1
                        if place==0:
                            counter-=1
                    elif joystick.up() and place==0 and len(rooms)>25 and not joystick.up_pressed():
                            counter-=1
                    if place<0:
                        place=0
                    if place>2:
                        place=2
                    if counter<0:
                        counter=len(rooms)-1
                    if counter>=len(rooms):
                        counter=0
                    for x in range(3):
                        draw_menuline(rooms[counter+x-2], x, place == x, 3)
                    if joystick.center_pressed():
                        room=rooms[counter-2+place]
                        room_number=int(room.replace('Zi', ''))
                        entered=[]
                        look=0
                        setting=4"""

            else:
                krispplay.fill(0)
                y = hoehe // 2 - 19
                text = 'v' + version
                krispplay.text(text, (breite - len(text) * 8) // 2, y)
                text = 'product' + production_number
                krispplay.text(text, (breite - len(text) * 8) // 2, y + 10)
                text = product
                krispplay.text(text, (breite - len(text) * 8) // 2, y + 20)
                text = "TK22"
                krispplay.text(text, (breite - len(text) * 8) // 2, y + 30)
                if joystick.center_pressed():
                    setting = 4

    elif i == 2 and not stupid_user:
        krispplay.fill(0)
        draw_segments(sensor.humidity, 124 - segment_length - 2*segment_width)
        draw_segments(sensor.temperature, 4 + segment_length + 4*segment_width)
        krispplay.text("%", 116, 50)
        krispplay.text("C", 2*segment_length + 6*segment_width - 4, 50)
        krispplay.text(".", 2*segment_length + 6*segment_width - 9, 45)
        if joystick.any_pressed():
            i = 0
    elif i == 3 and not stupid_user:
        krispplay.fill(0)
        draw_segments(sensor.co2, 124 - segment_length - 2*segment_width)
        krispplay.text("ppm CO2", 68, 50)
        if joystick.any_pressed():
            i = 0
    elif i < 0 or i > 3:
        if not d:
            Zeit=utime.ticks_add(jetzt, 5000)
            d = True
        krispplay.text("ERROR", breite // 2 - 20, hoehe // 2 - 4)
        if utime.ticks_diff(jetzt, Zeit) >= 0:
            i = 0
            d = False
    if joystick.any():
        if utime.ticks_diff(jetzt, last) > 0 and i == 3:
            i = 0
        last=utime.ticks_add(jetzt, sleeptime)
        if state == 2 and music.play:
            last_pressed = utime.ticks_add(jetzt, alarm_wait)
            music.play = False
    if joystick.center_pressed():
        start = utime.ticks_add(jetzt, 50_000)
    if joystick.center() and utime.ticks_diff(jetzt, start) > 0:
        machine.reset()
    if utime.ticks_diff(jetzt, last_pressed) > 0 and not music.play:
        music.play = True
    if utime.ticks_diff(jetzt, last) > 0 and i != 3:
        i=3

    if not done:
        load_config()
        done=True

    krispplay.show()
