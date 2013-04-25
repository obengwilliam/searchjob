
def    url_seen_test(url_test):
	'''
       	str()->bool()

        This module is to help check whether url has already beign seen
        >>>url_seen_test('http://www.google.com')
  	True
	>>>url_seen_test('http://www.gog.com')
	None
	'''
	try:
        	from pymongo import MongoClient
        	connection=MongoClient()
        	db=connection.jobsdbs
		assert db.connection==connection
		
		if db.crawler_page_info.find_one({'url':url_test}):
          			return True
                
        except:
		print 'problem from url_seen_test'
	
		




if __name__=='__main__':
    print url_seen_test('http://www.happykidschool.org')
