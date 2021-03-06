
def get_page_data(soup_read,url):
    '''
    This page is responsible for storing information on each     page we crawl.This module will also be responsible for using the tf-idf of each page.

    '''
    try:
        
       
       if soup_read.title==None:
          title=url
       else:
            title=soup_read.title.string

       style_num=soup_read.find_all('style')
       script_num=soup_read.find_all('script')

       for script in script_num:
           soup_read.script.decompose()
       for style in style_num:
           soup_read.style.decompose()
       content=soup_read.body.get_text(" ",strip=True).split()[:100]
       content=' '.join(content)
       

        
    except:
           import sys
           print sys.exc_info()
           return 'Problem from get page module'
    return 



if __name__=='__main__':
   import socket
   #setting default socket timeout
   timeout=10
   socket.setdefaulttimeout(timeout)
   from urllib2 import urlopen
   page=urlopen('http://www.happykidschool.org')
   page_read=page.read()
   from bs4 import BeautifulSoup as soup
   soup_read=soup(page_read,"lxml")

   get_page_data(soup_read,'http://www.happykidschool.org')
else:
    pass
