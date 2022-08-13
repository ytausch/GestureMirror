from typing import Callable, TypeVar, Optional

from soco import SoCo

T = TypeVar('T')


def _ignore_errors(command: Callable[[], T]) -> Optional[T]:
    """
    Wraps the given command in a try-except block and prints any exceptions to the console,
    and executes it.
    :param command: The command to wrap.
    :return: The result of the command, or None if an exception occurred.
    """
    # noinspection PyBroadException
    try:
        return command()
    except Exception as e:
        print(f"Error executing Sonos command: {e}")
        return None


class SonosController:
    def __init__(self, ip: str):
        self.sonos = SoCo(ip)

    def play_uri(self, uri: str, title: str, force_radio: bool):
        """
        Plays the given URI on the Sonos speaker. Errors will be ignored and printed to the console.

        :param uri: The URI to play.
        :param title: The title of the medium.
        :param force_radio: Whether to force the medium to be played as a radio station.
        """
        # Unfortunately, the errors that can occur here and are not well-documented,
        # so we have to catch all exceptions and print them to the console.
        _ignore_errors(lambda: self.sonos.play_uri(uri, title, force_radio=force_radio))

    def stop(self):
        """
        Stops the current playback.
        :return:
        """
        # Unfortunately, the errors that can occur here and are not well-documented,
        # so we have to catch all exceptions and print them to the console.
        _ignore_errors(lambda: self.sonos.stop())
