import enchant as checkword

def spell_check(word):
    d= checkword.Dict("en_GB")
    if d.check(word):
        return word
    else:
        return d.suggest(word)

if '__name__'=='__file__':
    word=raw_input('please provide word')
    print spell_check(word)

