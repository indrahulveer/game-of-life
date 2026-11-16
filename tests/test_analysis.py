import unittest
from life import patterns
from life.analysis import find_period, random_soup


class AnalysisTests(unittest.TestCase):
    def test_periods(self):
        self.assertEqual(find_period(patterns.get("block")), 1)
        self.assertEqual(find_period(patterns.get("blinker")), 2)
        self.assertEqual(find_period(patterns.get("pulsar")), 3)

    def test_glider_repeats_every_4_up_to_translation(self):
        self.assertEqual(find_period(patterns.get("glider")), 4)

    def test_soup_is_reproducible(self):
        self.assertEqual(random_soup(10, 10, seed=1), random_soup(10, 10, seed=1))


if __name__ == "__main__":
    unittest.main()
