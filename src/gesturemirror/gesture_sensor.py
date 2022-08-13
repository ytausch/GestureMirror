import apds9960
import smbus
from apds9960.const import APDS9960_DIR_NONE, APDS9960_DIR_UP, APDS9960_DIR_DOWN, APDS9960_DIR_LEFT, APDS9960_DIR_RIGHT, \
    APDS9960_DIR_NEAR, APDS9960_DIR_FAR


class GestureSensor:
    NO_GESTURE = APDS9960_DIR_NONE
    GESTURE_UP = APDS9960_DIR_UP
    GESTURE_DOWN = APDS9960_DIR_DOWN
    GESTURE_LEFT = APDS9960_DIR_LEFT
    GESTURE_RIGHT = APDS9960_DIR_RIGHT
    GESTURE_NEAR = APDS9960_DIR_NEAR
    GESTURE_FAR = APDS9960_DIR_FAR

    def __init__(self, bus: smbus.SMBus, rotation: int = 0):
        """
        Initializes the gesture sensor.
        :param bus: The bus to use for the sensor.
        :param rotation: Rotation of the device, in degrees (counter-clockwise with sensor facing towards you).
        Only multiples of 90 degrees make sense here. Defaults to 0.
        """
        self.device = apds9960.APDS9960(bus)
        self.device.enableGestureSensor()
        self.rotation = rotation

    def gesture(self):
        """
        Reads the gesture from the sensor and applies the rotation.
        :return: The gesture.
        """
        gesture = self.device.readGesture()

        rotation_gestures = [self.GESTURE_UP, self.GESTURE_LEFT, self.GESTURE_DOWN, self.GESTURE_RIGHT]
        if gesture in rotation_gestures:
            index = rotation_gestures.index(gesture)
            return rotation_gestures[(index + self.rotation // 90) % 4]

        # no rotation necessary
        return gesture
