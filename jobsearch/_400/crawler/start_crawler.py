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

def crawl_web(seed,mx_pg,mx_dp,filter_list):
    
    tocrawl = [[seed,0]]
    
    crawled = []
    
    
    while tocrawl:
        
        page_url ,depth= tocrawl.pop(0)
        
        if page_url in filter_list:
           print 'CAN NOT BE CRAWLED.......filtered....%s'%page_url
          
           return False
        
        if (page_url not in crawled) and (len(crawled)< mx_pg) and (depth <=mx_dp):
            print 'Crawling %s ,depth %d'%(page_url,depth)
            content_soup ,base_robot_parsed_url= get_page(page_url)
            
            make_index(page_url, content_soup)
            outlinks=all_links(content_soup,base_robot_parsed_url)
            add_to_tocrawl(tocrawl, outlinks,depth,crawled)
            crawled.append(page_url)
            
            print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            #yet to check for urls that contains urls that linked to the same pages
        print 'This is the number of pages crawled'+' '+str(len(crawled))
    return True

def main():
    try:
        from pymongo import MongoClient
        
        connection=MongoClient()
       
    except:
        print 'connection problem'
    db=connection.jobsdbs
    seed_urls=db.crawler_seed.find()
    filter_url=db.crawler_filterurl.find()
    
    seed_list=[]
    filter_list=[]

    for record in seed_urls:
        seed_list.append({'url':record['seeds_urls'],'max_pages':record['max_pages'],'max_depth':record['max_depth']})
    for url in filter_url:
         filter_list.append(str(url['filter_url']))
    
    return seed_list,filter_list
  

if __name__=='__main__':
      seed_list,filter_list=main()
      while len(seed_list)!=0:
            seed=seed_list.pop();
            crawl_web(seed['url'],seed['max_pages'],seed['max_depth'],filter_list)
else:
    pass
