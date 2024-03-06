import keyboard

from PySide6.QtCore import QObject, Signal

from utils.json import load_hotkey


class HotkeyChecker(QObject):
    key_signal = Signal()

    def __init__(self):
        super().__init__()

        self.hotkey = None

        self.update_hotkey()

    def update_hotkey(self):
        new_hotkey = load_hotkey()

        if self.hotkey != new_hotkey:
            if self.hotkey != None:
                keyboard.remove_hotkey(self.hotkey)

            self.hotkey = new_hotkey
            keyboard.add_hotkey(self.hotkey, self._emit_signal)

    def _emit_signal(self):
        self.key_signal.emit()
