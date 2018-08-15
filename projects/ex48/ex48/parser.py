
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

class Parser(object):
    def __init__(self,word_list):
        self.word_list=word_list
    
    def peektype(self):
        if self.word_list==None: return None
            word=self.word_list[0]
        return word[0]

    def skip_stop(self):
        while(self.word_list and peektype()=='stop'):
            match_one(self.word_list,'stop')

    def parse_one(self,type):
        if self.word_list==None: return None

        if(peektype()==type):
            return self.word_list.pop(0)
        else:
            return None

    def parse_subject(self):
        skip_stop()
        word=match_one('noun')
        if word==None:
            word=('noun','player')
        return word
    
    def parse_verb(self):
        skip_stop()
        word=match_one('verb')
        if word==None:
            raise ParseError("Expected a verb next.")
        else: 
            return word

    def parse_object(self):
        skip_stop()
        word=match_one('direction')
        if word==None:
            word=parse_one('noun')
            if word==None:
                raise ParseError("Expected a noun or direction")
        return word

    def parse_sentence(self):
        subject=parse_subject()
        verb=parse_verb()
        object=parse_object()
        return Sentence(subject,verb,object)
