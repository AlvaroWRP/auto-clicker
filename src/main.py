import sys

from PySide6.QtWidgets import QApplication

from layouts import TopLayout, MiddleLayout, BottomLayout, ButtonsLayout
from window import Window

from utils.read_qss_file import read_qss_file


if __name__ == '__main__':
    app = QApplication([])

    top_layout = TopLayout()
    middle_layout = MiddleLayout()
    bottom_layout = BottomLayout()

    window = Window(top_layout, middle_layout, bottom_layout)

    window.main_layout.addLayout(top_layout)
    window.main_layout.addLayout(middle_layout)
    window.main_layout.addLayout(bottom_layout)

    buttons_layout = ButtonsLayout(top_layout, middle_layout, bottom_layout, app)
    window.main_layout.addLayout(buttons_layout)

    read_qss_file(app)

    window.show()
    sys.exit(app.exec())
