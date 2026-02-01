from .laod_settings import load_settings
from .keys import add_base_keys
from .groups import add_group_keys, create_groups
from .screens import create_screens
from .layout import create_layouts

def build(settings_path: str = None, mod: str = 'mod4'):
    import os
    settings_path = settings_path if settings_path else f'{os.environ["HOME"]}/.config/qtile/configs/default.json'
    settings = load_settings(settings_path)
    
    groups = create_groups(settings.workspaces)
    screens = create_screens(settings)
    layouts = create_layouts(settings)
    
    keys = add_base_keys(settings, mod=mod)
    keys = keys + add_group_keys(groups)
    
    return keys, screens, groups, layouts, settings
    
