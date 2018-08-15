
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
    
    def __peektype(self):
        if self.word_list==None: return None
        word=self.word_list[0]
        return word[0]

    def __skip_stop(self):
        while(self.word_list and self.__peektype()=='stop'):
            self.__match_one('stop')

    def __match_one(self,type):
        if self.word_list==None: return None

        if(self.__peektype()==type):
            return self.word_list.pop(0)
        else:
            return None

    def __parse_subject(self):
        self.__skip_stop()
        word=self.__match_one('noun')
        if word==None:
            word=('noun','player')
        return word
    
    def __parse_verb(self):
        self.__skip_stop()
        word=self.__match_one('verb')
        if word==None:
            raise ParseError("Expected a verb next.")
        else: 
            return word

    def __parse_object(self):
        self.__skip_stop()
        word=self.__match_one('direction')
        if word==None:
            word=self.__match_one('noun')
            if word==None:
                raise ParseError("Expected a noun or direction")
        return word

    def parse_sentence(self):
        subject=self.__parse_subject()
        verb=self.__parse_verb()
        object=self.__parse_object()
        return Sentence(subject,verb,object)
