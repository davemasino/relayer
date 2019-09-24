from relayer.core import foo, handler

def test_handler():
    cx = type('',(object,),{"function_name": "handler"})()
    ret = handler(None, cx)
    msg = ret['message']
    assert msg == "Go Serverless v1.0! Your function executed successfully!"

def test_foo():
    a = foo()
    assert a == "bar"