import unittest
from main2 import *



class MyFirstTests(unittest.TestCase):
    def test_convertor_string_entered(self):
        original = "andela"
        if  original.isalpha():
        
            self.assertEqual(original.isalpha(), True)

        else:
            return False
             
            

    def test_convertor_vowel_start(self):
        original = "andela"
        if len(original) > 0 and original.isalpha():
        
            self.assertEqual(convertor(original), "andelaway")
            self.assertIsInstance(convertor(original), str)

    def test_convertor_consonant_start(self):
        original = "dog"
        if len(original) > 0 and original.isalpha():
        
            self.assertEqual(convertor(original), "ogday")
            self.assertIsInstance(convertor(original), str)

    def test_convertor_no_entry(self):
        original = ""
        self.assertEqual(convertor(original), "empty")