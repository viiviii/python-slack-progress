from book.message import _progress, _percent, _emoji, progress_result_message, progress_error_message


# 결과 메세지는 채널의 모든 구성원에게 보인다
def test_result_message_response_type_is_channel():
    message = progress_result_message(3, range(1, 10))
    assert "in_channel" == message.get("response_type")


# 에러 메세지는 명령을 실행한 사용자에게만 보인다
def test_error_message_response_type_is_ephemeral():
    message = progress_error_message("", range(1, 10))
    assert "ephemeral" == message.get("response_type")


def test_progress():
    goal = range(1, 4)
    current = 1
    assert "💚🤍🤍🤍🤍 *25*%" == _progress(current, goal)


def test_progress_percent_first_page_is_1():
    first_page = 1
    goal = range(first_page, 4)
    assert 75 == _percent(3, goal)


def test_progress_percent_first_page_is_not_1():
    first_page = 3
    goal = range(first_page, 6)
    assert 25 == _percent(3, goal)
    assert 100 == _percent(6, goal)


def test_progress_percent_page_is_less_than_goal_range():
    goal = range(30, 140)
    assert 0 == _percent(0, goal)
    assert 0 == _percent(29, goal)


def test_progress_percent_page_is_greater_than_goal_range():
    goal = range(30, 140)
    assert 109 == _percent(150, goal)


def test_progress_emoji():
    assert "🤍🤍🤍🤍🤍" == _emoji(percent=0)
    assert "💚🤍🤍🤍🤍" == _emoji(percent=20)
    assert "💚💚🤍🤍🤍" == _emoji(percent=40)
    assert "💚💚💚🤍🤍" == _emoji(percent=60)
    assert "💚💚💚💚🤍" == _emoji(percent=80)
    assert "💚💚💚💚💚" == _emoji(percent=100)


def test_progress_emoji_over_100_percent():
    assert "💚💚💚💚💚" == _emoji(percent=333)
