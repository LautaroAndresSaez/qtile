from libqtile import widget, bar, qtile
from libqtile.config import Screen
from libqtile.lazy import lazy
import subprocess

SEPARATOR_ICON = '\ue0b2'

WIFI_ICONS = [
    "󰤯",  # 0–20%
    "󰤟",  # 21–40%
    "󰤢",  # 41–60%
    "󰤥",  # 61–80%
    "󰤨",  # 81–100%
]

def get_volume_info():
    try:
        # Ejecutamos el comando
        out = subprocess.check_output(["wpctl", "get-volume", "@DEFAULT_AUDIO_SINK@"], text=True).strip()
        
        # out será algo como "Volume: 0.45" o "Volume: 1.00 [MUTED]"
        if "[MUTED]" in out:
            return "󰝟 Muted"
        
        # Extraemos solo el número (ej. "0.45")
        value_str = out.split(":")[1].split("[")[0].strip()
        vol_float = float(value_str)
        
        # Convertimos a porcentaje entero (1.0 -> 100%)
        vol_percent = int(vol_float * 100)
        
        # Iconos dinámicos según el porcentaje
        if vol_percent == 0:
            icon = "󰝟"
        elif vol_percent < 33:
            icon = "󰕿"
        elif vol_percent < 66:
            icon = "󰖀"
        else:
            icon = "󰕾"
            
        return f"{icon} {vol_percent}%"
    except Exception:
        return "󰝟 --"

def wifi_info():
    try:
        out = subprocess.check_output(
            ["nmcli", "-t", "-f", "IN-USE,SIGNAL,SSID", "dev", "wifi"],
            text=True,
        ).splitlines()

        for line in out:
            if line.startswith("*:"):
                _, signal, ssid = line.split(":", 2)
                level = int(signal)

                if level <= 20:
                    icon = WIFI_ICONS[0]
                elif level <= 40:
                    icon = WIFI_ICONS[1]
                elif level <= 60:
                    icon = WIFI_ICONS[2]
                elif level <= 80:
                    icon = WIFI_ICONS[3]
                else:
                    icon = WIFI_ICONS[4]

                return f"{icon}  {ssid}"
    except Exception:
        pass

    return "󰤭  No WiFi"


def create_screens(settings) -> list[Screen]:
    screens = []
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
            widget.TextBox(background=settings.colors.background, fmt=SEPARATOR_ICON,
                           foreground=settings.colors.color2, fontsize=20, padding=0),
            widget.GenPollText(
                update_interval=2,
                func=wifi_info,
                format=" {} ",
                background=settings.colors.color2
            ),
            widget.TextBox(background=settings.colors.color2, fmt=SEPARATOR_ICON,
                           foreground=settings.colors.color1, fontsize=20, padding=0),
            widget.GenPollText(
                func=get_volume_info,
                update_interval=1,
                background=settings.colors.color1,
                mouse_callbacks={
                    'Button1': lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"),
                    'Button4': lazy.spawn("wpctl set-volume -l 1.0 @DEFAULT_AUDIO_SINK@ 1%+"), # Scroll up
                    'Button5': lazy.spawn("wpctl set-volume -l 1.0 @DEFAULT_AUDIO_SINK@ 1%-"), # Scroll down
                }
            ),
            widget.Backlight(
                background=settings.colors.color1, 
                backlight_name="intel_backlight",
                change_command="brightnessctl s {0}%", 
                min_brightness=10, 
                fmt='\uf522 {}', 
                step=5
            ),
            widget.Memory(
                measure_mem="G", format="󰍛 {MemUsed:.1f}{mm}/{MemTotal:.0f}{mm}", background=settings.colors.color1),
            widget.Battery(format="{char} {percent:2.0%}", charge_char="󰂄", discharge_char="󰂂", empty_char="󰂎", full_char="󰁹",
                           not_charging_char="󰂃", unknown_char="󱉝", update_interval=1,
                           notify_below=60,
                           background=settings.colors.color1),
            widget.TextBox(background=settings.colors.color1, fmt=SEPARATOR_ICON,
                           foreground=settings.colors.background, fontsize=20, padding=0),
            widget.Clock(format="%a %I:%M %p %d/%m/%Y",
                         background=settings.colors.background),
    ]

    screens = [
        Screen(
            top=bar.Bar([*widgets], 20),
            wallpaper=settings.wallpaper,
            wallpaper_mode="fill",
        ),
    ]
    
    return screens