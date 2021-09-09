import esp
import esp32
import network
import urequests
import utime

_wlan = network.WLAN(network.STA_IF)

_wlan_settings = open('lib/wlan_settings.txt')
_SSID = _wlan_settings.readline().replace('\n', '')
_password = _wlan_settings.readline().replace('\n', '')
_wlan_settings.close()

_wait = utime.ticks_ms()
_interval = 10_000

def do_connect():
    _wlan.active(True)
    if not _wlan.isconnected():
        _wlan.connect(_SSID, _password)
        while not _wlan.isconnected():
            pass

def send(identity, data):
    print("https://informatik.mygymer.ch/co2/u.php?i=" + identity + "&d=" + data)
    try:
        _res = urequests.get("https://informatik.mygymer.ch/co2/u.php?i=" + identity + "&d=" + data)
        _res.close()
    except OSError:
        pass

def data_stream(identity, data, jetzt):
    global _wait
    if utime.ticks_diff(jetzt, _wait)>=0:
        _wait=utime.ticks_add(jetzt, _interval)
        send(identity, str(int(data)))
