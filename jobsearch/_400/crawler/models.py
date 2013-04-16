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
      doc=UrlsField()
      def __unicode__(self):
            return self.keyword

class FilterUrl(models.Model):
       filter_url=models.URLField(max_length=1000)

       def __unicode__(self):
             return self.filter_url



class Page_info(models.Model):
       title=models.CharField(max_length=255)
       body=models.TextField()
       url=models.URLField(max_length=1000)
  
       def  __unicode__(self):
            return self.title




class Rank(models.Model):
       url=models.URLField(max_length=1000)
       rank=models.FloatField()
       def __unicode__(self):
           return self.url

class Stopword(models.Model):
       words=models.CharField(max_length=255)
       def __unicode__(self):
           return self.words


class Error_log(models.Model):
       error_type=models.TextField(max_length=255)
       date=models.DateTimeField(auto_now_add=True,null=True)
       from_module=models.CharField(max_length=255)




