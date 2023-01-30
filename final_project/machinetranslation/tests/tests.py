import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
    
    def test2(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 
    
    def test3(self): 
        self.assertEqual(french_to_english(''), 'Error: The input text is empty')

    def test4(self): 
        self.assertEqual(english_to_french(''), 'Error: The input text is empty')

unittest.main()