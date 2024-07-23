import yaml

from typing import Optional

from tcod.ecs import World, Entity

import components as comps
from geom import Point


class GameData:
    def __init__(self, fn: str):
        with open(fn, "r") as f:
            self.data = yaml.load(f, yaml.SafeLoader)


CHARDATA = GameData("./data/chardata.yml")

def new_entity(w: World, build_id: str, is_player: bool):
    template = CHARDATA.data[build_id]
    ch = ord(template["ch"])
    fg = tuple(template["fg"])
    nm = template["name"]
    tags = template.get("tags", list())
    desc = template["desc"]
    base_tags = ["blocker", "actor"]
    pt: Optional[Point] = template["location"]
    e = None


    c = {
        comps.Renderables: comps.Renderables(ch, fg),
        comps.Location: Point(0, 0),
        comps.Name: nm,
        comps.Description: desc,
    }

    if is_player:
        e = w["player"]
        e.tags.add("player")
        e.components[comps.Location] = pt
    else:
        e = w.new_entity()

    for tag in base_tags + tags:
        e.tags.add(tag)

    e.components.update(c)

    return e
