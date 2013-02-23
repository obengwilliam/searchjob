from django.contrib import admin
from crawler.models import Seed,Index,FilterUrl

def urls(instance):
    return ', '.join(instance.urls)
 
class IndexAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'urls']
    search_fields=('keyword','urls')

class SeedAdmin(admin.ModelAdmin):
      list_display = ['seeds_urls', 'max_depth','max_pages']




admin.site.register(FilterUrl)
admin.site.register(Seed,SeedAdmin)
admin.site.register(Index,IndexAdmin)



 

 

