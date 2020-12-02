import os

import aoc2020.core as co

from aoc2020 import __version__


def test_version():
    assert __version__ == '0.1.0'


TESTDIR = os.path.dirname(__file__)
TESTINPUTDIR = os.path.join(TESTDIR, 'inputs')

class TestExpenseReport():

    class_ = co.ExpenseReport
    file = os.path.join(TESTINPUTDIR, 'day1')

    def test_input_reader_all_ints(self):

        expense_report = self.class_._input_reader(self.file)

        assert all([isinstance(num, int) for num in expense_report])

    def test_sum_equals_2020(self):

        numbers = self.class_._sum_2020_getter(self.file)
        expected_numbers = [1721, 299]
        assert set(numbers).issubset(set(expected_numbers))

    def test_product_sum_equals_2020(self):

        assert self.class_.product_sum_equals_2020(self.file) == 514579

    def test_sum_r3_equals_2020(self):

        numbers = self.class_._sum_2020_getter(
            self.file,
            r=3
        )
        expected_numbers = [979, 366, 675]
        assert set(numbers).issubset(set(expected_numbers))
