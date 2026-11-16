"""Command line interface: python -m life glider --gens 50"""
import argparse
import sys
import time

from . import patterns
from .analysis import find_period, random_soup
from .rle import parse_rle, to_rle
from .engine import step
from .render import render


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="life", description="Conway's Game of Life in your terminal")
    p.add_argument("pattern", nargs="?", default="glider", help="pattern name (see --list)")
    p.add_argument("--list", action="store_true", help="list available patterns and exit")
    p.add_argument("--gens", type=int, default=100, help="number of generations (default 100)")
    p.add_argument("--delay", type=float, default=0.08, help="seconds between frames")
    p.add_argument("--width", type=int, default=60)
    p.add_argument("--height", type=int, default=24)
    p.add_argument("--random", type=float, metavar="DENSITY", help="start from a random soup instead of a pattern")
    p.add_argument("--seed", type=int, help="seed for --random (reproducible runs)")
    p.add_argument("--rle", metavar="FILE", help="load a pattern from an RLE file")
    p.add_argument("--export-rle", action="store_true", help="print the starting pattern as RLE and exit")
    p.add_argument("--period", action="store_true", help="report the pattern's period and exit")
    args = p.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):  # Windows consoles may default to cp1252
        sys.stdout.reconfigure(encoding="utf-8")

    if args.list:
        print("\n".join(sorted(patterns.PATTERNS)))
        return 0
    try:
        if args.random is not None:
            live = random_soup(args.width, args.height, args.random, args.seed)
        elif args.rle:
            with open(args.rle, encoding="utf-8") as f:
                live = parse_rle(f.read())
        else:
            live = patterns.get(args.pattern, offset=(args.width // 4, args.height // 4))
    except (KeyError, OSError) as e:
        print(e.args[0] if isinstance(e, KeyError) else e, file=sys.stderr)
        return 2

    if args.export_rle:
        print(to_rle(live))
        return 0
    if args.period:
        period = find_period(live)
        print(f"period: {period}" if period else "no repeat found within 500 generations")
        return 0

    for gen in range(args.gens + 1):
        sys.stdout.write("\x1b[H\x1b[J")  # clear screen
        print(render(live, args.width, args.height, origin=(0, 0)))
        print(f"\ngeneration {gen}  population {len(live)}")
        if not live:
            break
        time.sleep(args.delay)
        live = step(live)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
