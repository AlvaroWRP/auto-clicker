from typing import TYPE_CHECKING

from PySide6.QtWidgets import QPushButton

from settings import SettingsWindow

from utils.clicker_functions import start

if TYPE_CHECKING:
    from layouts import TopLayout, MiddleLayout, BottomLayout


class StartStopButton(QPushButton):
    def __init__(self, top_layout: 'TopLayout'):
        super().__init__()

        self.setText('Start (hotkey)')
        self.clicked.connect(lambda: start(top_layout))


class SettingsButton(QPushButton):
    def __init__(self):
        super().__init__()

        self.setText('Settings')

        self.clicked.connect(self._open_settings_window)

    def _open_settings_window(self):
        self.settings_window = SettingsWindow()
        self.settings_window.exec()
