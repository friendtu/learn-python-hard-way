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
        assert_equal(resp.headers,headers)