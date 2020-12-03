import os
import pytest as pt

import aoc2020.day3 as d3
import tests.test_common as tc

test_input_file = os.path.join(tc.TESTINPUTDIR, 'day3.txt')

@pt.fixture
def tree_map():
    return d3.TreeMap(
        file_path=test_input_file
    )

class TestTreeMap():


    def test_returns_xmax(
        self,
        tree_map
    ):
        assert tree_map.xmax == 11

    @pt.mark.parametrize(
        "x, y, el",
        [
            (0, 0, "."),
            (2, 0, "#"),
            (1, 2, "#"),
            (12, 0, "."),
        ]
    )
    def test_what_is(
        self,
        tree_map,
        x, y,
        el
    ):
        assert tree_map.what_is((x, y)) == el


class TestRider():

    class_ = d3.Rider

    trace_extract = [
        (3, 1),
        (6, 2),
        (9, 3)
    ]

    def test_trace(
        self,
        tree_map
    ):
        rider = self.class_(
            map_ = tree_map
        )
        trace = rider._trace
        assert trace[:3] == self.trace_extract
        assert len(trace) == rider.map.ymax - 1

    @pt.mark.parametrize(
        "slope, trees",
        [
            ((3, 1), 7),
            ((1, 1), 2),
            ((5, 1), 3),
            ((7, 1), 4),
            ((1, 2), 2)
        ]
    )
    def test_trees_encountered(
        self,
        tree_map,
        slope,
        trees
    ):
        rider = self.class_(
            map_=tree_map,
            slope=slope
        )
        assert rider.trees_encountered == trees
