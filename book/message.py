from book.page import PageRange


def progress_result_message(progress: str, goal: PageRange) -> dict:
    return {
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"> 📚 *이번 목표* _{goal}_"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": progress
                }
            }
        ]
    }


def progress_error_message(command: str, _all: PageRange) -> dict:
    return {
        "response_type": "ephemeral",
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"⚠️ 페이지 범위 내의 숫자만 가능해요!({_all}) -> 입력 값 _{command}_"
                    }
                ]
            }
        ]
    }
