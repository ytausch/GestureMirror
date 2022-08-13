from typing import Callable, Any, Dict

from gesturemirror.gesture_sensor import GestureSensor


class GestureController:
    def __init__(self, gesture_sensor: GestureSensor):
        self._gesture_action_map: Dict[int, Callable[[], Any]] = {}

        self.gesture_sensor = gesture_sensor

    def register_gesture_action(self, gesture: int, action: Callable[[], Any]):
        """
        Register a new gesture action.
        :param gesture: the gesture to register the action for
        :param action: the action to execute when the gesture is detected
        """
        if gesture not in GestureSensor.ALL_GESTURES:
            raise ValueError("Invalid gesture")
        self._gesture_action_map[gesture] = action

    def update(self):
        """
        Read the current gesture and execute the corresponding action, if present.
        """
        gesture = self.gesture_sensor.gesture()
        if gesture not in self._gesture_action_map:
            return

        self._gesture_action_map[gesture]()
