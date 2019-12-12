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
        
    # def test_convert(self):
    #     self.assertEqual(convert(0), 'A')
    #     self.assertEqual(convert(1), 'B')
    #     self.assertEqual(convert(25), 'Z')
    #     self.assertEqual(convert(26), 'BA')
    #     self.assertEqual(convert(27), 'BB')
    #     self.assertEqual(convert(28), 'BC')
    #     self.assertEqual(convert(29), 'BD')
    #     self.assertEqual(convert(51), 'BZ')
    #     self.assertEqual(convert(52), 'CA')
    #     self.assertEqual(convert(675), 'ZZ')
    #     self.assertEqual(convert(676), 'BAA')
    #     self.assertEqual(convert(690), 'BAO')
    #     self.assertEqual(convert(701), 'BAZ')
    #     self.assertEqual(convert(702), 'BBA')
    #     self.assertEqual(convert(703), 'BBB')

if __name__ == '__main__':
    unittest.main()