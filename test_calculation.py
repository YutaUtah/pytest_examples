# if you want to run unittest, firstly, create this file 'test_calculation.py' and go to edit configuration to select unit test
# the path has to be under this file
# below commented example is an example that you execute pytest using unittest but you can also simply use pytest
import unittest
import calculation
import pytest

# no need to create class just function is good under pytest config
class TestCal(object):
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        assert cal.add_num_and_double(1,1) == 4

    @pytest.mark.skip(reason='skip!') # go to config to set up option to be -rs
    def test_add_num_and_double(self):
        with pytest.raises(ValueError):
            cal = calculation.Cal()
            cal.add_num_and_double('1', '1')



#     def setUp(self) -> None:
#         print('setup')
#         self.cal = calculation.Cal()
#
#     def tearDown(self) -> None:
#         print('clean up')
#         del self.cal
#
#     # if you wish to skip unittest
#     @unittest.skip('skip this test')
#     def test_add_num_and_double_raise(self):
#         # if exception occurs, the test succeeds
#         with self.assertRaises(ValueError):
#             self.cal.add_num_and_double('1', '1')

# this is for the terminal
# if __name__ == '__main__':
#     unittest.main()