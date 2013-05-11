from django.contrib import admin
from crawler.models import *

def urls(instance):
    return ', '.join(instance.urls)











 
class IndexAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'doc']
    search_fields=('keyword',)

class SeedAdmin(admin.ModelAdmin):
      list_display = ['seeds_urls', 'max_depth','max_pages','completed','details']



class Page_info_admin(admin.ModelAdmin):
       list_display=['title','url','body','rank_score','doc_digest','date_updated']
       search_fields=('url',)
       



class Stopwords_admin(admin.ModelAdmin):
       list_display=['words']
       search_fields=('words',)

class Error_log_admin(admin.ModelAdmin):
       list_display=['date','from_module','error_type']
       search_fields=('date',)
       ordering=('-date',)
       list_filter = ('date',)



class Web_StatInline(admin.TabularInline):
       model=Web_Statistic
    



class Web_stat_admin(admin.ModelAdmin):
	list_display=['Number_of_removed_urls','Number_of_robotstxt_request','Number_of_excluded_urls','Number_of_Http_Request','Number_of_duplicate_documents']
	

class Http_status_admin(admin.ModelAdmin):
	list_display=[ 'from_400_500','Bad_status_line','Socket_time_out','Ungrouped','Url_errors']


admin.site.register(Http_status_errors,Http_status_admin)

admin.site.register(FilterUrl)
admin.site.register(Seed,SeedAdmin)
admin.site.register(Index,IndexAdmin)
admin.site.register(Page_info,Page_info_admin)
admin.site.register(Stopword,Stopwords_admin)
admin.site.register(Error_log,Error_log_admin)
admin.site.register(Web_Statistic,Web_stat_admin)



 

 

