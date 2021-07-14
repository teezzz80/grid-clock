from machine import Pin, RTC
from neopixel import NeoPixel
from nettime import NetTime
import time, utime
from grid_display import GridDisplay
from constants import *
from secrets import *


def render_time(datetime, force=False):
    global is_display_off, last_hour, last_minute
    hour = NetTime.get_datetime_element(datetime, "hour")
    minute = NetTime.get_datetime_element(datetime, "minute")
    if not is_display_off or hour != last_hour or minute != last_minute or force:
        display.clear()
        (upper_hour, lower_hour) = divmod(hour, 10)
        (upper_minute, lower_minute) = divmod(minute, 10)
        if upper_hour != 0:
            display.pattern(0, 0, NUMBER_FONT[upper_hour], display.get_theme_color(0))
        display.pattern(4, 0, NUMBER_FONT[lower_hour], display.get_theme_color(1))
        display.pattern(0, 6, NUMBER_FONT[upper_minute], display.get_theme_color(2))
        display.pattern(4, 6, NUMBER_FONT[lower_minute], display.get_theme_color(3))
        last_hour = hour
        last_minute = minute
        display.on()


def handle_button1(cycle):
    global is_display_off
    if cycle > 1 and cycle <= 3:
        print("Button1 pressed: toggle display")
        if not is_display_off:
            display.off()
            is_display_off = True
        else:
            render_time(now, True)
            is_display_off = False
    if cycle > 3 and not is_display_off:
        print("Button1 long pressed: decrease brightness")
        display.decrease_brightness()
        render_time(now, True)


def handle_button2(cycle):
    global is_display_off
    if cycle > 1 and cycle <= 3 and not is_display_off:
        print("Button2 pressed: next theme")
        display.next_theme()
        render_time(now, True)
    if cycle > 3 and not is_display_off:
        print("Button2 long pressed: increase brightness")
        display.increase_brightness()
        render_time(now, True)


try:
    is_display_off = False

    n = 83
    np_pin = Pin(25, Pin.OUT)
    np = NeoPixel(np_pin, n)

    button1 = Pin(33, Pin.IN, Pin.PULL_UP)
    button2 = Pin(21, Pin.IN, Pin.PULL_UP)
    button1_cycle = 0
    button2_cycle = 0

    col0 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    col1 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    col2 = [34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24]
    col3 = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
    col4 = [58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48]
    col5 = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
    col6 = [82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72]
    display = GridDisplay(np, [col0, col1, col2, col3, col4, col5, col6])

    display.off()
    display.set_brightness(0.5)

    nt = NetTime(WIFI_SSID, WIFI_PASSWORD)
    rtc = RTC()
    now = None
    update_time = utime.time() - WEB_QUERY_DELAY  # always sync time on start
    last_minute = 0
    last_hour = 0

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

        render_time(now)

        if button1.value() == 0: # button1 is pressed
            button1_cycle += 1
        elif button1.value() == 1 and button1_cycle > 0: # button1 is released
            handle_button1(button1_cycle)
            button1_cycle = 0
        
        if button2.value() == 0: # button2 is pressed
            button2_cycle += 1
        elif button2.value() == 1 and button2_cycle > 0: # button2 is released
            handle_button2(button2_cycle)
            button2_cycle = 0        

        time.sleep_ms(REFRESH_DELAY)

except Exception as ex:
    status_pin = Pin(27, Pin.OUT)
    status_led = NeoPixel(status_pin, 1)
    status_led[0] = (255, 0, 0)
    status_led.write()
    raise
