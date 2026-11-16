import unittest
from life import patterns
from life.rle import parse_rle, to_rle

GLIDER = "#C glider\nx = 3, y = 3, rule = B3/S23\nbob$2bo$3o!\n"


class RleTests(unittest.TestCase):
    def test_parse_glider(self):
        self.assertEqual(parse_rle(GLIDER), patterns.get("glider"))

    def test_roundtrip_all_patterns(self):
        for name in patterns.PATTERNS:
            cells = patterns.get(name)
            self.assertEqual(parse_rle(to_rle(cells)), cells, name)

    def test_multi_row_skip(self):
        self.assertEqual(parse_rle("o2$o!"), {(0, 0), (0, 2)})


if __name__ == "__main__":
    unittest.main()
