import time
import smbus

from gesturemirror.gesture_sensor import GestureSensor

I2C_PORT = 1
ROTATION = 180


def main():
    i2c = smbus.SMBus(I2C_PORT)
    sensor = GestureSensor(i2c, ROTATION)
    while True:
        gesture = sensor.gesture()
        if gesture == GestureSensor.GESTURE_UP:
            print("Up")
        elif gesture == GestureSensor.GESTURE_DOWN:
            print("Down")
        elif gesture == GestureSensor.GESTURE_LEFT:
            print("Left")
        elif gesture == GestureSensor.GESTURE_RIGHT:
            print("Right")
        time.sleep(0.5)


if __name__ == '__main__':
    main()
