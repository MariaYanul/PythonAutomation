import unittest
import hw9_1
from logger import log

class HomeworkTest(unittest.TestCase):

    def test_1(self):
        """Addition, PT"""
        log.info('Addition positive test')
        out = hw9_1.arithmetic(3, 2, '+')
        exp = 5
        self.assertEqual(out, exp)
        log.debug = ('Addition, positsve test')

    def test_2(self):
        """Subtraction, PT"""
        log.info('Subtraction positive test')
        out = hw9_1.arithmetic(100, 57, '-')
        exp = 43
        self.assertEqual(out, exp)

    def test_3(self):
        """Multiplication, PT"""
        log.info('Multiplication positive test')
        out = hw9_1.arithmetic(4, 4, '*')
        exp = 16
        self.assertEqual(out, exp)

    def test_4(self):
        """Division, PT"""
        log.info('Division positive test')
        out = hw9_1.arithmetic(27, 3, '/')
        exp = 9
        self.assertEqual(out, exp)


    @unittest.skip
    def test_5(self):
        """Division by 0, NT"""
        out = hw9_1.arithmetic(27, 0, '/')
        exp = 'Division by 0 is not possible'
        self.assertEqual(out, exp)

    @unittest.skipIf(ZeroDivisionError, 'not support this library')
    def test_6(self):
        """Division by 0, NT"""
        out = hw9_1.arithmetic(27, 0, '/')
        exp = 'Division by 0 is not possible'
        self.assertEqual(out, exp)

if __name__ == '__main__':
    unittest.main(verbosity=2)
