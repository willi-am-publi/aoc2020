import typing as typ
import re

def sled_policy(
    first_num:int,
    second_num:int,
    letter:str,
    entry:str,
) -> bool:
    """
    Reflects sled company password policy

    Args:
        first_num (int):
            letter occurences lower limit
        second_num (int):
            letter occurences upper limit
        letter (str):
            letter of interest
        entry (str):
            password entry

    Returns:
        bool: 
            whether or not entry conforms to sled company
            password policy
    """
    matches = len(re.findall(
        letter,
        entry
    ))
    return first_num <= matches <= second_num

def toboggan_policy(
    first_num:int,
    second_num:int,
    letter:str,
    entry:str,
) -> bool:
    """
    Reflects toboggan company password policy

    Args:
        first_num (int):
            first index letter matching check in entry
        second_num (int):
            second index letter matching check in entry
        letter (str):
            letter of interest
        entry (str):
            password entry

    Returns:
        bool: 
            whether or not entry conforms to toboggan company
            password policy
    """
    return ((entry[first_num-1] == letter)
            != (entry[second_num-1] == letter)
    )

class Password():
    """
    Class that holds attributes and methods related to Password
    """

    def __init__(
            self,
            first_num:int,
            second_num:int,
            letter:str,
            entry:str
    ):
        """s/e

        Args:
            first_num (int):
                first condition, interpretation depends on policy
            second_num (int):
                first condition, interpretation depends on policy
            letter (str):
                letter of interest
            entry (str):
                (possibbly corrupted) entry password
        """
        self.kwargs = {
            "first_num": first_num,
            "second_num": second_num,
            "letter": letter,
            "entry": entry,
        }

    def is_valid(
        self,
        policy: typ.Optional[typ.Callable] = sled_policy
    ) -> bool:
        return policy(**self.kwargs)


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
        """Reads input file

        Args:
            file_path (str):
                Path to file
            linesep (typ.Optional[str], optional): 
                Line separator. Defaults to "\n".

        Returns:
            typ.List[str]:
                List of inputs, stripped from surrounding spaces
                and line separators 
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
        Parses and formats entries to tuples

        Args:
            file_path (str):
                File path

        Returns:
            typ.List[typ.Tuple[int, int, str, str]]:
                Tuples holding entries informations
        """
        content = cls._file_reader(
            file_path=file_path
        )
        return list(map(cls._parse_input, content))

    @classmethod
    def valid_counter(
        cls,
        file_path: str,
        policy: typ.Optional[typ.Callable] = sled_policy
        ) -> int:
        """
        Counts number of entries conforming to policy

        Args:
            file_path (str):
                File path
            policy (typ.Optional[typ.Callable], optional):
                Policy to use. Defaults to sled_policy.

        Returns:
            int: Number of valid entries
        """
        entries = cls._input_reader(
            file_path = file_path            
        )
        return sum([Password(*entry).is_valid(
                policy=policy
            ) for entry in entries]
        )
