import unittest
import pytest

from advanced_calc import AdvancedCalc

class Calctest(unittest.TestCase):
    calc = AdvancedCalc()

    def test_remain(self):
        self.assertEqual(self.calc.remain(10, 2), 0)

    def test_percent(self):
        self.assertEqual(self.calc.percent(10, 100), 10)

    def test_positve(self):
        self.assertEqual(self.calc.positive(2), True)


