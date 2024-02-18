from PySide6.QtWidgets import QRadioButton, QHBoxLayout, QButtonGroup, QWidget


class RadioGroup(QWidget):
    def __init__(self, button_group: QButtonGroup, text1: str, text2: str):
        super().__init__()

        layout = QHBoxLayout()

        button1 = QRadioButton(text1)
        self.button2 = QRadioButton(text2)

        button1.setChecked(True)

        button_group.addButton(button1)
        button_group.addButton(self.button2)

        layout.addWidget(button1)
        layout.addWidget(self.button2)

        self.setLayout(layout)
