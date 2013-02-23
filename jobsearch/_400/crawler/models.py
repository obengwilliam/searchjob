from django.db import models
from djangotoolbox.fields import ListField
from django.contrib.auth.models import User
from forms import StringListField
 
class UrlsField(ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, StringListField, **kwargs)
 


# Create your models here.
class Seed(models.Model):
	'''
	This model is responsible for storing all information about our seed pages
	so we have the seed urls, the date the user in the admin page added ,which user added it ,
	the maximum number of pages to crawl and the maximum depth the crawler can reach
	'''
        seeds_urls=models.URLField(max_length=1000)
        created_at=models.DateField(auto_now=True)
        max_depth=models.PositiveIntegerField(default=10)
        max_pages=models.PositiveIntegerField(default=10000)
        submitter=models.TextField(default=User,editable=False)
      
       
        def __unicode__(self):
              return self.seeds_urls
              #return u'URL: %s  MAXIMUMDEPTH: %s  MAXIMUMPAGE: %s  DATECREATED: %s    USER:%s' %#(self.seeds_urls,self.max_depth,self.max_pages,self.created_at,self.submitter)


class Index(models.Model):
      keyword=models.CharField(max_length=255,null=False)
      urls=UrlsField()
      def __unicode__(self):
            return self.keywords

class FilterUrl(models.Model):
       filter_url=models.URLField(max_length=1000)

       def __unicode__(self):
             return self.filter_url


