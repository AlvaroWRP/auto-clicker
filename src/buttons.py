from typing import TYPE_CHECKING

from PySide6.QtWidgets import QPushButton, QApplication

from settings import SettingsDialog, HotkeyDialog

from utils.clicker_functions import start

if TYPE_CHECKING:
    from layouts import TopLayout, MiddleLayout, BottomLayout


class StartStopButton(QPushButton):
    def __init__(
            self, top_layout: 'TopLayout',
            middle_layout: 'MiddleLayout', bottom_layout: 'BottomLayout'
        ):
        super().__init__()

        self.setText('Start (hotkey)')
        self.clicked.connect(lambda: start(top_layout, middle_layout, bottom_layout))

    def hotkey_received(self, hotkey: str):
        self.setText(f'Start ({hotkey})')


class SettingsButton(QPushButton):
    def __init__(self):
        super().__init__()

        self.setText('Settings')

        self.clicked.connect(self._open_settings_dialog)

    def _open_settings_dialog(self):
        settings_dialog = SettingsDialog()
        settings_dialog.exec()


class HotkeyButton(QPushButton):
    def __init__(self, start_stop_button: StartStopButton):
        super().__init__()

        self.start_stop_button = start_stop_button

        self.setText('Change hotkey')

        self.clicked.connect(self._open_hotkey_dialog)

    def _open_hotkey_dialog(self):
        hotkey_dialog = HotkeyDialog()
        hotkey_dialog.key_signal.connect(self.start_stop_button.hotkey_received)
        hotkey_dialog.exec()


class CloseButton(QPushButton):
    def __init__(self, app: QApplication):
        super().__init__()

        self.app = app

        self.setText('Close clicker')

        self.clicked.connect(self.app.quit)
