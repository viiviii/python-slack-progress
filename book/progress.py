from typing import Final

from book.page import PageRange


def progress_percent(current: int, goal: PageRange) -> int:
    goal_page_count: Final = goal.last - goal.first + 1
    page_count: Final = current - goal.first + 1
    return 0 if page_count < 1 else int(page_count / goal_page_count * 100)


# TODO: 무슨일이야?
def progress_emoji(percent: int) -> str:
    max_percent: Final = 100
    max_emoji_count: Final = 5
    quotient: Final = max_percent // max_emoji_count
    count: Final = max_emoji_count if percent > max_percent else percent // quotient
    return "💚" * count + "🤍" * (max_emoji_count - count)


