from django.db import models
#from djangotoolbox.fields import ListField
from django.contrib.auth.models import User

# Create your models here.
class Seed(models.Model):
	'''
	This model is responsible for storing all information about our seed pages
	so we have the seed urls, the date the user in the admin page added ,which user added it ,
	the maximum number of pages to crawl and the maximum depth the crawler can reach
	'''
        seeds_urls=models.CharField(max_length=255,null=False,unique=True)
        created_at=models.DateField(auto_now=True)
        max_depth=models.PositiveIntegerField(default=10)
        max_pages=models.PositiveIntegerField(default=10000)
        submitter=models.TextField(default=User,editable=False)
      
       
        def __unicode__(self):
              return u'URL: %s  MAXIMUMDEPTH: %s  MAXIMUMPAGE: %s  DATECREATED: %s    USER:%s' %(self.seeds_urls,self.max_depth,self.max_pages,self.created_at,self.submitter)
