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
        self._groups.append(Group(name))
        self._group_shortcuts(name, index)
        return self._create_groups(rest, index + 1)

    def _group_shortcuts(self, name: str, index: int):
        actual_key = str(index)
        self._keyBuilder.add_keys([
            Key(
                [self._mod],
                actual_key,
                lazy.group[name].toscreen(),
                desc="Switch to group {}".format(name),
            ),
            Key(
                [self._mod, "shift"],
                actual_key,
                lazy.window.togroup(name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    name),
            ),

        ])
