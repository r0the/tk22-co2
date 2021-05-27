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

segment_length = 15
segment_width = 2

res = machine.Pin(5)
dc = machine.Pin(4)
cs = machine.Pin(0)
sck = machine.Pin(18)
mosi = machine.Pin(23)
miso = machine.Pin(19)
spi = machine.SPI(1, sck=sck, mosi=mosi, miso=miso)

krispplay = sh1106.SH1106_SPI(128, 64, spi, dc, res, cs)
krispplay.rotate(True)

def startup(version, product):
    clear()
    y = hoehe // 2 - 18
    text_center("TK22", y)
    text_center("CO2-Messgeraet", y + 10)
    text_center("v" + version, y + 20)
    text_center(product, y + 30)
    krispplay.show()
    time.sleep(2.5)
    clear()
    show()

def text_center(text, y):
    krispplay.text(text, (breite - len(text) * 8) // 2, y)

def show():
    krispplay.show()

def clear():
    krispplay.fill(0)

def draw_segment(x, y, digit):
    w = segment_width
    l = segment_length
    krispplay.rect(x, y + 2 * w + l, w, l, digit[0])
    krispplay.rect(x, y + w, w, l, digit[1])
    krispplay.rect(x + w, y, l, w, digit[2])
    krispplay.rect(x + w + l, y + w, w, l, digit[3])
    krispplay.rect(x + w + l, y + 2 * w + l, w, l, digit[4])
    krispplay.rect(x + w, y + 2 * (w + l), l, w, digit[5])
    krispplay.rect(x + w, y + w + l, l, w, digit[6])

def draw_segments(number, x):
    y = 10
    number = int(number)
    while number > 0:
        draw_segment(x, y, digit[number % 10])
        x = x - segment_length - 4 * segment_width
        number = number // 10

def draw_menuline(text, pos, selected, amount):
    l = len(text) * 8
    krispplay.text(text, (breite - l) // 2, hoehe // (amount + 1) * pos + 4)
    if selected:
        krispplay.rect((breite - l) // 2 - 4, hoehe // (amount + 1) * pos, l + 8, 16, 1)

def run_stupid_user(jetzt, expire, stupid_user):
    if stupid_user and utime.ticks_diff(jetzt, expire) <= 0:
        clear()
        y = hoehe // 2 - 19
        text_center("stupid User", y)
        text_center("Exception,", y + 10)
        text_center("chosen option", y + 20)
        text_center("not accepted", y + 40)
