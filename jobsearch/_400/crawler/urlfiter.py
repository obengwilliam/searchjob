def url_filter(urlf):
	try:   
        	from pymongo import MongoClient
        	connection=MongoClient()
        	db=connection.jobsdbs
        	assert db.connection==connection
	
       
      
		if[url for url in db.crawler_filterurl.find() if url['filter_url']==urlf]:
           		return True
	except:
               print 'problem in trying to filter'

    
           



if __name__=='__main__':
    print url_filter('http://www.happykidschool.org')