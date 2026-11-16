import unittest
from life.render import render


class RenderTests(unittest.TestCase):
    def test_render_marks_live_cells(self):
        out = render({(0, 0), (2, 1)}, width=3, height=2, origin=(0, 0), alive="#", dead=".")
        self.assertEqual(out, "#..\n..#")

    def test_empty_board(self):
        self.assertEqual(render(set(), 2, 1, alive="#", dead="."), "..")


if __name__ == "__main__":
    unittest.main()
