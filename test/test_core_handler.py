from relayer.core import handler


def test_handler():
    cx = type('', (object,), {"function_name": "relayer-unit-test"})()
    ret = handler(None, cx)
    msg = ret['message']
    assert msg == "Go Serverless v1.0! Your function executed successfully!"
