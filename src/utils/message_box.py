from PySide6.QtWidgets import QMessageBox


def show_error(text: str):
    message_box = QMessageBox()

    message_box.setText(text)
    message_box.setIcon(message_box.Icon.Critical)
    message_box.exec()
