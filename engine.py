import tcod
from tcod.ecs import Entity

from event_handler import EventHandler
from actions import MovementAction, EscapeAction
from components import Location
from map import GameMap


class Engine:
    def __init__(self):
        self.tileset = tcod.tileset.load_tilesheet(
            "data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
        )
        self.console = tcod.console.Console(80, 50, order="F")
        self.context = tcod.context.new(console=self.console, tileset=self.tileset, title='AAAAAAAAAAAAAAAAAAAAAAA')
        self.event_handler = EventHandler()
        self.player = None
        self.map = GameMap(50, 50)

    def handle_events(self):
        for event in tcod.event.wait():
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            if isinstance(action, MovementAction):
                if self.map.tiles["walkable"][self.player.components[Location].x + action.dx, self.player.components[Location].y + action.dy]:
                    print(self.player.components[Location])
                    print(self.player.components[Location].x + action.dx, self.player.components[Location].y + action.dy)
                    print(self.map.tiles[30, 22])
                    self.player.components[Location].x += action.dx
                    self.player.components[Location].y += action.dy

            elif isinstance(action, EscapeAction):
                raise SystemExit()

    def draw(self):
        self.map.render(self.console)

        self.console.print(x=self.player.components[Location].x, y=self.player.components[Location].y, string="@")
        self.context.present(self.console)

        self.console.clear()