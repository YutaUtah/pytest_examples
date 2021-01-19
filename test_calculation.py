# if you want to run unittest, firstly, create this file 'test_calculation.py' and go to edit configuration to select unit test
# the path has to be under this file
import unittest
import calculation
import pytest


class CalTest(unittest.TestCase):
    def setUp(self) -> None:
        print('setup')
        self.cal = calculation.Cal()

    def tearDown(self) -> None:
        print('clean up')
        del self.cal

    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    # if you wish to skip unittest
    @unittest.skip('skip this test')
    def test_add_num_and_double_raise(self):
        # if exception occurs, the test succeeds
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')

# this is for the terminal
# if __name__ == '__main__':
#     unittest.main()