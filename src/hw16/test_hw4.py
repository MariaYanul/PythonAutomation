import unittest
import hw4

class HomeworkTest(unittest.TestCase):

    def test_1(self):
        """escape_sequences string out compare by value (condition - 3 tab)"""
        out = hw4.escape_sequences(r'\a', 'Bell (alert)')
        exp = '|\t\\a\t|\tBell (alert)\t\t\t|'
        self.assertEqual(out, exp)

    def test_2(self):
        """escape_sequences string out compare by len (condition - 3 tab)"""
        out = hw4.escape_sequences(r'\a', 'Bell (alert)')
        self.assertEqual(len(out), 23)

    def test_3(self):
        """escape_sequences string out compare by count (condition - 3 tab)"""
        out = hw4.escape_sequences(r'\a', 'Bell (alert)')
        exp = out.count('\t')
        self.assertEqual(6, exp)

    def test_4(self):
        """escape_sequences string out compare by empty (condition - 3 tab)"""
        out = hw4.escape_sequences(r'\a', 'Bell (alert)')
        exp = ''
        self.assertEqual(out, exp, 'The test is not failed if the string is not empty')

    def test_5(self):
        """escape_sequences string out compare by value (condition - 4 tab)"""
        out = hw4.escape_sequences(r'\b', 'Backspace')
        exp = '|\t\\b\t|\tBackspace\t\t\t\t|'
        self.assertEqual(out, exp)

    def test_6(self):
        """escape_sequences string out compare by len (condition - 4 tab)"""
        out = hw4.escape_sequences(r'\b', 'Backspace')
        self.assertEqual(len(out), 21)

    def test_7(self):
        """escape_sequences string out compare by count (condition - 4 tab)"""
        out = hw4.escape_sequences(r'\b', 'Backspace')
        exp = out.count('\t')
        self.assertEqual(7, exp)

    def test_8(self):
        """escape_sequences string out compare by empty (condition - 4 tab)"""
        out = hw4.escape_sequences(r'\b', 'Backspace')
        exp = ''
        self.assertEqual(out, exp, 'The test is not failed if the string is not empty')

    def test_9(self):
        """escape_sequences string out compare by value (condition - 1 tab)"""
        out = hw4.escape_sequences(r'\"', 'Double quotation mark \"')
        exp = '|\t\\\"\t|\tDouble quotation mark \"\t|'
        self.assertEqual(out, exp)

    def test_10(self):
        """escape_sequences string out compare by len (condition - 1 tab)"""
        out = hw4.escape_sequences(r'\"', 'Double quotation mark \"')
        self.assertEqual(len(out), 32)

    def test_11(self):
        """escape_sequences string out compare by count (condition - 1 tab)"""
        out = hw4.escape_sequences(r'\"', 'Double quotation mark \"')
        exp = out.count('\t')
        self.assertEqual(4, exp)

    def test_12(self):
        """escape_sequences string out compare by empty (condition - 1 tab)"""
        out = hw4.escape_sequences(r'\"', 'Double quotation mark \"')
        exp = ''
        self.assertEqual(out, exp, 'The test is not failed if the string is not empty')

if __name__ == '__main__':
    unittest.main(verbosity=2)
