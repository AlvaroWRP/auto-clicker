import pyautogui as pag

from typing import TYPE_CHECKING

from utils.message_box import show_error
from utils.strings import *

if TYPE_CHECKING:
    from layouts import TopLayout, MiddleLayout, BottomLayout

pag.PAUSE = 0


def start(top_layout: 'TopLayout', middle_layout: 'MiddleLayout', bottom_layout: 'BottomLayout'):
    try:
        time_between_clicks = float(top_layout.time_between_clicks_input.text())

        mouse_button = top_layout.mouse_button_input.currentText()

        is_repeat_n_times_enabled = middle_layout.repeat_n_times_input.isEnabled()

        are_coordinates_enabled = bottom_layout.x_coordinate_input.isEnabled()

        if are_coordinates_enabled:
            try:
                x = int(bottom_layout.x_coordinate_input.text())
                y = int(bottom_layout.y_coordinate_input.text())
            except ValueError:
                show_error(MISSING_X_AND_Y_VALUES_STRING)
                return

        if is_repeat_n_times_enabled and not are_coordinates_enabled:
            try:
                number_of_times = int(middle_layout.repeat_n_times_input.text())

                pag.click(
                    clicks=number_of_times, interval=time_between_clicks, button=mouse_button
                )
            except ValueError:
                show_error(MISSING_REPEAT_N_TIMES_VALUE_STRING)
        elif are_coordinates_enabled and not is_repeat_n_times_enabled:
            while True:
                pag.click(
                    x=x, y=y, interval=time_between_clicks, button=mouse_button  # type: ignore
                )
        elif is_repeat_n_times_enabled and are_coordinates_enabled:
            try:
                number_of_times = int(middle_layout.repeat_n_times_input.text())

                pag.click(
                    x=x, y=y, clicks=number_of_times,  # type: ignore
                    interval=time_between_clicks, button=mouse_button
                )
            except ValueError:
                show_error(MISSING_REPEAT_N_TIMES_VALUE_STRING)
        else:
            while True:
                pag.click(interval=time_between_clicks, button=mouse_button)
    except ValueError:
        show_error(MISSING_TIME_BETWEEN_CLICKS_STRING)


def get_mouse_position():
    return pag.position()
