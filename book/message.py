from book.page import Range


def progress_result_message(goal_page: Range, emoji: str, percent: int) -> dict:
    return {
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"> 📚 *이번 목표* _{_range_text(goal_page)}_"
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


def progress_error_message(command: str, all_page_range: Range) -> dict:
    return {
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"⚠️ 페이지 범위 내의 숫자만 가능해요!({_range_text(all_page_range)}) -> 입력 값 _{command}_"
                    }
                ]
            }
        ]
    }


def _range_text(_range: Range) -> str:
    return f"p.{_range.first}~{_range.last}"
