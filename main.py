from machine import Pin, RTC
from neopixel import NeoPixel
from nettime import NetTime
import time, utime
from grid_display import GridDisplay
from constants import *
from secrets import *


def get_datetime_element(datetime, element):
    return list(datetime)[DATETIME_ENUM[element]]

    
def display_clock(datetime):
    if not is_display_off:
        render_time(datetime)
        display.on()


def render_time(datetime):
    display.clear()
    hour = get_datetime_element(datetime, "hour")
    minute = get_datetime_element(datetime, "minute")
    (upper_hour, lower_hour) = divmod(hour, 10)
    (upper_minute, lower_minute) = divmod(minute, 10)
    if upper_hour != 0:
        display.pattern(0, 0, TIME_FONT[upper_hour], COLORS["orange"])
    display.pattern(4, 0, TIME_FONT[lower_hour], COLORS["orange"])
    display.pattern(0, 6, TIME_FONT[upper_minute], COLORS["orange"])
    display.pattern(4, 6, TIME_FONT[lower_minute], COLORS["orange"])


try:
    is_display_off = False

    n = 83
    np_pin = Pin(25, Pin.OUT)
    np = NeoPixel(np_pin, n)
    col0 = [0, 1, 2, 3, 4, 5 ,6, 7, 8, 9, 10]
    col1 = [23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13]
    col2 = [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
    col3 = [47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37]
    col4 = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]
    col5 = [71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61]
    col6 = [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82]
    display = GridDisplay(np, [col0, col1, col2, col3, col4, col5, col6])

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

except Exception as ex:
    print("Exception occured: ", ex)
    status_pin = Pin(27, Pin.OUT)
    status_led = NeoPixel(status_pin, 1)
    status_led[0] = (255, 0, 0)
    status_led.write()

