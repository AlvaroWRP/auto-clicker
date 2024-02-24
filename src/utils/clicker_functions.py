import pyautogui as pag

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from layouts import TopLayout, MiddleLayout, BottomLayout


def start(top_layout: 'TopLayout', middle_layout: 'MiddleLayout', bottom_layout: 'BottomLayout'):
    print(top_layout.time_between_clicks_input.text())
