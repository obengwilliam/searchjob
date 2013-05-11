from bs4 import BeautifulSoup as soup
import sys

def content_seen_test(page):
	'''
	This document is responsible for performing a document seen test
	Checking to see if the document has being downloaded already by using the sha224 algorithm
        >>>content_seen(page)
       	True
	'''

	try:
		from pymongo import MongoClient
		from hashlib import sha224


 		connection=MongoClient()
		db=connection.jobsdbs
		
		assert db.connection==connection

                if page==soup('','lxml'):
			return False
			
		if db.crawler_page_info.find_one({'doc_digest':sha224(page.body.encode('utf-8')).hexdigest()}):
			return True
                else: 
			return False
	except:
                import sys
		db.crawler_error_log.insert({'error_type':str(sys.exc_info()),'from_module':str(__file__)})
		print 'problem with document finger printing algorithm'

		return False







if __name__=='__main__':
 	print content_seen_test('<a> herf ghana jfjfy89d</a>')
