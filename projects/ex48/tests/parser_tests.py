from nose.tools import *
from ex48 import lexicon,parser


def test_parser_noun_verb_object():
    word_list=lexicon.scan("bear go north")
    sentence=parser.parse_sentence(word_list)
    assert_equal(sentence.subject,"bear")
    assert_equal(sentence.verb,'go')
    assert_equal(sentence.obj,'north')

def test_parser_stop_noun_verb_object():
    word_list=lexicon.scan("the bear go north")
    sentence=parser.parse_sentence(word_list)
    assert_equal(sentence.subject,"bear")
    assert_equal(sentence.verb,'go')
    assert_equal(sentence.obj,'north')

def test_parser_verb_object():
    word_list=lexicon.scan("go north")
    sentence=parser.parse_sentence(word_list)
    assert_equal(sentence.subject,'player')
    assert_equal(sentence.verb,'go')
    assert_equal(sentence.obj,'north')

def test_parser_verb_stop_object():
    word_list=lexicon.scan("go the north")
    sentence=parser.parse_sentence(word_list)
    assert_equal(sentence.subject,'player')
    assert_equal(sentence.verb,'go')
    assert_equal(sentence.obj,'north')

@raises(parser.ParseError)
def test_parser_verb_error_object():
    word_list=lexicon.scan("go there north")
    sentence=parser.parse_sentence(word_list)
    assert_equal(sentence.subject,'player')
    assert_equal(sentence.verb,'go')
    assert_equal(sentence.obj,'north')