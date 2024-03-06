import json

from utils.paths import SETTINGS_FILE_PATH


def apply_changes(settings: dict[str, str | bool]):
    with open(SETTINGS_FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(settings, file, indent=4)


def load_hotkey():
    with open(SETTINGS_FILE_PATH, encoding='utf-8') as file:
        settings = json.load(file)
        return settings['hotkey']


def save_hotkey(hotkey: str):
    with open(SETTINGS_FILE_PATH, encoding='utf-8') as file:
        settings = json.load(file)
        settings['hotkey'] = hotkey

        apply_changes(settings)
