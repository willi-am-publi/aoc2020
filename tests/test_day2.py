import os
import pytest as pt

import aoc2020.day2 as d2
import tests.test_common as tc


class TestPassword():

    class_ = d2.Password

    @pt.mark.parametrize(
        "fn, sn, l, e, iv",
        [
            (1, 3, "a", "abcde", True),
            (2, 9, "c", "ccccccccc", True),
            (1, 3, "b", "cdefg", False)
        ]
    )
    def test_is_valid_sled(
        self,
        fn:int, sn:int, l:str, e:str,
        iv: bool
    ):    
        password = self.class_(
            first_num=fn,
            second_num=sn,
            letter=l,
            entry=e
        )
        assert password.is_valid() == iv

    @pt.mark.parametrize(
        "fn, sn, l, e, iv",
        [
            (1, 3, "a", "abcde", True),
            (2, 9, "c", "ccccccccc", False),
            (1, 3, "b", "cdefg", False)
        ]
    )
    def test_is_valid_toboggan(
        self,
        fn:int, sn:int, l:str, e:str,
        iv: bool
    ):    
        password = self.class_(
            first_num=fn,
            second_num=sn,
            letter=l,
            entry=e
        )
        assert password.is_valid(
            policy=d2.toboggan_policy
        ) == iv


class TestPasswordDB():

    class_ = d2.PasswordDB
    file = os.path.join(tc.TESTINPUTDIR, 'day2')

    def test_file_reader_is_list(self):
        content = self.class_._file_reader(
            file_path = self.file
        )
        assert isinstance(content, list) == True

    __parsed_entry = [
            (1, 3, "a", "abcde"),
            (1, 3, "b", "cdefg"),
            (2, 9, "c", "ccccccccc")
    ]

    def test_parse_input(self):
        assert self.class_._parse_input(
            i = "1-3 a: abcde"
        ) == self.__parsed_entry[0]

    def test_input_reader(self):
        input_ = self.class_._input_reader(
            file_path = self.file
        )
        assert input_ == self.__parsed_entry

    def test_valid_counter(self):
        assert self.class_.valid_counter(
            file_path = self.file
        ) == 2
