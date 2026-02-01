from libqtile.lazy import lazy
from libqtile.config import Group, Key

def create_groups(names: list[str], index = 1) -> list[Group]:
    if len(names) == 0:
        return []
    [name, *rest] = names
    group = Group(str(index), label=name)

    results = create_groups(rest, index + 1)
    return [group, *results]


def add_group_keys(groups: list[Group], mod='mod4') -> list[Key]:
    if len(groups) == 0:
        return []
    [group, *rest] = groups
    new_keys = [
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    group.name),
            ),
    ]
    return new_keys + add_group_keys(rest) 
