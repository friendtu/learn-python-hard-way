
class ParseError(Exception):
    pass
    
class Sentence(object):
    def __init__(self,subject,verb,obj):
        if(subject==None):
             self.subject=None
        else:
            self.subject=subject[1]
        self.verb=verb[1]
        self.obj=obj[1]

def peektype(word_list):
    if word_list==None: return None
    word=word_list[0]
    return word[0]

def skip_stop(word_list):
    while(word_list and peektype(word_list)=='stop'):
        parse_one(word_list,'stop')

def parse_one(word_list,type):
    if word_list==None: return None

    if(peektype(word_list)==type):
        return word_list.pop(0)
    else:
        return None

def parse_subject(word_list):
    skip_stop(word_list)
    word=parse_one(word_list,'noun')
    if word==None:
        word=('noun','player')
    return word
    
def parse_verb(word_list):
    skip_stop(word_list)
    word=parse_one(word_list,'verb')
    if word==None:
        raise ParseError("Expected a verb next.")
    else: 
        return word

def parse_object(word_list):
    skip_stop(word_list)
    word=parse_one(word_list,'direction')
    if word==None:
        word=parse_one(word_list,'noun')
        if word==None:
            raise ParseError("Expected a noun or direction")
    return word

def parse_sentence(word_list):
    subject=parse_subject(word_list)
    verb=parse_verb(word_list)
    object=parse_object(word_list)
    return Sentence(subject,verb,object)
