import enchant as checkword

def spell_check(word):
   try:
    d= checkword.Dict("en_GB")
   
    if d.check(word):
        return word
    else:
        return d.suggest(word)

   except:
      return ' '

if __name__=='__main__':
    word=raw_input('please provide word  ')
    print spell_check(word)
