import unittest
from main import convert, getLetter, getA1Notation

class A1NotationTest(unittest.TestCase):
    def test1_getLetter(self):
        self.assertEqual(getLetter(0), 'A')
        self.assertEqual(getLetter(1), 'B')
        self.assertEqual(getLetter(25), 'Z')
        self.assertEqual(getLetter(26), 'A')
        self.assertEqual(getLetter(27), 'B')
        self.assertEqual(getLetter(51), 'Z')
        self.assertEqual(getLetter(52), 'A')
        
    def test2_convert(self):
        self.assertEqual(convert(0), 'A')
        self.assertEqual(convert(1), 'B')
        self.assertEqual(convert(25), 'Z')
        self.assertEqual(convert(26), 'BA')
        self.assertEqual(convert(27), 'BB')
        self.assertEqual(convert(28), 'BC')
        self.assertEqual(convert(29), 'BD')
        self.assertEqual(convert(51), 'BZ')
        self.assertEqual(convert(52), 'CA')
        self.assertEqual(convert(675), 'ZZ')
        self.assertEqual(convert(676), 'BAA')
        self.assertEqual(convert(690), 'BAO')
        self.assertEqual(convert(701), 'BAZ')
        self.assertEqual(convert(702), 'BBA')
        self.assertEqual(convert(703), 'BBB')

    def test3_getA1Notation(self):
        self.assertEqual(getA1Notation(1), 'A')
        self.assertEqual(getA1Notation(2), 'B')
        self.assertEqual(getA1Notation(25), 'Y')
        self.assertEqual(getA1Notation(26), 'Z')

        self.assertEqual(getA1Notation(27), 'AA')
        self.assertEqual(getA1Notation(28), 'AB')
        self.assertEqual(getA1Notation(51), 'AY')
        self.assertEqual(getA1Notation(52), 'AZ')
        self.assertEqual(getA1Notation(53), 'BA')
        self.assertEqual(getA1Notation(54), 'BB')

        self.assertEqual(getA1Notation(675), 'YY')
        self.assertEqual(getA1Notation(676), 'YZ')
        self.assertEqual(getA1Notation(677), 'ZA')
        self.assertEqual(getA1Notation(678), 'ZB')


if __name__ == '__main__':
    unittest.main()