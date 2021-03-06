from pymongo import MongoClient

                   
def restructuring_index(finvindex):
     '''
	dict()->dict()
	This full index module contains a keyword and a list of documents where the the keyword appears
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


if __name__=='__main__':
   import profile
   print profile.run('restructuring_index({})')






