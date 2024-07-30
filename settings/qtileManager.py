import os
import json

from types import SimpleNamespace

from .layout import LayoutBuilder
from .key import KeyBuilder
from .groups import GroupsBuilder
from .screens import ScreensBuilder


class QTileManager():
    def __init__(self, settings_path):
        self._settings = self._load_settings(settings_path)
        self._keyBuilder = KeyBuilder(self._settings)
        self._layoutBuilder = LayoutBuilder(self._settings)
        self._groupBuilder = GroupsBuilder(self._settings)
        self._screenBuilder = ScreensBuilder(self._settings)

    def _load_settings(self, path):
        if not (os.path.exists(path) and os.path.isfile(path)):
            path = f'{os.environ["HOME"]}/.config/qtile/configs/default.json'
        f = open(path)
        return json.loads(f.read(), object_hook=lambda x: SimpleNamespace(**x))

    @property
    def settings(self):
        return self._settings

    @property
    def layouts(self):
        return self._layoutBuilder.layouts

    @property
    def keys(self):
        return self._keyBuilder.keys

    @property
    def groups(self):
        return self._groupBuilder.groups

    @property
    def screens(self):
        return self._screenBuilder.screens
