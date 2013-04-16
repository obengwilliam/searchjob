
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
	        
		for i in db.crawler_stopword.find():
                     stopword_list.append(i['words'])
               
         	return stopword_list
        except:
               print 'problem with calling from database'
		
if __name__=='__main__':
    print stopword([])
