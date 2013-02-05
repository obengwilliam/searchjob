from crawler.spell_check import spell_check

def ch_re(jobtitles):
    keywords=[]
    for i in jobtitiles:
         
         if not check(i):
             suggested_keywords=check(i);
 
             for i in suggested_keywords:
                  keywords.append(i)
             


if __name__=='__main__':
   ch_re(['','computer','science'])
