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


class PasswordDB():
    """
    Class that holds attributes and methods related to
    PasswordDB
    """

    @classmethod
    def _file_reader(
        cls,
        file_path: str,
        linesep: typ.Optional[str] = "\n"
    ) -> typ.List[str]:
        """[summary]

        Args:
            file_path (str):
                Path to file
            linesep (typ.Optional[str], optional): [description]. Defaults to "\n".

        Returns:
            typ.List[str]: [description]
        """
        with open(file_path) as file:
            return [raw_str.strip().rstrip(linesep) for raw_str
                    in file.readlines()]

    @classmethod
    def _parse_input(
        cls,
        i:str
    ) -> typ.Tuple[int, int, str, str]:
        matches = re.match(
            r"^(\d+)-(\d+) (\w): (\w+)$",
            i
        ).groups()
        return (
            int(matches[0]),
            int(matches[1]),
            matches[2],
            matches[3]
        )

    @classmethod
    def _input_reader(
        cls,
        file_path: str,
    ) -> typ.List[typ.Tuple[int, int, str, str]]:
        """
        [summary]

        Args:
            file_path (str):
                [description]

        Returns:
            typ.List[typ.Tuple[int, int, str, str]]:
                [description]
        """
        content = cls._file_reader(
            file_path=file_path
        )
        return list(map(cls._parse_input, content))

    @classmethod
    def valid_counter(
        cls,
        file_path: str,
        ) -> int:
        entries = cls._input_reader(
            file_path = file_path
        )
        return sum([Password(*entry).is_valid
                    for entry in entries])
