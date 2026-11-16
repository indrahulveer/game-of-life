"""Helpers for seeding and analysing simulations."""
import random

from .engine import Cell, step


def random_soup(width: int, height: int, density: float = 0.3, seed: int | None = None) -> set[Cell]:
    rng = random.Random(seed)
    return {(x, y) for x in range(width) for y in range(height) if rng.random() < density}


def normalize(live: set[Cell]) -> frozenset[Cell]:
    """Translate so the top-left of the bounding box is (0, 0); used for cycle detection."""
    if not live:
        return frozenset()
    mx = min(x for x, _ in live)
    my = min(y for _, y in live)
    return frozenset((x - mx, y - my) for x, y in live)


def find_period(live: set[Cell], max_gens: int = 500):
    """Run until the pattern repeats (up to translation).

    Returns (period, displacement-free) or None. Extinction counts as period 1 (empty board).
    """
    seen: dict[frozenset[Cell], int] = {}
    cur = set(live)
    for gen in range(max_gens + 1):
        key = normalize(cur)
        if key in seen:
            return gen - seen[key]
        seen[key] = gen
        cur = step(cur)
    return None
