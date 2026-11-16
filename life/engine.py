"""Core Game of Life engine using a sparse set of live cells (unbounded grid)."""
from collections import Counter

Cell = tuple[int, int]


def step(live: set[Cell]) -> set[Cell]:
    """Return the next generation for a set of live (x, y) cells."""
    counts = Counter(
        (x + dx, y + dy)
        for (x, y) in live
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if (dx, dy) != (0, 0)
    )
    return {c for c, n in counts.items() if n == 3 or (n == 2 and c in live)}
