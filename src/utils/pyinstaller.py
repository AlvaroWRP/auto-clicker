import os
import sys

from utils.paths import RESOURCES_FOLDER_PATH


def resource_path(relative_path: str):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(RESOURCES_FOLDER_PATH)

    return os.path.join(base_path, relative_path)
