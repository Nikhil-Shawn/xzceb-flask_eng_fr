import unittest

from translator import englishToFrench
from translator import frenchToEnglish

class Test_Translator(unittest.TestCase):
    
    def test_e2f(self):
        self.assertEqual(englishToFrench('im fine'),'Amende im')
    
    def test_e2f_2(self):
        self.assertEqual(englishToFrench('Hello, How are you doing today?'),'Bonjour, comment faites-vous aujourd\'hui?')

    def test_e2f_3(self):
        self.assertNotEqual(englishToFrench('None'),"")

    def test_e2f_4(self):
        self.assertNotEqual(englishToFrench(0),0)

class Test_Translator1(unittest.TestCase):

    def test_f2e(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
    
    def test_f2e_2(self):
        self.assertEqual(frenchToEnglish('Bonjour, comment faites-vous aujourd\'hui?'),'Hello, how do you do it today?')

    def test_f2e_3(self):
        self.assertNotEqual(frenchToEnglish('None'),"")

    def test_f2e_4(self):
        self.assertNotEqual(frenchToEnglish(0),0)


    
    
unittest.main()
