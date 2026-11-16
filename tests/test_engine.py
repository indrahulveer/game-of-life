import unittest
from life.engine import step


class EngineTests(unittest.TestCase):
    def test_block_is_stable(self):
        block = {(0, 0), (1, 0), (0, 1), (1, 1)}
        self.assertEqual(step(block), block)

    def test_blinker_oscillates(self):
        h = {(0, 1), (1, 1), (2, 1)}
        v = {(1, 0), (1, 1), (1, 2)}
        self.assertEqual(step(h), v)
        self.assertEqual(step(v), h)

    def test_lonely_cell_dies(self):
        self.assertEqual(step({(5, 5)}), set())


if __name__ == "__main__":
    unittest.main()
