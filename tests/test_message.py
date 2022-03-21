from book.message import _percent, _emoji, progress_percent_message, error_message


# 결과 메세지는 채널의 모든 구성원에게 보인다
def test_result_message_response_type_is_channel():
    message = progress_percent_message(3, range(1, 10))
    assert "in_channel" == message.get("response_type")


# 에러 메세지는 명령을 실행한 사용자에게만 보인다
def test_error_message_response_type_is_ephemeral():
    message = error_message("", range(1, 10))
    assert "ephemeral" == message.get("response_type")


def test_percent():
    goal = range(30, 140)
    assert 0 == _percent(0, goal)
    assert 0 == _percent(29, goal)
    assert 109 == _percent(150, goal)


def test_emoji():
    assert "🤍🤍🤍🤍🤍" == _emoji(percent=0)
    assert "💚🤍🤍🤍🤍" == _emoji(percent=20)
    assert "💚💚🤍🤍🤍" == _emoji(percent=40)
    assert "💚💚💚🤍🤍" == _emoji(percent=60)
    assert "💚💚💚💚🤍" == _emoji(percent=80)
    assert "💚💚💚💚💚" == _emoji(percent=100)


def test_emoji_over_100_percent():
    assert "💚💚💚💚💚" == _emoji(percent=333)
