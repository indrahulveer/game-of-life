"""A small library of classic Game of Life patterns."""
from .engine import Cell

PATTERNS: dict[str, list[str]] = {
    "block": ["##", "##"],
    "blinker": ["###"],
    "glider": [".#.", "..#", "###"],
    "toad": [".###", "###."],
    "beacon": ["##..", "##..", "..##", "..##"],
    "pulsar": [
        "..###...###..", ".............", "#....#.#....#", "#....#.#....#",
        "#....#.#....#", "..###...###..", ".............", "..###...###..",
        "#....#.#....#", "#....#.#....#", "#....#.#....#", ".............",
        "..###...###..",
    ],
    "lwss": [".#..#", "#....", "#...#", "####."],
    "r-pentomino": [".##", "##.", ".#."],
    "gosper-gun": [
        "........................#...........",
        "......................#.#...........",
        "............##......##............##",
        "...........#...#....##............##",
        "##........#.....#...##..............",
        "##........#...#.##....#.#...........",
        "..........#.....#.......#...........",
        "...........#...#....................",
        "............##......................",
    ],
}


def parse(rows: list[str], offset: Cell = (0, 0)) -> set[Cell]:
    """Convert '#'/'.' rows into a set of live cells."""
    ox, oy = offset
    return {
        (x + ox, y + oy)
        for y, row in enumerate(rows)
        for x, ch in enumerate(row)
        if ch == "#"
    }


def get(name: str, offset: Cell = (0, 0)) -> set[Cell]:
    try:
        return parse(PATTERNS[name], offset)
    except KeyError:
        raise KeyError(f"unknown pattern {name!r}; choose from {', '.join(PATTERNS)}") from None
