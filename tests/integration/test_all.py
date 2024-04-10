from pathlib import Path
import sys
import unittest

path = str(
    Path(Path(Path(__file__).parent.absolute()).parent.absolute()).parent.absolute()
)
sys.path.insert(0, path)

from projectCICD.AESClone import main


class TestAll(unittest.TestCase):
    def test_integ_func(self):
        self.assertEqual("H", main.integ_test("H"))


if __name__ == "__main__":
    unittest.main()
