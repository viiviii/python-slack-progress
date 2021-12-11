import pytest
from progress.page import Page, Range


# 범위 값은 `int type`이다
def test_range_values_type_is_int():
    _range = Range(0, 0)
    return type(_range.first) is int and type(_range.last) is int


# 범위 값이 `int type`이 아니면 예외가 발생한다
def test_range_values_type_is_not_int_to_raises():
    with pytest.raises(TypeError):
        Range('1', 0)
    with pytest.raises(TypeError):
        Range(0, 3.4)


# 모든 페이지 범위는 양수이다
def test_page_has_positive_values():
    page = Page(_all=Range(1, 1), goal=Range(1, 1))
    assert page.all.first, page.all.last > 0
    assert page.goal.first, page.goal.last > 0


# 페이지가 양수가 아니면 예외가 발생한다
def test_not_positive_to_raises():
    with pytest.raises(ValueError):
        Page(_all=Range(0, 1), goal=Range(1, 1))
    with pytest.raises(ValueError):
        Page(_all=Range(-1, 1), goal=Range(1, 1))


# 페이지가 3000보다 크면 예외가 발생한다
def test_exceeded_max_range_to_raises():
    with pytest.raises(ValueError):
        Page(_all=Range(1, 3000), goal=Range(1, 1))


# 시작 페이지는 마지막 페이지보다 작거나 같다
def test_first_page_is_not_greater_than_last_page():
    page = Page(_all=Range(1, 10), goal=Range(3, 3))
    assert page.all.first <= page.all.last
    assert page.goal.first <= page.goal.last


# 시작 페이지가 마지막 페이지보다 크면 예외가 발생한다
def test_first_page_is_greater_than_last_page_to_raises():
    with pytest.raises(ValueError):
        Page(_all=Range(100, 1), goal=Range(1, 1))
    with pytest.raises(ValueError):
        Page(_all=Range(1, 1), goal=Range(100, 1))


# 목표 페이지는 전체 페이지에 포함된다
def test_all_page_contains_goal_page():
    page = Page(_all=Range(1, 10), goal=Range(3, 3))
    assert page.all.first <= page.goal.first <= page.goal.last <= page.all.last


# 목표 페이지가 전체 페이지에 포함되지 않으면 예외가 발생한다
def test_all_page_not_contains_goal_page_to_raises():
    with pytest.raises(ValueError):
        Page(_all=Range(10, 100), goal=Range(10, 130))
    with pytest.raises(ValueError):
        Page(_all=Range(10, 100), goal=Range(3, 99))
