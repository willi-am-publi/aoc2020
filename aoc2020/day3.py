import functools as ft

import typing as typ

class TreeMap():

    def _file_reader(
        self,
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
                List of inputs, stripped from surrounding sslopes
                and line separators 
        """
        with open(file_path) as file:
            return [list(raw_str.strip().rstrip(linesep)) for raw_str
                    in file.readlines()]

    def __init__(
        self,
        file_path:str
    ):
        """
        s/e

        Args:
            file_path (str): Map file path
        """
        self.map = self._file_reader(file_path)
        self.symb = {
            "tree":"#"
        }

    @property
    def xmax(self) -> int:
        """
        Width of single map

        Returns:
            int: number of map chars width-wise
        """
        return len(self.map[0])

    @property
    def ymax(self):
        """
        Height of single map

        Returns:
            int: number of map chars height-wise
        """

        return len(self.map)

    def what_is(
        self,
        coord: typ.Tuple[int, int]
    ) -> str:
        """
        Returns the character at coordinates

        Args:
            coord (typ.Tuple[int, int]): 
                coordinates (x, y)

        Returns:
            str: map content at coordinates
        """
        x = coord[0] % self.xmax
        y = coord[1]
        return self.map[y][x]


class Rider():

    def __init__(
        self,
        map_,
        slope: typ.Tuple[int, int] = (3, 1),
        origin: typ.Tuple[int, int] = (0, 0),
    ):
        """
        s/e

        Args:
            map_ ([type]):
                TreeMap instance
            slope (typ.Tuple[int, int], optional):
                Slope at which the rider moves on the map.
                Defaults to (3, 1).
            origin (typ.Tuple[int, int], optional): 
                Point of origin, corresponds to the top-left corner.
                Defaults to (0, 0).
        """
        self.origin = origin
        self.slope = slope
        self.map = map_

    @property
    def _trace(self) -> typ.List[typ.Tuple[int, int]]:
        """
        Determines the jumps coordinates for the rider to reach
        the bottom of the map

        Returns:
            typ.List[Tuple[int, int]]:
                Sequence of coordinates
        """
        position = self.origin
        trace = list()
        while position[1] < self.map.ymax - 1:
            position = (
                position[0] + self.slope[0],
                position[1] + self.slope[1]
            )
            trace.append(position)
        return trace

    @property
    def trees_encountered(self) -> int:
        """
        Counts of encountered trees during the toboggan ride

        Returns:
            int:
                Number of encountered trees
        """
        encounters = [self.map.what_is(coord) 
            for coord in self._trace
        ]
        return len(list(filter(
            lambda el: el==self.map.symb["tree"],
            encounters
        )))

if __name__ == "__main__":
    slopes = [
        (3, 1),
        (1, 1),
        (5, 1),
        (7, 1),
        (1, 2)        
    ]
    trees_encountered_sensit = list()
    for slope in slopes:
        trees_encountered_sensit.append(
            Rider(
                map_=TreeMap('inputs/input_day_3'),
                slope=slope
            ).trees_encountered
        )
    print(ft.reduce(
        lambda x, y: x*y,
        trees_encountered_sensit
    ))
