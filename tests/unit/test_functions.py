"""
This will test the functions implemented in main.py
"""

from pathlib import Path
import sys
import unittest

path = str(
    Path(Path(Path(__file__).parent.absolute()).parent.absolute()).parent.absolute()
)
sys.path.insert(0, path)

from projectCICD.AESClone import main

# print(main.to_ascii("H"))


class TestFunction(unittest.TestCase):
    def test_ascii(self):
        self.assertEqual([72], main.to_ascii("H"))


if __name__ == "__main__":
    unittest.main()
