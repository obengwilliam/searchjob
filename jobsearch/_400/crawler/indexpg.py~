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
from stopwords import stopword
from hashlib import sha224




def visible(element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title','a']:
        	return ''
    	result = re.sub('<!--.*-->|\r|\n', '', element.encode('utf-8'), flags=re.DOTALL)
    	result = re.sub('\s{2,}|&nbsp;', ' ', result)
    	return result



def make_index( url, content_soup):
    docdigest=sha224(str(content_soup)).hexdigest()
    texts=content_soup.findAll(text=True)
   
   
    '''
    (str(),str())->()
    
    This module is responsible for preprocessing content to obtain only keywords 
    This keywords are inserted into the document together with their location and frequency in the document
    This helps us to calculate relevant scores based on this document.

    '''
    
    try:
      
       if content_soup.title==None:
          title=url
       else:
            title=content_soup.title.string

       '''
       style_num=content_soup.find_all('style')
       script_num=content_soup.find_all('script')
       
       for script in script_num:
           content_soup.script.decompose()
       for style in style_num:
           content_soup.style.decompose()
       content=content_soup.body.get_text()
       #finding the best way to obtain only text from a page
       '''
      
       
       

       
       content= ''.join([visible(elem) for elem in texts])      
       #content=content.encode('ascii','ignore')
       
       

       page_body=' '.join(content.split()[:20]).lower()
       print page_body
       
       
    except:
      
             
               import sys
               print 'problem with obtaining index from the make_index module','.......',sys.exc_info()
               from pymongo import MongoClient
               from datetime import datetime
               date=datetime.today()
               connection=MongoClient()
               db=connection.jobsdbs
               db.crawler_error_log.insert({'error_type':str(sys.exc_info()),'date':date,'from_module':str(__file__)})
               return
    
    #content=content.encode('ascii','ignore')
    splitter=re.compile('\\W*')
    
    words=[s.lower( ) for s in splitter.split(content) if s!='']
    #later try to remove all stopwords
    
    
   

    
    stopwords=stopword([])
    
    unwanted_punctuations="!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~>>"
    '''
    try:
        with open('stopwords.csv','rb') as sw :#stopword from google
            read=csv.reader(sw)
            for stopword in read:
                stopwords.append(''.join(stopword))
    except:
        print 'problem from stopwords.csv'
    '''
    def isStringLike(word):
         '''
           str()->bool()
		This module checks if a word is a string by using the duck typing style .
		if it wals like a duck and quacks like a duck then it duck like enough for a purpose
	 '''
         try: word+''
         except: return False
	 else:   return True
    
    for i in xrange(len(words)):
        word=words[i]
       
        
       
        
        #if word=='code':
        #  print word
        
       
       
        if word not in stopwords and (not word.isdigit()) and (word not in unwanted_punctuations) and(word.isalpha()) :
           if isStringLike(word):
           	'''
           	have to check for alphabet using regular expressions
           	'''
           	location,count =i,words.count(word)
           
           
           	word=word.lstrip(unwanted_punctuations)
           	word=word.rstrip(unwanted_punctuations)
           
           
           
           
           
           	#if word=='code':
           	#to index i stem every word and a url a location, etc. 
           	#add_to_search_index(stem(word),url,title,page_body,location,count,docdigest)
          
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
       import profile
       for i in glob('check*.html'):
          opened=open(i,'rb')
          page=opened.read()
          make_index( i, soup(page,'lxml'))
          #profile.run("make_index( i, soup(page,'lxml'))") 
         
