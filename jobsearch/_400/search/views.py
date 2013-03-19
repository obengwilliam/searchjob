# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from crawler.spell_check import spell_check

def search(request):
    return render_to_response('search/index.html')

def response(request):
     jobtitle=request.GET.get('job','')


     
     
     return HttpResponse(jobtitle)



def socialmedia(request):
     return render_to_response('search/social_network.html')

