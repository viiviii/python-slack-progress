from typing import Final


class Range:
    def __init__(self, first: int, last: int) -> None:
        Range._validate(first, last)
        self.first: Final = first
        self.last: Final = last

    def __str__(self) -> None:
        return f"Range({self.first}, {self.last})"

    @staticmethod
    def _validate(first: int, last: int) -> None:
        if not Range._valid_types(first, last):
            raise TypeError(f"Arguments is not int type: first={type(first)}, last={type(last)}")

    @staticmethod
    def _valid_types(first: int, last: int) -> bool:
        return type(first) is int and type(last) is int


class Page:
    def __init__(self, _all: Range, goal: Range) -> None:
        Page._validate(_all, goal)
        self.all: Final = _all
        self.goal: Final = goal

    def __str__(self) -> None:
        return f"Page(all={self.all}, goal={self.goal})"

    @staticmethod
    def _validate(_all: Range, goal: Range) -> None:
        if not Page._valid_ranges(_all, goal):
            raise ValueError(f"Invalid progress ranges: {_all}, {goal}")

    @staticmethod
    def _valid_ranges(_all: Range, goal: Range) -> bool:
        return 0 < _all.first <= goal.first <= goal.last <= _all.last < 3000
