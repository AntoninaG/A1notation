import unittest
from main import convert, getLetter

class A1NotationTest(unittest.TestCase):
    def test_getLetter(self):
        self.assertEqual(getLetter(1), 'A')
        self.assertEqual(getLetter(2), 'B')
        self.assertEqual(getLetter(25), 'Y')
        self.assertEqual(getLetter(26), 'Z')
        self.assertEqual(getLetter(27), 'A')
        self.assertEqual(getLetter(28), 'B')
        self.assertEqual(getLetter(52), 'Z')
        self.assertEqual(getLetter(53), 'A')
        
    def test_convert(self):
        self.assertEqual(convert(1), 'A')
        self.assertEqual(convert(2), 'B')
        self.assertEqual(convert(26), 'Z')
        self.assertEqual(convert(27), 'AA')
        self.assertEqual(convert(28), 'AB')
        self.assertEqual(convert(29), 'AC')
        self.assertEqual(convert(30), 'AD')
        self.assertEqual(convert(52), 'AZ')
        self.assertEqual(convert(53), 'BA')
        self.assertEqual(convert(676), 'YZ')
        self.assertEqual(convert(677), 'ZA')
        self.assertEqual(convert(703), 'AAA')
        self.assertEqual(convert(717), 'AAO')
        self.assertEqual(convert(728), 'AAZ')
        self.assertEqual(convert(729), 'ABA')
        self.assertEqual(convert(730), 'ABB')
        self.assertEqual(convert(18278), 'ZZZ')

if __name__ == '__main__':
    unittest.main()