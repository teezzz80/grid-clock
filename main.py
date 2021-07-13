from machine import Pin, RTC
from neopixel import NeoPixel
from nettime import NetTime
import time, utime
from grid_display import GridDisplay
from grid_col import GridCol
from grid_pixel import GridPixel
from constants import *
from secrets import *


def get_datetime_element(datetime, element):
    return list(datetime)[DATETIME_ENUM[element]]

    
def display_clock(datetime):
    if not is_display_off:
        render_time(datetime, False)


def render_time(datetime, force):
    hour = get_datetime_element(datetime, "hour")
    minute = get_datetime_element(datetime, "minute")
    if hour != last_hour or minute != last_minute:
        display.off()
        last_hour = hour
        last_minute = minute
        (upper_hour, lower_hour) = divmod(hour, 10)
        (upper_minute, lower_minute) = divmod(minute, 10)
        if upper_hour != 0:
            display.pattern(0, 0, TIME_FONT[upper_hour], COLORS["orange"])
        display.pattern(4, 0, TIME_FONT[lower_hour], COLORS["orange"])
        display.pattern(0, 6, TIME_FONT[upper_minute], COLORS["orange"])
        display.pattern(4, 6, TIME_FONT[lower_minute], COLORS["orange"])


try:
    is_display_off = False
    last_hour = None
    last_minute = None

    n = 83
    np_pin = Pin(25, Pin.OUT)
    np = NeoPixel(np_pin, n)
    col0 = GridCol([GridPixel(np, 0), GridPixel(np, 1), GridPixel(np, 2), GridPixel(np, 3), GridPixel(np, 4), GridPixel(np, 5), GridPixel(np, 6), GridPixel(np, 7), GridPixel(np, 8), GridPixel(np, 9), GridPixel(np, 10)])
    col1 = GridCol([GridPixel(np, 23), GridPixel(np, 22), GridPixel(np, 21), GridPixel(np, 20), GridPixel(np, 19), GridPixel(np, 18), GridPixel(np, 17), GridPixel(np, 16), GridPixel(np, 15), GridPixel(np, 14), GridPixel(np, 13)])
    col2 = GridCol([GridPixel(np, 24), GridPixel(np, 25), GridPixel(np, 26), GridPixel(np, 27), GridPixel(np, 28), GridPixel(np, 29), GridPixel(np, 30), GridPixel(np, 31), GridPixel(np, 32), GridPixel(np, 33), GridPixel(np, 34)])
    col3 = GridCol([GridPixel(np, 47), GridPixel(np, 46), GridPixel(np, 45), GridPixel(np, 44), GridPixel(np, 43), GridPixel(np, 42), GridPixel(np, 41), GridPixel(np, 40), GridPixel(np, 39), GridPixel(np, 38), GridPixel(np, 37)])
    col4 = GridCol([GridPixel(np, 48), GridPixel(np, 49), GridPixel(np, 50), GridPixel(np, 51), GridPixel(np, 52), GridPixel(np, 53), GridPixel(np, 54), GridPixel(np, 55), GridPixel(np, 56), GridPixel(np, 57), GridPixel(np, 58)])
    col5 = GridCol([GridPixel(np, 71), GridPixel(np, 70), GridPixel(np, 69), GridPixel(np, 68), GridPixel(np, 67), GridPixel(np, 66), GridPixel(np, 65), GridPixel(np, 64), GridPixel(np, 63), GridPixel(np, 62), GridPixel(np, 61)])
    col6 = GridCol([GridPixel(np, 72), GridPixel(np, 73), GridPixel(np, 74), GridPixel(np, 75), GridPixel(np, 76), GridPixel(np, 77), GridPixel(np, 78), GridPixel(np, 79), GridPixel(np, 80), GridPixel(np, 81), GridPixel(np, 82)])
    display = GridDisplay([col0, col1, col2, col3, col4, col5, col6])

    display.off()
    display.set_brightness(BRIGHTNESS)

    nt = NetTime(WIFI_SSID, WIFI_PASSWORD)
    rtc = RTC()
    now = None
    update_time = utime.time() - WEB_QUERY_DELAY  # always sync time on start

    while True:
        if utime.time() - update_time >= WEB_QUERY_DELAY:
            display.message("Sync")
            netTime = nt.sync_time(API_URL)
            if netTime[0] != "error":
                rtc.datetime(netTime) # update internal rtc time
                update_time = utime.time()
            else:
                display.message("Err")
                update_time = utime.time() - WEB_QUERY_DELAY + RETRY_DELAY
        
        now = rtc.datetime()

        display_clock(now)

        time.sleep_ms(REFRESH_DELAY)

except:
    status_pin = Pin(27, Pin.OUT)
    status_led = NeoPixel(status_pin, 1)
    status_led[0] = (255, 0, 0)
    status_led.write()
