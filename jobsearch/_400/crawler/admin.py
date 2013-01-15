from django.contrib import admin
from crawler.models import Seed


class SeedAdmin(admin.ModelAdmin):
      pass

admin.site.register(Seed,SeedAdmin)
