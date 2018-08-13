def scan(sentence):
    result=[]
    words=sentence.split()
    for word in words:
        lower_word=word.lower()
        type=''
        if lower_word in ['north','south','east','west']:
            type='direction'
        elif lower_word in ['go','kill','eat']:
            type='verb'
        elif lower_word in ['the','in','of']:
            type='stop'
        elif lower_word in ['bear', 'princess']:
            type='noun'
        else:
            try:
                word=int(lower_word)
                type='number'
            except ValueError:
                type='error'
        result.append((type,word))
    return result


