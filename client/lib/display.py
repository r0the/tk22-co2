import sh1106
import machine
import lib.joystick as joystick
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

sleeptime = 30_000

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
    show()
    
def text(string, x, y):
    krispplay.text(string, x, y)

def text_center(string, y):
    text(string, (breite - len(string) * 8) // 2, y)
    
def text_rightbound(string, y):
    text(string, breite - 8 * len(string) - 4, y)
    
def text_leftbound(string, y):
    text(string, 4, y)
    
def rect(x, y, length, height, color):
    krispplay.rect(x, y, length, height, color)

def show():
    krispplay.show()

def clear():
    krispplay.fill(0)

def draw_segment(x, y, digit):
    w = segment_width
    l = segment_length
    rect(x, y + 2 * w + l, w, l, digit[0])
    rect(x, y + w, w, l, digit[1])
    rect(x + w, y, l, w, digit[2])
    rect(x + w + l, y + w, w, l, digit[3])
    rect(x + w + l, y + 2 * w + l, w, l, digit[4])
    rect(x + w, y + 2 * (w + l), l, w, digit[5])
    rect(x + w, y + w + l, l, w, digit[6])

def draw_segments(number, x):
    y = 10
    number = int(number)
    while number > 0:
        draw_segment(x, y, digit[number % 10])
        x = x - segment_length - 4 * segment_width
        number = number // 10

def draw_menuline(string, pos, selected, amount):
    l = len(string) * 8
    real_y = hoehe // amount * pos + (hoehe//amount - 8) // 2
    text(string, (breite - l) // 2, real_y)
    if selected:
        rect((breite - l) // 2 - 4, real_y - 4, l + 8, 16, 1)
        
def about(standalone, product, production_number, version, y):
    clear()
    text_center("" + product, y)
    text_center("v" + version, y + 10)
    if standalone:
        text_center("standalone", y + 20)
    else:
        text_center("online", y + 20)
    text_center("product" + production_number, y + 30)
    text_center("by TK22", y + 40)
    text_center("Gymer Chilefeld", y + 50)
    
def reset():
    clear()
    text_center('resetting...', hoehe // 2 - 4)
    show()
    
def update_sleeptime():
    global sleeptime
    if joystick.up():
        sleeptime += 1000
    if joystick.down():
        sleeptime -= 1000
    if sleeptime < 10000:
        sleeptime = 10000
    if sleeptime > 120000:
        sleeptime = 120000
