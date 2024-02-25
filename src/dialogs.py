from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon, QKeyEvent, QKeySequence
from PySide6.QtWidgets import QDialog, QVBoxLayout, QCheckBox, QLabel

from utils.json import save_hotkey, load_hotkey
from utils.paths import ICON_FILE_PATH
from utils.pyinstaller import resource_path


class SettingsDialog(QDialog):
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


class HotkeyDialog(QDialog):
    key_signal = Signal(str)

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
        self.setWindowTitle('Auto Clicker - Change hotkey')

    def _add_widgets(self):
        explanation_label = self._create_widgets()

        self.main_layout.addWidget(explanation_label)
        self.main_layout.addWidget(self.hotkey_text_field)

    def _create_widgets(self):
        self.hotkey_text_field = self._create_hotkey_text_field()
        return self._create_explanation_label()

    def _create_explanation_label(self):
        return QLabel('Type to choose another key')

    def _create_hotkey_text_field(self):
        hotkey = load_hotkey()

        label = QLabel()
        label.setText(hotkey)
        return label

    def keyPressEvent(self, arg__1: QKeyEvent):
        key = arg__1.key()
        key_text = QKeySequence(key).toString()

        self.hotkey_text_field.setText(key_text)
        self.key_signal.emit(key_text)

        save_hotkey(key_text)

        return arg__1.ignore()
