import functools as ft
import itertools as it
import typing as typ

class ExpenseReport():
    """
    Class that holds attributes and methods related to Expense Report
    """

    @classmethod
    def _input_reader(
        cls,
        file_path: str,
        linesep: typ.Optional[str] = "\n"
    ) -> typ.List[int]:
        """
        Reads text file containing numbers

        Args:
            file_path (str): 
                Path to file
            linesep (typ.Optional[str], optional): 
                Line separator. Defaults to "\n".

        Returns:
            typ.List[int]: List of integers

        :Example:
            >>> er = ExpenseReport._input_reader(
            >>>     'tests/inputs/day1'
            >>> )
            >>> type(er)
            list
        """
        with open(file_path) as file:
            inputs = file.readlines()
            inputs = [raw_str.rstrip(linesep) for raw_str in inputs]
            return [int(string) for string in inputs]

    @classmethod
    def _sum_2020_getter(
        cls,
        file_path: str,
        r: typ.Optional[int] = 2
    ) -> typ.Tuple[int, ...]:
        """Founds integers which sums equals to 2020

        Args:
            file_path (str):
                File path
            r (typ.Optional[int], optional):
                Number of integers to sum up. Defaults to 2.

        Returns:
            typ.Tuple[int, ...]: 
                Tuple of integers, number of integers depends on r

        :Example:
            >>> ExpenseReport._sum_2020_getter(
            >>>     'tests/inputs/day1'
            >>> )
            (1721, 299)

        """
        target = 2020
        expense_report = cls._input_reader(file_path=file_path)
        for combination in it.permutations(
          iterable=expense_report,
          r=r  
        ):
            if ft.reduce(lambda x, y,: x+y, combination) == target:
                return combination

    @classmethod
    def product_sum_equals_2020(
        cls,
        file_path: str,
        r: typ.Optional[int] = 2
    ) -> int:
        """[summary]

        Args:
            file_path (str): [description]
            r (typ.Optional[int], optional): [description]. Defaults to 2.

        Returns:
            int: [description]

        :Example:
            >>> ExpenseReport.product_sum_equals_2020(
            >>>     'tests/inputs/day1'
            >>> )
            514579

        """
        nums = cls._sum_2020_getter(
            file_path=file_path,
            r=r
        )
        return ft.reduce(lambda x, y: x*y, nums)
