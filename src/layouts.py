from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit, QComboBox,
                               QHBoxLayout, QButtonGroup, QApplication)

from buttons import StartStopButton, SettingsButton, HotkeyButton, CloseButton
from mouse_tracker import MouseTracker
from radio_group import RadioGroup

from utils.regex import FLOAT_REGEX
from utils.strings import *


class TopLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self._add_widgets()

    def _add_widgets(self):
        time_between_clicks_label, mouse_button_label = self._create_widgets()

        self.addWidget(time_between_clicks_label)
        self.addWidget(self.time_between_clicks_input)
        self.addWidget(mouse_button_label)
        self.addWidget(self.mouse_button_input)

    def _create_widgets(self):
        self.time_between_clicks_input = self._create_time_between_clicks_input()
        self.time_between_clicks_input.setText(DEFAULT_TIME_BETWEEN_CLICKS_VALUE_STRING)

        self.mouse_button_input = self._create_mouse_button_input()

        time_between_clicks_label = self._create_label(TIME_BETWEEN_CLICKS_STRING)
        mouse_button_label = self._create_label(MOUSE_BUTTON_STRING)

        return time_between_clicks_label, mouse_button_label

    def _create_time_between_clicks_input(self):
        input = QLineEdit()

        expression = QRegularExpression(FLOAT_REGEX)
        validator = QRegularExpressionValidator()
        validator.setRegularExpression(expression)

        input.setValidator(validator)
        return input

    def _create_label(self, text: str):
        return QLabel(text)

    def _create_mouse_button_input(self):
        combo_box = QComboBox()
        combo_box.addItems([LEFT_STRING, MIDDLE_STRING, RIGHT_STRING])
        return combo_box


class MiddleLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self._add_widgets()

    def _add_widgets(self):
        radio_button_group = self._create_widgets()

        self.addWidget(radio_button_group)
        self.addWidget(self.repeat_n_times_input)

    def _create_widgets(self):
        self.repeat_n_times_input = self._create_repeat_n_times_input()

        radio_button_group = self._group_radio_buttons()
        self._link_group_to_input(radio_button_group)

        return radio_button_group

    def _link_group_to_input(self, group: RadioGroup):
        group.button2.toggled.connect(self._toggle_enabled_input)

    def _toggle_enabled_input(self, checked: bool):
        self.itemAt(1).widget().setEnabled(checked)

    def _group_radio_buttons(self):
        group = QButtonGroup()
        return RadioGroup(group, REPEAT_UNTIL_HOTKEY_PRESS_STRING, REPEAT_N_TIMES_STRING)

    def _create_repeat_n_times_input(self):
        input = QLineEdit()
        input.setEnabled(False)

        expression = QRegularExpression(FLOAT_REGEX)
        validator = QRegularExpressionValidator()
        validator.setRegularExpression(expression)

        input.setValidator(validator)
        return input


class BottomLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.mouse_tracker = MouseTracker(self)

        self._add_widgets()

    def _add_widgets(self):
        radio_button_group, x_coordinate_label, y_coordinate_label = self._create_widgets()

        self.addWidget(radio_button_group)
        self.addWidget(x_coordinate_label)
        self.addWidget(self.x_coordinate_input)
        self.addWidget(y_coordinate_label)
        self.addWidget(self.y_coordinate_input)

    def _create_widgets(self):
        self.x_coordinate_input = self._create_coordinate_input()
        self.y_coordinate_input = self._create_coordinate_input()

        radio_button_group = self._group_radio_buttons()
        self._link_group_to_input(radio_button_group)

        x_coordinate_label = self._create_coordinate_label(X_STRING)
        y_coordinate_label = self._create_coordinate_label(Y_STRING)

        return radio_button_group, x_coordinate_label, y_coordinate_label

    def _link_group_to_input(self, group: RadioGroup):
        group.button2.toggled.connect(self._toggle_enabled_input)

    def _toggle_enabled_input(self, checked: bool):
        self.x_coordinate_input.setEnabled(checked)
        self.x_coordinate_input.setReadOnly(checked)

        self.y_coordinate_input.setEnabled(checked)
        self.y_coordinate_input.setReadOnly(checked)

        if checked:
            self.mouse_tracker.show_tracker()
        else:
            self.mouse_tracker.hide_tracker()

    def _group_radio_buttons(self):
        group = QButtonGroup()
        return RadioGroup(group, CURRENT_LOCATION_STRING, GET_COORDINATES_STRING)

    def _create_coordinate_label(self, text: str):
        return QLabel(text)

    def _create_coordinate_input(self):
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
