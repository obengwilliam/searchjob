from urllib2 import urlopen
from Queue import Queue
from hashlib import sha224
from bs4 import BeautifulSoup as soup
urls=Queue()
urls.put('http://www.jobsinghana.com')
urls.put('http://www.happykidschool.org')
urls.put('http://www.gh.3wjobs.com/')
urls.put('http://www.gh.3wjobs.com/j__s__Engineering.html')
urls.put('http://www.gh.3wjobs.com/j__s__Engineering.html')
urls.put('http://www.gh.3wjobs.com/j__s__Engineering.html')
urls.put('http://www.jobsinghana.com')

urls.put('http://www.jobsinghana.com')
urls.put('http://www.happykidschool.org')



while urls.not_empty:
	url=urls.get()
	page=urlopen(url)
	page_read=soup(page.read(),'lxml').body
	print sha224(page_read.encode('utf-8')).hexdigest(),url
	
	
