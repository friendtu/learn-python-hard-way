from nose.tools import *
import re


def assert_response(resp,contains=None,matches=None,headers=None,status="200"):

    assert status in resp.status, "Expected response %r not in %r" %(status, resp.status)
    if status=="200":
        assert resp.data,"Reponse data is empty."
    
    if contains:
        assert contains in resp.data,"%r doesn't contain %r" % (resp.data,contains)

    if matches:
        reg=re.compile(matches)
        assert reg.matches(resp.data), "Response doesn't match %r" % matches
    
    if headers:
        #assert headers in resp.headers,"Headers %r doesn't match %r" %(resp.headers,headers)
        assert_equal(resp.headers,headers)

def get_session_id(resp):
    cookies_str = resp.headers['Set-Cookie']
    if cookies_str:
        for kv in cookies_str.split(';'):
            if 'webpy_session_id=' in kv:
                return kv