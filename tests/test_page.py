import pytest
from book.page import Page


# 목표 페이지가 전체 페이지 범위가 아닌 경우 예외가 발생한다
def test_all_page_not_contains_goal_page_to_raises():
    with pytest.raises(ValueError):
        Page(_all=range(10, 100), goal=range(10, 999))
    with pytest.raises(ValueError):
        Page(_all=range(10, 100), goal=range(1, 99))
