from book.page import PageRange
from book.progress import progress, _percent, _emoji


def test_progress():
    goal = PageRange(1, 4)
    current = 1
    assert "💚🤍🤍🤍🤍 *25*%" == progress(current, goal)


def test_progress_percent_first_page_is_1():
    first_page = 1
    goal = PageRange(first_page, 4)
    assert 75 == _percent(3, goal)


def test_progress_percent_first_page_is_not_1():
    first_page = 3
    goal = PageRange(first_page, 6)
    assert 25 == _percent(3, goal)
    assert 100 == _percent(6, goal)


def test_progress_percent_page_is_less_than_goal_range():
    goal = PageRange(30, 140)
    assert 0 == _percent(0, goal)
    assert 0 == _percent(29, goal)


def test_progress_percent_page_is_greater_than_goal_range():
    goal = PageRange(30, 140)
    assert 109 == _percent(150, goal)


def test_progress_emoji():
    assert "🤍🤍🤍🤍🤍" == _emoji(percent=0)
    assert "💚🤍🤍🤍🤍" == _emoji(percent=20)
    assert "💚💚🤍🤍🤍" == _emoji(percent=40)
    assert "💚💚💚🤍🤍" == _emoji(percent=60)
    assert "💚💚💚💚🤍" == _emoji(percent=80)
    assert "💚💚💚💚💚" == _emoji(percent=100)


def test_progress_emoji_over_100_percent():
    assert "💚💚💚💚💚" == _emoji(percent=333)
