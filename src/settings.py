from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QVBoxLayout, QCheckBox

from utils.paths import ICON_FILE_PATH
from utils.pyinstaller_media import resource_path


class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()

        self._set_icon_and_title()

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self._add_widgets()

    def _set_icon_and_title(self):
        icon_path = resource_path(ICON_FILE_PATH)
        icon = QIcon(icon_path)

        self.setWindowIcon(icon)
        self.setWindowTitle('Auto Clicker - Settings')

    def _add_widgets(self):
        dark_mode_check_box, topmost_check_box = self._create_widgets()
        self.main_layout.addWidget(dark_mode_check_box)
        self.main_layout.addWidget(topmost_check_box)

    def _create_widgets(self):
        dark_mode_check_box = self._create_check_box('Toggle dark mode')
        topmost_check_box = self._create_check_box('Set window as topmost')
        return dark_mode_check_box, topmost_check_box

    def _create_check_box(self, text: str):
        check_box = QCheckBox(text)
        check_box.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        return check_box
