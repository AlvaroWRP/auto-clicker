import pyautogui as pag

from typing import TYPE_CHECKING

from utils.message_box import show_error

if TYPE_CHECKING:
    from layouts import TopLayout, MiddleLayout, BottomLayout

pag.PAUSE = 0


def start(top_layout: 'TopLayout', middle_layout: 'MiddleLayout', bottom_layout: 'BottomLayout'):
    try:
        time_between_clicks = float(top_layout.time_between_clicks_input.text())

        mouse_button = top_layout.mouse_button_input.currentText()

        is_repeat_n_times_enabled = middle_layout.repeat_n_times_input.isEnabled()

        if is_repeat_n_times_enabled:
            try:
                number_of_times = int(middle_layout.repeat_n_times_input.text())

                pag.click(
                    clicks=number_of_times, interval=time_between_clicks, button=mouse_button
                )
            except ValueError:
                show_error('Missing "Repeat N times" value')
        else:
            while True:
                pag.click(interval=time_between_clicks, button=mouse_button)
    except ValueError:
        show_error('Missing "Time between clicks (seconds):" value')
