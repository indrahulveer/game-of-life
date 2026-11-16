import unittest
from life import patterns
from life.engine import step


class PatternTests(unittest.TestCase):
    def test_glider_moves_diagonally_after_4_gens(self):
        g = patterns.get("glider")
        s = g
        for _ in range(4):
            s = step(s)
        self.assertEqual(s, {(x + 1, y + 1) for x, y in g})

    def test_pulsar_has_period_3(self):
        p = patterns.get("pulsar")
        s = p
        for _ in range(3):
            s = step(s)
        self.assertEqual(s, p)

    def test_unknown_pattern(self):
        with self.assertRaises(KeyError):
            patterns.get("nope")


if __name__ == "__main__":
    unittest.main()
