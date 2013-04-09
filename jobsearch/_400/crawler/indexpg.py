'''
Under this module we intend to do preprocessing on text and also on web pages
.
text pre-processing includes
stemminng,
all to lower cases
hyphen removal or replacing all hyphen with spaces
puntuations
digit removal---because we think they irrelevant to the job search
stopwords removal




problem with web page pre processing


identifying the main block of a page
'''
import csv
from search_indexes import add_to_search_index
from stemming.porter2 import stem 
import re
import sys


def make_index( url, content_soup):
    try:
       if content_soup.title==None:
          title=url
       else:
            title=content_soup.title.string


       style_num=content_soup.find_all('style')
       script_num=content_soup.find_all('script')
       
       for script in script_num:
           content_soup.script.decompose()
       for style in style_num:
           content_soup.style.decompose()
       content=content_soup.body.get_text()
       
       
       
       #content=content.encode('ascii','ignore')
       
       

       page_body=' '.join(content.split()[:100]).lower()
       
       
    except:
      
        print 'problem with obtaining index from the make_index module','.......',sys.exc_info()
        return
    
    content=content.encode('ascii','ignore')
    splitter=re.compile('\\W*')
    
    words=[s.lower( ) for s in splitter.split(content) if s!='']
    #later try to remove all stopwords
    
   

    
    stopwords=['']
    unwanted_punctuations="!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~>>"
    
    try:
        with open('stopwords.csv','rb') as sw :#stopword from google
            read=csv.reader(sw)
            for stopword in read:
                stopwords.append(''.join(stopword))
    except:
        print 'problem from stopwords.csv'
    
    for i in xrange(len(words)):
        word=words[i]
       
        
        #if word=='code':
        #  print word
       
        
        
        
        if word not in stopwords and (not word.isdigit()) and (word not in unwanted_punctuations) and(not word.isalpha()) :
           
          
           
           
           word=word.lstrip(unwanted_punctuations)
           word=word.rstrip(unwanted_punctuations)
           location,count =i,words.count(word)
          
           
           #if word=='code':
           add_to_search_index(stem(word),url,title,page_body,location,count)
          
           #may be we add the location of the word in the document
           
           					
if __name__=='__main__':  
       #import socket
       #import sys
       #setting timeout
       #timeout=50
       #socket.setdefaulttimeout(timeout)
       #from urllib2 import urlopen
       #ob=urlopen('http://www.happykidschool.org/')
       from bs4 import BeautifulSoup as soup
       #page=obread();
       from glob  import glob
       for i in glob('check*.html'):
          opened=open(i,'rb')
       
          page=opened.read()
       
          make_index( 'http://www.happykidschool', soup(page,'lxml')) 
