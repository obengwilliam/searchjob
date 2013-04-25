from urlfiter import url_filter as filter
from url_seen_test import url_seen_test as test




def add_to_tocrawl(to_crawl,outlinks,depth,crawled):
        '''
This is the  union module that is responsible make sure to populate our tocrawl data structure with url to be crawled
It also makes sure that it does not duplicate the urls
        '''
	try:
		for url in outlinks:
			if (url not in to_crawl) and (not filter(url)) and (not test(url)):
				to_crawl.append([url,depth+1])
		
	except:
		print 'problem from union.add_tocrawl :check link'
			




if __name__=='__main__':
    add_to_tocrawl('',[],2,[]);
