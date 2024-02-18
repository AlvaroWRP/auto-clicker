from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from utils.paths import ICON_FILE_PATH
from utils.pyinstaller_media import resource_path


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

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
