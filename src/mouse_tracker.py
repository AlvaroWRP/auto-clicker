from typing import TYPE_CHECKING

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QCursor, QKeyEvent, QKeySequence, QIcon
from PySide6.QtWidgets import QLabel, QWidget, QGridLayout

if TYPE_CHECKING:
    from layouts import BottomLayout

from utils.clicker_functions import get_mouse_position
from utils.paths import ICON_FILE_PATH
from utils.pyinstaller import resource_path
from utils.strings import *


class MouseTracker(QWidget):
    def __init__(self, bottom_layout: 'BottomLayout'):
        super().__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # type: ignore

        self.bottom_layout = bottom_layout

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self._set_icon_and_title()
        self._make_timer()
        self._add_widgets()

    def _set_icon_and_title(self):
        icon_path = resource_path(ICON_FILE_PATH)
        icon = QIcon(icon_path)

        self.setWindowIcon(icon)
        self.setWindowTitle(GET_COORDINATES_STRING)

    def _add_widgets(self):
        key_to_save_label = self._create_widgets()

        self.main_layout.addWidget(key_to_save_label, 0, 0)
        self.main_layout.addWidget(self.x_coordinate_label, 1, 0)
        self.main_layout.addWidget(self.y_coordinate_label, 1, 1)

    def _create_widgets(self):
        self.x_coordinate_label = self._create_coordinate_label()
        self.y_coordinate_label = self._create_coordinate_label()

        return self._create_coordinate_label(PRESS_ESC_TO_SAVE_COORDINATES_STRING)

    def _create_coordinate_label(self, text: str | None = None):
        return QLabel(text)

    def _make_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_position)

    def _update_position(self):
        x, y = get_mouse_position()

        self.x_coordinate_label.setText(f'{X_STRING} {x}')
        self.y_coordinate_label.setText(f'{Y_STRING} {y}')

        cursor_position = QCursor().pos()
        self.move(cursor_position.x() + 15, cursor_position.y() + 15)

    def show_tracker(self):
        self._update_position()
        self.timer.start(10)
        self.show()

    def hide_tracker(self):
        self.timer.stop()
        self.hide()

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        key_text = QKeySequence(key).toString()

        if key_text == ESC_STRING:
            x_coordinate_text = self.x_coordinate_label.text()
            x_coordinate_text = x_coordinate_text[3:]

            y_coordinate_text = self.y_coordinate_label.text()
            y_coordinate_text = y_coordinate_text[3:]

            self.bottom_layout.x_coordinate_input.setText(x_coordinate_text)
            self.bottom_layout.y_coordinate_input.setText(y_coordinate_text)

            self.hide_tracker()

        return event.ignore()
