from book.page import PageRange
from book.progress import progress_percent, progress_emoji


def test_progress_percent_first_page_is_1():
    first_page = 1
    goal = PageRange(first_page, 4)
    assert 75 == progress_percent(3, goal)


def test_progress_percent_first_page_is_not_1():
    first_page = 3
    goal = PageRange(first_page, 6)
    assert 25 == progress_percent(3, goal)
    assert 100 == progress_percent(6, goal)


def test_progress_percent_page_is_less_than_goal_range():
    goal = PageRange(30, 140)
    assert 0 == progress_percent(0, goal)
    assert 0 == progress_percent(29, goal)


def test_progress_percent_page_is_greater_than_goal_range():
    goal = PageRange(30, 140)
    assert 109 == progress_percent(150, goal)


def test_progress_emoji():
    assert "🤍🤍🤍🤍🤍" == progress_emoji(0)
    assert "💚🤍🤍🤍🤍" == progress_emoji(20)
    assert "💚💚🤍🤍🤍" == progress_emoji(40)
    assert "💚💚💚🤍🤍" == progress_emoji(60)
    assert "💚💚💚💚🤍" == progress_emoji(80)
    assert "💚💚💚💚💚" == progress_emoji(100)


def test_progress_emoji_over_100_percent():
    assert "💚💚💚💚💚" == progress_emoji(333)
