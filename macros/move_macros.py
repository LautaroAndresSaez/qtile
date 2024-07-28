from libqtile.config import Key
from libqtile.lazy import lazy


def generate_move_macros(mod, configs):
    return [
        Key([mod], configs.keys.left, lazy.layout.left(),
            desc="Move focus to left"),
        Key([mod], configs.keys.right, lazy.layout.right(),
            desc="Move focus to right"),
        Key([mod], configs.keys.down, lazy.layout.down(), desc="Move focus down"),
        Key([mod], configs.keys.up, lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(),
            desc="Move window focus to other window"),
        Key([mod, "shift"], configs.keys.left, lazy.layout.shuffle_left(),
            desc="Move window to the left"),
        Key([mod, "shift"], configs.keys.right, lazy.layout.shuffle_right(),
            desc="Move window to the right"),
        Key([mod, "shift"], configs.keys.down, lazy.layout.shuffle_down(),
            desc="Move window down"),
        Key([mod, "shift"], configs.keys.up,
            lazy.layout.shuffle_up(), desc="Move window up"),
        Key([mod, "control"], configs.keys.left, lazy.layout.grow_left(),
            desc="Grow window to the left"),
        Key([mod, "control"], configs.keys.right, lazy.layout.grow_right(),
            desc="Grow window to the right"),
        Key([mod, "control"], configs.keys.down, lazy.layout.grow_down(),
            desc="Grow window down"),
        Key([mod, "control"], configs.keys.up,
            lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    ]
