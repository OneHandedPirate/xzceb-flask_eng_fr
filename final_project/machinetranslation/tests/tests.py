import unittest

from maci import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french('Day'), 'Jour')
        self.assertEqual(english_to_french('Mother'), 'Mère')
        self.assertEqual(english_to_french('Hi'), 'Salut')
        self.assertEqual(english_to_french(''), 'You have entered an empty string')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english('Jour'), 'Day')
        self.assertEqual(french_to_english('Mère'), 'Mother')
        self.assertEqual(french_to_english('Salut'), 'Hi')
        self.assertEqual(french_to_english(''), 'Vous avez entré une chaîne vide')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


unittest.main()