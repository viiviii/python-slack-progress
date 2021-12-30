from main import decode, parse_query_string, lambda_handler

# todo: 테스트가 너무 빈약함


def test_lambda_handler():
    dummy = {'body': 'dGV4dD05NQ=='}
    actual = lambda_handler(dummy, None)
    assert 200 == actual.get("statusCode")


def test_decode():
    actual = decode("dGV4dD05NQ==")
    assert "text=95" == actual


def test_parse_query_string():
    actual = parse_query_string("text=95")
    assert dict == type(actual)
    assert ['95'] == actual.get("text")
