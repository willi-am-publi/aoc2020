import typing as typ
import re


class Password():
    """
    Class that holds attributes and methods related to Password
    """

    def __init__(
            self,
            lower_limit:int,
            upper_limit:int,
            letter:str,
            entry:str
    ):
        """s/e

        Args:
            lower_limit (int): letter count lower limit
            upper_limit (int): letter count upper limit
            letter (str): letter of interest
            entry (str): (possibbly corrupted) entry password
        """
        self.ll = lower_limit
        self.ul = upper_limit
        self.letter = letter
        self.entry = entry

    @property
    def is_valid(self) -> bool:
        matches = len(re.findall(
            self.letter,
            self.entry
        ))
        return self.ll <= matches <= self.ul
