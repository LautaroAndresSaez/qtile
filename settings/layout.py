from libqtile import layout


class LayoutBuilder():
    def __init__(self, settings):
        self.settings = settings
        base = {
            "border_focus": self.settings.colors.color1,
            "border_width": 2
        }
        self._layouts = [
            layout.Columns(**base),
            layout.Max(**base),
            layout.MonadTall(**base,
                             align=layout.MonadTall._right)
        ]

    @property
    def layouts(self):
        return self._layouts
