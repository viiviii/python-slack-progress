from typing import Final


def progress_result_message(current: int, goal: range) -> dict:
    return {
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"> 📚 *이번 목표* _{goal.start} ~ {goal.stop}_"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": _progress(current, goal)
                }
            }
        ]
    }


def progress_error_message(command: str, _all: range) -> dict:
    return {
        "response_type": "ephemeral",
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"⚠️ 전체 페이지 범위 내의 숫자만 가능해요!({_all.start} ~ {_all.stop}) -> 입력 값 _{command}_"
                    }
                ]
            }
        ]
    }


def _progress(current: int, goal: range) -> str:
    percent = _percent(current, goal)
    return f"{_emoji(percent)} *{percent}*%"


def _percent(current: int, goal: range) -> int:
    goal_page_count: Final = goal.stop - goal.start + 1
    page_count: Final = current - goal.start + 1
    return 0 if page_count < 1 else int(page_count / goal_page_count * 100)


def _emoji(percent: int) -> str:
    max_percent: Final = 100
    max_emoji_count: Final = 5
    quotient: Final = max_percent // max_emoji_count
    count: Final = max_emoji_count if percent > max_percent else percent // quotient
    return "💚" * count + "🤍" * (max_emoji_count - count)
