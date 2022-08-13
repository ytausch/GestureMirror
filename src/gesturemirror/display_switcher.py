import subprocess


class DisplaySwitcher:
    def __init__(self):
        self._powered = True
        self.turn_on()

    @property
    def powered(self):
        return self._powered

    def turn_off(self):
        print("Turning off display")
        subprocess.run(['vcgencmd', 'display_power', '0'])
        self._powered = False

    def turn_on(self):
        print("Turning on display")
        subprocess.run(['vcgencmd', 'display_power', '1'])
        self._powered = True
