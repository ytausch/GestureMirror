import smbus
import time

from gesturemirror.display_switcher import DisplaySwitcher
from gesturemirror.gesture_controller import GestureController
from gesturemirror.gesture_sensor import GestureSensor
from gesturemirror.sonos_controller import SonosController

I2C_PORT = 1

# the rotation of the APDS9960 sensor (counter-clockwise, in degrees)
ROTATION = 180
SONOS_IP = "192.168.2.10"   # set your Sonos IP here

RADIO_URL = "SET_YOUR_RADIO_URL_HERE"
RADIO_TITLE = "SET_YOUR_RADIO_TITLE_HERE"


def main():
    i2c = smbus.SMBus(I2C_PORT)
    sensor = GestureSensor(i2c, ROTATION)
    gesture_controller = GestureController(sensor)

    display = DisplaySwitcher()
    sonos = SonosController(SONOS_IP)

    def play_radio():
        sonos.play_uri(RADIO_URL, RADIO_TITLE, force_radio=True)

    gesture_controller.register_gesture_action(GestureSensor.GESTURE_UP, lambda: display.turn_on())
    gesture_controller.register_gesture_action(GestureSensor.GESTURE_LEFT, play_radio)
    gesture_controller.register_gesture_action(GestureSensor.GESTURE_RIGHT, lambda: sonos.stop())

    while True:
        gesture_controller.update()
        display.timeout_update()
        time.sleep(0.5)


if __name__ == '__main__':
    main()
