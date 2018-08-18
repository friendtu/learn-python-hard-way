from nose.tools import *
from bin.app import *
from gothonweb import map
from tests.tools import assert_response



def test_index():
    resp=app.request("/")
    assert_response(resp,status="303")

def test_game_engine():
    resp=app.request("/game")
    assert_response(resp,contains="You Died")

def test_hello():
    resp=app.request("/hello")

    assert_response(resp)

    resp=app.request("/hello",method="POST")
    assert_response(resp,contains="Nobody")

    data={'name':'Zed','green':'Hola'}
    resp=app.request("/hello",method="POST",data=data)
    assert_response(resp,contains='Zed')