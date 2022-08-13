import subprocess
import time
from typing import Optional


class DisplaySwitcher:
    def __init__(self, timeout: Optional[float] = None):
        """
        Initializes the display switcher.
        :param timeout: The timeout in seconds after which the display is turned off,
        or None if no timeout should be set.
        """
        self._powered = True
        self._turned_on: float = 0
        self.turn_on()
        self.timeout = timeout

    @property
    def powered(self):
        return self._powered

    def turn_off(self):
        print("Turning off display")
        subprocess.run(['vcgencmd', 'display_power', '0'], stdout=subprocess.DEVNULL)
        self._powered = False

    def turn_on(self):
        print("Turning on display")
        subprocess.run(['vcgencmd', 'display_power', '1'], stdout=subprocess.DEVNULL)
        self._powered = True
        self._turned_on = time.time()

    def timeout_update(self):
        """
        Call this method regularly to turn off the display after the timeout has elapsed.
        """
        if self._powered and self.timeout is not None and time.time() - self._turned_on > self.timeout:
            self.turn_off()
