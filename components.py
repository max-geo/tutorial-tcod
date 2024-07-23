from dataclasses import dataclass
from geom import Point

@dataclass
class Renderables:
    ch: str
    fg: tuple[int, int, int]

# Named components
Location = ("location", Point)
Name = ("name", str)
Description = ("desc", str)