import functools as ft
import itertools as it
import typing as typ

class ExpenseReport():

    @classmethod
    def _input_reader(
        cls,
        file_path: str,
        linesep: typ.Optional[str] = "\n"
    ) -> typ.List[int]:
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
        nums = cls._sum_2020_getter(
            file_path=file_path,
            r=r
        )
        return ft.reduce(lambda x, y: x*y, nums)
