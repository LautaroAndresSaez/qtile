from libqtile import widget, bar
from libqtile.config import Screen
import subprocess
SEPARATOR_ICON = '\ue0b2'


class ScreensBuilder():
    def __init__(self, settings):
        widgets = [
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
            widget.Wlan(),
            widget.TextBox(background=settings.colors.background, fmt=SEPARATOR_ICON,
                           foreground=settings.colors.color1, fontsize=30, padding=0),
            widget.Backlight(background=settings.colors.color1, backlight_name="intel_backlight",
                             change_command="brightnessctl s {0}%", min_brigthness=10, fmt='\uf522 {}', step=5),
            widget.Memory(
                measure_mem="G", format="󰍛 {MemUsed:.1f}{mm}/{MemTotal:.0f}{mm}", background=settings.colors.color1),
            widget.Battery(format="{char} {percent:2.0%}", charge_char="󰂄", discharge_char="󱊡", empty_char="󰂎", full_char="󰁹",
                           not_charging_char="󰂃", unknown_char="󱉝", update_interval=1,
                           notify_below=60,
                           background=settings.colors.color1),
            widget.TextBox(background=settings.colors.color1, fmt=SEPARATOR_ICON,
                           foreground=settings.colors.background, fontsize=30, padding=0),
            widget.Clock(format="%a %I:%M %p %d/%m/%Y",
                         background=settings.colors.background),
        ]

        self._screens = [
            Screen(
                top=bar.Bar([*widgets], 24),
                wallpaper=settings.wallpaper,
                wallpaper_mode="fill"
            ),
        ]
        xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

        command = subprocess.run(
            xrandr,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        if command.returncode != 0:
            error = command.stderr.decode("UTF-8")
            print(error)
            connected_monitors = 1
        else:
            connected_monitors = int(command.stdout.decode("UTF-8"))

        if connected_monitors > 1:
            for _ in range(1, connected_monitors):
                self._screens.append(Screen(
                    top=bar.Bar([*widgets], 24),
                    wallpaper=settings.wallpaper,
                    wallpaper_mode="fill"
                ),)

    @property
    def screens(self):
        return self._screens

    def _add_section(self, widgets, background, next_brackground_color):
        pass
