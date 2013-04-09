'''
This class is responsible for getting all links on the page 
making use of the class get_next_target class
'''




from seed import check_if_seed_hostname

from urlparse import urlparse,urljoin

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
           print sys.exc_info()
           return links
      links=list(set(links))
      return links



if __name__=='__main__':
    from bs4 import BeautifulSoup as soup
    from urllib2 import urlopen
    c=urlopen('http://jobs.classifieds1000.com/Ghana/Internet_Jobs/i_would_like_to_be_a_vender')
    page=c.read();

    print links(soup(page,'lxml'),'http://www.ghanacurrentjobs.com/'),
else:
    pass
