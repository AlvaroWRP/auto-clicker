from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit, QComboBox,
                               QHBoxLayout, QButtonGroup, QApplication)

from buttons import StartStopButton, SettingsButton, HotkeyButton, CloseButton
from radio_group import RadioGroup


class TopLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self._add_widgets()

    def _add_widgets(self):
        time_between_clicks_label, mouse_button_label, mouse_button_input = self._create_widgets()

        self.addWidget(time_between_clicks_label)
        self.addWidget(self.time_between_clicks_input)
        self.addWidget(mouse_button_label)
        self.addWidget(mouse_button_input)

    def _create_widgets(self):
        self.time_between_clicks_input = self._create_time_between_clicks_input()

        time_between_clicks_label = self._create_label('Time between clicks (ms):')
        mouse_button_label = self._create_label('Mouse button:')
        mouse_button_input = self._create_mouse_button_input()

        return time_between_clicks_label, mouse_button_label, mouse_button_input

    def _create_time_between_clicks_input(self):
        input = QLineEdit()

        expression = QRegularExpression('^[0-9]*$')
        validator = QRegularExpressionValidator()
        validator.setRegularExpression(expression)

        input.setValidator(validator)
        return input

    def _create_label(self, text: str):
        return QLabel(text)

    def _create_mouse_button_input(self):
        combo_box = QComboBox()
        combo_box.addItems(['Left', 'Middle', 'Right'])
        return combo_box


class MiddleLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self._add_widgets()

    def _add_widgets(self):
        radio_button_group, repeat_n_times_input = self._create_widgets()

        self.addWidget(radio_button_group)
        self.addWidget(repeat_n_times_input)

    def _create_widgets(self):
        radio_button_group = self._group_radio_buttons()
        repeat_n_times_input = self._create_repeat_n_times_input()
        self._link_group_to_input(radio_button_group)

        return radio_button_group, repeat_n_times_input

    def _link_group_to_input(self, group: RadioGroup):
        group.button2.toggled.connect(self._toggle_input_read_only_mode)

    def _toggle_input_read_only_mode(self, checked: bool):
        self.itemAt(1).widget().setEnabled(checked)

    def _group_radio_buttons(self):
        group = QButtonGroup()
        return RadioGroup(group, 'Repeat until hotkey press', 'Repeat N times')

    def _create_repeat_n_times_input(self):
        input = QLineEdit()
        input.setEnabled(False)

        expression = QRegularExpression('^[0-9]*$')
        validator = QRegularExpressionValidator()
        validator.setRegularExpression(expression)

        input.setValidator(validator)
        return input


class BottomLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self._add_widgets()

    def _add_widgets(self):
        (radio_button_group, x_coordinate_label, x_coordinate_input,
         y_coordinate_label, y_coordinate_input) = self._create_widgets()

        self.addWidget(radio_button_group)
        self.addWidget(x_coordinate_label)
        self.addWidget(x_coordinate_input)
        self.addWidget(y_coordinate_label)
        self.addWidget(y_coordinate_input)

    def _create_widgets(self):
        radio_button_group = self._group_radio_buttons()
        x_coordinate_label = self._create_coordinate_label('X:')
        x_coordinate_input = self._create_coordinate_input('x')
        y_coordinate_label = self._create_coordinate_label('Y:')
        y_coordinate_input = self._create_coordinate_input('y')

        return (radio_button_group, x_coordinate_label, x_coordinate_input,
                y_coordinate_label, y_coordinate_input)

    def _group_radio_buttons(self):
        group = QButtonGroup()
        return RadioGroup(group, 'Current location', 'Get coordinates')

    def _create_coordinate_label(self, text: str):
        return QLabel(text)

    def _create_coordinate_input(self, axis: str):
        input = QLineEdit()
        input.setEnabled(False)
        return input


class ButtonsLayout(QGridLayout):
    def __init__(
            self, top_layout: TopLayout, middle_layout: MiddleLayout,
            bottom_layout: BottomLayout, app: QApplication
        ):
        super().__init__()

        start_stop_button = StartStopButton(top_layout, middle_layout, bottom_layout)
        settings_button = SettingsButton()
        hotkey_button = HotkeyButton(start_stop_button)
        close_button = CloseButton(app)

        self.addWidget(start_stop_button, 0, 0)
        self.addWidget(settings_button, 0, 1)
        self.addWidget(hotkey_button, 1, 0)
        self.addWidget(close_button, 1, 1)
