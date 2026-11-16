"""Render a set of live cells as text."""
from .engine import Cell


def bounds(live: set[Cell]) -> tuple[int, int, int, int]:
    xs = [x for x, _ in live]
    ys = [y for _, y in live]
    return min(xs), min(ys), max(xs), max(ys)


def render(live: set[Cell], width: int = 60, height: int = 24,
           origin: Cell | None = None, alive: str = "█", dead: str = " ") -> str:
    """Draw a width x height viewport. If origin is None, center on the live cells."""
    if origin is None:
        if live:
            x0, y0, x1, y1 = bounds(live)
            origin = ((x0 + x1) // 2 - width // 2, (y0 + y1) // 2 - height // 2)
        else:
            origin = (0, 0)
    ox, oy = origin
    return "\n".join(
        "".join(alive if (ox + x, oy + y) in live else dead for x in range(width))
        for y in range(height)
    )
