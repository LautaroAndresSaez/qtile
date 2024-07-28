import json
import os
from types import SimpleNamespace


def load_config(config_path=f'{os.environ["HOME"]}/.config/qtile/configs/default.json'):
    f = open(config_path)
    return json.loads(f.read(), object_hook=lambda x: SimpleNamespace(**x))
