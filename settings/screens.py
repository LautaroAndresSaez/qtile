from libqtile import widget, bar
from libqtile.config import Screen

SEPARATOR_ICON = '\ue0b2'


class ScreensBuilder():
    def __init__(self, settings):
        self._screens = [
            Screen(
                top=bar.Bar(
                    [
                        widget.CurrentLayoutIcon(scale=.75),
                        widget.GroupBox(),
                        widget.Prompt(),
                        widget.WindowName(),
                        widget.Chord(
                            chords_colors={
                                "launch": (settings.colors.color2, settings.colors.color3),
                            },
                            name_transform=lambda name: name.upper(),
                        ),

                        widget.Systray(),
                        widget.TextBox(background=settings.colors.background, fmt=SEPARATOR_ICON,
                                       foreground=settings.colors.color3, fontsize=30, padding=0),
                        widget.Memory(
                            measure_mem="G", format="󰍛 {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}", background=settings.colors.color3),
                        widget.TextBox(background=settings.colors.color3, fmt=SEPARATOR_ICON,
                                       foreground=settings.colors.color2, fontsize=30, padding=0),
                        widget.Battery(format="{percent:2.0%}{char}", charge_char="󰂄", discharge_char="󱊡", empty_char="󰂎", full_char="󰁹",
                                       not_charging_char="󰂃", unknown_char="󱉝", update_interval=5, background=settings.colors.color2),
                        widget.TextBox(background=settings.colors.color2, fmt=SEPARATOR_ICON,
                                       foreground=settings.colors.color1, fontsize=30, padding=0),
                        widget.Clock(format="%a %I:%M %p %d/%m/%Y",
                                     background=settings.colors.color1),
                    ],
                    24,
                ),
                wallpaper=settings.wallpaper
            ),
        ]

    @property
    def screens(self):
        return self._screens

    def _add_rigth_widget(self, widget, background, next_brackground_color):
        pass
