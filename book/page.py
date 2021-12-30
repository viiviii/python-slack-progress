from typing import Final


class PageRange:
    def __init__(self, first: int, last: int) -> None:
        PageRange._validate(first, last)
        self.first: Final = first
        self.last: Final = last

    def __str__(self) -> None:
        return f"p.{self.first}~{self.last}"

    @staticmethod
    def _validate(first: int, last: int) -> None:
        if not PageRange._valid_types(first, last):
            raise TypeError(f"Arguments is not int type: first={type(first)}, last={type(last)}")

    @staticmethod
    def _valid_types(first: int, last: int) -> bool:
        return type(first) is int and type(last) is int

    def includes(self, page: int) -> bool:
        return self.first <= page <= self.last


class Page:
    def __init__(self, _all: PageRange, goal: PageRange) -> None:
        Page._validate(_all, goal)
        self.all: Final = _all
        self.goal: Final = goal

    def __str__(self) -> None:
        return f"Page(all={self.all}, goal={self.goal})"

    @staticmethod
    def _validate(_all: PageRange, goal: PageRange) -> None:
        if not Page._valid_ranges(_all, goal):
            raise ValueError(f"Invalid progress ranges: {_all}, {goal}")

    @staticmethod
    def _valid_ranges(_all: PageRange, goal: PageRange) -> bool:
        return 0 < _all.first <= goal.first <= goal.last <= _all.last < 3000
