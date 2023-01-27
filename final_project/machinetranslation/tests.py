import unittest
from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') 
    
    def test2(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') 
    
    def test3(self): 
        self.assertEqual(frenchToEnglish(''), 'Error: The input text is empty')

    def test4(self): 
        self.assertEqual(englishToFrench(''), 'Error: The input text is empty')

unittest.main()