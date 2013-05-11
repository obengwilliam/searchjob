# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from crawler.models import Stopword
from retrieve import termsearch,phrasesearch
from check_retrieve import ch_re as checks
import re
from stemming.porter2 import stem 
from pymongo import MongoClient
from django.template import Context
from operator import itemgetter
import traceback
import sys
from django.core.paginator import Paginator,InvalidPage ,EmptyPage
from crawler.start_crawler import start_crawler as crawls


try: 
	connection=MongoClient()
	db=connection.jobsdbs
except:
       print 'connection problem problem'




def search(request):
    return render_to_response('search/index.html')

def crawl(request):
    crawls()
    return HttpResponseRedirect('http://localhost:8000/admin/')

def response(request):
   
     jobtitle=request.GET.get('job','')
     
     if re.match('"',jobtitle) and len(jobtitle.strip().strip('"').split()) > 1:
        print 1
        jobtitles=' '.join(list(stem(i.lower().strip()) for i in jobtitle.split()))
        result_unsorted=list(db.crawler_page_info.find_one({'_id': i}) for i in  phrasesearch(jobtitles))
        result=sorted(result_unsorted, key=itemgetter('rank_score'))
        results= jooblepaginator(request,result,10)
       
        context=Context({'final_results':results,'value':jobtitle,'length':len(result)})
	
        
        return render_to_response('search/joobleresults.html',context)

        
     else:

      try:
          
         
          try:result_unsorted=list(db.crawler_page_info.find_one({'_id': i}) for i in list(termsearch([stem(i.lower())for i in str(jobtitle).strip('"').strip(' ').split(' ')])))
          except: print traceback.print_exc()
          
          result=sorted(result_unsorted, key=itemgetter('rank_score'))
          results= jooblepaginator(request,result,10)
          context=Context({'final_results':results,'value':jobtitle,'length':len(result)})
          return render_to_response('search/joobleresults.html',context)
      except:
          db.crawler_error_log.insert({'error_type':str(sys.exc_info()),'from_module':str(__file__)})
          print 'Error from search...views',traceback.print_exc()
          context=Context({'final_results':[],'value':' ','length':len([])})
          return render_to_response('search/joobleresults.html',context)
         
     

def jooblepaginator(request,querylist,resultsperPage):
    paginator = Paginator(querylist,resultsperPage)
    page_range = paginator.page_range
    try:
        page = int(request.GET.get("page",1))
    except ValueError:
        page = 1        
    try:
        querylist = paginator.page(page)
        
    except InvalidPage, EmptyPage:
        
        querylist = paginator.page(paginator.num_pages)
        print "there was and InvalidPage or Emptypage error"
    return querylist 
     
    
     
   
     #keywords_stopedwords=query_operation(keywords)
     

     
     
    #return render_to_response('search/joobleresults.html')



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

