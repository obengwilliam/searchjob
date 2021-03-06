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
        completed=models.BooleanField(default=False)
        details=models.TextField(blank=True)
       
        def __unicode__(self):
              return self.seeds_urls
        class Meta:
		verbose_name_plural='Seed URLs'
              #return u'URL: %s  MAXIMUMDEPTH: %s  MAXIMUMPAGE: %s  DATECREATED: %s    USER:%s' %#(self.seeds_urls,self.max_depth,self.max_pages,self.created_at,self.submitter)


class Index(models.Model):
      keyword=models.CharField(max_length=255,null=False)
      doc=UrlsField()
      def __unicode__(self):
            return self.keyword
      class Meta:
		verbose_name_plural='Full Inverted Index'

class FilterUrl(models.Model):
       filter_url=models.URLField('Add url to prevent crawling',max_length=1000)

       def __unicode__(self):
             return self.filter_url
       class Meta:
		verbose_name='Filter Url'



class Page_info(models.Model):
       title=models.CharField(max_length=255)
       body=models.TextField()
       url=models.URLField(max_length=1000)
       doc_digest=models.CharField(max_length=255)
       rank_score=models.FloatField(null=True , default=0)
       date_updated=models.DateTimeField(null=True)

  
       def  __unicode__(self):
            return self.title
       class Meta:
		verbose_name_plural='Page Data'




class Rank(models.Model):
       url=models.URLField(max_length=1000)
       rank=models.FloatField()
       def __unicode__(self):
           return self.url

class Stopword(models.Model):
       words=models.CharField('Stopwords',max_length=255)
       def __unicode__(self):
           return self.words
       class Meta:
		verbose_name='Stopword'


class Error_log(models.Model):
       error_type=models.TextField('Type of Error',max_length=255)
       date=models.DateTimeField('Date Occurred',auto_now_add=True,null=True)
       from_module=models.CharField('Module',max_length=255)
       def __unicode__(self):
           return self.date
       class Meta:
		verbose_name='Module Error Log'


class Web_Statistic(models.Model):
	Number_of_removed_urls=models.PositiveIntegerField(null=True,default=0)
	Number_of_robotstxt_request=models.PositiveIntegerField(null=True,default=0)
	Number_of_excluded_urls=models.PositiveIntegerField(null=True,default=0)
	Number_of_Http_Request=models.PositiveIntegerField(null=True,default=0)
        Number_of_duplicate_documents=models.PositiveIntegerField(null=True,default=0)
        def __unicode__(self):
           return str(self.Number_of_Http_Request)
        class Meta:
		verbose_name='Statistics Gathered from Crawler'
'''
class Crawler_Time_statistics(models.Model):
       Previousdate=
       Nextdate=
       Completed=
       Timetaken=

'''
       
	
class Http_status_errors(models.Model):
       Url_errors=models.PositiveIntegerField('Number of url error or server errors',null=True,default=0)

       ok_200=models.PositiveIntegerField('Number of requests with status code: 200',null=True,default=0)

       from_400_500=models.PositiveIntegerField('Number of requests with status code :400 to 500',null=True,default=0)
       Bad_status_line=models.PositiveIntegerField('Number of BadStatusLine',null=True,default=0)
       Socket_time_out=models.PositiveIntegerField('Number of requests that Timed out',null=True,default=0 )
       Ungrouped=models.PositiveIntegerField('Other Http request errors',null=True,default=0)

       def __unicode__(self):
           return str(self.ok_200)
       class Meta:
		verbose_name='Http Error log'

	
	







