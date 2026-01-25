from libqtile.lazy import lazy
from libqtile.config import Key
from libqtile.utils import guess_terminal
from libqtile.widget import backlight

import os

SH = "~/.config/qtile/sh"


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
            Key([mod], "Left", lazy.layout.left(),
                desc="Move focus to left"),
            Key([mod], "Right", lazy.layout.right(),
                desc="Move focus to right"),
            Key([mod], "Down",
                lazy.layout.down(), desc="Move focus down"),
            Key([mod], "Up",
                lazy.layout.up(), desc="Move focus up"),
            Key([mod], "space", lazy.layout.next(),
                desc="Move window focus to other window"),
            Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
                desc="Move window to the left"),
            Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
                desc="Move window to the right"),
            Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
                desc="Move window down"),
            Key([mod, "shift"], "Up",
                lazy.layout.shuffle_up(), desc="Move window up"),
            Key([mod, "control"], "Left", lazy.layout.grow_left(),
                desc="Grow window to the left"),
            Key([mod, "control"], "Right", lazy.layout.grow_right(),
                desc="Grow window to the right"),
            Key([mod, "control"], "Down", lazy.layout.grow_down(),
                desc="Grow window down"),
            Key([mod, "control"], "Up",
                lazy.layout.grow_up(), desc="Grow window up"),

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
            Key([mod, "control"], "n", lazy.layout.normalize(),
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
      
            Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
            Key([mod, "shift"], "r", lazy.spawncmd(),
                desc="Spawn a command using a prompt widget"),
            Key([mod, "control"], "r", lazy.spawn("wofi --show")),
            Key([mod], "r", lazy.spawn("wofi --show drun")),
            Key([], "Print", lazy.spawn("flameshot gui")),
            Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%"), desc="Brillo +"),
            Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="Brillo -"),
            
        ]

    @ property
    def keys(self):
        return self._keys

    @ property
    def mod(self):
        return self._mod

    @ property
    def terminal(self):
        return self._terminal

    def add_key(self, key: Key):
        self._keys.append(key)

    def add_keys(self, keys: list[Key]):
        self._keys.extend(keys)
