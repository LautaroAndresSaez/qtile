from libqtile.lazy import lazy

from libqtile.config import Group, Key

from .key import KeyBuilder


class GroupsBuilder():
    def __init__(self, settings):
        self._keyBuilder = KeyBuilder(settings)
        self._mod = self._keyBuilder.mod
        self._groups = []
        self._create_groups(settings.workspaces)

    @property
    def groups(self):
        return self._groups

    def _create_groups(self, names: list[str], index=1):
        if len(names) == 0:
            return
        name, *rest = names
        self._groups.append(Group(str(index), label=name))
        self._group_shortcuts(str(index))
        return self._create_groups(rest, index + 1)

    def _group_shortcuts(self, name: str):
        self._keyBuilder.add_keys([
            Key(
                [self._mod],
                name,
                lazy.group[name].toscreen(),
                desc="Switch to group {}".format(name),
            ),
            Key(
                [self._mod, "shift"],
                name,
                lazy.window.togroup(name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    name),
            ),
        ])
