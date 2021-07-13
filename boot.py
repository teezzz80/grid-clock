import gc
import machine
import network
import senko
import secrets
from neopixel import NeoPixel
from constants import *


def connect_wlan(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(True)
    ap_if.active(False)

    if not sta_if.isconnected():
        print("Connecting to WLAN ({})...".format(ssid))
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass

    return True


def main():
    """Main function. Runs after board boot, before main.py
    Connects to Wi-Fi and checks for latest OTA version.
    """

    gc.collect()
    gc.enable()

    led_pin = machine.Pin(27, machine.Pin.OUT)
    np = NeoPixel(led_pin, 1)
    np[0] = (255, 0, 0)

    if USE_SENKO:
        np[0] = (0, 255, 0)
        connect_wlan(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        
        OTA = senko.Senko(
            user="teezzz80",
            repo="grid-clock",
            files=[
                "main.py",
                "lib/constants.py",
                "lib/nettime.py",
                "lib/grid_display.py",
                "lib/grid_col.py",
                "lib/grid_pixel.py",
                "lib/senko.py",
                "lib/urequests.py",
            ]
        )

        if OTA.update():
            print("Updated to the latest version! Rebooting...")
            machine.reset()

    np[0] = (0, 0, 255)

if __name__ == "__main__":
    main()