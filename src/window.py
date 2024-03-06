from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from layouts import TopLayout, MiddleLayout, BottomLayout
from separate_hotkey_thread import HotkeyChecker

from utils.clicker_functions import start
from utils.paths import ICON_FILE_PATH
from utils.pyinstaller import resource_path
from utils.strings import *


class Window(QMainWindow):
    def __init__(
            self, top_layout: TopLayout, middle_layout: MiddleLayout, bottom_layout: BottomLayout
        ):
        super().__init__()

        self.top_layout = top_layout
        self.middle_layout = middle_layout
        self.bottom_layout = bottom_layout

        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # type: ignore

        self.main_layout = QVBoxLayout()

        self._set_icon_and_title()
        self._set_central_widget()

        self._create_hotkey_checker()
        self._create_hotkey_update_timer()

    def _set_icon_and_title(self):
        icon_path = resource_path(ICON_FILE_PATH)
        icon = QIcon(icon_path)

        self.setWindowIcon(icon)
        self.setWindowTitle(PROGRAM_NAME_STRING)

    def _set_central_widget(self):
        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def _create_hotkey_checker(self):
        self.hotkey_checker = HotkeyChecker()
        self.hotkey_checker.key_signal.connect(self._connect_key_to_start_function)

    def _create_hotkey_update_timer(self):
        self.hotkey_update_timer = QTimer()
        self.hotkey_update_timer.timeout.connect(self.hotkey_checker.update_hotkey)
        self.hotkey_update_timer.start(100)

    def _connect_key_to_start_function(self):
        start(self.top_layout, self.middle_layout, self.bottom_layout)
