from typing import Final


def progress_percent_message(current: int, goal: range) -> dict:
    percent: Final = _percent(current, goal)
    return {
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"> đ *ė´ë˛ ëĒŠí* _{goal.start} ~ {goal.stop}_"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{_emoji(percent)} *{percent}*%"
                }
            }
        ]
    }


def error_message(command: str, _all: range) -> dict:
    return {
        "response_type": "ephemeral",
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"â ī¸ ė ė˛´ íė´ė§ ë˛ė ë´ė ėĢėë§ ę°ëĨí´ė!({_all.start} ~ {_all.stop}) -> ėë Ĩ ę° _{command}_"
                    }
                ]
            }
        ]
    }


def _percent(current: int, goal: range) -> int:
    goal_page_count: Final = goal.stop - goal.start + 1
    page_count: Final = current - goal.start + 1
    return 0 if page_count < 1 else int(page_count / goal_page_count * 100)


def _emoji(percent: int) -> str:
    max_percent: Final = 100
    max_emoji_count: Final = 5
    quotient: Final = max_percent // max_emoji_count
    count: Final = max_emoji_count if percent > max_percent else percent // quotient
    return "đ" * count + "đ¤" * (max_emoji_count - count)
