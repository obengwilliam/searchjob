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
       list_display=['title','url','body','rank_score','doc_digest']
       search_fields=('title','url')

class Ranks_admin(admin.ModelAdmin):
       list_display=['url','rank']
       search_fields=('url',)

class Stopwords_admin(admin.ModelAdmin):
       list_display=['words']
       search_fields=('words',)

class Error_log_admin(admin.ModelAdmin):
       list_display=['date','from_module','error_type']
       search_fields=('date',)
       ordering=('-date',)


class Web_stat_admin(admin.ModelAdmin):
	list_display=['removed_urls','robotstxt_request','excluded_urls','Http_Request']



admin.site.register(Rank,Ranks_admin)
admin.site.register(FilterUrl)
admin.site.register(Seed,SeedAdmin)
admin.site.register(Index,IndexAdmin)
admin.site.register(Page_info,Page_info_admin)
admin.site.register(Stopword,Stopwords_admin)
admin.site.register(Error_log,Error_log_admin)
admin.site.register(Web_Statistics,Web_stat_admin)



 

 

