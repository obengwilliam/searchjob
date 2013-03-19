from django.contrib import admin
from crawler.models import Seed,Index,FilterUrl,Page_info,Rank

def urls(instance):
    return ', '.join(instance.urls)
 
class IndexAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'urls']
    search_fields=('keyword',)

class SeedAdmin(admin.ModelAdmin):
      list_display = ['seeds_urls', 'max_depth','max_pages']



class Page_info_admin(admin.ModelAdmin):
       list_display=['title','url','body']
       search_fields=('title','url')

class Ranks_admin(admin.ModelAdmin):
       list_display=['url','rank']
       search_fields=('url',)






admin.site.register(Rank,Ranks_admin)
admin.site.register(FilterUrl)
admin.site.register(Seed,SeedAdmin)
admin.site.register(Index,IndexAdmin)
admin.site.register(Page_info,Page_info_admin)



 

 

