from inverted import load_index
from fullinverted import restructuring_index
from collections import Counter





invindex={}
finvindex={} 	




def termsearch (terms):#searches a full inverted index
    '''list()->set()

      This document is responsible for performing a term search on a full inverted index.
      An empty list is not allowed
    >>>termsearch(['computer','science'])
    [ObjectId('51607f5640ade63653e31e69'...]
    >>>termsearch(['computerse','science'])#if terms are not present it returns a [1]
    '''
    if load_index(invindex):#The first thing we do here is to make sure the full inverted index is loaded in memory
        try:
            return reduce(set.intersection ,(set(x[0]for x in doc) for keyword,doc in invindex.items() if keyword in terms))
        except:
            return set([])



def phrasesearch(phrase):
	'''
          
	str()->counter()
        This function is responsible for taking a phrase and then returning a an object which
        contains each id and the number of time they appear 
	
        >>>phrasesearch(phrase)
           counter({ObjectId('51607f5640ade63653e31e69'):4,ObjectId('51607f5640ade63653e31e690'):2..}])
	'''
        restructuring_index(finvindex)
        phrasewords=phrase.strip().strip('"').split()
       
        firstword,otherwords=phrasewords[0],phrasewords[1:]
        found=[]
        found_count=Counter()
        def index(otherword):
            '''
              str()->list()
            This method is responsible for returning list of document and location where the string can be found
            >>> index('cloud')
            [[1,2],[2,3]] 
            '''
            try:
                return finvindex[otherword]
            except:
                return set([1,0])
       
        
        for id in termsearch(phrasewords):
            #The above gives us all posible doc ids that have those word in arguments
           
           
            for firstindex in (ind for t,ind in finvindex[firstword] if t==id):
               
               if all((id,firstindex+1+otherindex) in index(otherword) for otherindex,otherword in enumerate(otherwords)):
                    found.append(id)
        for id in found:
                found_count[id]+=1
        return  found_count,found
           
            
                 

   

if __name__=='__main__':
     from pprint import pprint as pp
      
     #pp(termsearch(['check']))
     #empty strings are not allowed at all for phrasesearch
     pp(termsearch([]))
     





