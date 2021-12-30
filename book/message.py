from book.page import PageRange


def progress_result_message(goal: PageRange, emoji: str, percent: int) -> dict:
    return {
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"> 📚 *이번 목표* _{_range_text(goal)}_"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{emoji} *{percent}*%"
                }
            }
        ]
    }


def progress_error_message(command: str, _all: PageRange) -> dict:
    return {
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"⚠️ 페이지 범위 내의 숫자만 가능해요!({_range_text(_all)}) -> 입력 값 _{command}_"
                    }
                ]
            }
        ]
    }


def _range_text(_range: PageRange) -> str:
    return f"p.{_range.first}~{_range.last}"
