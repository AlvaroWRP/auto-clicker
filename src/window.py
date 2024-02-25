from PySide6.QtGui import QIcon, QKeyEvent, QKeySequence
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from layouts import TopLayout, MiddleLayout, BottomLayout

from utils.clicker_functions import start
from utils.json import load_hotkey
from utils.paths import ICON_FILE_PATH
from utils.pyinstaller import resource_path


class Window(QMainWindow):
    def __init__(
            self, top_layout: TopLayout, middle_layout: MiddleLayout, bottom_layout: BottomLayout
        ):
        super().__init__()

        self.top_layout = top_layout
        self.middle_layout = middle_layout
        self.bottom_layout = bottom_layout

        self.main_layout = QVBoxLayout()

        self._set_icon_and_title()
        self._set_central_widget()

    def _set_icon_and_title(self):
        icon_path = resource_path(ICON_FILE_PATH)
        icon = QIcon(icon_path)

        self.setWindowIcon(icon)
        self.setWindowTitle('Auto Clicker')

    def _set_central_widget(self):
        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def keyPressEvent(self, event: QKeyEvent):
        hotkey = load_hotkey()

        key = event.key()
        key_text = QKeySequence(key).toString()

        if key_text == hotkey:
            start(self.top_layout, self.middle_layout, self.bottom_layout)

        return event.ignore()
