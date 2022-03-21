from typing import Final


# todo: 왤케 필요 없어보이셔 그리고 클래스명도 뭔가 별로임
# todo: 유효성 검사도 PageRange / all, goal 분리
# todo: 3000 여기랑 테스트에서 사용중인 것 상수로 변경
class Page:
    def __init__(self, _all: range, goal: range) -> None:
        if goal.start not in _all or goal.stop not in _all:
            raise ValueError(f"Invalid progress ranges: {_all}, {goal}")
        self.all: Final = _all
        self.goal: Final = goal

    def __str__(self) -> str:
        return f"Page(all={self.all}, goal={self.goal})"

