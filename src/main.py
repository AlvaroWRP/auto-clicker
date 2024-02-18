import sys

from PySide6.QtWidgets import QApplication

from layouts import TopLayout, MiddleLayout, BottomLayout, ButtonsLayout
from window import Window

from utils.read_qss_file import read_qss_file


if __name__ == '__main__':
    app = QApplication([])
    window = Window()

    top_layout = TopLayout()
    window.main_layout.addLayout(top_layout)

    middle_layout = MiddleLayout()
    window.main_layout.addLayout(middle_layout)

    bottom_layout = BottomLayout()
    window.main_layout.addLayout(bottom_layout)

    buttons_layout = ButtonsLayout(top_layout)
    window.main_layout.addLayout(buttons_layout)

    read_qss_file(app)

    window.show()
    sys.exit(app.exec())
