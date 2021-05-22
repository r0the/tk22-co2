import sh1106
import machine
import time
import utime

breite = 128
hoehe = 64

digit = [[1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0, 1, 1],
        [0, 0, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 1],
        [0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1]]

segment_length=15
segment_width=2

res = machine.Pin(5)
dc = machine.Pin(4)
cs = machine.Pin(0)
sck = machine.Pin(18)
mosi = machine.Pin(23)
miso = machine.Pin(19)
spi = machine.SPI(1, sck=sck, mosi=mosi, miso=miso)

krispplay = sh1106.SH1106_SPI(128, 64, spi, dc, res, cs)

def startup(version, product):
    clear()
    y=hoehe//2-18
    text="TK22"
    krispplay.text(text, (breite-len(text)*8)//2, y)
    text="CO2-Messgeraet"
    krispplay.text(text, (breite-len(text)*8)//2, y+10)
    text="v" + version
    krispplay.text(text, (breite-len(text)*8)//2, y+20)
    text=product
    krispplay.text(text, (breite-len(text)*8)//2, y+30)
    krispplay.rotate(True)
    krispplay.show()
    time.sleep(2.5)

    clear()
    krispplay.show()

def clear():
    krispplay.fill(0)

def draw_segment(x, y, digit):
    krispplay.rect(x, y+2*segment_width+segment_length, segment_width, segment_length, digit[0])
    krispplay.rect(x, y+segment_width, segment_width, segment_length, digit[1])
    krispplay.rect(x+segment_width, y, segment_length, segment_width, digit[2])
    krispplay.rect(x+segment_width+segment_length, y+segment_width, segment_width, segment_length, digit[3])
    krispplay.rect(x+segment_width+segment_length, y+2*segment_width+segment_length, segment_width, segment_length, digit[4])
    krispplay.rect(x+segment_width, y+2*(segment_width+segment_length), segment_length, segment_width, digit[5])
    krispplay.rect(x+segment_width, y+segment_width+segment_length, segment_length, segment_width, digit[6])

def draw_segments(number, x):
    y = 10
    number = int(number)
    while number > 0:
        draw_segment(x, y, digit[number % 10])
        x = x - segment_length - 4 * segment_width
        number = number // 10


def draw_menuline(text, pos, selected, amount):
    l = len(text) * 8
    krispplay.text(text, (breite - l) // 2, hoehe // (amount+1) * pos + 4)
    if selected:
        krispplay.rect((breite - l) // 2 - 4, hoehe // (amount+1) * pos, l + 8, 16, 1)

def run_stupid_user(jetzt, expire, stupid_user):
    if stupid_user and utime.ticks_diff(jetzt, expire) <= 0:
        clear()
        text = "stupid User"
        y = hoehe//2 - 19
        krispplay.text(text, (breite-8*len(text))//2, y)
        text="Exception,"
        krispplay.text(text, (breite-8*len(text))//2, y + 10)
        text="chosen option"
        krispplay.text(text, (breite-8*len(text))//2, y + 20)
        text="not accepted"
        krispplay.text(text, (breite-8*len(text))//2, y + 30)

