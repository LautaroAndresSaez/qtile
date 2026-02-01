import os
import json
from types import SimpleNamespace


def load_settings(path: str | None):
    if not (os.path.exists(path) and os.path.isfile(path)):
        path = f'{os.environ["HOME"]}/.config/qtile/configs/default.json'
    f = open(path)
    return json.loads(f.read(), object_hook=lambda x: SimpleNamespace(**x))
