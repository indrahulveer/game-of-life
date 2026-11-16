"""Parse/serialize the standard RLE pattern format used by LifeWiki and Golly."""
import re

from .engine import Cell


def parse_rle(text: str) -> set[Cell]:
    body = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.lower().startswith("x"):
            continue
        body.append(line)
    data = "".join(body)
    cells: set[Cell] = set()
    x = y = 0
    for count, tag in re.findall(r"(\d*)([bo$!])", data):
        n = int(count) if count else 1
        if tag == "b":
            x += n
        elif tag == "o":
            cells.update((x + i, y) for i in range(n))
            x += n
        elif tag == "$":
            y += n
            x = 0
        else:  # '!'
            break
    return cells


def to_rle(live: set[Cell]) -> str:
    if not live:
        return "x = 0, y = 0, rule = B3/S23\n!"
    x0 = min(x for x, _ in live)
    y0 = min(y for _, y in live)
    w = max(x for x, _ in live) - x0 + 1
    h = max(y for _, y in live) - y0 + 1

    def run(n: int, tag: str) -> str:
        return (str(n) if n > 1 else "") + tag

    out = []
    for row in range(h):
        xs = sorted(x - x0 for x, y in live if y - y0 == row)
        pos = 0
        parts = []
        for x in xs:
            if x > pos:
                parts.append(("b", x - pos))
                pos = x
            if parts and parts[-1][0] == "o":
                parts[-1] = ("o", parts[-1][1] + 1)
            else:
                parts.append(("o", 1))
            pos += 1
        out.append("".join(run(n, t) for t, n in parts))
    return f"x = {w}, y = {h}, rule = B3/S23\n" + "$".join(out) + "!"
