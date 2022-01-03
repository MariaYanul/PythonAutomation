import unittest
import hw5

class HomeworkTest(unittest.TestCase):

    def test_task_one(self):
        """if out is str"""
        out = hw5.task_one()
        self.assertIsInstance(out, str)

    def test_task_two(self):
        """if out is list"""
        out = hw5.task_two()
        self.assertIsInstance(out, str)

    def test_task_three(self):
        """if out is str"""
        out = hw5.task_three()
        self.assertIsInstance(out, str)

    def test_task_four(self):
        """if out is list"""
        out = hw5.task_four()
        self.assertIsInstance(out, list)

    def test_task_five(self):
        """if out is list"""
        out = hw5.task_five()
        self.assertIsInstance(out, list)



if __name__ == '__main__':
    unittest.main(verbosity=2)