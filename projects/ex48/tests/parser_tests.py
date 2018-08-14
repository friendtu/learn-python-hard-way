from nose.tools import *
from ex48 import lexicon,parser


def test_parser():
    word_list=lexicon.scan("bear go north")
    sentence=parse_sentence(word_list)
    assert_equal(sentence.subject,"bear")
    assert_equal(sentence.verb,'go')
    assert_equal(object,'north')