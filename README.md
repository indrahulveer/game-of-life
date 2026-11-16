# Game of Life

Conway's Game of Life for your terminal, in pure Python 3.10+ with no dependencies.

- Sparse, unbounded grid (patterns can fly off forever)
- Built-in pattern library: glider, pulsar, Gosper glider gun, R-pentomino, ...
- Load and export patterns in standard **RLE** format
- Random soups with reproducible seeds
- Period detection for oscillators and spaceships

## Usage

```bash
python -m life --list                 # available patterns
python -m life gosper-gun --gens 200  # animate a pattern
python -m life --random 0.3 --seed 7  # random soup
python -m life --rle my_pattern.rle   # load RLE file
python -m life pulsar --period        # -> period: 3
python -m life glider --export-rle    # print as RLE
```

## Development

```bash
python -m unittest discover -s tests -t .
```

## Layout

| Module | Purpose |
| --- | --- |
| `life/engine.py` | `step()` — next generation from a set of live cells |
| `life/patterns.py` | named pattern library |
| `life/render.py` | text rendering of a viewport |
| `life/rle.py` | RLE parser / serializer |
| `life/analysis.py` | random soups, period detection |
