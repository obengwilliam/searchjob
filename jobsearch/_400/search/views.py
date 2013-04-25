# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from crawler.models import Stopword
from retrieve import termsearch,phrasesearch
from check_retrieve import ch_re as checks
import re
from stemming.porter2 import stem 
from pymongo import MongoClient
from django.template import Context
from operator import itemgetter

try: 
	connection=MongoClient()
	db=connection.jobsdbs
except:
       print 'connection problem problem'




def search(request):
    return render_to_response('search/index.html')

def response(request):
     jobtitle=request.GET.get('job','')
     if re.match('"',jobtitle) and len(jobtitle.split()) > 1:
        jobtitle=' '.join(list(stem(i.lower()) for i in jobtitle.split()))
        result_unsorted=list(db.crawler_page_info.find_one({'_id': i}) for i in  phrasesearch(jobtitle.lower()))
        results=sorted(result_unsorted, key=itemgetter('rank_score'))
        
            
        context=Context({'final_results':results,'value':jobtitle})
        
        return render_to_response('search/joobleresults.html',context)

        
     else:
          result_unsorted=list(db.crawler_page_info.find_one({'_id': i}) for i in list(termsearch([stem(i.lower())for i in checks(str(jobtitle).split(' '))])))
          results=sorted(result_unsorted, key=itemgetter('rank_score'))
          
          context=Context({'final_results':results,'value':jobtitle})
          return render_to_response('search/joobleresults.html',context)
         
     
    
     
    
     
   
     #keywords_stopedwords=query_operation(keywords)
     

     
     
     return render_to_response('search/joobleresults.html')



def query_operation(keyword):
    stopwords=Stopword.objects.all()
    
    for i in stopwords:
         for j in keyword:
             print i, j , i ==j, type(str(i))==type(j)
             if i is j:
                 print i,j
    keywords=[jobtitle for jobtitle in keyword if jobtitle not in Stopword.objects.all()]
    return keywords


"""
the next is to remove all stopwords if any
"""
'''
in the response modle we will have 
1.query operation module
  some operations include removal of stopwords.




2.a retrieval module that uses the document index
the retrieval module is responsible for submitting document based on the query terms.
Now this document will scored and then ranked b4 being submitted to the user
queries might include keywored queries,boolean queries and 
'''


def socialmedia(request):
     return render_to_response('search/social_network.html')

