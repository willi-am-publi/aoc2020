import os
import pytest as pt

import aoc2020.day2 as d2


class TestPassword():

    class_ = d2.Password

    @pt.mark.parametrize(
        "ll, ul, l, e, iv",
        [
            (1, 3, "a", "abcde", True),
            (2, 9, "c", "ccccccccc", True),
            (1, 3, "b", "cdefg", False)
        ]
    )
    def test_is_valid(
        self,
        ll:int, ul:int, l:str, e:str,
        iv: bool
    ):    
        password = self.class_(
            lower_limit=ll,
            upper_limit=ul,
            letter=l,
            entry=e
        )
        assert password.is_valid == iv
