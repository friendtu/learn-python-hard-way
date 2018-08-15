
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
        while(self.word_list and self.peektype()=='stop'):
            self.match_one('stop')

    def match_one(self,type):
        if self.word_list==None: return None

        if(self.peektype()==type):
            return self.word_list.pop(0)
        else:
            return None

    def parse_subject(self):
        self.skip_stop()
        word=self.match_one('noun')
        if word==None:
            word=('noun','player')
        return word
    
    def parse_verb(self):
        self.skip_stop()
        word=self.match_one('verb')
        if word==None:
            raise ParseError("Expected a verb next.")
        else: 
            return word

    def parse_object(self):
        self.skip_stop()
        word=self.match_one('direction')
        if word==None:
            word=self.match_one('noun')
            if word==None:
                raise ParseError("Expected a noun or direction")
        return word

    def parse_sentence(self):
        subject=self.parse_subject()
        verb=self.parse_verb()
        object=self.parse_object()
        return Sentence(subject,verb,object)
