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
    col0 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    col1 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    col2 = [34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24]
    col3 = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
    col4 = [58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48]
    col5 = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
    col6 = [82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72]
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

