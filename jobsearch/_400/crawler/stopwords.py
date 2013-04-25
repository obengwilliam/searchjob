
def stopword(stopword_list):
	'''
        	list()->list()
	This module is responsible for fetching all stopwords from the database
	>>>stopword([])
	['a','who']
	'''
	try:
		from pymongo import MongoClient
		connection=MongoClient()
                db=connection.jobsdbs
                assert db.connection==connection
	except:
                print 'connection problem'
	try:
	        
		stopword_list=[['words'] for i in db.crawler_stopword.find()]
                 
               
         	return stopword_list
        except:
               print 'problem with calling from database'
		
if __name__=='__main__':
    print stopword([])
