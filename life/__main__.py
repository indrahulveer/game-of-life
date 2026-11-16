"""Command line interface: python -m life glider --gens 50"""
import argparse
import sys
import time

from . import patterns
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
    args = p.parse_args(argv)

    if args.list:
        print("\n".join(sorted(patterns.PATTERNS)))
        return 0
    try:
        live = patterns.get(args.pattern, offset=(args.width // 4, args.height // 4))
    except KeyError as e:
        print(e.args[0], file=sys.stderr)
        return 2

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
