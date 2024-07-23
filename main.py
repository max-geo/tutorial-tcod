import tcod

from tcod.ecs import World

from engine import Engine
from factory import new_entity
from map import GameMap
from components import Location

def main() -> None:
    w = World()

    e = Engine()

    e.player = new_entity(w, "base_hero", True)



    tcod.tileset.procedural_block_elements(tileset=e.tileset)

    while True:


        e.draw()
        e.handle_events()

if __name__ == "__main__":
    main()