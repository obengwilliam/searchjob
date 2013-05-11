#!usr/bin/env python2.7
"""
/*
//     _ +------------------------------+ _
//    /o)|   Search Engine               |(o\
//   / / |       obeng william  & tk     | \ \
//  ( (_ |  _                         _  | _) )
// ((\ \)+-/o)-----------------------(o\-+(/ /))
// (\\\ \_/ /                         \ \_/ ///)
//  \      /                           \      /
//   \____/                             \____/
*/
"""

from fetchpg import get_page
import indexpg 
from get_all_links import links as all_links
from union import add_to_tocrawl
from indexpg import make_index
from page_info import get_page_data as info
from job_rank import compute_ranks  as ranks
import traceback
from bson import ObjectId
import sys





from document_seen_test import content_seen_test as test_doc




try:
	'''
        	Making a global connection to the Mongodb database
	'''
        from pymongo import MongoClient
        
        connection=MongoClient()

        db=connection.jobsdbs
	
 	assert db.connection==connection
       
except:
        print 'connection problem in start_Crawler.py'














def crawl_web(seed,mx_pg,mx_dp,filter_list=None):
    '''
         
	The function is responsible for the entire crawling process 
	This includes making index,getting all links on a particular page 
	passing and so on.
	>>>
    '''
    
    tocrawl = [[seed,0]]
    
    crawled = []
    graph={}
    outlinks=[]
    No_crawled=0
    
    
    
    while tocrawl:
        
        page_url ,depth= tocrawl.pop(0);#here we will count the number of document removed from the frontier
        if page_url:
           db.crawler_web_statistic.update({"_id":ObjectId("517dc20440ade61b20becb7d")},{"$inc":{"Number_of_removed_urls":1}},safe=True)
        
        if (page_url not in crawled) and (len(crawled)< mx_pg) and (depth <=mx_dp):
            print 'Crawling %s ,depth %d'%(page_url,depth)
            content_soup ,base_robot_parsed_url= get_page(page_url)
            '''
            This module is responsible for obtaining all page info
            '''
            if not test_doc(content_soup):
            	make_index(page_url, content_soup)
            	outlinks=all_links(content_soup,base_robot_parsed_url)
               
               
            else:
                 db.crawler_web_statistic.update({"_id":ObjectId("517dc20440ade61b20becb7d")},{"$inc":{"Number_of_duplicate_documents":1}},safe=True)
	          #here will count the number of document where duplicate existed
            '''
            Below am trying to obtain the relation between the page_url and it links. This 
            pairs form a graph to be used in our importance score calculation
            '''
            graph[page_url]=outlinks
            add_to_tocrawl(tocrawl, outlinks,depth,crawled)
            crawled.append(page_url)
            
            print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            #yet to check for urls that contains urls that linked to the same pages
	    No_crawled=len(crawled)
            print 'This is the number of pages crawled'+' '+str(len(crawled))
    return graph,No_crawled,mx_pg,seed











def main(ranks={},No_crawled=None,mx_pg=None,seed=None):
    '''
    ()->list()

    This module is responsible for returning all seed list from the database
    >>>main()
    ['http://www.jobsinghana.com','http://www.jobsin.com'....]
    '''
    
    #update all urls with their ranks
    if ranks:

       assert db.connection==connection
       
       #check for completed number of pages crawled
       if (No_crawled !=None) and (mx_pg !=None) and (seed !=None):#not  and (No_crawled == mx_pg):


          if (No_crawled != mx_pg):
	      db.crawler_seed.update({"seeds_urls":seed},{"$set":{"details":'Number of pages crawled is not the equal to maximum number of pages assigned'}})
          else:
                 db.crawler_seed.update({"seeds_urls":seed},{"$set":{"details":'Number of pages crawled is the equal to maximum number of pages assigned'}})

          db.crawler_seed.update({"seeds_urls":seed},{"$set":{"completed":True}})
       
       for i in ranks:
            db.crawler_page_info.update({"url":i},{"$set":{"rank_score":ranks[i]}},safe=True)
       return True



    #providing seeds b4 crawling 
    else:
    	seed_urls=db.crawler_seed.find()
    	#filter_url=db.crawler_filterurl.find()
    
    	seed_list=[{'url':record['seeds_urls'],'max_pages':record['max_pages'],'max_depth':record['max_depth']} for record in seed_urls]
    	#filter_list=[]
        '''
    	for record in seed_urls:
        	seed_list.append({'url':record['seeds_urls'],'max_pages':record['max_pages'],'max_depth':record['max_depth']})
        '''
	'''
    	for url in filter_url:
         	filter_list.append(str(url['filter_url']))
	'''
    
    	return seed_list
  









def start_crawler():
    try:
	      seed_list=main()
	      while len(seed_list)!=0:
	            seed=seed_list.pop();
                     
	            graph,No_crawled,mx_pg,seed=crawl_web(seed['url'],seed['max_pages'],seed['max_depth'])
	            main(ranks(graph),No_crawled,mx_pg,seed)
	            #main()
	            '''
	            Now we insert the ranks of our graph into our mongodb 
	            '''
            
            
    except:    
               
               print 'error',traceback.print_exc()
               db.crawler_error_log.insert({'error_type':str(sys.exc_info()),'from_module':str(__file__)})
               
    




import threading
import datetime






class ThreadClass(threading.Thread):
          def run(self):
            start_crawler()



if __name__=='__main__':
                    
      t = ThreadClass()
      t.start()
            
	
   
