from django.contrib import admin
from crawler.models import Seed,Index

def urls(instance):
    return ', '.join(instance.urls)
 
class IndexAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'urls']

class SeedAdmin(admin.ModelAdmin):
      list_display = ['seeds_urls', 'max_depth','max_pages']

admin.site.register(Seed,SeedAdmin)
admin.site.register(Index,IndexAdmin)



 

 

