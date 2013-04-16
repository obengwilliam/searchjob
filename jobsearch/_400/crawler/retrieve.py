from pymongo import MongoClient





invindex={}	

def load_index(inverted_index=False):
     '''Empty->bool()
     This document simply loads the full inverted index into memory
     >>>load_index
     True
     
     '''
   
     try:
     	connection=MongoClient()
     	db=connection.jobsdbs
     	assert db.connection==connection
     except:
        print 'Problem with in retrieve in retrieve.py '




     try: 
	     for index in db.crawler_index.find():
	          invindex[index['keyword']]=[]
	          for doc in index['doc']:
	              invindex[index['keyword']].append([doc['id'],doc['location'],doc['count']])
	     if inverted_index==True:
	         return invindex
	     else:
	         return True
     except:
           print 'Exception from loading index into memory'
           return True


def termsearch (terms):#searches a full inverted index
    '''list()->set()

      This document is responsible for performing a term search on a full inverted index.
      An empty list is not allowed
    >>>termsearch(['computer','science'])
    [ObjectId('51607f5640ade63653e31e69'...]
    >>>termsearch(['computerse','science'])#if terms are not present it returns a [1]
    '''
    
    if load_index():#The first thing we do here is to make sure the full inverted index is loaded in memory
        try:
            return reduce(set.intersection ,(set(x[0]for x in doc) for keyword,doc in invindex.items() if keyword in terms))
        except:
            print 'Exception from termsearch:check it out'
            return set([])
   




   












def phrasesearch(phrase):
	'''  
	str()->list()
        This function is responsible for taking a phrase and then returning a list of document id's  
	
        >>>phrasesearch(phrase)
           [ObjectId('51607f5640ade63653e31e69'),ObjectId('51607f5640ade63653e31e690')...]
	'''
        
        phrasewords=phrase.strip().strip('"').split()
        
       
        firstword,otherwords=phrasewords[0],phrasewords[1:]
        found=[]
       
        
        for id in termsearch(phrasewords):
            #The above gives us all posible doc ids that have those word in arguments
           
            
            for firstindex in (ind for t,ind in finvindex[firstword] if t==id):
               
               if all((id,firstindex+1+otherindex) in finvindex[otherword] for otherindex,otherword in enumerate(otherwords)):
                    found.append(id)
        return found
           
   











         
                 

                    
def restructuring_index():
     '''
	dict()->dict()
	This document receives an index from the load_index() module ..it then convert it into a full index module
        for phrase search. This full index module contains a keyword and a list of documents where the the keyword appears
    >>>restructuring_index()
      {'a': [('ObjectId('51607f5640ade63653e31e69')', 2)],
	 'banana': [('ObjectId('51607f5640ade63653e31e69')', 3)],
 	'is': [('ObjectId('51607f5640ade63653e31e69')', 1), ('ObjectId('51607f5640ade63653e31e69')', 4), ('ObjectId('51607f5640ade63653e31e69')', 1), ('ObjectId('51607f5640ade63653e31e69')', 1)],
	 'it': [('ObjectId('51607f5640ade63653e31e69')', 0), ('TObjectId('51607f5640ade63653e31e69'), 3)]

     '''
     
     try:
     	connection=MongoClient()
     	db=connection.jobsdbs
     	assert db.connection==connection
     except:
        print 'Problem with in retrieve in retrieve.py '
     
      
     for index in db.crawler_index.find():
          finvindex[index['keyword']]=set()
          [finvindex[index['keyword']].add((doc['id'],location)) for doc in index['doc'] for location in doc['location']]
     return True





'''
finvindex={}


def check_finvindex(keyword):
	try:    
                restructuring_index()
		return finvindex[keyword]
	except:
                
		return set(('',''))



print check_finvindex('acco')
'''
finvindex={}
   

if __name__=='__main__':
     from pprint import pprint as pp
     
     if restructuring_index():
	pp(termsearch('check'))
     





