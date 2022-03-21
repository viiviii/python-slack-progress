

def progress_result_message(progress: str, goal: range) -> dict:
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
                    "text": progress
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
