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
                List of inputs, stripped from surrounding spaces
                and line separators 
        """
        with open(file_path) as file:
            return [list(raw_str.strip().rstrip(linesep)) for raw_str
                    in file.readlines()]

    def __init__(
        self,
        file_path:str
    ):
        self.map = self._file_reader(file_path)
        self.symb = {
            "tree":"#"
        }

    @property
    def xmax(self):
        return len(self.map[0])

    @property
    def ymax(self):
        return len(self.map)

    def what_is(
        self,
        coord: typ.Tuple[int, int]
    ):
        x = coord[0] % self.xmax
        y = coord[1]
        return self.map[y][x]


class Walker():

    def __init__(
        self,
        map_,
        pace: typ.Tuple[int, int] = (3, 1),
        origin: typ.Tuple[int, int] = (0, 0),
    ):
        self.origin = origin
        self.pace = pace
        self.map = map_

    @property
    def _trace(self):
        position = self.origin
        trace = list()
        while position[1] < self.map.ymax - 1:
            position = (
                position[0] + self.pace[0],
                position[1] + self.pace[1]
            )
            trace.append(position)
        return trace

    @property
    def tree_encountered(self):
        encounters = [self.map.what_is(coord) 
            for coord in self._trace
        ]
        return len(list(filter(
            lambda el: el==self.map.symb["tree"],
            encounters
        )))
