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


 		connectin=MongoClient()
		db=connection.jobsdbs
		
		assert db.connection==connection


		if db.crawler_page_info.find_one({'doc_digest':sha224(str(page)).hexdigest()}):
			return True
                else:
			return False
	except:
		'problem with document'
		return False







if __name__=='__main__':
 	print content_seen_test('<a> herf ghana jfjfy89d</a>')
