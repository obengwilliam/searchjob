'''
This class is responsible for getting all links on the page 
making use of the class get_next_target class
'''



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





from seed import check_if_seed_hostname

from urlparse import urlparse,urljoin
import traceback

def links(content_soup,url):
      links = []
      try:
        content_soup_all_a=content_soup.find_all('a')
        #content_soup_all_base=content_soup.find_all('base')
        
        for a in content_soup_all_a:
            
            href=a.get('href')
           
        
            parse_url=urlparse(href)
            
            if href==None:
                pass
            elif href=="":
                pass
            elif parse_url.fragment and not parse_url.scheme:
                 pass
                
            elif parse_url.scheme:
                
                if check_if_seed_hostname(parse_url):
                    
                    links.append(str(href))
                    
                    
                else:
                    
                    pass
                
                
                 
            else:
                '''
                converting relative urls into absolute urls 
                '''
                absolute_link=urljoin(url,href.replace('../','').replace('./',''))
                
                links.append(absolute_link)
                
      
      except:
           import sys
           print 'Error in get_all_links.py '+url
           print sys.exc_info(), traceback.print_exc()
           try: db.crawler_error_log.insert({'error_type':str(sys.exc_info()),'from_module':str(__file__)})
           except: return links
          
           return links
      links=list(set(links))
      return links



if __name__=='__main__':
    import socket

    # timeout in seconds
    timeout = 10
    socket.setdefaulttimeout(timeout)
    from bs4 import BeautifulSoup as soup
    from urllib2 import urlopen
    c=urlopen('http://www.jobberman.com.gh/job/6830/senior-lecturer-school-of-theology-and-mission-at-central-university-college/')
    page=c.read();

    print links(soup(page,'lxml'),'http://www.jobberman.com.gh/job/6830/senior-lecturer-school-of-theology-and-mission-at-central-university-college/'),
else:
    pass
