from libqtile import layout

def create_layouts(settings) -> list:
    base = {
        "border_focus": settings.colors.color1,
        "border_width": 2
    }
    return [
        layout.MonadTall(**base, align=layout.MonadTall._right),
        layout.Columns(**base),
        layout.Max(**base),
    ]
