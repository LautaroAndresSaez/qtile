from libqtile.lazy import lazy
from libqtile.config import Key
from libqtile.utils import guess_terminal


class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_)
        return class_._instance


class KeyBuilder(Singleton):
    def __init__(self, settings, mod="mod4", terminal=guess_terminal()):
        self._mod = mod
        self._terminal = terminal
        self._keys = [
            Key([mod], settings.keys.left, lazy.layout.left(),
                desc="Move focus to left"),
            Key([mod], settings.keys.right, lazy.layout.right(),
                desc="Move focus to right"),
            Key([mod], settings.keys.down,
                lazy.layout.down(), desc="Move focus down"),
            Key([mod], settings.keys.up,
                lazy.layout.up(), desc="Move focus up"),
            Key([mod], "space", lazy.layout.next(),
                desc="Move window focus to other window"),
            Key([mod, "shift"], settings.keys.left, lazy.layout.shuffle_left(),
                desc="Move window to the left"),
            Key([mod, "shift"], settings.keys.right, lazy.layout.shuffle_right(),
                desc="Move window to the right"),
            Key([mod, "shift"], settings.keys.down, lazy.layout.shuffle_down(),
                desc="Move window down"),
            Key([mod, "shift"], settings.keys.up,
                lazy.layout.shuffle_up(), desc="Move window up"),
            Key([mod, "control"], settings.keys.left, lazy.layout.grow_left(),
                desc="Grow window to the left"),
            Key([mod, "control"], settings.keys.right, lazy.layout.grow_right(),
                desc="Grow window to the right"),
            Key([mod, "control"], settings.keys.down, lazy.layout.grow_down(),
                desc="Grow window down"),
            Key([mod, "control"], settings.keys.up,
                lazy.layout.grow_up(), desc="Grow window up"),
            Key([mod], "n", lazy.layout.normalize(),
                desc="Reset all window sizes"),
            Key(
                [mod, "shift"],
                "Return",
                lazy.layout.toggle_split(),
                desc="Toggle between split and unsplit sides of stack",
            ),
            Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
            # Toggle between different layouts as defined below
            Key([mod], "Tab", lazy.next_layout(),
                desc="Toggle between layouts"),
            Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
            Key(
                [mod],
                "f",
                lazy.window.toggle_fullscreen(),
                desc="Toggle fullscreen on the focused window",
            ),
            Key([mod], "t", lazy.window.toggle_floating(),
                desc="Toggle floating on the focused window"),
            Key([mod, "control"], "r", lazy.reload_config(),
                desc="Reload the config"),
            Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
            Key([mod, "shift"], "r", lazy.spawncmd(),
                desc="Spawn a command using a prompt widget"),
            Key([mod, "control"], "r", lazy.spawn("rofi -show")),
            Key([mod], "r", lazy.spawn("rofi -show drun"))
        ]

    @property
    def keys(self):
        return self._keys

    @property
    def mod(self):
        return self._mod

    @property
    def terminal(self):
        return self._terminal

    def add_key(self, key: Key):
        self._keys.append(key)

    def add_keys(self, keys: list[Key]):
        self._keys.extend(keys)
