from PySide6.QtWidgets import QApplication

from utils.paths import QSS_FILE_PATH
from utils.pyinstaller_media import resource_path


def read_qss_file(app: QApplication):
    qss_file_path = resource_path(QSS_FILE_PATH)

    with open(qss_file_path, 'r') as file:
        style = file.read()
        app.setStyleSheet(style)
