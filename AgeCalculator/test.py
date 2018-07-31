import unittest
from main1 import ageCalculator
from datetime import datetime,date


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        birth_year = datetime.strptime("05 05 1995", "%d %m %Y")
        
        self.assertEqual(ageCalculator(birth_year), 23)
        self.assertIsInstance(ageCalculator(birth_year), int)