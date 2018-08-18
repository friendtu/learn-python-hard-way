from nose.tools import *
from bin.app import *
from gothonweb import map
from tests.tools import assert_response,get_session_id


def setUp():
    pass


def test_index():
    resp=app.request("/")
    assert_response(resp,status="303")
    session_id=get_session_id(resp)
    headers={'Cookie':session_id}
    resp=app.request("/game",headers=headers)
    print "session_id:%r" % session_id
    print "resp: %r" % resp
    assert_response(resp,contains='Central Corridor')


def test_first_game_page_without_session():
    resp=app.request("/game")
    assert_response(resp,contains="You Died")

def test_first_game_page_with_central_corridor():
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