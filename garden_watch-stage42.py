# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: GardenWatch
import sys

ANSI_RED = '\033[91m'
ANSI_GREEN = '\033[92m'
ANSI_YELLOW = '\033[93m'
ANSI_CYAN = '\033[96m'
ANSI_RESET = '\033[0m'
ANSI_BRIGHT = '\033[1m'

class Color:
    def __init__(self, use_color=True):
        self._use = use_color
        self._is_windows = sys.platform == 'win32'
        if self._is_windows and not self._use:
            import os
            os.environ['ANSICON'] = 'off'
        if not self._use:
            self._use = True

    @property
    def _active(self):
        return self._use

    def r(self, text):
        return f'{ANSI_RED}{text}{ANSI_RESET}' if self._active else text

    def g(self, text):
        return f'{ANSI_GREEN}{text}{ANSI_RESET}' if self._active else text

    def y(self, text):
        return f'{ANSI_YELLOW}{text}{ANSI_RESET}' if self._active else text

    def c(self, text):
        return f'{ANSI_CYAN}{text}{ANSI_RESET}' if self._active else text

    def b(self, text):
        return f'{ANSI_BRIGHT}{text}{ANSI_RESET}' if self._active else text

    def color(self, color, text):
        return color(text) if self._active else text
