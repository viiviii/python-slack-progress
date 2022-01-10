from main import *

# 유효하지 않은 값이 오더라도 200으로 응답해야 내가 처리한 예외 메세지가 사용자에게 보임
# https://api.slack.com/interactivity/handling#acknowledgment_response

_text_is_95: Final = "dGV4dD05NQ=="
_text_is_hi: Final = "dGV4dD1oaQ=="
_text_is_minus999: Final = "dGV4dD0tOTk5"


# 올바른 입력 값일 경우 응답에 결과 메세지를 리턴한다
def test_lambda_handler_valid_commands_returns_result_message():
    event = {'body': _text_is_95}

    # TODO
    percent = progress_percent(95, page.goal)
    emoji = progress_emoji(percent)
    result_message = progress_result_message(page.goal, emoji, percent)
    expected = response(result_message)
    assert expected == lambda_handler(event, None)


# 입력 값이 빈 값일 경우 응답에 에러 메세지를 리턴한다
def test_empty_command_returns_error_message():
    event = {'body': ''}

    error_message = progress_error_message("없음", page.all)
    expected = response(error_message)
    assert expected == lambda_handler(event, None)


# 입력 값이 숫자가 아닌 경우 응답에 에러 메세지를 리턴한다
def test_invalid_command_returns_error_message():
    event = {'body': _text_is_hi}

    error_message = progress_error_message("hi", page.all)
    expected = response(error_message)
    assert expected == lambda_handler(event, None)


# 입력 값이 전체 페이지 범위에 속하지 않으면 응답에 에러 메세지를 리턴한다
def test_out_of_range_command_returns_error_message():
    event = {'body': _text_is_minus999}

    error_message = progress_error_message("-999", page.all)
    expected = response(error_message)
    assert expected == lambda_handler(event, None)


def test_decode():
    assert "text=95" == decode(_text_is_95)
    assert "text=hi" == decode(_text_is_hi)
    assert "text=-999" == decode(_text_is_minus999)


def test_parse_query_string():
    actual = parse_query_string("text=95")
    assert dict == type(actual)
    assert ['95'] == actual.get("text")


def test_response_status_code_is_200():
    actual = response(view_data={})
    assert 200 == actual.get("statusCode")


def test_response_content_type_is_json():
    actual = response(view_data={})
    expect = {"Content-Type": "application/json"}
    assert expect == actual.get("headers")
