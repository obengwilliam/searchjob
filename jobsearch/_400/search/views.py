# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from crawler.models import Stopword

def search(request):
    return render_to_response('search/index.html')

def response(request):
     jobtitle=request.GET.get('job','')
     
     from check_retrieve import ch_re as checks
     keywords=checks(str(jobtitle).split(' '))
     keywords_stopedwords=query_operation(keywords)
     

     
     
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

