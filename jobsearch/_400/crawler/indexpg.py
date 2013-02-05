

import csv
from bs4 import BeautifulSoup as soup

def make_index( url, content_soup):
    try:
       style_num=content_soup.find_all('style')
       script_num=content_soup.find_all('script')
       
       for script in script_num:
           content_soup.script.decompose()
       for style in style_num:
           content_soup.style.decompose()
       content=content_soup.body.get_text()
       
    except:
        return
    words=content.split()
    
    stopwords=['']
    unwanted_punctuations="!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~>>"
    
    try:
        with open('stopwords.csv','rb') as sw :#stopword from google
            read=csv.reader(sw)
            for stopword in read:
                stopwords.append(''.join(stopword))
    except:
        pass
    for word in words:
        
        word=word.lstrip(unwanted_punctuations)
        word=word.rstrip(unwanted_punctuations)
        word=word.lower()
        
        if word not in stopwords and (not word.isdigit()):
           from search_indexes import add_to_search_index
           #add_to_search_index(word,url)
           
           
if __name__=='__main__':  
       from urllib2 import urlopen
       ob=urlopen('http://www.google.com')
       page=ob.read();
       
 
       make_index( 'http://www.google.com', soup(page)) 
