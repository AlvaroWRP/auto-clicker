import pyautogui as pag

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from layouts import TopLayout, MiddleLayout, BottomLayout


def start(top_layout: 'TopLayout'):
    print(top_layout.time_between_clicks_input.text())
