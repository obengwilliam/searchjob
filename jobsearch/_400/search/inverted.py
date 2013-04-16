from pymongo import MongoClient



def load_index(invindex,inverted_index=False):
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




      
     for index in db.crawler_index.find():
          invindex[index['keyword']]=[]
          for doc in index['doc']:
              invindex[index['keyword']].append([doc['id'],doc['location'],doc['count']])
     if inverted_index==True:
         return invindex
     else:
         return True
