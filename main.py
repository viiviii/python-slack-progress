import base64
import json
import urllib.parse
from typing import Final, List

from book.message import error_message, progress_percent_message

all_range: Final = range(1, 477)
goal_range: Final = range(96, 176)


def lambda_handler(event, context) -> dict:
    body: str = base64decode(event['body'])
    slack_data: dict = parse_query_string(body)
    commands: List[str] = slack_data.get('text')

    if not commands:
        return response(error_message('없음', all_range))

    try:
        # TODO: commands[0] 리팩토링
        current_page = int(commands[0])
    except ValueError:
        return response(error_message(commands[0], all_range))

    if current_page not in all_range:
        return response(error_message(str(current_page), all_range))

    return response(progress_percent_message(current_page, goal_range))


def base64decode(string: str) -> str:
    return base64.b64decode(string).decode()


def parse_query_string(query_string: str) -> dict:
    return urllib.parse.parse_qs(query_string)


def response(message: dict) -> dict:
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(message),
    }
