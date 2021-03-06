from main import *


# 유효하지 않은 값이 오더라도 200으로 응답해야 내가 처리한 예외 메세지가 사용자에게 보임
# https://api.slack.com/interactivity/handling#acknowledgment_response


# 올바른 입력 값일 경우 응답에 결과 메세지를 리턴한다
def test_lambda_handler_valid_commands_returns_result_message():
    text_is_95: Final = "dGV4dD05NQ=="
    actual = lambda_handler({'body': text_is_95}, None)
    message = progress_percent_message(95, goal_range)
    assert actual == response(message)


# 입력 값이 빈 값일 경우 응답에 에러 메세지를 리턴한다
def test_empty_command_returns_error_message():
    actual = lambda_handler({'body': ''}, None)
    message = error_message("없음", all_range)
    assert actual == response(message)


# 입력 값이 숫자가 아닌 경우 응답에 에러 메세지를 리턴한다
def test_invalid_command_returns_error_message():
    text_is_hi: Final = "dGV4dD1oaQ=="
    actual = lambda_handler({'body': text_is_hi}, None)
    message = error_message("hi", all_range)
    assert actual == response(message)


# 입력 값이 전체 페이지 범위에 속하지 않으면 응답에 에러 메세지를 리턴한다
def test_out_of_range_command_returns_error_message():
    text_is_minus999: Final = "dGV4dD0tOTk5"
    actual = lambda_handler({'body': text_is_minus999}, None)
    message = error_message("-999", all_range)
    assert actual == response(message)


def test_parse_query_string():
    actual = parse_query_string("text=95")
    assert dict == type(actual)
    assert ['95'] == actual.get("text")


def test_response_status_code_is_200():
    actual = response(message={})
    assert 200 == actual.get("statusCode")


def test_response_content_type_is_json():
    actual = response(message={})
    expect = {"Content-Type": "application/json"}
    assert expect == actual.get("headers")
