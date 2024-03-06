from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox

from utils.strings import *


def show_error(text: str):
    message_box = QMessageBox()

    message_box.setWindowFlags(Qt.WindowStaysOnTopHint)  # type: ignore
    message_box.setWindowTitle(ERROR_STRING)

    message_box.setText(text)
    message_box.setIcon(message_box.Icon.Critical)

    message_box.exec()
