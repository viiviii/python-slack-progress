from book.message import *
from main import page


# 결과 메세지는 채널의 모든 구성원에게 보인다
def test_result_message_response_type_is_channel():
    message = progress_result_message(page.goal, "", 0)
    assert "in_channel" == message.get("response_type")


# 에러 메세지는 명령을 실행한 사용자에게만 보인다
def test_error_message_response_type_is_ephemeral():
    message = progress_error_message("", page.all)
    assert "ephemeral" == message.get("response_type")
