import base64
import json
import urllib.parse
from typing import Final, List

from book.message import progress_error_message, progress_result_message
from book.page import PageRange, Page
from book.progress import progress_percent, progress_emoji

page: Final = Page(_all=PageRange(1, 477), goal=PageRange(96, 176))


def lambda_handler(event, context) -> dict:
    body: str = base64decode(event['body'])
    slack_data: dict = parse_query_string(body)
    commands: List[str] = slack_data.get('text')

    if not commands:
        return response(progress_error_message('없음', page.all))

    try:
        # TODO: commands[0] 리팩토링
        current_page = int(commands[0])
    except ValueError:
        return response(progress_error_message(commands[0], page.all))

    if not page.all.includes(current_page):
        return response(progress_error_message(str(current_page), page.all))

    goal_percent: int = progress_percent(current_page, page.goal)
    goal_emoji: str = progress_emoji(goal_percent)
    return response(progress_result_message(page.goal, goal_emoji, goal_percent))


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
